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


    # Enter a parse tree produced by GeraltParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:GeraltParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by GeraltParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:GeraltParser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by GeraltParser#declaration.
    def enterDeclaration(self, ctx:GeraltParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GeraltParser#declaration.
    def exitDeclaration(self, ctx:GeraltParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GeraltParser#arrayAssign.
    def enterArrayAssign(self, ctx:GeraltParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by GeraltParser#arrayAssign.
    def exitArrayAssign(self, ctx:GeraltParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by GeraltParser#assign.
    def enterAssign(self, ctx:GeraltParser.AssignContext):
        pass

    # Exit a parse tree produced by GeraltParser#assign.
    def exitAssign(self, ctx:GeraltParser.AssignContext):
        pass


    # Enter a parse tree produced by GeraltParser#arrayInput.
    def enterArrayInput(self, ctx:GeraltParser.ArrayInputContext):
        pass

    # Exit a parse tree produced by GeraltParser#arrayInput.
    def exitArrayInput(self, ctx:GeraltParser.ArrayInputContext):
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


    # Enter a parse tree produced by GeraltParser#outputBool.
    def enterOutputBool(self, ctx:GeraltParser.OutputBoolContext):
        pass

    # Exit a parse tree produced by GeraltParser#outputBool.
    def exitOutputBool(self, ctx:GeraltParser.OutputBoolContext):
        pass


    # Enter a parse tree produced by GeraltParser#returnStatement.
    def enterReturnStatement(self, ctx:GeraltParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by GeraltParser#returnStatement.
    def exitReturnStatement(self, ctx:GeraltParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by GeraltParser#ifStatement.
    def enterIfStatement(self, ctx:GeraltParser.IfStatementContext):
        pass

    # Exit a parse tree produced by GeraltParser#ifStatement.
    def exitIfStatement(self, ctx:GeraltParser.IfStatementContext):
        pass


    # Enter a parse tree produced by GeraltParser#whileStatement.
    def enterWhileStatement(self, ctx:GeraltParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by GeraltParser#whileStatement.
    def exitWhileStatement(self, ctx:GeraltParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by GeraltParser#dividing.
    def enterDividing(self, ctx:GeraltParser.DividingContext):
        pass

    # Exit a parse tree produced by GeraltParser#dividing.
    def exitDividing(self, ctx:GeraltParser.DividingContext):
        pass


    # Enter a parse tree produced by GeraltParser#string.
    def enterString(self, ctx:GeraltParser.StringContext):
        pass

    # Exit a parse tree produced by GeraltParser#string.
    def exitString(self, ctx:GeraltParser.StringContext):
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


    # Enter a parse tree produced by GeraltParser#float.
    def enterFloat(self, ctx:GeraltParser.FloatContext):
        pass

    # Exit a parse tree produced by GeraltParser#float.
    def exitFloat(self, ctx:GeraltParser.FloatContext):
        pass


    # Enter a parse tree produced by GeraltParser#exprTrue.
    def enterExprTrue(self, ctx:GeraltParser.ExprTrueContext):
        pass

    # Exit a parse tree produced by GeraltParser#exprTrue.
    def exitExprTrue(self, ctx:GeraltParser.ExprTrueContext):
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


    # Enter a parse tree produced by GeraltParser#functionCallNum.
    def enterFunctionCallNum(self, ctx:GeraltParser.FunctionCallNumContext):
        pass

    # Exit a parse tree produced by GeraltParser#functionCallNum.
    def exitFunctionCallNum(self, ctx:GeraltParser.FunctionCallNumContext):
        pass


    # Enter a parse tree produced by GeraltParser#exprFalse.
    def enterExprFalse(self, ctx:GeraltParser.ExprFalseContext):
        pass

    # Exit a parse tree produced by GeraltParser#exprFalse.
    def exitExprFalse(self, ctx:GeraltParser.ExprFalseContext):
        pass


    # Enter a parse tree produced by GeraltParser#arrayAccess.
    def enterArrayAccess(self, ctx:GeraltParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by GeraltParser#arrayAccess.
    def exitArrayAccess(self, ctx:GeraltParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by GeraltParser#multiplication.
    def enterMultiplication(self, ctx:GeraltParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by GeraltParser#multiplication.
    def exitMultiplication(self, ctx:GeraltParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by GeraltParser#addition.
    def enterAddition(self, ctx:GeraltParser.AdditionContext):
        pass

    # Exit a parse tree produced by GeraltParser#addition.
    def exitAddition(self, ctx:GeraltParser.AdditionContext):
        pass


    # Enter a parse tree produced by GeraltParser#indexes.
    def enterIndexes(self, ctx:GeraltParser.IndexesContext):
        pass

    # Exit a parse tree produced by GeraltParser#indexes.
    def exitIndexes(self, ctx:GeraltParser.IndexesContext):
        pass


    # Enter a parse tree produced by GeraltParser#neg.
    def enterNeg(self, ctx:GeraltParser.NegContext):
        pass

    # Exit a parse tree produced by GeraltParser#neg.
    def exitNeg(self, ctx:GeraltParser.NegContext):
        pass


    # Enter a parse tree produced by GeraltParser#compare.
    def enterCompare(self, ctx:GeraltParser.CompareContext):
        pass

    # Exit a parse tree produced by GeraltParser#compare.
    def exitCompare(self, ctx:GeraltParser.CompareContext):
        pass


    # Enter a parse tree produced by GeraltParser#functionCallBool.
    def enterFunctionCallBool(self, ctx:GeraltParser.FunctionCallBoolContext):
        pass

    # Exit a parse tree produced by GeraltParser#functionCallBool.
    def exitFunctionCallBool(self, ctx:GeraltParser.FunctionCallBoolContext):
        pass


    # Enter a parse tree produced by GeraltParser#or.
    def enterOr(self, ctx:GeraltParser.OrContext):
        pass

    # Exit a parse tree produced by GeraltParser#or.
    def exitOr(self, ctx:GeraltParser.OrContext):
        pass


    # Enter a parse tree produced by GeraltParser#boolvar.
    def enterBoolvar(self, ctx:GeraltParser.BoolvarContext):
        pass

    # Exit a parse tree produced by GeraltParser#boolvar.
    def exitBoolvar(self, ctx:GeraltParser.BoolvarContext):
        pass


    # Enter a parse tree produced by GeraltParser#and.
    def enterAnd(self, ctx:GeraltParser.AndContext):
        pass

    # Exit a parse tree produced by GeraltParser#and.
    def exitAnd(self, ctx:GeraltParser.AndContext):
        pass


    # Enter a parse tree produced by GeraltParser#true.
    def enterTrue(self, ctx:GeraltParser.TrueContext):
        pass

    # Exit a parse tree produced by GeraltParser#true.
    def exitTrue(self, ctx:GeraltParser.TrueContext):
        pass


    # Enter a parse tree produced by GeraltParser#false.
    def enterFalse(self, ctx:GeraltParser.FalseContext):
        pass

    # Exit a parse tree produced by GeraltParser#false.
    def exitFalse(self, ctx:GeraltParser.FalseContext):
        pass


    # Enter a parse tree produced by GeraltParser#xor.
    def enterXor(self, ctx:GeraltParser.XorContext):
        pass

    # Exit a parse tree produced by GeraltParser#xor.
    def exitXor(self, ctx:GeraltParser.XorContext):
        pass


    # Enter a parse tree produced by GeraltParser#lessThan.
    def enterLessThan(self, ctx:GeraltParser.LessThanContext):
        pass

    # Exit a parse tree produced by GeraltParser#lessThan.
    def exitLessThan(self, ctx:GeraltParser.LessThanContext):
        pass


    # Enter a parse tree produced by GeraltParser#lessEqual.
    def enterLessEqual(self, ctx:GeraltParser.LessEqualContext):
        pass

    # Exit a parse tree produced by GeraltParser#lessEqual.
    def exitLessEqual(self, ctx:GeraltParser.LessEqualContext):
        pass


    # Enter a parse tree produced by GeraltParser#greaterThan.
    def enterGreaterThan(self, ctx:GeraltParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by GeraltParser#greaterThan.
    def exitGreaterThan(self, ctx:GeraltParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by GeraltParser#greaterEqual.
    def enterGreaterEqual(self, ctx:GeraltParser.GreaterEqualContext):
        pass

    # Exit a parse tree produced by GeraltParser#greaterEqual.
    def exitGreaterEqual(self, ctx:GeraltParser.GreaterEqualContext):
        pass


    # Enter a parse tree produced by GeraltParser#equal.
    def enterEqual(self, ctx:GeraltParser.EqualContext):
        pass

    # Exit a parse tree produced by GeraltParser#equal.
    def exitEqual(self, ctx:GeraltParser.EqualContext):
        pass


    # Enter a parse tree produced by GeraltParser#notEqual.
    def enterNotEqual(self, ctx:GeraltParser.NotEqualContext):
        pass

    # Exit a parse tree produced by GeraltParser#notEqual.
    def exitNotEqual(self, ctx:GeraltParser.NotEqualContext):
        pass


    # Enter a parse tree produced by GeraltParser#jezeliBlock.
    def enterJezeliBlock(self, ctx:GeraltParser.JezeliBlockContext):
        pass

    # Exit a parse tree produced by GeraltParser#jezeliBlock.
    def exitJezeliBlock(self, ctx:GeraltParser.JezeliBlockContext):
        pass


    # Enter a parse tree produced by GeraltParser#dopokiBlock.
    def enterDopokiBlock(self, ctx:GeraltParser.DopokiBlockContext):
        pass

    # Exit a parse tree produced by GeraltParser#dopokiBlock.
    def exitDopokiBlock(self, ctx:GeraltParser.DopokiBlockContext):
        pass


    # Enter a parse tree produced by GeraltParser#block.
    def enterBlock(self, ctx:GeraltParser.BlockContext):
        pass

    # Exit a parse tree produced by GeraltParser#block.
    def exitBlock(self, ctx:GeraltParser.BlockContext):
        pass


    # Enter a parse tree produced by GeraltParser#functionDecl.
    def enterFunctionDecl(self, ctx:GeraltParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by GeraltParser#functionDecl.
    def exitFunctionDecl(self, ctx:GeraltParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by GeraltParser#parameters.
    def enterParameters(self, ctx:GeraltParser.ParametersContext):
        pass

    # Exit a parse tree produced by GeraltParser#parameters.
    def exitParameters(self, ctx:GeraltParser.ParametersContext):
        pass


    # Enter a parse tree produced by GeraltParser#parameter.
    def enterParameter(self, ctx:GeraltParser.ParameterContext):
        pass

    # Exit a parse tree produced by GeraltParser#parameter.
    def exitParameter(self, ctx:GeraltParser.ParameterContext):
        pass


    # Enter a parse tree produced by GeraltParser#functionCall.
    def enterFunctionCall(self, ctx:GeraltParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by GeraltParser#functionCall.
    def exitFunctionCall(self, ctx:GeraltParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by GeraltParser#arguments.
    def enterArguments(self, ctx:GeraltParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by GeraltParser#arguments.
    def exitArguments(self, ctx:GeraltParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by GeraltParser#type.
    def enterType(self, ctx:GeraltParser.TypeContext):
        pass

    # Exit a parse tree produced by GeraltParser#type.
    def exitType(self, ctx:GeraltParser.TypeContext):
        pass



del GeraltParser