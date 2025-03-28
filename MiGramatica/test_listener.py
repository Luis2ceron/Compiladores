import unittest
from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener

class TestMyListener(unittest.TestCase):
    def test_for_loop_detection(self):
        input_code = """
        for (i = 0; i < 10; i = i + 1) {
            x = i * 2;
        }
        """
        
        input_stream = InputStream(input_code)
        lexer = MiGramaticaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiGramaticaParser(stream)
        tree = parser.program()
        
        listener = MyListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        for_loops = listener.get_for_loops()
        self.assertEqual(len(for_loops), 1)
        
        detected_loop = for_loops[0]
        self.assertEqual(detected_loop['initialization'], 'i=0')
        self.assertEqual(detected_loop['condition'], 'i<10')
        self.assertEqual(detected_loop['update'], 'i=i+1')

if __name__ == '__main__':
    unittest.main()