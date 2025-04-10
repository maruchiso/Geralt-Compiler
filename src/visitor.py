from antlr4 import *
from antlr.GeraltVisitor import GeraltVisitor
from antlr.GeraltParser import GeraltParser
from ast_nodes import * 

class WitcherVisitor(GeraltVisitor):
    def visitProgram(self, ctx):
        statements = [self.visit(statement) for statement in ctx.statement()]
        return ProgramNode(statements=statements)
    
    def visitDeclaration(self, ctx):
        variable_type = self.visit(ctx.type_())
        variable_name = ctx.ID().getText()
        if ctx.getToken(GeraltParser.INT, 0):
            size = int(ctx.getToken(GeraltParser.INT, 0).getText())
        else:
            size = None

            
        #print(f"DEBUG Declaration: type = {variable_type}, name = {variable_name}")
        return DeclarationNode(variable_type=variable_type, variable_name=variable_name, size=size)

    def visitAssign(self, ctx):
        variable_name = ctx.ID().getText()
        # Result of visit expression on right side
        value = self.visit(ctx.expr())
        token = ctx.getToken(GeraltParser.INT, 0)
        if token:
            index = int(token.getText())
        else:
            index = None

        return AssignNode(variable_name=variable_name, value=value, index=index)
    
    def visitInput(self, ctx):
        variable_name = ctx.ID().getText()
        if ctx.INT():
            index = int(ctx.INT().getText())
        else:
            index = None
            
        return InputNode(variable_name=variable_name, index=index)
    
    def visitOutput(self, ctx):
        value = self.visit(ctx.expr())
        
        return OutputNode(value=value)
    
    def visitDividing(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return BinOpNode(left=left, operator='/', right=right)
    
    def visitVar(self, ctx):
        name = ctx.getText()

        return VarNode(name=name)
    
    def visitSubtraction(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return BinOpNode(left=left, operator='-', right=right)
    
    def visitMultiplication(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return BinOpNode(left=left, operator='*', right=right)
    
    def visitFloat(self, ctx):
        value = ctx.getText()
        
        return NumberNode(float(value))
    
    def visitParenthesis(self, ctx):
        return self.visit(ctx.expr())
    
    def visitInt(self, ctx):
        value = ctx.getText()
        
        return NumberNode(int(value))
    
    def visitAddition(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return BinOpNode(left=left, operator='+', right=right)
    
    def visitType(self, ctx):
        return ctx.getText()
    
    def visitTrue(self, ctx):
        return BooleanNode(value=True)

    def visitFalse(self, ctx):
        return BooleanNode(value=False)

    def visitBoolvar(self, ctx):
        name = ctx.getText()
        return VarNode(name=name)

    def visitAnd(self, ctx):
        left = self.visit(ctx.booleanExpr(0))
        right = self.visit(ctx.booleanExpr(1))
        return BinOpBoolNode(left=left, operator='AND', right=right)

    def visitOr(self, ctx):
        left = self.visit(ctx.booleanExpr(0))
        right = self.visit(ctx.booleanExpr(1))
        return BinOpBoolNode(left=left, operator='OR', right=right)

    def visitXor(self, ctx):
        left = self.visit(ctx.booleanExpr(0))
        right = self.visit(ctx.booleanExpr(1))
        return BinOpBoolNode(left=left, operator='XOR', right=right)

    def visitNeg(self, ctx):
        operand = self.visit(ctx.booleanExpr())
        return NegNode(operator='NEG', operand=operand)


    def visitOutputBool(self, ctx):
        value = self.visit(ctx.booleanExpr())
        return OutputNode(value=value)
