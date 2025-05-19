from antlr4 import *
from antlr.GeraltLexer import GeraltLexer
from antlr.GeraltParser import GeraltParser
from visitor import WitcherVisitor
from ast_nodes import *
from ir_generator import *
from antlr4.error.ErrorListener import ErrorListener

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


class GeraltErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}:{column} -> {msg}")

def main():
    file_stream = FileStream('tests/program.witcher', encoding='utf-8')
    
    lexer = GeraltLexer(file_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(GeraltErrorListener())  # Dodajemy nasłuchiwacz błędów

    stream = CommonTokenStream(lexer)

    parser = GeraltParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(GeraltErrorListener())  # Dodajemy nasłuchiwacz błędów

    tree = parser.program()

    visitor = WitcherVisitor()
    ast = visitor.visit(tree)
    print_ast(ast)
    ir_generator = IRGenerator()
    ir_generator.generate(ast)
    ir_generator.save("output.ll")
    
if __name__ == '__main__':
    main()