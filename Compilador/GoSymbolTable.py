#Dicionario que representa a tabela de simbolos.
symbolTable = [{'scope': 'global', 'print': {'bindable': 'func', 'params': ['', 'string'], 'type': 'string'}, 'println': {'bindable': 'func', 'params': ['', 'string'], 'type': 'string'}}]
# 'int': 'INT',
# 'string': 'STRING',
# 'bool' : 'BOOL',
# 'byte' : 'BYTE',
# 'float' : 'FLOAT',

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
YES = 'yes'
NO = 'no'
USED = 'used'
SWITCHTYPE = 'switchtype'
Number = [INT, FLOAT]
TiposPrimitivos = [INT, FLOAT, BOOL, STRING]

#beginScope = criar um novo escopo
def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope

#basicamente elimina o ultimo escopo
def endScope():
    global symbolTable
    lista_dicionario = []
    for i in symbolTable[-1]:
        if(type(symbolTable[-1][i]) == type({})):
            if (symbolTable[-1][i][USED] == NO):
                lista_dicionario.append(i)
    symbolTable = symbolTable[0:-1]
    return lista_dicionario

#adiciona uma variavel na tabela de simbolos
def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VAR, TYPE: type, USED: NO} #acessa a ultima posição da lista com o nome da variavel ou metodo [nome], associando um dicionario

#adiciona uma função na tabela de simbolos
def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNC, PARAMS: params, TYPE: returnType} #lembrando que params é uma lista, com o identificador e o tipo respectivamente

#ver se a função ou nome de variavel foi definida
def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if(bindableName in symbolTable[i].keys()):
            symbolTable[i][bindableName][USED] = YES
            return symbolTable[i][bindableName]
    return None

# Verifica
def varCheck(listVar):
    if(listVar != None):
        for k in range(len(listVar)):
            print('[Erro]:',listVar[k], 'declarada mas nao usada')