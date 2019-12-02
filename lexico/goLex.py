# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex

reserved = {
    'break' : 'BREAK',
    'default': 'DEFAULT',
    'func': 'FUNC',
    'interface': 'INTERFACE',
    'select': 'SELECT',
    'const': 'CONST',
    'if': 'IF',
    'range': 'RANGE',
    'case': 'CASE',
    'defer': 'DEFER',
    'go': 'GO',
    'map': 'MAP',
    'struct': 'STRUCT',
    'type': 'TYPE',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'chan': 'CHAN',
    'else': 'ELSE',
    'goto': 'GOTO',
    'package': 'PACKAGE',
    'switch': 'SWITCH',
    'import': 'IMPORT',
    'return': 'RETURN',
    'var': 'VAR',
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
}

# List of token names.   This is always required
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PAREN_OPEN',
    'PAREN_CLOSE',
    'CHAR',
    'ARRAY',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS        = r'\+'
t_MINUS       = r'-'
t_TIMES       = r'\*'
t_DIVIDE      = r'/'
t_PAREN_OPEN  = r'\('
t_PAREN_CLOSE = r'\)'
t_EQUAL       = r'=='
t_ATTRIBUTE   = r'\='
t_BIG         = r'\>'
t_SMALL       = r'\<'
t_BIGEQUAL    = r'\>='  

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0], t.lineno, t.lexpos)
    t.lexer.skip(1)

# START A CLASSE LEXER
lexer = lex.lex()

data = '''
int variavel = 10;
'''

lexer.input(data)

for tok in lexer:
    print(tok)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)