# Lexer

Python tokenizer that is the first step of a compiler project.

This lexer converts an input such as "(+ 3 2)" into a list of tokens:

[('LeftParenToken', '('), ('PlusToken', '+'), ('DIGIT', '3'), ('DIGIT', '2'), ('RightParenToken', ')')]
