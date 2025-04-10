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
        4,1,24,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,54,8,2,10,2,12,2,57,
        9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,4,1,4,1,4,0,2,4,6,5,0,2,
        4,6,8,0,1,1,0,18,19,95,0,11,1,0,0,0,2,29,1,0,0,0,4,39,1,0,0,0,6,
        64,1,0,0,0,8,80,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,
        0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,16,5,1,0,0,16,17,3,
        8,4,0,17,18,5,20,0,0,18,30,1,0,0,0,19,20,5,2,0,0,20,21,5,20,0,0,
        21,22,5,3,0,0,22,30,3,4,2,0,23,24,5,4,0,0,24,30,5,20,0,0,25,26,5,
        5,0,0,26,30,3,4,2,0,27,28,5,5,0,0,28,30,3,6,3,0,29,15,1,0,0,0,29,
        19,1,0,0,0,29,23,1,0,0,0,29,25,1,0,0,0,29,27,1,0,0,0,30,3,1,0,0,
        0,31,32,6,2,-1,0,32,40,5,21,0,0,33,40,5,22,0,0,34,40,5,20,0,0,35,
        36,5,10,0,0,36,37,3,4,2,0,37,38,5,11,0,0,38,40,1,0,0,0,39,31,1,0,
        0,0,39,33,1,0,0,0,39,34,1,0,0,0,39,35,1,0,0,0,40,55,1,0,0,0,41,42,
        10,8,0,0,42,43,5,6,0,0,43,54,3,4,2,9,44,45,10,7,0,0,45,46,5,7,0,
        0,46,54,3,4,2,8,47,48,10,6,0,0,48,49,5,8,0,0,49,54,3,4,2,7,50,51,
        10,5,0,0,51,52,5,9,0,0,52,54,3,4,2,6,53,41,1,0,0,0,53,44,1,0,0,0,
        53,47,1,0,0,0,53,50,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,
        0,0,0,56,5,1,0,0,0,57,55,1,0,0,0,58,59,6,3,-1,0,59,60,5,15,0,0,60,
        65,3,6,3,4,61,65,5,16,0,0,62,65,5,17,0,0,63,65,5,20,0,0,64,58,1,
        0,0,0,64,61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,77,1,0,0,0,66,
        67,10,7,0,0,67,68,5,12,0,0,68,76,3,6,3,8,69,70,10,6,0,0,70,71,5,
        13,0,0,71,76,3,6,3,7,72,73,10,5,0,0,73,74,5,14,0,0,74,76,3,6,3,6,
        75,66,1,0,0,0,75,69,1,0,0,0,75,72,1,0,0,0,76,79,1,0,0,0,77,75,1,
        0,0,0,77,78,1,0,0,0,78,7,1,0,0,0,79,77,1,0,0,0,80,81,7,0,0,0,81,
        9,1,0,0,0,8,13,29,39,53,55,64,75,77
    ]

class GeraltParser ( Parser ):

    grammarFileName = "Geralt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'set'", "'='", "'input'", "'print'", 
                     "'Igni'", "'Aard'", "'Quen'", "'Yrden'", "'('", "')'", 
                     "'AND'", "'OR'", "'XOR'", "'NEG'", "'true'", "'false'", 
                     "'Wilk'", "'Kot'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "COMMENT", "WHITE_SPACE" ]

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
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = GeraltParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(GeraltParser.T__0)
                self.state = 16
                self.type_()
                self.state = 17
                self.match(GeraltParser.ID)
                pass

            elif la_ == 2:
                localctx = GeraltParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(GeraltParser.T__1)
                self.state = 20
                self.match(GeraltParser.ID)
                self.state = 21
                self.match(GeraltParser.T__2)
                self.state = 22
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = GeraltParser.InputContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(GeraltParser.T__3)
                self.state = 24
                self.match(GeraltParser.ID)
                pass

            elif la_ == 4:
                localctx = GeraltParser.OutputContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.match(GeraltParser.T__4)
                self.state = 26
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = GeraltParser.OutputBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.match(GeraltParser.T__4)
                self.state = 28
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = GeraltParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 32
                self.match(GeraltParser.INT)
                pass
            elif token in [22]:
                localctx = GeraltParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(GeraltParser.FLOAT)
                pass
            elif token in [20]:
                localctx = GeraltParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(GeraltParser.ID)
                pass
            elif token in [10]:
                localctx = GeraltParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(GeraltParser.T__9)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(GeraltParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = GeraltParser.SubtractionContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 42
                        self.match(GeraltParser.T__5)
                        self.state = 43
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = GeraltParser.AdditionContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 45
                        self.match(GeraltParser.T__6)
                        self.state = 46
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = GeraltParser.MultiplicationContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 48
                        self.match(GeraltParser.T__7)
                        self.state = 49
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = GeraltParser.DividingContext(self, GeraltParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 51
                        self.match(GeraltParser.T__8)
                        self.state = 52
                        self.expr(6)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = GeraltParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 59
                self.match(GeraltParser.T__14)
                self.state = 60
                self.booleanExpr(4)
                pass
            elif token in [16]:
                localctx = GeraltParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(GeraltParser.T__15)
                pass
            elif token in [17]:
                localctx = GeraltParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(GeraltParser.T__16)
                pass
            elif token in [20]:
                localctx = GeraltParser.BoolvarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(GeraltParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = GeraltParser.AndContext(self, GeraltParser.BooleanExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpr)
                        self.state = 66
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 67
                        self.match(GeraltParser.T__11)
                        self.state = 68
                        self.booleanExpr(8)
                        pass

                    elif la_ == 2:
                        localctx = GeraltParser.OrContext(self, GeraltParser.BooleanExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpr)
                        self.state = 69
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 70
                        self.match(GeraltParser.T__12)
                        self.state = 71
                        self.booleanExpr(7)
                        pass

                    elif la_ == 3:
                        localctx = GeraltParser.XorContext(self, GeraltParser.BooleanExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpr)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        self.match(GeraltParser.T__13)
                        self.state = 74
                        self.booleanExpr(6)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
            self.state = 80
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
         




