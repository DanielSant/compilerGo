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

##ABSTRATA##
class Result(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Vistor):
		pass
##CONCRETA##
class DefinirTipo(Result):
	def __init__(self, Type):
		self.Type = Type

	def accept(self, Visitor):
		Visitor.visitDefinirTipo(self)

##ABSTRATA##
class Type(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class Tint(Type):
	def __init__(self, INT):
		self.INT = INT

	def accept(self, Visitor):
		Visitor.visitTint(self)

class Tstring(Type):
    def __init__(self, STRING):
        self.STRING = STRING

    def accept(self, Visitor):
        Visitor.visitTstring(self)

class Tbool(Type):
    def __init__(self, BOOL):
        self.BOOL = BOOL

    def accept(self, Visitor):
        Visitor.visitTbool(self)

class Tfloat(Type):
    def __init__(self, FLOAT)
        self.FLOAT = FLOAT

    def accept(self, Visitor):
        Visitor.visitTfloat(self)

##ABSTRATA##
class Parameters(metaclass=ABCMeta):
    @abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class DefinirParams(Parameters):
	def __init__(self,LPAREN,RPAREN):
		self.LPAREN = LPAREN
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitDefinirParams(self)

class Params(Parameters):
    def __init__(self,LPAREN,ParameterList,RPAREN):
    	self.LPAREN = LPAREN
        self.ParameterList = ParameterList
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitParams(self)

class ParamsList(Parameters):
    def __init__(self,LPAREN,ParameterList,COMMA,RPAREN):
    	self.LPAREN = LPAREN
        self.ParameterList = ParameterList
        self.COMMA = COMMA
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitParamsList(self)

##ABSTRATA##
class ParameterList(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class DefinirParamDecl(ParameterList):
    def __init__(self, ParameterDecl):
        self.ParameterDecl = ParameterDecl
    
    def accept(self, Visitor):
        Visitor.visitDefinirParamDecl(self)

class CompParamsDecl(ParameterList): ##PRECISA OBSERVAR ISSO
    def __init__(self, ParameterDecl, COMMA, ParameterDecl):
        self.ParameterDecl = ParameterDecl
        self.COMMA = COMMA
        self.ParameterDecl = ParameterDecl
    def accept(self, Visitor):
        Visitor.visitCompParamsDecl(self)


##ABSTRATA##
class ParameterDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass
##CONCRETA##
class ParamDecl(ParameterDecl):
    def __init__(self, Type):
        self.Type = Type

    def accept(self, Visitor):
        Visitor.visitParamDecl(self)

class ParamIdDecl(ParameterDecl):
    def __init__(self, IdentifierList, Type):
        self.IdentifierList = IdentifierList
        self.Type = Type

    def accept(self, Visitor):
        Visitor.visitParamIdDecl(self)

##ABSTRATA##
class FunctionBody(metaclass=ABCMeta):
    @abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class DefinirBlock(FunctionBody):
    def __init__(self, Block):
        self.Block = Block
    
    def accept(self, Visitor):
        Visitor.visitDefinirBlock(self)

##ABSTRATA##
class Block(metaclass=ABCMeta):
    @abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class DefinirStatement(Block):
    def __init__(self,LCHAVES, StatmentList, RCHAVES):
        self.LCHAVES = LCHAVES
        self.StatmentList = StatmentList
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitDefinirStatement(self)
        
##ABSTRATA##
class StatementList(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class DefinirStatement(StatementList): ##PRECISA OBSERVAR ISSO
    def _init_(self, Statement, SEMICOLON):
        self.Statement = Statement
        self.SEMICOLON = SEMICOLON
    def accept(self, Visitor):
        Visitor.visitDefinirStatement(self)

##ABSTRATA##
class ReturnStmt(metaclass=ABCMeta):
    @abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class SimpleReturn(ReturnStm):
    def _init_(self,RETURN):
        self.RETURN = RETURN

    def accept(self, Visitor):
        Visitor.visitSimpleReturn(self)

class ExpReturn(ReturnStm):
    def _init_(self,RETURN, ExpressionList):
        self.RETURN = RETURN
        self.ExpressionList = ExpressionList
    
    def accept(self, Visitor):
        Visitor.visitExpReturn(self)

 ##ABSTRATA##
class BreakStm(metaclass=ABCMeta):
    @abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA## 
class StmtBreak(BreakStm) :
    def _init_(self,BREAK):
        self.BREAK = BREAK

##ABSTRATA##
class ContinueStmt(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class StmtContinue(ContinueStmt):
    def _init_(self, CONTINUE):
        self.CONTINUE = CONTINUE
    def accept(self, Visitor):
        Visitor.visitStmtContinue(self)

##ABSTRATA##
class IfStmt(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class SimpleIf(IfStmt):
    def _init_(self, IF, Expression, Block):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
    def accept(self, Visitor):
        Visitor.visitSimpleIf(self)

class IfElse(IfStmt):
    def _init_(self, IF, Expression, Block, ELSE, Block):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
        self.ELSE = Block
    def accept(self, Visitor):
        Visitor.visitIfElse(self)
##CONCRETA##
class CompIfElse(IfStmt):
    def _init_(self, IF, Expression, Block, ELSE, IfStmt):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
        self.ELSE = ELSE
        self.IfStmt = IfStmt
    def accept(self, Visitor):
        Visitor.visitCompIfElse(self)