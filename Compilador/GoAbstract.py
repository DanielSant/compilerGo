from abc import abstractclassmethod
from abc import ABCMeta

##ABSTRATA##
class FunctionDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass
##CONCRETA##
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

##ABSTRATA##
class Signature(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass
##CONCRETA##
class DefinirParams(Signature):
    def __init__(self, Parameters):
        self.Parameters = Parameters

    def accept(self, Visitor):
        Visitor.visitDefinirParams(self)

class DefinirParamsT(Signature):
	def __init__(self, Params, Result):
		self.Params = Params
		self.Result = Result

	def accept(self, Visitor):
		Visitor.visitDefinirParams(self)

