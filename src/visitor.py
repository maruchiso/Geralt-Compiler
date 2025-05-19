from antlr4 import *
from antlr.GeraltVisitor import GeraltVisitor
from antlr.GeraltParser import GeraltParser
from ast_nodes import * 

class WitcherVisitor(GeraltVisitor):
    '''
    def visitProgram(self, ctx):
        statements = [self.visit(statement) for statement in ctx.statement()]
        return ProgramNode(statements=statements)
    '''
    def visitProgram(self, ctx):
        statements = [self.visit(statement) for statement in ctx.statement()]
        functions = [self.visit(func) for func in ctx.functionDecl()]
        return ProgramNode(statements + functions)
    
    def visitDeclaration(self, ctx):
        variable_type = ctx.type_().getText()
        variable_name = ctx.ID().getText()
        if ctx.getToken(GeraltParser.INT, 0):
            size = int(ctx.getToken(GeraltParser.INT, 0).getText())
        else:
            size = None

            
        #print(f"DEBUG Declaration: type_ = {variable_type}, name = {variable_name}")
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
    
    def visittype_(self, ctx):
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

    def visitExprTrue(self, ctx):
        return BooleanNode(value=True)

    def visitExprFalse(self, ctx):
        return BooleanNode(value=False)

    def visitBoolTrue(self, ctx):
        return BooleanNode(value=True)

    def visitBoolFalse(self, ctx):
        return BooleanNode(value=False)
    
    def visitJezeliBlock(self, ctx):
        condition = self.visit(ctx.booleanExpr())
        then_body = [self.visit(stmt) for stmt in ctx.block(0).statement()]

        else_body = None
        if ctx.block(1):  # jeśli jest w_przeciwnym_wypadku
            else_body = [self.visit(stmt) for stmt in ctx.block(1).statement()]

        return IfNode(condition=condition, then_body=then_body, else_body=else_body)

    def visitDopokiBlock(self, ctx):
        condition = self.visit(ctx.booleanExpr())
        body = [self.visit(stmt) for stmt in ctx.block().statement()]
        
        return WhileNode(condition=condition, body=body)
    def visitLessThan(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return CompareNode(left=left, op='<', right=right)

    def visitLessEqual(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return CompareNode(left=left, op='<=', right=right)

    def visitGreaterThan(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return CompareNode(left=left, op='>', right=right)

    def visitGreaterEqual(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return CompareNode(left=left, op='>=', right=right)

    def visitEqual(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return CompareNode(left=left, op='==', right=right)

    def visitNotEqual(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return CompareNode(left=left, op='!=', right=right)

    def visitFunctionDecl(self, ctx):
        return_type_ = ctx.type_().getText()
        name = ctx.ID().getText()
        params = []
        if ctx.parameters():
            for p in ctx.parameters().parameter():
                p_type_ = p.type_().getText()
                p_name = p.ID().getText()
                params.append((p_type_, p_name))

        body = [self.visit(stmt) for stmt in ctx.block().statement()]
        
  
        return FunctionDeclNode(return_type_, name, params, body)

    def visitFunctionCallStatement(self, ctx):
        name = ctx.ID().getText()
        args = []
        if ctx.arguments():
            args = [self.visit(e) for e in ctx.arguments().expr()]
        return FunctionCallNode(name, args)
    
    def visitFunctionCallNum(self, ctx):
        name = ctx.functionCall().ID().getText()
        args = []
        if ctx.functionCall().arguments():
            for expr_ctx in ctx.functionCall().arguments().expr():
                args.append(self.visit(expr_ctx))
        return FunctionCallNode(name=name, args=args)
    
    def visitFunctionCallBool(self, ctx):
        name = ctx.functionCall().ID().getText()
        args = []
        if ctx.functionCall().arguments():
            for expr_ctx in ctx.functionCall().arguments().expr():
                args.append(self.visit(expr_ctx))
        return FunctionCallNode(name=name, args=args)

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnNode(value)


    
