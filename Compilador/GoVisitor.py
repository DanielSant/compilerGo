class Visitor():
    def visitDefinirFunc(self, definirFunc):
        print('FUNC')
        print('ID')
        definirFunc.Signature.accept(self)