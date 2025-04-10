# Generated from Geralt.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,97,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,1,1,
        1,1,3,1,29,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,1,1,1,1,
        1,1,1,3,1,44,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,68,8,2,10,2,12,2,
        71,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,79,8,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,90,8,3,10,3,12,3,93,9,3,1,4,1,4,1,4,0,2,4,6,5,
        0,2,4,6,8,0,1,1,0,18,19,112,0,11,1,0,0,0,2,43,1,0,0,0,4,53,1,0,0,
        0,6,78,1,0,0,0,8,94,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,
        0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,16,5,1,0,0,16,
        17,3,8,4,0,17,21,5,20,0,0,18,19,5,25,0,0,19,20,5,21,0,0,20,22,5,
        26,0,0,21,18,1,0,0,0,21,22,1,0,0,0,22,44,1,0,0,0,23,24,5,2,0,0,24,
        28,5,20,0,0,25,26,5,25,0,0,26,27,5,21,0,0,27,29,5,26,0,0,28,25,1,
        0,0,0,28,29,1,0,0,0,29,30,1,0,0,0,30,31,5,3,0,0,31,44,3,4,2,0,32,
        33,5,4,0,0,33,37,5,20,0,0,34,35,5,25,0,0,35,36,5,21,0,0,36,38,5,
        26,0,0,37,34,1,0,0,0,37,38,1,0,0,0,38,44,1,0,0,0,39,40,5,5,0,0,40,
        44,3,4,2,0,41,42,5,5,0,0,42,44,3,6,3,0,43,15,1,0,0,0,43,23,1,0,0,
        0,43,32,1,0,0,0,43,39,1,0,0,0,43,41,1,0,0,0,44,3,1,0,0,0,45,46,6,
        2,-1,0,46,54,5,21,0,0,47,54,5,22,0,0,48,54,5,20,0,0,49,50,5,10,0,
        0,50,51,3,4,2,0,51,52,5,11,0,0,52,54,1,0,0,0,53,45,1,0,0,0,53,47,
        1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,54,69,1,0,0,0,55,56,10,8,0,0,
        56,57,5,6,0,0,57,68,3,4,2,9,58,59,10,7,0,0,59,60,5,7,0,0,60,68,3,
        4,2,8,61,62,10,6,0,0,62,63,5,8,0,0,63,68,3,4,2,7,64,65,10,5,0,0,
        65,66,5,9,0,0,66,68,3,4,2,6,67,55,1,0,0,0,67,58,1,0,0,0,67,61,1,
        0,0,0,67,64,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        5,1,0,0,0,71,69,1,0,0,0,72,73,6,3,-1,0,73,74,5,15,0,0,74,79,3,6,
        3,4,75,79,5,16,0,0,76,79,5,17,0,0,77,79,5,20,0,0,78,72,1,0,0,0,78,
        75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,91,1,0,0,0,80,81,10,7,
        0,0,81,82,5,12,0,0,82,90,3,6,3,8,83,84,10,6,0,0,84,85,5,13,0,0,85,
        90,3,6,3,7,86,87,10,5,0,0,87,88,5,14,0,0,88,90,3,6,3,6,89,80,1,0,
        0,0,89,83,1,0,0,0,89,86,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,
        1,0,0,0,92,7,1,0,0,0,93,91,1,0,0,0,94,95,7,0,0,0,95,9,1,0,0,0,11,
        13,21,28,37,43,53,67,69,78,89,91
    ]

class GeraltParser ( Parser ):

    grammarFileName = "Geralt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'set'", "'='", "'input'", "'print'", 
                     "'Igni'", "'Aard'", "'Quen'", "'Yrden'", "'('", "')'", 
                     "'AND'", "'OR'", "'XOR'", "'NEG'", "'true'", "'false'", 
                     "'Wilk'", "'Kot'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "COMMENT", "WHITE_SPACE", "LBRACK", 
                      "RBRACK" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_booleanExpr = 3
    RULE_type = 4

    ruleNames =  [ "program", "statement", "expr", "booleanExpr", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    INT=21
    FLOAT=22
    COMMENT=23
    WHITE_SPACE=24
    LBRACK=25
    RBRACK=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.StatementContext)
            else:
                return self.getTypedRuleContext(GeraltParser.StatementContext,i)


        def getRuleIndex(self):
            return GeraltParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GeraltParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 54) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GeraltParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OutputContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GeraltParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)


    class InputContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GeraltParser.ID, 0)
        def LBRACK(self):
            return self.getToken(GeraltParser.LBRACK, 0)
        def INT(self):
            return self.getToken(GeraltParser.INT, 0)
        def RBRACK(self):
            return self.getToken(GeraltParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)


    class OutputBoolContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self):
            return self.getTypedRuleContext(GeraltParser.BooleanExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputBool" ):
                listener.enterOutputBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputBool" ):
                listener.exitOutputBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputBool" ):
                return visitor.visitOutputBool(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(GeraltParser.TypeContext,0)

        def ID(self):
            return self.getToken(GeraltParser.ID, 0)
        def LBRACK(self):
            return self.getToken(GeraltParser.LBRACK, 0)
        def INT(self):
            return self.getToken(GeraltParser.INT, 0)
        def RBRACK(self):
            return self.getToken(GeraltParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GeraltParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(GeraltParser.ExprContext,0)

        def LBRACK(self):
            return self.getToken(GeraltParser.LBRACK, 0)
        def INT(self):
            return self.getToken(GeraltParser.INT, 0)
        def RBRACK(self):
            return self.getToken(GeraltParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = GeraltParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = GeraltParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(GeraltParser.T__0)
                self.state = 16
                self.type_()
                self.state = 17
                self.match(GeraltParser.ID)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 18
                    self.match(GeraltParser.LBRACK)
                    self.state = 19
                    self.match(GeraltParser.INT)
                    self.state = 20
                    self.match(GeraltParser.RBRACK)


                pass

            elif la_ == 2:
                localctx = GeraltParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(GeraltParser.T__1)
                self.state = 24
                self.match(GeraltParser.ID)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 25
                    self.match(GeraltParser.LBRACK)
                    self.state = 26
                    self.match(GeraltParser.INT)
                    self.state = 27
                    self.match(GeraltParser.RBRACK)


                self.state = 30
                self.match(GeraltParser.T__2)
                self.state = 31
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = GeraltParser.InputContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(GeraltParser.T__3)
                self.state = 33
                self.match(GeraltParser.ID)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 34
                    self.match(GeraltParser.LBRACK)
                    self.state = 35
                    self.match(GeraltParser.INT)
                    self.state = 36
                    self.match(GeraltParser.RBRACK)


                pass

            elif la_ == 4:
                localctx = GeraltParser.OutputContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(GeraltParser.T__4)
                self.state = 40
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = GeraltParser.OutputBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.match(GeraltParser.T__4)
                self.state = 42
                self.booleanExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GeraltParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DividingContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeraltParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDividing" ):
                listener.enterDividing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDividing" ):
                listener.exitDividing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDividing" ):
                return visitor.visitDividing(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GeraltParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class SubtractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeraltParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtraction" ):
                listener.enterSubtraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtraction" ):
                listener.exitSubtraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtraction" ):
                return visitor.visitSubtraction(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeraltParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GeraltParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GeraltParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GeraltParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class AdditionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.ExprContext)
            else:
                return self.getTypedRuleContext(GeraltParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GeraltParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = GeraltParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 46
                self.match(GeraltParser.INT)
                pass
            elif token in [22]:
                localctx = GeraltParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(GeraltParser.FLOAT)
                pass
            elif token in [20]:
                localctx = GeraltParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(GeraltParser.ID)
                pass
            elif token in [10]:
                localctx = GeraltParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(GeraltParser.T__9)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(GeraltParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 67
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = GeraltParser.SubtractionContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 56
                        self.match(GeraltParser.T__5)
                        self.state = 57
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = GeraltParser.AdditionContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 59
                        self.match(GeraltParser.T__6)
                        self.state = 60
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = GeraltParser.MultiplicationContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 62
                        self.match(GeraltParser.T__7)
                        self.state = 63
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = GeraltParser.DividingContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 65
                        self.match(GeraltParser.T__8)
                        self.state = 66
                        self.expr(6)
                        pass

             
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BooleanExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GeraltParser.RULE_booleanExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegContext(BooleanExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.BooleanExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self):
            return self.getTypedRuleContext(GeraltParser.BooleanExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg" ):
                listener.enterNeg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg" ):
                listener.exitNeg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg" ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(BooleanExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.BooleanExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.BooleanExprContext)
            else:
                return self.getTypedRuleContext(GeraltParser.BooleanExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class BoolvarContext(BooleanExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.BooleanExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GeraltParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolvar" ):
                listener.enterBoolvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolvar" ):
                listener.exitBoolvar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolvar" ):
                return visitor.visitBoolvar(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(BooleanExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.BooleanExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.BooleanExprContext)
            else:
                return self.getTypedRuleContext(GeraltParser.BooleanExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(BooleanExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.BooleanExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(BooleanExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.BooleanExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class XorContext(BooleanExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GeraltParser.BooleanExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeraltParser.BooleanExprContext)
            else:
                return self.getTypedRuleContext(GeraltParser.BooleanExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXor" ):
                listener.enterXor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXor" ):
                listener.exitXor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXor" ):
                return visitor.visitXor(self)
            else:
                return visitor.visitChildren(self)



    def booleanExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GeraltParser.BooleanExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_booleanExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = GeraltParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 73
                self.match(GeraltParser.T__14)
                self.state = 74
                self.booleanExpr(4)
                pass
            elif token in [16]:
                localctx = GeraltParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(GeraltParser.T__15)
                pass
            elif token in [17]:
                localctx = GeraltParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(GeraltParser.T__16)
                pass
            elif token in [20]:
                localctx = GeraltParser.BoolvarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(GeraltParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 89
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = GeraltParser.AndContext(self, GeraltParser.BooleanExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpr)
                        self.state = 80
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 81
                        self.match(GeraltParser.T__11)
                        self.state = 82
                        self.booleanExpr(8)
                        pass

                    elif la_ == 2:
                        localctx = GeraltParser.OrContext(self, GeraltParser.BooleanExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpr)
                        self.state = 83
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 84
                        self.match(GeraltParser.T__12)
                        self.state = 85
                        self.booleanExpr(7)
                        pass

                    elif la_ == 3:
                        localctx = GeraltParser.XorContext(self, GeraltParser.BooleanExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpr)
                        self.state = 86
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 87
                        self.match(GeraltParser.T__13)
                        self.state = 88
                        self.booleanExpr(6)
                        pass

             
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GeraltParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = GeraltParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[3] = self.booleanExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

    def booleanExpr_sempred(self, localctx:BooleanExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         




