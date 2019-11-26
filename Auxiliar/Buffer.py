class Buffer:

    def __init__(self, apontadorInicial, apontadorFinal, apontadorAtual):
        self.apontadorInicial = apontadorInicial
        self.apontadorFinal = apontadorFinal
        self.apontadorAtual = apontadorAtual

    def proximo():
        apontadorAtual += 1 #anda uma posição
        return apontadorAtual-1 #retorna o valor da posição anterior

    def marcarInicio():
        apontadorInicial = apontadorAtual #marca o inicio do lexema

    def marcarUltimo():
        apontadorFinal = apontadorAtual #marca o fim do lexema

    def retrair(value):
        apontadorAtual = apontadorAtual - value #volta o apontador x posições

    def retrairAoUltimo():
        apontadorAtual = apontadorAtual - 1

    def lexema():
        lex = substring(apontadorInicial, apontadorFinal) #concatena os caracteres
        return lex #retorna o lexema