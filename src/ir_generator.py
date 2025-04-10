from llvmlite import ir
from ast_nodes import *

# LLVM IR it takes AST and then generate LLVM code (.ll file)
class IRGenerator:
    def __init__(self):
        self.module = ir.Module(name='geralt_module') # container for LLVM module
        self.builder = None # object to create instructions LLVM
        self.symbol_table = {} # dict fo tracking varaibles and their adresses
        
        # Declare main() function that will be 'entry' block for LLVM
        ftype = ir.FunctionType(ir.VoidType(), [])
        self.main_func = ir.Function(self.module, ftype, name='main')
        block = self.main_func.append_basic_block(name='entry')
        self.builder = ir.IRBuilder(block=block)
        
        # prinf, scanf declaration
        # Declare pointer to string, but in LLVM string is like in C,
        # pointer to char table
        char_pointer_type = ir.IntType(8).as_pointer()
        
        # printf
        # Here we declare as int printf(char*, ...)
        printf_type = ir.FunctionType(return_type=ir.IntType(32), args=[char_pointer_type], var_arg=True)
        self.printf = ir.Function(module=self.module, ftype=printf_type, name='printf')
        
        # scanf (same as printf)
        scanf_type = ir.FunctionType(return_type=ir.IntType(32), args=[char_pointer_type], var_arg=True)
        self.scanf = ir.Function(module=self.module, ftype=scanf_type, name='scanf')
        
        # global format of string for printf
        printf_format = '%d\n\0' # print integer, \n new line and \0 end of string
        printf_bytes = bytearray(printf_format.encode('utf8')) # python string to byte array in UTF-8
        printf_const = ir.ArrayType(element=ir.IntType(8), count=len(printf_bytes)) # string is array of i8 = 1 byte
        self.printf_format = ir.GlobalVariable(module=self.module, typ=printf_const, name='printf_format') # global variable 
        self.printf_format.global_constant = True # change to constant
        self.printf_format.initializer = ir.Constant(typ=printf_const, constant=printf_bytes) # initialize with default value = '%d\n\0'
                                                                                              # const char printf_format[] = '%d\n\0';

        # global format of string for scanf 
        scanf_format = "%d\0"
        scanf_bytes = bytearray(scanf_format.encode("utf8"))
        scanf_const = ir.ArrayType(ir.IntType(8), len(scanf_bytes))
        self.scanf_format = ir.GlobalVariable(self.module, scanf_const, name="scanf_fmt")
        self.scanf_format.global_constant = True
        self.scanf_format.initializer = ir.Constant(scanf_const, scanf_bytes)
                        
    def generate(self, node):
        if isinstance(node, ProgramNode):
            # For the whole program, we generate code for each statement
            for statement in node.statements:
                self.generate(statement)
            # End main() function
            self.builder.ret_void()
            
        elif isinstance(node, DeclarationNode):
            if node.variable_type == 'Wilk':
                variable_type = ir.IntType(32)
            elif node.variable_type == 'Kot':
                variable_type = ir.FloatType()
            else:
                raise Exception(f'{node.variable_type} is unknown variable type.')
            pointer = self.builder.alloca(variable_type, name=node.variable_name)
            self.symbol_table[node.variable_name] = pointer
        
        elif isinstance(node, AssignNode):
            value = self.generate(node.value)
            pointer = self.symbol_table[node.variable_name]
            self.builder.store(value=value, ptr=pointer)
            
        elif isinstance(node, InputNode):
            variable_pointer = self.symbol_table.get(node.variable_name)
            if variable_pointer is None:
                raise Exception(f"Undefined variable: {node.variable_name}")
            
            format_pointer = self.builder.bitcast(self.scanf_format, ir.IntType(8).as_pointer())
            self.builder.call(self.scanf, [format_pointer, variable_pointer])
        
        elif isinstance(node, OutputNode):
            value = self.generate(node.value)
            # convert pointer to byte array to pointer to first byte
            format_pointer = self.builder.bitcast(self.printf_format, ir.IntType(8).as_pointer())
            self.builder.call(fn=self.printf, args=[format_pointer, value])
            
        elif isinstance(node, BinOpNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            
            if left.type != right.type:
                if left.type == ir.IntType(32) and right.type == ir.FloatType():
                    left = self.builder.sitofp(left, ir.FloatType(), name="int_to_float")
                elif left.type == ir.FloatType() and right.type == ir.IntType(32):
                    right = self.builder.sitofp(right, ir.FloatType(), name="int_to_float")
                else:
                    raise Exception(f"Unsupported types: {left.type} and {right.type}")
        
            if left.type == ir.FloatType():
                if node.operator == '+':
                    return self.builder.fadd(left, right, 'add')
                elif node.operator == '-':
                    return self.builder.fsub(left, right, 'sub')
                elif node.operator == '*':
                    return self.builder.fmul(left, right, 'mul')
                elif node.operator == '/':
                    return self.builder.fdiv(left, right, 'div')
            else:
                if node.operator == '+':
                    return self.builder.add(left, right, 'add')
                elif node.operator == '-':
                    return self.builder.sub(left, right, 'sub')
                elif node.operator == '*':
                    return self.builder.mul(left, right, 'mul')
                elif node.operator == '/':
                    return self.builder.sdiv(left, right, 'div')
        
        elif isinstance(node, NumberNode):
            return ir.Constant(ir.IntType(32), node.value)
        
        elif isinstance(node, VarNode):
            pointer = self.symbol_table.get(node.name)
            if pointer is None:
                raise Exception(f'Variable: {node.name} is undefined')
            return self.builder.load(ptr=pointer, name=node.name)
        
        
        else:
            raise NotImplementedError(f'Node type: {type(node)} is not implemented.')
    
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self.module))