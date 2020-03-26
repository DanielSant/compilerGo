from abc import abstractclassmethod
from abc import ABCMeta

class FunctionDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

class DefinirFunc(FunctionDecl):
    def __init__(self, FUNC, ID, Signature):
        self.FUNC = FUNC
        self.ID = ID
        self.Signature = Signature

    def accept(self, Visitor):
        Visitor.visitDefinirFunc(self)

class DefinirFuncBody(FunctionDecl):
    def __init__(self, FUNC, ID, Signature, FunctionBody):
        self.FUNC = FUNC
        self.ID = ID
        self.Signature = Signature
        self.FunctionBody = FunctionBody

    def accept(self, Vistor):
        Vistor.visitDefinirFuncBody(self)

