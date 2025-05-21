from llvmlite import ir
from ast_nodes import *

# LLVM IR it takes AST and then generate LLVM code (.ll file)
class IRGenerator:
    def __init__(self):
        self.module = ir.Module(name='geralt_module') # container for LLVM module
        self.builder = None # object to create instructions LLVM
        self.scopes = [{}] # to list scopes
        self.global_vars = {} # map for global variables
        
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
        
        # string printf
        printf_str_format = "%s\n\0"
        printf_str_bytes = bytearray(printf_str_format.encode('utf8'))
        printf_str_const = ir.ArrayType(ir.IntType(8), len(printf_str_bytes))
        self.printf_str_format = ir.GlobalVariable(self.module, printf_str_const, name="printf_str_format")
        self.printf_str_format.global_constant = True
        self.printf_str_format.initializer = ir.Constant(printf_str_const, printf_str_bytes)

        # string scanf
        scanf_str_format = "%s\0"
        scanf_str_bytes = bytearray(scanf_str_format.encode("utf8"))
        scanf_str_const = ir.ArrayType(ir.IntType(8), len(scanf_str_bytes))
        self.scanf_str_format = ir.GlobalVariable(self.module, scanf_str_const, name="scanf_str_format")
        self.scanf_str_format.global_constant = True
        self.scanf_str_format.initializer = ir.Constant(scanf_str_const, scanf_str_bytes)

        # string copy
        strcpy_type = ir.FunctionType(ir.IntType(8).as_pointer(), [ir.IntType(8).as_pointer(), ir.IntType(8).as_pointer()])
        self.strcpy = ir.Function(self.module, strcpy_type, name="strcpy")
        
        self.string_counter = 0
        self.string_constans = {}
        
    def _declare_function(self, node: FunctionDeclNode):
        def map_type(typ):
            if typ == 'Wilk':
                return ir.IntType(32)
            elif typ == 'Kot':
                return ir.FloatType()
            elif typ == 'Gryf':
                return ir.IntType(1)
            else:
                raise Exception(f"Unknown type: {typ}")

        return_type = map_type(node.return_type)
        arg_types = [map_type(t) for t, _ in node.params]

        # Create function and assign to variable
        func_type = ir.FunctionType(return_type, arg_types)
        func = ir.Function(self.module, func_type, name=node.name)

        return func
    
    def define_variable(self, name, ptr, global_scope=False):
        if global_scope:
            self.global_vars[name] = ptr
            self.scopes[0][name] = ptr
        else:
            self.scopes[-1][name] = ptr
    
    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def generate(self, node):
        if isinstance(node, ProgramNode):
            # Step 1: Register all functions
            for stmt in node.statements:
                if isinstance(stmt, FunctionDeclNode):
                    self._declare_function(stmt)

            # Step 2: Generate function body and the rest of the program
            for stmt in node.statements:
                if isinstance(stmt, FunctionDeclNode):
                    self.generate(stmt)
                    continue
                
                # Set new builder for new block, if current block is ended
                block = self.main_func.basic_blocks[-1]
                if block.terminator is not None:
                    block = self.main_func.append_basic_block(name="count")
                self.builder.position_at_end(block)
                
                self.generate(stmt)

            # Step 3: End main
            if self.builder.block.terminator is None:
                self.builder.ret_void()
            else:
                print("Main block already has a terminator.")

        elif isinstance(node, FunctionDeclNode):
            print(f"Generating function body: {node.name}")

            # Get function from module
            func = self.module.get_global(node.name)
            if func is None or not isinstance(func, ir.Function):
                raise Exception(f"Function {node.name} is not declared")

            # Create entry point
            block = func.append_basic_block(name="entry")
            self.builder = ir.IRBuilder(block)
            # Add scope to scopes list
            self.scopes.append({})

            # Parameters assign
            for arg, (_, param_name) in zip(func.args, node.params):
                arg.name = param_name
                ptr = self.builder.alloca(arg.type, name=param_name)
                self.builder.store(arg, ptr)
                print(f"DEBUG: {param_name} -> {ptr}")

            # Generate function body
            for stmt in node.body:
                self.generate(stmt)

            # Default return
            if self.builder.block.terminator is None:
                if isinstance(func.function_type.return_type, ir.VoidType):
                    self.builder.ret_void()
                else:
                    self.builder.ret(ir.Constant(func.function_type.return_type, 0))
            
            # Close scope -> Delete from scopes
            self.scopes.pop()

        elif isinstance(node, DeclarationNode):
            print(f"DEBUG IR: Declaring {node.variable_name} (size={node.size})")
            # Mapping types
            if node.variable_type == 'Wilk':
                variable_type = ir.IntType(32)
            elif node.variable_type == 'Kot':
                variable_type = ir.FloatType()
            elif node.variable_type == 'Gryf':
                variable_type = ir.IntType(1)
            elif node.variable_type == 'Niedźwiedź':
                #variable_type = ir.IntType(8).as_pointer()
                # Because pointer cause errors with Input so i changed it to buffor with 100 characters
                variable_type = ir.ArrayType(ir.IntType(8), 100)
            else:
                raise Exception(f'{node.variable_type} is unknown variable type.')

            # variable alloc
            if node.size is None:
                # Scalar
                pointer = self.builder.alloca(variable_type, name=node.variable_name)
            else:
                # Array
                array_type = variable_type
            if isinstance(node.size, list):
                array_type = variable_type
                for dim in reversed(node.size):
                    array_type = ir.ArrayType(array_type, dim)
                pointer = self.builder.alloca(array_type, name=node.variable_name)
            else:
                pointer = self.builder.alloca(variable_type, name=node.variable_name)
            is_global_scope = len(self.scopes) == 1
            self.define_variable(node.variable_name, pointer, global_scope=is_global_scope)
            print(f"Debug: {node.variable_name} -> {pointer} is global: {is_global_scope}")
            
        elif isinstance(node, AssignNode):
            print(f"DEBUG IR: Assigning to {node.variable_name}, index={node.index}")
            value = self.generate(node.value)
            pointer = self.lookup(node.variable_name)
            if pointer is None:
                raise Exception(f"Variable {node.variable_name} not found in any scope.")


            if node.index is not None:
                element_pointer = self.get_element_ptr(pointer, node.index)
                self.builder.store(value, element_pointer)
            else:
                # Check it type is [100 x i8] - which is string (here Niedźwiedź)
                pointee = pointer.type.pointee
                if isinstance(pointee, ir.ArrayType) and pointee.element == ir.IntType(8):
                    # get element ptr to array
                    dest_ptr = self.builder.gep(pointer, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])
                    self.builder.call(self.strcpy, [dest_ptr, value])
                else:
                    self.builder.store(value, pointer)

                    
        elif isinstance(node, InputNode):
            pointer = self.lookup(node.variable_name)
            if pointer is None:
                raise Exception(f"Variable {node.variable_name} not found in any scope.")


            if node.index is not None:
                pointer = self.get_element_ptr(pointer, node.index)

            variable_type = pointer.type.pointee

            if isinstance(variable_type, ir.FloatType):
                format_pointer = self.builder.bitcast(self.scanf_float_format, ir.IntType(8).as_pointer())
                input_pointer = format_pointer
                
            elif isinstance(variable_type, ir.ArrayType):
                format_pointer = self.builder.bitcast(self.scanf_str_format, ir.IntType(8).as_pointer())
                input_pointer = self.builder.gep(pointer, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])
            elif isinstance(variable_type, ir.IntType):
                format_pointer = self.builder.bitcast(self.scanf_format, ir.IntType(8).as_pointer())

            self.builder.call(self.scanf, [format_pointer, input_pointer])
        
        elif isinstance(node, OutputNode):
            value = self.generate(node.value)
            value_type = value.type

            if isinstance(value_type, ir.FloatType):
                format_pointer = self.builder.bitcast(self.printf_float_format, ir.IntType(8).as_pointer())
                value = self.builder.fpext(value, ir.DoubleType(), name="float_to_double")

            elif value_type == ir.IntType(1):
                format_pointer = self.builder.bitcast(self.printf_format, ir.IntType(8).as_pointer())
                value = self.builder.zext(value, ir.IntType(32), name="bool_to_int")

            elif value_type == ir.IntType(32):
                format_pointer = self.builder.bitcast(self.printf_format, ir.IntType(8).as_pointer())

            elif isinstance(value_type, ir.PointerType) and value_type.pointee == ir.IntType(8):
                # classic i8* (StringNode)
                format_pointer = self.builder.bitcast(self.printf_str_format, ir.IntType(8).as_pointer())
            
            elif isinstance(value_type, ir.PointerType) and isinstance(value_type.pointee, ir.ArrayType) and value_type.pointee.element == ir.IntType(8):
                # print tekst: [100 x i8]* → zrób GEP do i8*
                format_pointer = self.builder.bitcast(self.printf_str_format, ir.IntType(8).as_pointer())
                value = self.builder.gep(value, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])


            else:
                raise Exception(f"Unsupported type for print: {value_type}")

            self.builder.call(fn=self.printf, args=[format_pointer, value])


            
        elif isinstance(node, BinOpNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            
            if left.type != right.type:
                raise Exception(f"type mismatch: {left.type} vs {right.type}")
        
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
            pointer = self.lookup(node.name)
            if pointer is None:
                raise Exception(f"Variable {node.name} not found in any scope.")

            pointee = pointer.type.pointee

            if isinstance(pointee, ir.ArrayType) and pointee.element == ir.IntType(8):
                # if Niedźwiedź then reutrn pointer to first elem in array
                return pointer  # without load because load returns whole array

            return self.builder.load(ptr=pointer, name=node.name)

        
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

            # Then
            self.builder.position_at_start(then_block)
            for stmt in node.then_body:
                self.generate(stmt)
            if self.builder.block.terminator is None:
                self.builder.branch(end_block)
            
            # Else
            if else_block:
                self.builder.position_at_start(else_block)
                for stmt in node.else_body:
                    self.generate(stmt)
                if self.builder.block.terminator is None:
                    self.builder.branch(end_block)
            
            # Ifend
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

        elif isinstance(node, FunctionCallNode):
            func = self.module.get_global(node.name)
            if func is None or not isinstance(func, ir.Function):
                raise Exception(f"Function {node.name} is not defined")

            args = [self.generate(arg) for arg in node.args]
            return self.builder.call(func, args)

        elif isinstance(node, ReturnNode):
            if node.value:
                value = self.generate(node.value)
                self.builder.ret(value)
            else:
                self.builder.ret_void()
        
        elif isinstance(node, ArrayAccessNode):
            pointer = self.lookup(node.variable_name)
            if pointer is None:
                raise Exception(f"Variable {node.variable_name} not found in any scope.")

            element_pointer = self.get_element_ptr(pointer, node.indexes)
            return self.builder.load(element_pointer, name=node.name)
        
        elif isinstance(node, StringNode):
            text = node.value + "\0" # End sign for strings
            string_bytes = bytearray(text.encode("utf-8"))
            const_type = ir.ArrayType(ir.IntType(8), len(string_bytes))
            
            if text in self.string_constans:
                string_const = self.string_constans[text]
            else:
                name = f"str{self.string_counter}"
                self.string_counter += 1
                string_const = ir.GlobalVariable(self.module, const_type, name=name)
                string_const.global_constant = True
                string_const.initializer = ir.Constant(const_type, string_bytes)
            
            return self.builder.bitcast(string_const, ir.IntType(8).as_pointer())
        

        else:
            raise NotImplementedError(f'Node type: {type(node)} is not implemented.')
        
    def get_element_ptr(self, pointer, index_nodes):
        print(f"DEBUG GEP: pointer={pointer}, index_nodes={index_nodes}")
        indices = [ir.Constant(ir.IntType(32), 0)]  # first 0 for base
        for idx_node in index_nodes:
            idx_value = self.generate(idx_node)
            if idx_value.type != ir.IntType(32):
                idx_value = self.builder.fptoui(idx_value, ir.IntType(32))
            indices.append(idx_value)
        return self.builder.gep(pointer, indices, inbounds=True)

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self.module))