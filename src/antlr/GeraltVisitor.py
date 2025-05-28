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


    # Visit a parse tree produced by GeraltParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:GeraltParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#declaration.
    def visitDeclaration(self, ctx:GeraltParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#arrayAssign.
    def visitArrayAssign(self, ctx:GeraltParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#assign.
    def visitAssign(self, ctx:GeraltParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#arrayInput.
    def visitArrayInput(self, ctx:GeraltParser.ArrayInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#input.
    def visitInput(self, ctx:GeraltParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#output.
    def visitOutput(self, ctx:GeraltParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#outputBool.
    def visitOutputBool(self, ctx:GeraltParser.OutputBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#returnStatement.
    def visitReturnStatement(self, ctx:GeraltParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#ifStatement.
    def visitIfStatement(self, ctx:GeraltParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#whileStatement.
    def visitWhileStatement(self, ctx:GeraltParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#structAsign.
    def visitStructAsign(self, ctx:GeraltParser.StructAsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#structFieldPrint.
    def visitStructFieldPrint(self, ctx:GeraltParser.StructFieldPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#dividing.
    def visitDividing(self, ctx:GeraltParser.DividingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#string.
    def visitString(self, ctx:GeraltParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#var.
    def visitVar(self, ctx:GeraltParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#subtraction.
    def visitSubtraction(self, ctx:GeraltParser.SubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#structAccessExpr.
    def visitStructAccessExpr(self, ctx:GeraltParser.StructAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#float.
    def visitFloat(self, ctx:GeraltParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#exprTrue.
    def visitExprTrue(self, ctx:GeraltParser.ExprTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#parenthesis.
    def visitParenthesis(self, ctx:GeraltParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#int.
    def visitInt(self, ctx:GeraltParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#functionCallNum.
    def visitFunctionCallNum(self, ctx:GeraltParser.FunctionCallNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#exprFalse.
    def visitExprFalse(self, ctx:GeraltParser.ExprFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#arrayAccess.
    def visitArrayAccess(self, ctx:GeraltParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#multiplication.
    def visitMultiplication(self, ctx:GeraltParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#addition.
    def visitAddition(self, ctx:GeraltParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#indexes.
    def visitIndexes(self, ctx:GeraltParser.IndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#neg.
    def visitNeg(self, ctx:GeraltParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#compare.
    def visitCompare(self, ctx:GeraltParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#functionCallBool.
    def visitFunctionCallBool(self, ctx:GeraltParser.FunctionCallBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#or.
    def visitOr(self, ctx:GeraltParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#boolvar.
    def visitBoolvar(self, ctx:GeraltParser.BoolvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#and.
    def visitAnd(self, ctx:GeraltParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#true.
    def visitTrue(self, ctx:GeraltParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#false.
    def visitFalse(self, ctx:GeraltParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#xor.
    def visitXor(self, ctx:GeraltParser.XorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#lessThan.
    def visitLessThan(self, ctx:GeraltParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#lessEqual.
    def visitLessEqual(self, ctx:GeraltParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#greaterThan.
    def visitGreaterThan(self, ctx:GeraltParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#greaterEqual.
    def visitGreaterEqual(self, ctx:GeraltParser.GreaterEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#equal.
    def visitEqual(self, ctx:GeraltParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#notEqual.
    def visitNotEqual(self, ctx:GeraltParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#classDecl.
    def visitClassDecl(self, ctx:GeraltParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#classBody.
    def visitClassBody(self, ctx:GeraltParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#classMember.
    def visitClassMember(self, ctx:GeraltParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#visibility.
    def visitVisibility(self, ctx:GeraltParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#structDecl.
    def visitStructDecl(self, ctx:GeraltParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#structFields.
    def visitStructFields(self, ctx:GeraltParser.StructFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#structFieldAccess.
    def visitStructFieldAccess(self, ctx:GeraltParser.StructFieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#jezeliBlock.
    def visitJezeliBlock(self, ctx:GeraltParser.JezeliBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#dopokiBlock.
    def visitDopokiBlock(self, ctx:GeraltParser.DopokiBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#block.
    def visitBlock(self, ctx:GeraltParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#functionDecl.
    def visitFunctionDecl(self, ctx:GeraltParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#parameters.
    def visitParameters(self, ctx:GeraltParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#parameter.
    def visitParameter(self, ctx:GeraltParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#functionCall.
    def visitFunctionCall(self, ctx:GeraltParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#arguments.
    def visitArguments(self, ctx:GeraltParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GeraltParser#type.
    def visitType(self, ctx:GeraltParser.TypeContext):
        return self.visitChildren(ctx)



del GeraltParser