import coverage
import unittest

from lexer import Tokenize


class TestTokenize(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenize('')

    def test_tokenize_number(self):
        self.tokenizer.code = '123 456'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('DIGIT', '123'), ('DIGIT', '456')])

    def test_tokenize_reserved_word_or_identifier(self):
        self.tokenizer.code = 'if foo bar'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('IfToken', 'if'), ('IDENTIFIER', 'foo'), ('IDENTIFIER', 'bar')])

    def test_tokenize_symbol(self):
        self.tokenizer.code = '== && ( ) = { } > < : + - * / % \"'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('DoubleEqualToken', '=='), ('LogicalAndToken', '&&'),
                                                 ('LeftParenToken', '('), ('RightParenToken', ')'),
                                                 ('SingleEqualToken', '='), ('LeftBraceToken', '{'),
                                                 ('RightBraceToken', '}'), ('GreaterThanToken', '>'),
                                                 ('LessThanToken', '<'), ('ColonToken', ':'), ('PlusToken', '+'),
                                                 ('MinusToken', '-'), ('MultiplicationToken', '*'),
                                                 ('DivisionToken', '/'), ('ModToken', '%'), ('DoubleQuoteToken', '\"')])

    def test_tokenize(self):
        self.tokenizer.code = '(while 5 < 2 (= a 3))'
        tokens = self.tokenizer.tokenize()
        self.assertEqual(tokens, [('LeftParenToken', '('), ('WhileToken', 'while'), ('DIGIT', '5'),
                                  ('LessThanToken', '<'), ('DIGIT', '2'), ('LeftParenToken', '('),
                                  ('SingleEqualToken', '='), ('IDENTIFIER', 'a'), ('DIGIT', '3'), ('RightParenToken', ')'), ('RightParenToken', ')')])

    def test_tokenize2(self):
        self.tokenizer.code = '(+ 3 2)'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('LeftParenToken', '('), ('PlusToken', '+'), ('DIGIT', '3'),
                                                 ('DIGIT', '2'), ('RightParenToken', ')')])

    def test_tokenize1(self):
        self.tokenizer.code = '(if (-5 3) == 6' \
                              '(print lastName))'
        self.tokenizer.tokenize()
        self.assertEqual(self.tokenizer.tokens, [('LeftParenToken', '('), ('IfToken', 'if'), ('LeftParenToken', '('),
                                                 ('MinusToken', '-'), ('DIGIT', '5'), ('DIGIT', '3'), ('RightParenToken', ')'),
                                                 ('DoubleEqualToken', '=='), ('DIGIT', '6'),
                                                 ('LeftParenToken', '('), ('PrintToken', 'print'),
                                                 ('IDENTIFIER', 'lastName'), ('RightParenToken', ')'),
                                                 ('RightParenToken', ')')])

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main()
    cov.stop()
    cov.save()
    cov.report()

