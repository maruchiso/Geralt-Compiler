from antlr4 import *
from antlr.GeraltVisitor import GeraltVisitor
from antlr.GeraltParser import GeraltParser
from ast_nodes import * 

class WitcherVisitor(GeraltVisitor): 
    def visitProgram(self, ctx):
        print("DEBUG: visitProgram called")
        nodes = []
        for i, child in enumerate(ctx.children):
            print(f"DEBUG: child {i} = {child.getText()}, class = {type(child).__name__}")
            node = self.visit(child)
            if node is not None:
                nodes.append(node)
            else:
                print(f"visit() returned None for child {i}")
        return ProgramNode(statements=nodes)
    
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

    def visitIndexes(self, ctx:GeraltParser.IndexesContext):
        index_exprs = [self.visit(e) for e in ctx.expr()]
        print(f"DEBUG: visitIndexes → {index_exprs}")
        return index_exprs

    def visitArrayAccess(self, ctx):
        name = ctx.ID().getText()
        indexes = self.visit(ctx.indexes())
        return ArrayAccessNode(name=name, indexes=indexes)

    def visitArrayDeclaration(self, ctx:GeraltParser.ArrayDeclarationContext):
        print("DEBUG: visitArrayDeclaration triggered")
        variable_type = ctx.type_().getText()
        variable_name = ctx.ID().getText()
        dimensions = self.visit(ctx.indexes())
        print(f"DEBUG: Declaring array {variable_name} of type {variable_type} with dims {dimensions}")
        resolved_dims = []
        for dim in dimensions:
            if isinstance(dim, NumberNode):
                resolved_dims.append(dim.value)
            else:
                raise Exception("Array dimensions must be constant integers")

        return DeclarationNode(variable_type=variable_type, variable_name=variable_name, size=resolved_dims)

    def visitArrayAssign(self, ctx:GeraltParser.ArrayAssignContext):
        print("DEBUG: visitArrayAssign triggered")
        name = ctx.ID().getText()
        indexes = self.visit(ctx.indexes())
        print(f"DEBUG: Assigning to array {name} with indexes {indexes}")
        value = self.visit(ctx.expr())
        return AssignNode(variable_name=name, value=value, index=indexes)

    def visitArrayInput(self, ctx:GeraltParser.ArrayInputContext):
        name = ctx.ID().getText()
        indexes = self.visit(ctx.indexes())
        return InputNode(variable_name=name, index=indexes)

    def visitString(self, ctx):
        raw = ctx.getText()
        return StringNode(value=raw[1:-1])
    
    def visitStructDecl(self, ctx):
        name = ctx.ID().getText()
        fields = []

        field_tokens = ctx.structFields().children
        i = 0
        while i < len(field_tokens):
            # Skip whitespaces / newlines / etc.
            if not hasattr(field_tokens[i], 'getText'):
                i += 1
                continue

            typ = field_tokens[i].getText()
            var = field_tokens[i + 1].getText()
            fields.append((typ, var))
            i += 2

        print(f"VISITOR STRUCT: {name} with fields {fields}")
        return StructDefNode(name, fields)


    def visitStructFieldAccess(self, ctx):
        struct_var = ctx.ID(0).getText()
        field_name = ctx.ID(1).getText()
        return StructAccessNode(struct_var, field_name)

    def visitStructAsign(self, ctx):
        access = ctx.structAccess()
        struct_var = access.ID(0).getText()
        field_name = access.ID(1).getText()
        value = self.visit(ctx.expr())
        return AssignNode(variable_name=StructAccessNode(struct_var, field_name), value=value)

