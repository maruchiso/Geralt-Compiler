class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements
        
class DeclarationNode(Node):
    def __init__(self, variable_type, variable_name, size=None):
        self.variable_type = variable_type
        self.variable_name = variable_name
        self.size = size
        
class AssignNode(Node):
    def __init__(self, variable_name, value, index=None):
        self.variable_name = variable_name
        self.value = value
        self.index = index
        
class InputNode(Node):
    def __init__(self, variable_name, index=None):
        self.variable_name = variable_name
        self.index = index
        
class OutputNode(Node):
    def __init__(self, value):
        self.value = value

class BinOpNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

class VarNode(Node):
    def __init__(self, name):
        self.name = name
        
class BooleanNode(Node):
    def __init__(self, value):
        self.value = value

class BinOpBoolNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class NegNode(Node):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class IfNode(Node):
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class WhileNode(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
        
class CompareNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class FunctionDeclNode(Node):
    def __init__(self, return_type, name, params, body):
        self.return_type = return_type
        self.name = name
        self.params = params
        self.body = body

class FunctionCallNode(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class ReturnNode(Node):
    def __init__(self, value):
        self.value = value

class ArrayAccessNode(Node):
    def __init__(self, name, indexes):
        self.name = name
        self.indexes = indexes

class StringNode(Node):
    def __init__(self, value):
        self.value = value

class StructDefNode(Node):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

class StructAccessNode(Node):
    def __init__(self, struct_var, field_name):
        self.struct_var = struct_var  
        self.field_name = field_name  

class ClassDefNode:
    def __init__(self, name, fields):
        self.name = name                  
        self.fields = fields              

    def __repr__(self):
        return f"<Class {self.name}: {self.fields}>"

class ClassFieldNode:
    def __init__(self, visibility, type_name, field_name):
        self.visibility = visibility      
        self.type_name = type_name       
        self.field_name = field_name     

    def __repr__(self):
        return f"({self.visibility} {self.type_name} {self.field_name})"

class ClassAccessNode(Node):
    def __init__(self, class_var, field_name):
        self.class_var = class_var
        self.field_name = field_name
