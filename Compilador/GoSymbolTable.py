#Dicionario que representa a tabela de simbolos.
symbolTable = []
# 'int': 'INT',
#     'string': 'STRING',
#     'bool' : 'BOOL',
#     'byte' : 'BYTE',
#     'float' : 'FLOAT',

# break
# default
# case
# struct
# else
# switch
# const
# if
# range
# continue
# for
# return
# var

INT = 'int'
FLOAT = 'float'
STRING = 'string'
BOOL = 'bool'
BYTE = 'byte'
TYPE = 'type'
PARAMS = 'params'
FUNC = 'func'
CONST = 'const'
BREAK = 'break'
DEFAULT = 'default'
IF = 'if'
RANGE = 'range'
CASE = 'case'
MAP = 'map'
STRUCT = 'struct'
CONTINUE = 'continue'
FOR = 'for'
ELSE = 'else'
SWITCH = 'switch'
RETURN = 'return'
VAR = 'var'
TRUE = 'true'
FALSE = 'false'
PRINT = 'print'
PRINTLN = 'println'
BINDABLE = 'bindable'
SCOPE = 'scope'
Number = [INT, FLOAT]

#beginScope = criar um novo escopo
def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope

#basicamente elimina o ultimo escopo
def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]

#adiciona uma variavel na tabela de simbolos
def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VAR, TYPE: type} #acessa a ultima posição da lista com o nome da variavel ou metodo [nome], associando um dicionario

#adiciona uma função na tabela de simbolos
def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNC, PARAMS: params, TYPE: returnType} #lembrando que params é uma lista, com o identificador e o tipo respectivamente

#ver se a função ou nome de variavel foi definida
def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if(bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None
