from antlr4 import *
from antlr.GeraltLexer import GeraltLexer
from antlr.GeraltParser import GeraltParser
from visitor import WitcherVisitor


def main():
    file_stream = FileStream('tests/program.witcher', encoding='utf-8')
    lexer = GeraltLexer(file_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GeraltParser(token_stream)
    
    tree = parser.program()
    
    visitor = WitcherVisitor()
    visitor.visit(tree)
    

if __name__ == '__main__':
    main()