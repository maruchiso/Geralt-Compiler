# Generated from Geralt.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GeraltParser import GeraltParser
else:
    from GeraltParser import GeraltParser

# This class defines a complete generic visitor for a parse tree produced by GeraltParser.

class GeraltVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GeraltParser#program.
    def visitProgram(self, ctx:GeraltParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#declaration.
    def visitDeclaration(self, ctx:GeraltParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#assign.
    def visitAssign(self, ctx:GeraltParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#input.
    def visitInput(self, ctx:GeraltParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#output.
    def visitOutput(self, ctx:GeraltParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#dividing.
    def visitDividing(self, ctx:GeraltParser.DividingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#var.
    def visitVar(self, ctx:GeraltParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#subtraction.
    def visitSubtraction(self, ctx:GeraltParser.SubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#multiplication.
    def visitMultiplication(self, ctx:GeraltParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#float.
    def visitFloat(self, ctx:GeraltParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#parenthesis.
    def visitParenthesis(self, ctx:GeraltParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#int.
    def visitInt(self, ctx:GeraltParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#addition.
    def visitAddition(self, ctx:GeraltParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#type.
    def visitType(self, ctx:GeraltParser.TypeContext):
        return self.visitChildren(ctx)



del GeraltParser