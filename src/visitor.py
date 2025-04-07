from antlr4 import *
from antlr.GeraltVisitor import GeraltVisitor
from antlr.GeraltParser import GeraltParser

class WitcherVisitor(GeraltVisitor):
    def visitProgram(self, ctx):
        print("Medalion drży, to miejsce mocy!")
        
        # Visit each statement in program.
        for child in ctx.statement():
            self.visit(child)
        
        print("Zaraza, uspokój się Płotka")
        
        return None
    
    def visitDeclaration(self, ctx):
        # Get type of variable (Wilk or Kot)
        variable_type = ctx.type_().getText()
        # Get name of variable
        variable_name = ctx.ID().getText()
        print(f"Declared variable: {variable_name} of type {variable_type}")
        
        return None
    
    def visitAssign(self, ctx):
        variable_name = ctx.ID().getText()
        # Result of visit expression on right side
        expr = self.visit(ctx.expr())
        print(f"Assign to {variable_name} the value of: {expr}")
        
        return None
    
    def visitInput(self, ctx):
        variable_name = ctx.ID().getText()
        print(f"Input value for variable: {variable_name}")
        
        return None
    
    def visitOutput(self, ctx):
        value = self.visit(ctx.expr())
        print(f"Output value: {value}")
        
        return None
    
    def visitDividing(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return f"({left} / {right})"
    
    
    def visitVar(self, ctx):
        return ctx.getText()
    
    def visitSubtraction(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return f"({left} - {right})"
    
    def visitDividing(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return f"({left} / {right})"
    
    def visitMultiplication(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return f"({left} * {right})"
    
    def visitFloat(self, ctx):
        return ctx.getText()
    
    def visitParenthesis(self, ctx):
        return f"({self.visit(ctx.expr)})"
    
    def visitInt(self, ctx):
        return ctx.getText()
    
    def visitAddition(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return f"({left} + {right})"
    
    def visitType(self, ctx):
        return ctx.getText()
    