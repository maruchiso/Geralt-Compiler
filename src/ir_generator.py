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
        
    def generate(self, node):
        if isinstance(node, ProgramNode):
            # For the whole program, we generate code for each statement
            for statement in node.statements:
                self.generate(statement)
            # End main() function
            self.builder.ret_void()
            
        elif isinstance(node, DeclarationNode):
            variable_type = ir.IntType(32)
            pointer = self.builder.alloca(variable_type, name=node.variable_name)
            self.symbol_table[node.variable_name] = pointer
        
        elif isinstance(node, AssignNode):
            value = self.generate(node.value)
            pointer = self.symbol_table[node.variable_name]
            self.builder.store(value=value, ptr=pointer)
            
        elif isinstance(node, InputNode):
            pass
        
        elif isinstance(node, OutputNode):
            value = self.generate(node.value)
            print(f"; print {value}")
            
        elif isinstance(node, BinOpNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            
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