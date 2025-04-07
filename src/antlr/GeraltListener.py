# Generated from Geralt.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GeraltParser import GeraltParser
else:
    from GeraltParser import GeraltParser

# This class defines a complete listener for a parse tree produced by GeraltParser.
class GeraltListener(ParseTreeListener):

    # Enter a parse tree produced by GeraltParser#program.
    def enterProgram(self, ctx:GeraltParser.ProgramContext):
        pass

    # Exit a parse tree produced by GeraltParser#program.
    def exitProgram(self, ctx:GeraltParser.ProgramContext):
        pass


    # Enter a parse tree produced by GeraltParser#declaration.
    def enterDeclaration(self, ctx:GeraltParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GeraltParser#declaration.
    def exitDeclaration(self, ctx:GeraltParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GeraltParser#assign.
    def enterAssign(self, ctx:GeraltParser.AssignContext):
        pass

    # Exit a parse tree produced by GeraltParser#assign.
    def exitAssign(self, ctx:GeraltParser.AssignContext):
        pass


    # Enter a parse tree produced by GeraltParser#input.
    def enterInput(self, ctx:GeraltParser.InputContext):
        pass

    # Exit a parse tree produced by GeraltParser#input.
    def exitInput(self, ctx:GeraltParser.InputContext):
        pass


    # Enter a parse tree produced by GeraltParser#output.
    def enterOutput(self, ctx:GeraltParser.OutputContext):
        pass

    # Exit a parse tree produced by GeraltParser#output.
    def exitOutput(self, ctx:GeraltParser.OutputContext):
        pass


    # Enter a parse tree produced by GeraltParser#dividing.
    def enterDividing(self, ctx:GeraltParser.DividingContext):
        pass

    # Exit a parse tree produced by GeraltParser#dividing.
    def exitDividing(self, ctx:GeraltParser.DividingContext):
        pass


    # Enter a parse tree produced by GeraltParser#var.
    def enterVar(self, ctx:GeraltParser.VarContext):
        pass

    # Exit a parse tree produced by GeraltParser#var.
    def exitVar(self, ctx:GeraltParser.VarContext):
        pass


    # Enter a parse tree produced by GeraltParser#subtraction.
    def enterSubtraction(self, ctx:GeraltParser.SubtractionContext):
        pass

    # Exit a parse tree produced by GeraltParser#subtraction.
    def exitSubtraction(self, ctx:GeraltParser.SubtractionContext):
        pass


    # Enter a parse tree produced by GeraltParser#multiplication.
    def enterMultiplication(self, ctx:GeraltParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by GeraltParser#multiplication.
    def exitMultiplication(self, ctx:GeraltParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by GeraltParser#float.
    def enterFloat(self, ctx:GeraltParser.FloatContext):
        pass

    # Exit a parse tree produced by GeraltParser#float.
    def exitFloat(self, ctx:GeraltParser.FloatContext):
        pass


    # Enter a parse tree produced by GeraltParser#parenthesis.
    def enterParenthesis(self, ctx:GeraltParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by GeraltParser#parenthesis.
    def exitParenthesis(self, ctx:GeraltParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by GeraltParser#int.
    def enterInt(self, ctx:GeraltParser.IntContext):
        pass

    # Exit a parse tree produced by GeraltParser#int.
    def exitInt(self, ctx:GeraltParser.IntContext):
        pass


    # Enter a parse tree produced by GeraltParser#addition.
    def enterAddition(self, ctx:GeraltParser.AdditionContext):
        pass

    # Exit a parse tree produced by GeraltParser#addition.
    def exitAddition(self, ctx:GeraltParser.AdditionContext):
        pass


    # Enter a parse tree produced by GeraltParser#type.
    def enterType(self, ctx:GeraltParser.TypeContext):
        pass

    # Exit a parse tree produced by GeraltParser#type.
    def exitType(self, ctx:GeraltParser.TypeContext):
        pass



del GeraltParser