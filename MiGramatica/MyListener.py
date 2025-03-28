from antlr4 import *
from MiGramaticaListener import MiGramaticaListener
from MiGramaticaParser import MiGramaticaParser

class MyListener(MiGramaticaListener):
    def __init__(self):
        self.for_loops = []
        self.current_for_loop = None

    def enterForStatement(self, ctx:MiGramaticaParser.ForStatementContext):
        self.current_for_loop = {
            'initialization': ctx.forControl().forInit().getText() if ctx.forControl().forInit() else None,
            'condition': ctx.forControl().expression().getText() if ctx.forControl().expression() else None,
            'update': ctx.forControl().forUpdate().getText() if ctx.forControl().forUpdate() else None,
            'body': ctx.statement().getText(),
            'line': ctx.start.line,
            'column': ctx.start.column
        }
        self.for_loops.append(self.current_for_loop)
        
        print(f"Detected FOR loop at line {ctx.start.line}:")
        print(f"  Initialization: {self.current_for_loop['initialization']}")
        print(f"  Condition: {self.current_for_loop['condition']}")
        print(f"  Update: {self.current_for_loop['update']}")
        print(f"  Body: {self.current_for_loop['body']}")

    def exitForStatement(self, ctx:MiGramaticaParser.ForStatementContext):
        self.current_for_loop = None

    def enterAssignmentStatement(self, ctx:MiGramaticaParser.AssignmentStatementContext):
        variable = ctx.ID().getText()
        value = ctx.expression().getText()
        print(f"Assignment detected: {variable} = {value}")

    def get_for_loops(self):
        return self.for_loops