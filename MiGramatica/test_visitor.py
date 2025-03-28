import unittest
from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

class TestEvalVisitor(unittest.TestCase):
    def test_for_loop_simulation(self):
        input_code = """
        for (i = 0; i < 5; i = i + 1) {
            x = i * 2;
        }
        """
        
        input_stream = InputStream(input_code)
        lexer = MiGramaticaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiGramaticaParser(stream)
        tree = parser.program()
        
        visitor = EvalVisitor()
        visitor.visit(tree)
        
        loop_iterations = visitor.get_loop_iterations()
        self.assertEqual(len(loop_iterations), 1)
        
        iteration_details = loop_iterations[0]
        self.assertEqual(len(iteration_details['iterations']), 5)
        self.assertEqual(len(iteration_details['variables_state']), 5)

if __name__ == '__main__':
    unittest.main()