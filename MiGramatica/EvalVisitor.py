from antlr4 import *
from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}
        self.loop_iterations = []

    def visitProgram(self, ctx:MiGramaticaParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitForStatement(self, ctx:MiGramaticaParser.ForStatementContext):
        initial_context = self.visit(ctx.forControl().forInit())
        
        iteration_details = {
            'iterations': [],
            'variables_state': []
        }
        
        while self.visit(ctx.forControl().expression()):
            iteration_variables = self.variables.copy()
            iteration_details['variables_state'].append(iteration_variables)
            
            body_result = self.visit(ctx.statement())
            iteration_details['iterations'].append(body_result)
            
            self.visit(ctx.forControl().forUpdate())
        
        self.loop_iterations.append(iteration_details)
        return iteration_details

    def visitAssignmentStatement(self, ctx:MiGramaticaParser.AssignmentStatementContext):
        variable = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[variable] = value
        return value

    def visitExpression(self, ctx:MiGramaticaParser.ExpressionContext):
        if ctx.getText().isdigit():
            return int(ctx.getText())
        
        if ctx.ID():
            return self.variables.get(ctx.ID().getText(), 0)
        
        if ctx.MULT():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left * right
        
        if ctx.LT():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left < right
        
        if ctx.PLUS():
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return left + right
        
        return self.visitChildren(ctx)

    def get_loop_iterations(self):
        return self.loop_iterations