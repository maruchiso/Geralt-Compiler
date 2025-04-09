from antlr4 import *
from antlr.GeraltLexer import GeraltLexer
from antlr.GeraltParser import GeraltParser
from visitor import WitcherVisitor
from ast_nodes import *
from ir_generator import *

def print_ast(ast):
    for stmt in ast.statements:
        print(f"Node type: {type(stmt).__name__}")
        if isinstance(stmt, DeclarationNode):
            print(f"  Declaration: {stmt.variable_type} {stmt.variable_name}")
        elif isinstance(stmt, InputNode):
            print(f"  Input: {stmt.variable_name}")
        elif isinstance(stmt, AssignNode):
            print(f"  Assign: {stmt.variable_name} = {stmt.value}")
        elif isinstance(stmt, OutputNode):
            print(f"  Output: {stmt.value}")
        else:
            print(f"  Unknown node: {stmt}")

            
def main():
    file_stream = FileStream('tests/program.witcher', encoding='utf-8')
    lexer = GeraltLexer(file_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GeraltParser(token_stream)
    tree = parser.program()

    visitor = WitcherVisitor()
    ast = visitor.visit(tree)
    #print_ast(ast)
    
    ir_generator = IRGenerator()
    ir_generator.generate(ast)
    ir_generator.save('output.ll')
    
if __name__ == '__main__':
    main()