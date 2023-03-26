class Tokenize:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.tokens = []

    class TokenizeException(Exception):
        pass

    def tokenize_number(self):
        digits = ''
        while self.position < len(self.code) and self.code[self.position].isdigit():
            digits += self.code[self.position]
            self.position += 1
        if len(digits) > 0:
            self.tokens.append(('DIGIT', digits))

    def tokenize_reserved_word_or_identifier(self):
        name = ''
        if self.position < len(self.code) and self.code[self.position].isalpha():
            name += self.code[self.position]
            self.position += 1
            while self.position < len(self.code) and self.code[self.position].isalnum():
                name += self.code[self.position]
                self.position += 1

        if len(name) > 0:
            if name == 'if':
                self.tokens.append(('IfToken', name))
            elif name == 'while':
                self.tokens.append(('WhileToken', name))
            elif name == 'for':
                self.tokens.append(('ForToken', name))
            elif name == 'var':
                self.tokens.append(('VarToken', name))
            elif name == 'def':
                self.tokens.append(('DefToken', name))
            elif name == 'print':
                self.tokens.append(('PrintToken', name))
            else:
                self.tokens.append(('IDENTIFIER', name))

    def tokenize_symbol(self):
        if self.position + 1 < len(self.code):
            if self.code[self.position:self.position + 2] == '==':
                self.tokens.append(('DoubleEqualToken', '=='))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '>=':
                self.tokens.append(('GreaterOrEqualToken', '>='))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '<=':
                self.tokens.append(('LessOrEqualToken', '<='))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '&&':
                self.tokens.append(('LogicalAndToken', '&&'))
                self.position += 2
            elif self.code[self.position:self.position + 2] == '||':
                self.tokens.append(('LogicalOrToken', '||'))
                self.position += 2
        if self.code[self.position] == '(':
            self.tokens.append(('LeftParenToken', '('))
            self.position += 1
        elif self.code[self.position] == ')':
            self.tokens.append(('RightParenToken', ')'))
            self.position += 1
        elif self.code[self.position] == '=':
            self.tokens.append(('SingleEqualToken', '='))
            self.position += 1
        elif self.code[self.position] == '{':
            self.tokens.append(('LeftBraceToken', '{'))
            self.position += 1
        elif self.code[self.position] == '}':
            self.tokens.append(('RightBraceToken', '}'))
            self.position += 1
        elif self.code[self.position] == '<':
            self.tokens.append(('LessThanToken', '<'))
            self.position += 1
        elif self.code[self.position] == '>':
            self.tokens.append(('GreaterThanToken', '>'))
            self.position += 1
        elif self.code[self.position] == ':':
            self.tokens.append(('ColonToken', ':'))
            self.position += 1
        elif self.code[self.position] == '+':
            self.tokens.append(('PlusToken', '+'))
            self.position += 1
        elif self.code[self.position] == '-':
            self.tokens.append(('MinusToken', '-'))
            self.position += 1
        elif self.code[self.position] == '*':
            self.tokens.append(('MultiplicationToken', '*'))
            self.position += 1
        elif self.code[self.position] == '/':
            self.tokens.append(('DivisionToken', '/'))
            self.position += 1
        elif self.code[self.position] == '%':
            self.tokens.append(('ModToken', '%'))
            self.position += 1
        elif self.code[self.position] == '\"':
            self.tokens.append(('DoubleQuoteToken', '\"'))
            self.position += 1

    def tokenize(self):
        while self.position < len(self.code):
            cur_pos = self.position
            if self.code[self.position] == ' ':
                self.position += 1
            elif self.code[self.position].isdigit():
                self.tokenize_number()
            elif self.code[self.position].isalpha():
                self.tokenize_reserved_word_or_identifier()
            else:
                self.tokenize_symbol()
            if cur_pos == self.position:
                raise self.TokenizeException(f'Couldn\'t parse this character {self.code[self.position]}')
        return self.tokens
