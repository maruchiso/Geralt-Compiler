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

