# ------------------------------------------------------------
# goLex.py
#
# tokenizer for a simplification language Golang(Go)
# ------------------------------------------------------------

import ply.lex as lex

reserved = {
    'break' : 'BREAK',
    'default': 'DEFAULT',
    'func': 'FUNC',
    'const': 'CONST',
    'if': 'IF',
    'range': 'RANGE',
    'case': 'CASE',
    'map': 'MAP',
    'struct': 'STRUCT',
    'type': 'TYPE',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'return': 'RETURN',
    'var': 'VAR',
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'int': 'INT',
    'string': 'STRING',
    'bool' : 'BOOL',
    'byte' : 'BYTE',
    'float' : 'FLOAT',
    'print': 'PRINT',
    'println': 'PRINTLN'
}

# List of token names.   This is always required
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POT',
    'EQUALS',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LCHAVES',
    'RCHAVES',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'AND',
    'OR',
    'SEMICOLON',
    'TWOPOINTS',
     'COMMA'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_EQUALS        = r'=='
t_ASSIGN        = r'\='
t_GREATER       = r'\>'
t_LESS          = r'\<'
t_GREATER_EQUAL = r'\>='
t_LESS_EQUAL    = r'\<='
t_AND           = r'\&&'
t_OR            = r'\||'
t_POT           = r'\^'
t_LCHAVES       = r'\{'
t_RCHAVES       = r'\}'
t_SEMICOLON     = r'\;'
t_TWOPOINTS     = r'\:'
t_COMMA = r'\,' 
 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Indentacao # Wedson Help
ArrayTabulacao = [0]
IndicePosicao = 0
ConstTabulacao = 8

def t_IDENTATION(t):
    r'\n[ \t]*'
    global IndicePosicao
    global ConstTabulacao
    Tamanho = 0
    
    for i in t.value:
        if(i == ' '):
            Tamanho += 1
        else:
            if(i != '\n'):
                Auxiliar = Tamanho // ConstTabulacao
                Tamanho = (Auxiliar + 1) * ConstTabulacao

    if(ArrayTabulacao[IndicePosicao] < Tamanho):
        ArrayTabulacao.append(Tamanho)
        IndicePosicao += 1
    if(ArrayTabulacao[IndicePosicao] > Tamanho):
        if(Tamanho in ArrayTabulacao):
            del ArrayTabulacao[ArrayTabulacao.index(Tamanho)+1:len(ArrayTabulacao)]
            IndicePosicao = ArrayTabulacao.index(Tamanho)
        else:
            print("Identação ilegal foi encontrada")

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_coment(t):
    #r'(\/{2}.+)|(\/\*\*\/)' Tentando pegar o de várias linhas btm
    r'(\/{2}.+)'
    pass

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0], t.lineno, t.lexpos)
    t.lexer.skip(1)

# START A CLASSE LEXER
lexer = lex.lex()

data = '''
int variavel = 10
// Isto é comentário
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