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
        
        #print(f"DEBUG Declaration: type = {variable_type}, name = {variable_name}")
        return DeclarationNode(variable_type=variable_type, variable_name=variable_name)

    def visitAssign(self, ctx):
        variable_name = ctx.ID().getText()
        # Result of visit expression on right side
        value = self.visit(ctx.expr())
        
        return AssignNode(variable_name=variable_name, value=value)
    
    def visitInput(self, ctx):
        variable_name = ctx.ID().getText()
        
        return InputNode(variable_name=variable_name)
    
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
    