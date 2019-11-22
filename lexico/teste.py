class Carro:

    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
    
    def obterNome(self):
        return self.nome

    def obterAno(self):
        return self.ano

carro = Carro('Camaro', 2010)
print(carro.obterNome())
print(carro.obterAno())