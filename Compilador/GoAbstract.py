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

    def accept(self, Visitor):
        Visitor.visitDefinirFuncBody(self)

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
	def accept(self, Visitor):
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
    def __init__(self, FLOAT):
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
class DefinirStatementL(Block):
    def __init__(self,LCHAVES, StatmentList, RCHAVES):
        self.LCHAVES = LCHAVES
        self.StatmentList = StatmentList
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitDefinirStatementL(self)

##ABSTRATA##
class StatementList(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class DefinirStatement(StatementList): ##PRECISA OBSERVAR ISSO
    def __init__ (self, Statement, SEMICOLON):
        self.Statement = Statement
        self.SEMICOLON = SEMICOLON
    def accept(self, Visitor):
        Visitor.visitDefinirStatement(self)
        
class Statement(metaclass=ABCMeta):
    @abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class StmtDeclaration(Statement):
    def __init__(self, Declaration):
        self.Declaration = Declaration

    def accept(self, Visitor):
        Visitor.visitStmtDeclaration(self)

class StmtSimple(Statement):
    def __init__(self, SimpleStmt):
        self.SimpleStmt = SimpleStmt

    def accept(self, Visitor):
        Visitor.visitStmtSimple(self)

class StmtReturn(Statement):
    def __init__(self, ReturnStmt):
        self.ReturnStmt = ReturnStmt

    def accept(self, Visitor):
        Visitor.visitStmtReturn(self)

class StmtBreak(Statement):
    def __init__(self, BreakStmt):
        self.BreakStmt = BreakStmt

    def accept(self, Visitor):
        Visitor.visitStmtBreak(self)

class StmtContinue(Statement):
    def __init__(self, ContinueStmt):
        self.ContinueStmt = ContinueStmt

    def accept(self, Visitor):
        Visitor.visitStmtContinue(self)

class StmtBlock(Statement):
    def __init__(self, Block):
        self.Block = Block
    
    def accept(self, Visitor):
        Visitor.visitStmtBlock(self)

class StmtIf(Statement):
    def __init__(self, IfStmt)
        self.IfStmt = IfStmt

    def accept(self, Visitor):
        Visitor.visitStmtIf(self)

class StmtSwitch(Statement):
    def __init__(self, SwitchStmt)
        self.SwitchStmt = SwitchStmt

    def accept(self, Visitor):
        Visitor.visitStmtSwitch(self)

class StmtFor(Statement):
    def __init__(self, ForStmt):
        self.ForStmt = ForStmt

    def accept(self, Visitor):
        Visitor.visitStmtFor(self)

##ABSTRATA##
class Declaration(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass
##CONCRETA##
class DeclConst(Declaration):
    def __init__(self, ConstDecl):
        self.ConstDecl = ConstDecl

    def accept(self, Visitor):
        Visitor.visitDeclConst(self)

    class DeclType(Declaration):
    def __init__(self, TypeDecl):
        self.TypeDecl = TypeDecl

    def accept(self, Visitor):
        Visitor.visitDeclType(self)

    class DeclVar(Declaration):
    def __init__(self, ConstVar):
        self.ConstVar = ConstVar

    def accept(self, Visitor):
        Visitor.visitDeclVar(self)

##ABSTRATA##
class SimpleStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass
##CONCRETA##
class StmtEmpty(SimpleStmt):
    def __init__(self, none): #Duvidas
        self.none = none

    def accept(self, Visitor):
        Visitor.visitStmtEmpty(self)

class StmtExpression(SimpleStmt):
    def __init__(self, Expression):
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitStmtExpression(self)

class StmtIncDec(SimpleStmt):
    def __init__(self, IncDec):
        self.IncDec = IncDec

    def accept(self, Visitor):
        Visitor.visitStmtIncDec(self)

class Assign(SimpleStmt):
    def __init__(self, Assignment):
        self.Assignment = Assignment

    def accept(self, Visitor):
        Visitor.visitAssign(self)

class DeclShortVar(SimpleStmt):
    def __init__(self, ShortVarDecl):
        self.ShortVarDecl = ShortVarDecl

    def accept(self, Visitor):
        Visitor.visitDeclShortVar(self)

##ABSTRATA##
class ReturnStmt(metaclass=ABCMeta):
    @abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class SimpleReturn(ReturnStm):
    def __init__(self,RETURN):
        self.RETURN = RETURN

    def accept(self, Visitor):
        Visitor.visitSimpleReturn(self)

class ExpReturn(ReturnStm):
    def __init__(self,RETURN, ExpressionList):
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
    def __init__(self,BREAK):
        self.BREAK = BREAK

##ABSTRATA##
class ContinueStmt(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass
##CONCRETA##
class StmtContinue(ContinueStmt):
    def __init__(self, CONTINUE):
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
    def __init__(self, IF, Expression, Block):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
    def accept(self, Visitor):
        Visitor.visitSimpleIf(self)

class IfElse(IfStmt):
    def __init__(self, IF, Expression, Block, ELSE, Block):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
        self.ELSE = Block
    def accept(self, Visitor):
        Visitor.visitIfElse(self)
##CONCRETA##
class CompIfElse(IfStmt):
    def __init__(self, IF, Expression, Block, ELSE, IfStmt):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
        self.ELSE = ELSE
        self.IfStmt = IfStmt
    def accept(self, Visitor):
        Visitor.visitCompIfElse(self)

##ABSTRATA##
class SwitchStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass
##CONCRETA##
class ExprSwitch(SwitchStmt):
    def __init__(self, SWITCH, LCHAVES, ExprCaseClause, RCHAVES):
        self.SWITCH = SWITCH
        self.LCHAVES = LCHAVES
        self.ExprCaseClause = ExprCaseClause
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitch(self)

class ExprSwitch(SwitchStmt):
    def __init__(self, SWITCH, SimpleStmt, SEMICOLON, LCHAVES, ExprCaseClause, RCHAVES):
        self.SWITCH = SWITCH
        self.SimpleStmt = SimpleStmt
        self.SEMICOLON = SEMICOLON
        self.LCHAVES = LCHAVES
        self.ExprCaseClause = ExprCaseClause
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitch(self)

class ExprSwitch(SwitchStmt):
    def __init__(self, SWITCH, SimpleStmt, SEMICOLON, Expression, LCHAVES, ExprCaseClause, RCHAVES):
        self.SWITCH = SWITCH
        self.SimpleStmt = SimpleStmt
        self.SEMICOLON = SEMICOLON
        self.Expression = Expression
        self.LCHAVES = LCHAVES
        self.ExprCaseClause = ExprCaseClause
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitch(self)

class ExprSwitch(SwitchStmt):
    def __init__(self, SWITCH, Expression, LCHAVES, ExprCaseClause, RCHAVES):
        self.SWITCH = SWITCH
        self.Expression = Expression
        self.LCHAVES = LCHAVES
        self.ExprCaseClause = ExprCaseClause
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitch(self)

##ABSTRATA##
class ExprCaseClause(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class ExprCase(ExprCaseClause):
    def __init__(self, ExprSwitchCase, COLON, StatementList):
        self.ExprSwitchCase = ExprSwitchCase
        self.COLON = COLON
        self.StatementList = StatementList
    
    def accept(self, Visitor):
        Visitor.visitExprCase(self)

##ABSTRATA##
class ExprSwitchCase(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass
##CONCRETA##
class CaseClauseExp(ExprSwitchCase):
    def __init__(self, CASE, ExpressionList):
        self.CASE = CASE
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        Visitor.visitCaseClause(self)

class CaseClause(ExprSwitchCase):
    def __init__(self, DEFAULT):
        self.DEFAULT = DEFAULT

    def accept(self, Visitor):
        Visitor.visitCaseClause(self)

##ABSTRATA##
class ForStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class StmtFor(ForStmt):
    def __init__(FOR, Condition, Block):
        self.FOR = FOR
        self.Condition = Condition
        self.Block = Block

    def accept(self, Visitor):
        Visitor.visitStmtFor(self)

class StmtForClause(ForStmt):
    def __init__(FOR, ForClause, Block):
        self.FOR = FOR
        self.ForClause = ForClause
        self.Block = Block

    def accept(self, Visitor):
        Visitor.visitStmtForClause(self)

class StmtForRange(ForStmt):
    def __init__(FOR, RangeClause, Block):
        self.FOR = FOR
        self.RangeClause = Block
        self.Block = Block

    def accept(self, Visitor):
        Visitor.visitStmtForRange(self)

class StmtForBlock(ForStmt):
    def __init__(FOR, Block):
        self.FOR = FOR
        self.Block = Block

    def accept(self, Visitor):
        Visitor.visitStmtForBlock(self)

##ABSTRATA##
class Condition(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirCondition(Condition):
    def __init__(self, Expression):
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitDefinirCondition(self)

##ABSTRATA##
class ForClause(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ClassicFor(ForClause):
    def __init__(self, InitStmt, SEMICOLON, Condition, SEMICOLON, PostStmt)
        self.InitStmt = InitStmt
        self.SEMICOLON = SEMICOLON
        self.Condition = Condition
        self.SEMICOLON = SEMICOLON
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitClassicFor(self)

class ConditionFor(ForClause):
    def __init__(self, Condition):
        self.Condition = Condition

    def accept(self, Visitosr):
        Visitosr.visitConditionFor(self)

class InitFor(ForClause):
    def __init__(self, InitStmt):
        self.InitStmt = InitStmt

    def accept(self, Visitor):
        Visitor.visitInitFor(self)

class PostFor(ForClause):
    def __init__(self, PostStmt):
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitPostFor(self)

class InCoFor(ForClause):
    def __init__(self, InitStmt, Condition):
        self.InitStmt = InitStmt
        self.Condition = Condition

    def accept(self, Visitor):
        Visitor.visitInCoFor(self)

class CoPoFor(ForClause):
    def __init__(self, Condition, PostStmt):
        self.Condition = Condition
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitCoPoFor(self)

class InPoFor(ForClause):
    def __init__(self, InitStmt, PostStmt):
        self.InitStmt = InitStmt
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitInPoFor(self)

##ABSTRATA##
class InitStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class StmtInit(InitStmt):
    def __init__(self, SimpleStmt):
        self.SimpleStmt = SimpleStmt

    def accept(self, Visitor)
        Visitor.visitStmtInit(self)

##ABSTRATA##
class PostStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class StmtPost(PostStmt):
    def __init__(self, SimpleStmt):
        self.SimpleStmt = SimpleStmt

    def accept(self, Visitor):
        Visitor.visitStmtPost(self)

##ABSTRATA##
class RangeClause(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirRange(RangeClause):
    def __init__(self, RANGE, Expression):
        self.RANGE = RANGE
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitDefinirRange(self)

class RangeExpList(RangeClause): ### Duvida observacao
    def __init__(self, ExpressionList, ASSIGN, RANGE, Expression):
        self.ExpressionList = ExpressionList
        self.ASSIGN = ASSIGN
        self.RANGE = RANGE
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitRangeExpList(self)

class RangeIDList(RangeClause):
    def __init__(self, IdentifierList, ASSIGN, Expression):
        self.IdentifierList = IdentifierList
        self.ASSIGN = ASSIGN
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitRangIDList(self)