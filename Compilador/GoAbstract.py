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
		Visitor.visitDefinirParamsT(self)

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

class CompoundParamDecl(ParameterList): ##PRECISA OBSERVAR ISSO
    def __init__(self, ParameterDecl, ParameterDecList):
        self.ParameterDecl = ParameterDecl
        self.ParameterDecList = ParameterDecList

    def accept(self, Visitor):
        Visitor.visitCompParamsDecl(self)

##ABSTRATA##
class ParameterDecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCREATA##
class DecParamComp(ParameterDecList):
    def __init__(self, COMMA, ParameterDecl):
        self.COMMA = COMMA
        self.ParameterDecl = ParameterDecl

    def accept(self, Visitor):
        Visitor.visitDecParamComp(self)

class DecListCompound(ParameterDecList):
    def __init__(self, COMMA, ParameterDecl, ParameterDecList):
        self.COMMA = COMMA
        self.ParameterDecl = ParameterDecl
        self.ParameterDecList = ParameterDecList

    def accept(self, Visitor):
        Visitor.visitDecListCompound(self)

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

##ABSTRATA##       
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
    def __init__(self, None): #Duvidas
        self = None

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

    def accept(self, Visitor):
        Visitor.visitStmtBreack(self)

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
    def __init__(self, SimpleStmt, SEMICOLON, Expression, LCHAVES, ExprCaseClauseList, RCHAVES):
        self.SimpleStmt = SimpleStmt
        self.SEMICOLON = SEMICOLON
        self.Expression = Expression
        self.LCHAVES = LCHAVES
        self.ExprCasaClauseList = ExprCasaClauseList
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitch(self)

class ExprSwitchNone(SwitchStmt):
    def __init__(self, SWITCH, LCHAVES, ExprCaseClauseList, RCHAVES):
        self.SWITCH = SWITCH
        self.LCHAVES = LCHAVES
        self.ExprCaseClauseList = ExprCaseClauseList
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitchNone(self)

class ExprSwitchSimple(SwitchStmt):
    def __init__(self, SWITCH, SimpleStmt, LCHAVES, ExprCaseClauseList, RCHAVES):
        self.SWITCH = SWITCH
        self.SimpleStmt = SimpleStmt
        self.LCHAVES = LCHAVES
        self.ExprCaseClauseList = ExprCaseClauseList
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitchSimple(self)

class ExprSwitchExp(SwitchStmt):
    def __init__(self, SWITCH, Expression, LCHAVES, ExprCaseClauseList, RCHAVES):
        self.SWITCH = SWITCH
        self.Expression = Expression
        self.LCHAVES = LCHAVES
        self.ExprCaseClause = ExprCaseClause
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitchExp(self)

##ABSTRATA
class ExprCaseClauseList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA
class CallExprCaseClause(ExprCaseClauseList):
    def __init__(self, ExprCaseClause):
        self.ExprCaseClause = ExprCaseClause

    def accept(self, Visitor):
        Visitor.visitCallExprCaseClause(self)

class CompoundCaseClause(ExprCaseClauseList):
    def __init__(self, ExprCaseClause, ExprCaseClauseList):
        self.ExprCaseClause = ExprCaseClause
        self.ExprCaseClauseList = ExprCaseClauseList

    def accept(self, Visitor):
        Visitor.visitCompoundCaseClase(self)

class EmptyCaseClause(ExprCaseClauseList):
    def __init__(self, None)
        self = None
        pass

    def accept(self, Visitor):
        Visitor.visitEmptyCaseClause(self)

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
    def __init__(self, FOR, ForClause, Block):
        self.FOR = FOR
        self.ForClause = ForClause
        self.Block = Block

    def accept(self, Visitor):
        Visitor.visitStmtForClause(self)

class StmtForRange(ForStmt):
    def __init__(self, FOR, RangeClause, Block):
        self.FOR = FOR
        self.RangeClause = Block
        self.Block = Block

    def accept(self, Visitor):
        Visitor.visitStmtForRange(self)

class StmtForBlock(ForStmt):
    def __init__(self, FOR, Block):
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

##ABSTRATA##
class ConstDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class SimpleConst(ConstDecl):
    def __init__ (self, CONST, ConstSpec):
        self.CONST = CONST
        self.ConstSpec = ConstSpec

    def accept(self, Visitor):
        Visitor.visitSimpleConst(self)

class CompConst(ConstDecl):
    def __init__(self, CONST, LPAREN, ConstSpec, RPAREN):
        self.CONST = CONST
        self.LPAREN = LPAREN
        self.ConstSpec = ConstSpec
        self.RPAREN = RPAREN
    
    def accept(self, Visitor):
        Visitor.visitCompConst(self)

##ABSTRATA##
class ConstSpec(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class SimpleIdList(ConstSpec):
    def __init__(self, IdentifierList):
        self.IdentifierList = IdentifierList

    def accept(self, Visitor):
        Visitor.visitSimpleIdList(self)

class ListIdExp(ConstSpec):
    def __init__(self, IdentifierList, ASSIGN, ExpressionList):
        self.IdentifierList = IdentifierList
        self.ASSIGN = ASSIGN
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        Visitor.visitListIdExp(self)

class ListIdTypeExp(ConstSpec):
    def __init__(self, IdentifierList, Type, ASSIGN, ExpressionList):
        self.IdentifierList = IdentifierList
        self.Type = Type
        self.ASSIGN = ASSIGN
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        Visitor.visitListTypeExp(self)

##ABSTRATA##
class ConstSpecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CallConstSpec(ConstSpecList):
    def __init__(self, ConstSpec, SEMICOLON):
        self.ConstSpec = ConstSpec
        self.SEMICOLON = SEMICOLON

    def accept(self, Visitor):
        Visitor.visitCallConstSpec(self)

class CompoundConstSpec(ConstSpecList):
    def __init__(self, ConstSpec, SEMICOLON, ConstSpecList):
        self.ConstSpec = ConstSpec
        self.SEMICOLON = SEMICOLON
        self.ConstSpecList = ConstSpecList

    def accept(self, Visitor):
        Visitor.visitCompoundConstSpec(self)

##ABSTRATA##
class IdentifierList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor)
        pass

##CONCRETA##
class DefinirIDList(IdentifierList):
    def __init__(self, ID, CompIDList):
        self.ID = ID
        self.CompIDList

    def accept(self, Visitor):
        Visitor.visitDefinirIDList(self)

##ABSTRATA
class CompIDList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DoubleID(CompIDList):
    def __init__(self, COMMA, ID):
        self.COMMA = COMMA
        self.ID

    def accept(self, Visitor):
        Visitor.visitDoubleID(self)

class CompoundIDList(CompIDList):
    def __init__(self, COMMA, CompIDList):
        self.COMMA = COMMA
        self.CompIDList = CompIDList

    def accept(self, Visitor):
        Visitor.visitCompoundIDList(self)

class SimpleID(CompIDList):
    def __init__(self, None):
        self = None
        pass

    def accept(self, Visitor):
        Visitor.visitSimpleID(self)

##ABSTRATA##
class ExpressionList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirExpList(ExpressionList):
    def __init__(self, Expression):
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitDefinirExpList(self)

class CallExpList(ExpressionList):
    def __init__(self, Expression, ListExpr):
        self.Expression = Expression
        self.ListExpr = ListExpr

    def accept(self, Visitor):
        Visitor.visitDefinirExpList(self)

##ABSTRATA##
class ListExpr(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class SimpleExpList(ListExpr):
    def __init__(self, COMMA, Expression):
        self.COMMA = COMMA
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitSimpleExpList(self)

class CompoundExpList(ListExpr):
    def __init__(self, COMMA, Expression, ListExpr):
        self.COMMA = COMMA
        self.Expression = Expression
        self.ListExpr = ListExpr

    def accept(self, Visitor):
        Visitor.visitCompoundExpList(self)

##ABSTRATA##
class TypeDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirType(TypeDecl): #Não é o type dos tipos primitivos
    def __init__(self, TYPE, TypeSpec):
        self.TYPE = TYPE
        self.TypeSpec = TypeSpec

    def accept(self, Visitor):
        Visitor.visitDefinirType(self)

class CallTypeSpecList(TypeDecl):
    def __init__(self, TYPE, LPAREN, TypeSpecList, RPAREN):
        self.TYPE = TYPE
        self.LPAREN = LPAREN
        self.TypeSpecList = TypeSpecList
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitCallTypeSpecList(self)

##ABSTRATA##
class TypeSpecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class TypeSpecDouble(TypeSpecList):
    def __init__(self, TypeSpec, SEMICOLON):
        self.TypeSpec = TypeSpec
        self.SEMICOLON = SEMICOLON

    def accept(self, Visitor):
        Visitor.visitTypeSpecDouble(self)

class CompTypeSpecList(TypeSpecList):
    def __init__(self, TypeSpec, SEMICOLON, TypeSpecList):
        self.TypeSpec = TypeSpec
        self.SEMICOLON = SEMICOLON
        self.TypeSpecList = TypeSpecList

    def accept(self, Visitor):
        Visitor.visitCompTypeSpecList(self)

class TypeSpecSimple(TypeSpecList):
    def __init__(self, None):
        self = None
        pass

    def accept(self, Visitor):
        Visitor.visitTypeSpecSimple(self)

##ABSTRATA##
class TypeSpec(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class SpecType(TypeSpec):
	def __init__(self, ID, Type):
        self.ID = ID
        self.Type = Type

    def accept(self, Visitor):
	    Visitor.visitSpecType(self)

##ABSTRATA##
class VarDecl(metaclass=ABCMeta):
	@abstractmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class DefinirVar(VarDecl):
	def __init__(self, VAR, VarSpec):
		self.VAR = VAR
		self.VarSpec = VarSpec

	def accept(self, Visitor):
		Visitor.visitDefinirVar(self)

class CompVar(VarDecl):
	def __init__(self, VAR, LPAREN, VarSpecList, RPAREN):
		self.VAR = VAR
        self.LPAREN = LPAREN
        self.VarSpecList = VarSpecList
        self.RPAREN = RPAREN

	def accept(self, Visitor):
		Visitor.visitCompVar(self)

##ABSTRATA##
class VarSpecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class VarDef(VarSpecList):
    def __init__(self, VarSpec, SEMICOLON):
        self.VarSpec = VarSpec
        self.SEMICOLON = SEMICOLON

    def accept(self, Visitor):
        Visitor.visitVarDef(self)

class CompoundVarSpec(VarSpecList):
    def __init__(self, VarSpec, SEMICOLON, VarSpecList):
        self.VarSpec = VarSpec
        self.SEMICOLON = SEMICOLON
        self.VarSpecList = VarSpecList

    def accept(self, Visitor):
        Visitor.visitCompoundVarSpec(self)

class SimpleVar(VarSpecList):
    def __init__(self, None):
        self = None
        pass

    def accept(self, Visitor):
        Visitor.visitSimpleVar(self)

##ABSTRATA##
class VarSpec(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class SpecVar(VarSpec):
	def __init__(self, IdentifierList, Type):
		self.IdentifierList = IdentifierList
		self.Type = Type

	def accept(self, Visitor):
		Visitor.visitSpecVar(self)

class ClassicVarSpec(VarSpec):
	def __init__(self, IdentifierList, Type, ASSIGN, ExpressionList):
		self.IdentifierList = IdentifierList
		self.Type = Type
		self.ASSIGN = ASSIGN
		self.ExpressionList = ExpressionList

	def accept(self, Visitor):
		Visitor.visitClassicVarSpec(self)

class SimpleVarSpec(VarSpec):
	def __init__(self, IdentifierList, ASSIGN, ExpressionList):
		self.IdentifierList = IdentifierList
		self.ASSIGN = ASSIGN
		self.ExpressionList = ExpressionList

	def accept(self, Visitor):
		Visitor.visitSimpleVarSpec(self)

##ABSTRATA##
class Expression(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class DefinirExp(Expression):
	def __init__(self, Expression, binary_op, Expression):
		self.Expression = Expression
		self.binary_op =  binary_op
		self.Expression = Expression

	def accept(self, Visitor):
		Visitor.visitDefinirExp(self)

class ExprUnary(Expression):
	def __init__(self, UnaryExpr):
		self.UnaryExpr = UnaryExpr

	def accept(self, Visitor):
		Visitor.visitExprUnary(self)

##ABSTRATA##
class Binary_op(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class OpOr(Binary_op):
	def __init__(self, OR):
		self.”OR” = “OR”

	def accept(self, Visitor):
		Visitor.visitOpOr(self)

class OpAnd(Binary_op):
	def __init__(self, AND):
		self.AND = AND

	def accept(self, Visitor):
		Visitor.visitOpAnd(self)

class OpRel(Binary_op):
	def __init__(self, rel_op):
		self.rel_op = rel_op

	def accept(self, Visitor):
		Visitor.visitOpRel(self)

class OpAdd(Binary_op):
	def __init__(self, add_op):
		self.add_op = add_op

	def accept(self, Visitor):
		Visitor.visitOpAdd(self)

class OpMul(Binary_op):
	def __init__(self, mul_op):
		self.mul_op = mul_op

	def accept(self, Visitor):
		Visitor.visitOpMul(self)

##ABSTRATA##
class Rel_op(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class iqualsOp(Rel_op):
	def __init__(self, EQUALS):
		self.EQUALS = EQUALS

	def accept(self, Visitor):
		Visitor.visitiqualsOp(self)

class difereOp(Rel_op):
    def __init__(self, DIFERENTE):
		self.DIFERENTE = DIFERENTE

	def accept(self, Visitor):
		Visitor.visitdifereOp(self)

class menorOp(Rel_op):
    def __init__(self, LESS):
		self.LESS = LESS

	def accept(self, Visitor):
		Visitor.visitmenorOp(self)

class menorIgualOp(Rel_op):
    def __init__(self, LESS_EQUAL):
		self.LESS_EQUAL = LESS_EQUAL

    def accept(self, Visitor):
		Visitor.visitmenorIgualOp(self)

class maiorOp(Rel_op):
    def __init__(self, GREATER):
		self.GREATER = GREATER

    def accept(self, Visitor):
		Visitor.visitmaiorOp(self)  

class maiorIgual(Rel_op):
    def __init__(self, GREATER_EQUAL):
		self.GREATER_EQUAL = GREATER_EQUAL

    def accept(self, Visitor):
		Visitor.visitmaiorIgual(self)

##ABSTRATA##
class Add_op(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class maisOp(Add_op):
	def __init__(self,PLUS):
		self.PLUS = PLUS

	def accept(self, Visitor):
		Visitor.visitmaisOp(self)

class menosOp(Add_op):
    def __init__(self,MINUS):
		self.MINUS = MINUS

	def accept(self, Visitor):
		Visitor.visitmenosOp(self)
    
##ABSTRATA##
class Mul_op(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class vezesOp(Mul_op):
	def __init__(self,TIMES):
		self.TIMES =  TIMES

	def accept(self, Visitor):
		Visitor.visitvezesOp(self)

class divideOp(Mul_op):
    	def __init__(self,DIVIDE):
		self.DIVIDE = DIVIDE

	def accept(self, Visitor):
		Visitor.visitdivideOp(self)

class modOp(Mul_op):
    def __init__(self,MOD):
		self.MOD = MOD

	def accept(self, Visitor):
		Visitor.visitmodOp(self)

##ABSTRATA##
class IncDec(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class IncOp(IncDec):
	def __init__(self,Expression,PLUS, PLUS):
		self.Expression = Expression
        self.PLUS = PLUS
        self.PLUS = PLUS                       ##observar

	def accept(self, Visitor):
		Visitor.visitIncOp(self)

class DecOp(IncDec):
    def __init__(self,Expression,MINUS,MINUS):
		self.Expression = Expression
        self.MINUS = MINUS
        self.MINUS = MINUS                     ##observar

	def accept(self, Visitor):
		Visitor.visitDecOp(self)

##ABSTRATA##
class Assignment(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class AssignOp(Assignment):
    def __init__(self,Expression,ASSIGN,ExpressionList):
		self.Expression = Expression
        self.ASSIGN = ASSIGN
        self.ExpressionList = ExpressionList    ##observar

	def accept(self, Visitor):
		Visitor.visitAssignOp(self)

##ABSTRATA##
class ShortVarDecl(metaclass=ABCMeta):
	@abstractmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class DeclShortVar(ShortVarDecl):
    def __init__(self,IdentifierList,ASSIGN,ExpressionList):
		self.IdentifierList = IdentifierList
        self.ASSIGN = ASSIGN
        self.ExpressionList = ExpressionList    ##observar

	def accept(self, Visitor):
		Visitor.visitDeclShortVar(self)

