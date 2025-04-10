class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements
        
class DeclarationNode(Node):
    def __init__(self, variable_type, variable_name):
        self.variable_type = variable_type
        self.variable_name = variable_name
        
class AssignNode(Node):
    def __init__(self, variable_name, value):
        self.variable_name = variable_name
        self.value = value
        
class InputNode(Node):
    def __init__(self, variable_name):
        self.variable_name = variable_name
        
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
