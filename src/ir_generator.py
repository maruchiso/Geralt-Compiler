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

        # float
        # global format of string for printf
        printf_float_format = '%f\n\0'
        printf_float_bytes = bytearray(printf_float_format.encode('utf8'))
        printf_float_const = ir.ArrayType(element=ir.IntType(8), count=len(printf_float_bytes))
        self.printf_float_format = ir.GlobalVariable(module=self.module, typ=printf_float_const, name='printf_float_format')
        self.printf_float_format.global_constant = True # change to constant
        self.printf_float_format.initializer = ir.Constant(typ=printf_float_const, constant=printf_float_bytes)

        # global format of string for scanf 
        scanf_float_format = "%f\0"
        scanf_float_bytes = bytearray(scanf_float_format.encode("utf8"))
        scanf_float_const = ir.ArrayType(ir.IntType(8), len(scanf_float_bytes))
        self.scanf_float_format = ir.GlobalVariable(self.module, scanf_float_const, name="scanf_float_format")
        self.scanf_float_format.global_constant = True
        self.scanf_float_format.initializer = ir.Constant(scanf_float_const, scanf_float_bytes)
        
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
            elif node.variable_type == 'Gryf':
                variable_type = ir.IntType(1)
            else:
                raise Exception(f'{node.variable_type} is unknown variable type.')
            if node.size == None:
                pointer = self.builder.alloca(variable_type, name=node.variable_name)
            else:
                array_type = ir.ArrayType(variable_type, node.size)
                pointer = self.builder.alloca(array_type, name=node.variable_name)
                
            self.symbol_table[node.variable_name] = pointer
        
        elif isinstance(node, AssignNode):
            value = self.generate(node.value)
            pointer = self.symbol_table[node.variable_name]
            if node.index is not None:
                zero = ir.Constant(ir.IntType(32), 0)
                index = ir.Constant(ir.IntType(32), node.index)
                element_pointer = self.builder.gep(pointer, [zero, index], inbounds=True)
                self.builder.store(value, element_pointer)
            else:
                self.builder.store(value, pointer)
                    
        elif isinstance(node, InputNode):
            pointer = self.symbol_table[node.variable_name]

            if node.index is not None:
                zero = ir.Constant(ir.IntType(32), 0)
                index = ir.Constant(ir.IntType(32), node.index)
                pointer = self.builder.gep(pointer, [zero, index], inbounds=True)

            variable_type = pointer.type.pointee

            if isinstance(variable_type, ir.FloatType):
                format_pointer = self.builder.bitcast(self.scanf_float_format, ir.IntType(8).as_pointer())
            else:
                format_pointer = self.builder.bitcast(self.scanf_format, ir.IntType(8).as_pointer())

            self.builder.call(self.scanf, [format_pointer, pointer])
        
        elif isinstance(node, OutputNode):
            value = self.generate(node.value)
            value_type = value.type
            
            # convert pointer to byte array to pointer to first byte
            if isinstance(value_type, ir.FloatType):
                format_pointer = self.builder.bitcast(self.printf_float_format, ir.IntType(8).as_pointer())
                # float has to be double!
                value = self.builder.fpext(value, ir.DoubleType(), name="float_to_double")
            elif value_type == ir.IntType(1):
                format_pointer = self.builder.bitcast(self.printf_format, ir.IntType(8).as_pointer())
                value = self.builder.zext(value, ir.IntType(32), name="bool_to_int")
            else:
                format_pointer = self.builder.bitcast(self.printf_format, ir.IntType(8).as_pointer())

            self.builder.call(fn=self.printf, args=[format_pointer, value])

            
        elif isinstance(node, BinOpNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            
            if left.type != right.type:
                raise Exception(f"Type mismatch: {left.type} vs {right.type}")
        
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
            if isinstance(node.value, float):
                return ir.Constant(ir.FloatType(), node.value)
            elif isinstance(node.value, int):
                return ir.Constant(ir.IntType(32), node.value)
            else:
                raise(f"{node.value} is unknown type.")
        
        elif isinstance(node, VarNode):
            pointer = self.symbol_table.get(node.name)
            if pointer is None:
                raise Exception(f'Variable: {node.name} is undefined')
            return self.builder.load(ptr=pointer, name=node.name)
        
        # elif isinstance(node, BinOpBoolNode):
        #     left = self.generate(node.left)
        #     right = self.generate(node.right)

        #     if left.type == ir.IntType(32):
        #         left = self.builder.trunc(left, ir.IntType(1), name="left_trunc")

        #     if right.type == ir.IntType(32):
        #         right = self.builder.trunc(right, ir.IntType(1), name="right_trunc")

        #     if node.operator == 'AND':
        #         return self.builder.and_(left, right, name='and')
        #     elif node.operator == 'OR':
        #         return self.builder.or_(left, right, name='or')
        #     elif node.operator == 'XOR':
        #         return self.builder.xor(left, right, name='xor')
        #     else:
        #         raise Exception(f'Unknown boolean operator: {node.operator}')
        elif isinstance(node, BinOpBoolNode):
            left = self.generate(node.left)
            right = self.generate(node.right)

            if left.type == ir.IntType(32):
                left = self.builder.trunc(left, ir.IntType(1), name="left_trunc")

            if right.type == ir.IntType(32):
                right = self.builder.trunc(right, ir.IntType(1), name="right_trunc")

            if node.operator == 'AND':
                and_right_block = self.builder.append_basic_block('and.right')
                and_end_block = self.builder.append_basic_block('and.end')
                
                result = self.builder.alloca(ir.IntType(1), name='and_result')
                self.builder.store(left, result)
                
                self.builder.cbranch(left, and_right_block, and_end_block)
                
                self.builder.position_at_start(and_right_block)
                self.builder.store(right, result)
                self.builder.branch(and_end_block)
                
                self.builder.position_at_start(and_end_block)
                return self.builder.load(result, name='and')
            
            elif node.operator == 'OR':
                or_right_block = self.builder.append_basic_block('or.right')
                or_end_block = self.builder.append_basic_block('or.end')
                
                result = self.builder.alloca(ir.IntType(1), name='or_result')
                self.builder.store(left, result)
                
                self.builder.cbranch(left, or_end_block, or_right_block)
                
                self.builder.position_at_start(or_right_block)
                self.builder.store(right, result)
                self.builder.branch(or_end_block)
                
                self.builder.position_at_start(or_end_block)
                return self.builder.load(result, name='or')

            elif node.operator == 'XOR':
                return self.builder.xor(left, right, name='xor')
            else:
                raise Exception(f'Unknown boolean operator: {node.operator}')


        elif isinstance(node, NegNode):
            value = self.generate(node.operand)

            if value.type == ir.IntType(32):
                value = self.builder.trunc(value, ir.IntType(1), name="bool")

            return self.builder.xor(value, ir.Constant(ir.IntType(1), 1), name='neg')
        
        elif isinstance(node, BooleanNode):
            return ir.Constant(ir.IntType(1), int(node.value))

        elif isinstance(node, IfNode):
            cond = self.generate(node.condition)
            if cond.type == ir.IntType(32):
                cond = self.builder.trunc(cond, ir.IntType(1))
            
            then_block = self.builder.append_basic_block('then')
            else_block = self.builder.append_basic_block('else') if node.else_body else None
            end_block = self.builder.append_basic_block('ifend')
            
            if else_block:
                self.builder.cbranch(cond, then_block, else_block)
            else:
                self.builder.cbranch(cond, then_block, end_block)

            # then
            self.builder.position_at_start(then_block)
            for stmt in node.then_body:
                self.generate(stmt)
            self.builder.branch(end_block)
            
            # else
            self.builder.position_at_start(else_block)
            if node.else_body:
                for stmt in node.else_body:
                    self.generate(stmt)
                self.builder.branch(end_block)
            
            self.builder.position_at_start(end_block)

        elif isinstance(node, WhileNode):
            loop_condition_block = self.builder.append_basic_block('loop.cond')
            loop_body_block = self.builder.append_basic_block('loop.body')
            loop_end_block = self.builder.append_basic_block('loop.end')
            
            self.builder.branch(loop_condition_block)
            
            # condition
            self.builder.position_at_start(loop_condition_block)
            cond = self.generate(node.condition)
            if cond.type == ir.IntType(32):
                cond = self.builder.trunc(cond, ir.IntType(1))
            self.builder.cbranch(cond, loop_body_block, loop_end_block)
            
            # body
            self.builder.position_at_start(loop_body_block)
            for stmt in node.body:
                self.generate(stmt)
            self.builder.branch(loop_condition_block)
            
            # end
            self.builder.position_at_start(loop_end_block)
            
        elif isinstance(node, CompareNode):
            left = self.generate(node.left)
            right = self.generate(node.right)

            if left.type != right.type:
                raise Exception("Comparison operands must have the same type")

            if node.op == '<':
                if left.type == ir.FloatType():
                    return self.builder.fcmp_ordered('<', left, right)
                else:
                    return self.builder.icmp_signed('<', left, right)
            elif node.op == '<=':
                if left.type == ir.FloatType():
                    return self.builder.fcmp_ordered('<=', left, right)
                else:
                    return self.builder.icmp_signed('<=', left, right)
            elif node.op == '>':
                if left.type == ir.FloatType():
                    return self.builder.fcmp_ordered('>', left, right)
                else:
                    return self.builder.icmp_signed('>', left, right)
            elif node.op == '>=':
                if left.type == ir.FloatType():
                    return self.builder.fcmp_ordered('>=', left, right)
                else:
                    return self.builder.icmp_signed('>=', left, right)
            elif node.op == '==':
                if left.type == ir.FloatType():
                    return self.builder.fcmp_ordered('==', left, right)
                else:
                    return self.builder.icmp_signed('==', left, right)
            elif node.op == '!=':
                if left.type == ir.FloatType():
                    return self.builder.fcmp_ordered('!=', left, right)
                else:
                    return self.builder.icmp_signed('!=', left, right)
            else:
                raise Exception(f"Unknown comparison operator {node.op}")

        else:
            raise NotImplementedError(f'Node type: {type(node)} is not implemented.')
    
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self.module))