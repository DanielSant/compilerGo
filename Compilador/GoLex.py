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
    'type': 'TYPE',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'return': 'RETURN',
    'var': 'VAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'int': 'INT',
    'string': 'STRING',
    'bool' : 'BOOL',
    'byte' : 'BYTE',
    'float' : 'FLOAT',
}

# List of token names.   This is always required
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'DIFERENTE',
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
    'COLON',
    'COMMA',
    'MOD',
    'DPLUS',
    'DMINUS',
    'COLONEQ'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS          = r'\+'
t_MINUS         = r'\-'
t_TIMES         = r'\*'
t_DIVIDE        = r'\/'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_EQUALS        = r'\=='
t_DIFERENTE     = r'\!='
t_ASSIGN        = r'\='
t_GREATER       = r'\>'
t_LESS          = r'\<'
t_GREATER_EQUAL = r'\>='
t_LESS_EQUAL    = r'\<='
t_AND           = r'\&&'
t_OR            = r'\|\|'
t_LCHAVES       = r'\{'
t_RCHAVES       = r'\}'
t_SEMICOLON     = r'\;'
t_COLON         = r'\:'
t_COMMA         = r'\,'
t_MOD           = r'\%'
t_DPLUS         = r'\+\+'
t_DMINUS        = r'\-\-'
t_COLONEQ       = r'\:\='
 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.type = reserved.get(t.value, 'STRING')
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
    
# Tipo da funcao não esta sendo printado
data = '''
func factorial(x int) int {
	if x == 0 {
		return 1;
	};
	return x * factorial(x-1);
}

func principal(par1 int, par2 bool) string {
    type ohloko int;
    type newString string;
    var b newString = "Daniel";
    const (z ohloko = 15;);
    return b;
}

func principal2() string {
    type newString string;
    var l newString = "Daniel";
    var b newString = "Daniel";
    var d = 1;
    var e = principal(e, d);
    if 3 > 4 {
        var g = true;
        var f = principal(d, g);
    };
    var f int = 2;
    if f || b{println(b);};
    for k := 0; k < 15; k++ {println(b);};
    const (z int = 15;);
    return b;
}

func tests(prm int) int {
    //Definicao de tipos
    type integer int;
    type charset string;
    type boolean bool;

    //Variaveis
    var a = "initial";
    var b, c int = 1, 2;
    var d = true;
    var e int;
    f := "apple";
    var idade integer = 21;
    var nome, sobrenome charset = "Jhonatan", "Bitencourt";
    var TorF boolean = true;
    var aTrueVar boolean = true;
    var aFalseVar boolean = false;

    //Constantes
    const n = 500000000;
    const (
        z int = 15;
        y string = "Teste";
    );

    //For's
    i := 1;
    for i <= 3 {
        i = i + 1;
    };

    for j := 7; j <= 9; j++ {
        println(j);
    };

    for n := 0; n <= 5; n++ {
        if n%2 == 0 {
            continue;
        };
        println(n);
    };

    //If If-else
    if 7%2 == 0 {
        println("7 is even");
    } else {
        println("7 is odd");
    };

    if 8%4 == 0 {
        println("8 is divisible by 4");
    };

    if aFalseVar || aTrueVar {
        println("here we are, OR not");
    };

    if aFalseVar && aTrueVar {
        println("AND here we are");
    };

    if 8>5 {
        println("8 is greater than 5");
    };

    if 2<5 {
        println("2 is less than 5");
    } else {
        println("how did you get here?");
    };

    //Switch
    variable := 1;
    switch variable {
        case 1:
            println("one");
        case 2:
            println("two");
        case 3:
            println("three");
    };
    //FunctionCalls
    b = factorial(4);
    f = principal(idade, TorF);
    print(nome);
    print(sobrenome);
    var result = factorial(2) - 9 + 3;
    result = result * 2;
    //return
    return result;
}
// Isto é comentário
'''



lexer.input(data)