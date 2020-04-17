from abc import abstractclassmethod
from abc import ABCMeta
import GoVisitor as Visitor

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

class Tbyte(Type):
    def __init__(self, BYTE):
        self.BYTE = BYTE

    def accept(self, Visitor):
        Visitor.visitTbyte(self)

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
class DefinirParamsParameters(Parameters):
    def __init__(self,LPAREN,RPAREN):
        self.LPAREN = LPAREN
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitDefinirParamsParameters(self)

class Params(Parameters):
    def __init__(self,LPAREN,ParameterList,RPAREN):
        self.LPAREN = LPAREN
        self.ParameterList = ParameterList
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitParams(self)

class ParamsList(Parameters):
    def __init__(self, LPAREN, ParameterList, COMMA, RPAREN):
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
    def __init__(self, ParameterDecl, ParameterList2):
        self.ParameterDecl = ParameterDecl
        self.ParameterList2 = ParameterList2
    
    def accept(self, Visitor):
        Visitor.visitDefinirParamDecl(self)

##ABSTRATA##
class ParameterList2(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompoundParamDecl(ParameterList2): ##PRECISA OBSERVAR ISSO
    def __init__(self, COMMA, ParameterList):
        self.COMMA = COMMA
        self.ParameterlList = ParameterlList

    def accept(self, Visitor):
        Visitor.visitCompParamsDecl(self)

##ABSTRATA##
class ParameterDeclList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCREATA##
class DecParamComp(ParameterDecList):
    def __init__(self, COMMA, ParameterList2):
        self.COMMA = COMMA
        self.ParameterList2 = ParameterList2

    def accept(self, Visitor):
        Visitor.visitDecParamComp(self)

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

class CompoundStatementList(StatementList):
    def _init_(self, statement, SEMICOLON, statementList2):
        self.statement = statement
        self.SEMICOLON = SEMICOLON
        self.statementList = statmentList2

    def accept(self, Visitor):
        Visitor.visitCompoundStatmenteList(self)

##ABSTRATA##
class StatementList2(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CallBackStatementList(StatementList2):
    def __init__(self, StatementList):
        self.StatementList = StatementList

    def accept(self, Visitor):
        Visitor.visitCallBackStatementList(self)

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
    def __init__(self, IfStmt):
        self.IfStmt = IfStmt

    def accept(self, Visitor):
        Visitor.visitStmtIf(self)

class StmtSwitch(Statement):
    def __init__(self, SwitchStmt):
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
class SimpleReturn(ReturnStmt):
    def __init__(self,RETURN):
        self.RETURN = RETURN

    def accept(self, Visitor):
        Visitor.visitSimpleReturn(self)

class ExpReturn(ReturnStmt):
    def __init__(self,RETURN, ExpressionList):
        self.RETURN = RETURN
        self.ExpressionList = ExpressionList
    
    def accept(self, Visitor):
        Visitor.visitExpReturn(self)

 ##ABSTRATA##
class BreakStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA## 
class StmtBreak(BreakStmt) :
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
    def __init__(self, IF, Expression, Block, ELSE, Block1):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
        self.ELSE = ELSE
        self.Block1 = Block1

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
    def __init__(self, SWITCH, SimpleStmt, SEMICOLON, Expression, LCHAVES, ExprCaseClauseList, RCHAVES):
        self.SWITCH = SWITCH
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

##ABSTRATA##
class ExprCaseClauseList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompoundCaseClause(ExprCaseClauseList):
    def __init__(self, ExprCaseClause, ExprCaseClauseList):
        self.ExprCaseClause = ExprCaseClause
        self.ExprCaseClauseList = ExprCaseClauseList

    def accept(self, Visitor):
        Visitor.visitCompoundCaseClase(self)

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
        Visitor.visitCaseClauseExp(self)

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
        self.RangeClause = RangeClause
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
    def __init__(self, InitStmt, SEMICOLON, Condition, SEMICOLON1, PostStmt):
        self.InitStmt = InitStmt
        self.SEMICOLON = SEMICOLON
        self.Condition = Condition
        self.SEMICOLON1 = SEMICOLON1
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitClassicFor(self)

class InCoFor(ForClause):
    def __init__(self, InitStmt, SEMICOLON, Condition):
        self.InitStmt = InitStmt
        self.SEMICOLON = SEMICOLON
        self.Condition = Condition

    def accept(self, Visitor):
        Visitor.visitInCoFor(self)

class InitFor(ForClause):
    def __init__(self, InitStmt):
        self.InitStmt = InitStmt

    def accept(self, Visitor):
        Visitor.visitInitFor(self)

class CoPoFor(ForClause):
    def __init__(self, Condition, SEMICOLON, PostStmt):
        self.Condition = Condition
        self.SEMICOLON = SEMICOLON
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitCoPoFor(self)

class ConditionFor(ForClause):
    def __init__(self, Condition):
        self.Condition = Condition

    def accept(self, Visitor):
        Visitosr.visitConditionFor(self)

class InPoFor(ForClause):
    def __init__(self, InitStmt, SEMICOLON, PostStmt):
        self.InitStmt = InitStmt
        self.SEMICOLON = SEMICOLON
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitInPoFor(self)

class PostFor(ForClause):
    def __init__(self, PostStmt):
        self.PostStmt = PostStmt

    def accept(self, Visitor):
        Visitor.visitPostFor(self)

##ABSTRATA##
class InitStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class StmtInit(InitStmt):
    def __init__(self, SimpleStmt):
        self.SimpleStmt = SimpleStmt

    def accept(self, Visitor):
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
    def __init__(self, IdentifierList, ASSIGN, RANGE, Expression):
        self.IdentifierList = IdentifierList
        self.ASSIGN = ASSIGN
        self.RANGE = RANGE
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
    def __init__(self, CONST, LPAREN, ConstSpecList, RPAREN):
        self.CONST = CONST
        self.LPAREN = LPAREN
        self.ConstSpec = ConstSpec
        self.RPAREN = RPAREN
    
    def accept(self, Visitor):
        Visitor.visitCompConst(self)

##ABSTRATA##
class ConstSpecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass


class CompoundConstSpec(ConstSpecList):
    def __init__(self, ConstSpec, SEMICOLON, ConstSpecList):
        self.ConstSpec = ConstSpec
        self.SEMICOLON = SEMICOLON
        self.ConstSpecList = ConstSpecList

    def accept(self, Visitor):
        Visitor.visitCompoundConstSpec(self)

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
class IdentifierList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirID(IdentifierList):
    def __init__(self, ID):
        self.ID = ID

    def accept(self, Visitor):
        Visitor.visitDefinirID(self)

class DefinirIDList(IdentifierList):
    def __init__(self, ID, CompIDList):
        self.ID = ID
        self.CompIDList = CompIDList

    def accept(self, Visitor):
        Visitor.visitDefinirIDList(self)

##ABSTRATA
class CompIDList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

class CompoundIDList(CompIDList):
    def __init__(self, COMMA, ID, CompIDList2):
        self.COMMA = COMMA
        self.ID = ID
        self.CompIDList2 = CompIDList2

    def accept(self, Visitor):
        Visitor.visitCompoundIDList(self)

##ABSTRATA##
class CompIDList2(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##ABSTRATA##
class callBackCompID(CompIDList):
    def __init__(self, CompIDList):
        self.CompIDList = CompIDList

    def accept(self, Visitor):
        Visitor.visitCallBackCompID(self)

##ABSTRATA##
class ExpressionList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

class CallExpList(ExpressionList):
    def __init__(self, Expression, ListExpr):
        self.Expression = Expression
        self.ListExpr = ListExpr

    def accept(self, Visitor):
        Visitor.visitCallExpList(self)

##ABSTRATA##
class ListExpr(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

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

class CompTypeSpecList(TypeSpecList):
    def __init__(self, TypeSpec, SEMICOLON, TypeSpecList):
        self.TypeSpec = TypeSpec
        self.SEMICOLON = SEMICOLON
        self.TypeSpecList = TypeSpecList

    def accept(self, Visitor):
        Visitor.visitCompTypeSpecList(self)

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
	@abstractclassmethod
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

class CompoundVarSpec(VarSpecList):
    def __init__(self, VarSpec, SEMICOLON, VarSpecList):
        self.VarSpec = VarSpec
        self.SEMICOLON = SEMICOLON
        self.VarSpecList = VarSpecList

    def accept(self, Visitor):
        Visitor.visitCompoundVarSpec(self)

##ABSTRATA##
class VarSpec(metaclass=ABCMeta):
    @abstractclassmethod
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
class Exp(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class OperadorOr(Exp):
    def __init__(self, exp, OR, exp1):
        self.exp = exp
        self.OR = OR
        self.exp1 = exp1

    def accept(self, Visitor):
        Visitor.visitOperadorOr(self)


class CallExp1(Exp):
    def __init__(self, exp1):
        self. exp1 = exp1

    def accept(self, Visitor):
        Visitor.visitCallExp1(self)

##ABSTRATA##
class Exp1(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class OperadorAnd(Exp1):
    def __init__(self, exp1, AND, exp2):
        self.exp1 = exp1
        self.AND = AND
        self.exp2 = exp2
    
    def accept(self, Visitor):
        Visitor.visitOperadorAnd(self)

class CallExp2(Exp1):
    def __init__(self, exp2):
        self.exp2 = exp2
    
    def accept(self, Visitor):
        Visitor.visitCallExp2(self)

##ABSTRATA##
class Exp2(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class OperadorIgual(Exp2):
    def __init__(self, exp2, EQUALS, exp3):
        self.exp2 = exp2
        self.EQUALS = EQUALS
        self.exp3 = exp3

    def accept(self, Visitor):
        Visitor.visitOperadorIgual(self)

class OperadorDiferente(Exp2):
    def __init__(self, exp2, DIFERENTE, exp3):
        self.exp2 = exp2
        self.DIFERENTE = DIFERENTE
        self.exp3 = exp3

    def accept(self, Visitor):
        Visitor.visitOperadorDiferente(self)

class OperadorMenor(Exp2):
    def __init__(self, exp2, LESS, exp3):
        self.exp2 = exp2
        self.LESS = LESS
        self.exp3 = exp3

    def accept(self, Visitor):
        Visitor.visitOperadorMenor(self)

class OperadorMenorIgual(Exp2):
    def __init__(self, exp2, LESS_EQUAL, exp3):
        self.exp2 = exp2
        self.LESS_EQUAL = LESS_EQUAL
        self.exp3 = exp3

    def accept(self, Visitor):
        Visitor.visitOperadorMenorIgual(self)

class OperadorMaior(Exp2):
    def __init__(self, exp2, GREATER, exp3):
        self.exp2 = exp2
        self.GREATER = GREATER
        self.exp3 = exp3

    def accept(self, Visitor):
        Visitor.visitOperadorMaior(self)

class OperadorMaiorIgual(Exp2):
    def __init__(self, exp2, GREATER_EQUAL, exp3):
        self.exp2 = exp2
        self.GREATER_EQUAL = GREATER_EQUAL
        self.exp3 = exp3

    def accept(self, Visitor):
        Visitor.visitOperadorMaiorIgual(self)

class CallExp3(Exp2):
    def __init__(self, exp3):
        self.exp3 = exp3
    
    def accept(self, Visitor):
        Visitor.visitCallExp3(self)

##ABSTRATA##
class Exp3(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class OperadorMais(Exp3):
    def __init__(self, exp3, PLUS, exp4):
        self.exp3 = exp3
        self.PLUS = PLUS
        self.exp4 = exp4
    
    def accept(self, Visitor):
        Visitor.visitOperadorMais(self)

class OperadorMenos(Exp3):
    def __init__(self, exp3, MINUS, exp4):
        self. exp3 = exp3
        self.MINUS = MINUS
        self.exp4 = exp4

    def accept(self, Visitor):
        Visitor.visitOperadorMenos(self)

class OperadorPot(Exp3):
    def __init__(self, exp3, POT, exp4):
        self.exp3 = exp3
        self.POT = POT
        self.exp4 = exp4

    def accept(self, Visitor):
        Visitor.visitOperadorPot(self)

class CallExp(Exp3):
    def __init__(self, exp4):
        self.exp4 = exp4

    def accept(self, Visitor):
        Visitor.visitCallExp(self)

##ABSTRATA##
class Exp4(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class OperadorVezes(Exp4):
    def __init__(self, exp4, TIMES, exp5):
        self.exp4 = exp4
        self.TIMES = TIMES
        self.exp5 = exp5

    def accept(self, Visitor):
        Visitor.visitOperadorVezes(self)

class OperadorDividir(Exp4):
    def __init__(self, exp4, DIVIDE, exp5):
        self.exp4 = exp4
        self.DIVIDE = DIVIDE
        self.exp5 = exp5

    def accept(self, Visitor):
        Visitor.visitOperadorDividir(self)

class OperadorMod(Exp4):
    def __init__(self, exp4, MOD, exp5):
        self.exp4 = exp4
        self.MOD = MOD
        self.exp5 = exp5
    
    def accept(self, Visitor):
        Visitor.visitorOperadorMod(self)

class CallExp5(Exp4):
    def __init__(self, exp5):
        self.exp5 = exp5

    def accept(self, Visitor):
        Visitor.visitCallExp5(self)

##ABSTRATA##
class Exp5(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CallArguments(Exp5):
    def __init__(self, arguments):
        self.arguments = arguments

    def accept(self, Visitor):
        Visitor.visitCallArguments(self)

class CallAssignment(Exp5):
    def __init__(self, assignment):
        self.assignment = assignment
    
    def accept(self, Visitor):
        Visitor.visitCallAssignment(self)

class CallNumber(Exp5):
    def __init__(self, NUMBER):
        self.NUMBER = NUMBER

    def accept(self, Visitor):
        Visitor.visitCallNumber(self)

class MostrarID(Exp5):
    def __init__(self, ID):
        self.ID = ID

    def accept(self, Visitor):
        Visitor.visitMostrarID(self)


##ABSTRATA##
class Arguments(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompoundExp(Arguments):
    def __init__(self, ID, ExpressionList):
        self.ID = ID
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        Visitor.visitCompoundExp(self)

class CallExp(Arguments):
    def __init__(self, exp):
        self.exp = exp
    
    def accept(self, Visitor):
        Visitor.visitCallExp(self)

##ABSTRATA##
class IncDec(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class IncOp(IncDec):
    def __init__(self, Expression, PLUS, PLUS1):
        self.Expression = Expression
        self.PLUS = PLUS
        self.PLUS1 = PLUS1                       ##observar
        
    def accept(self, Visitor):
        Visitor.visitIncOp(self)

class DecOp(IncDec):
    def __init__(self, Expression, MINUS, MINUS1):
        self.Expression = Expression
        self.MINUS = MINUS
        self.MINUS1 = MINUS1                     ##observar
        
    def accept(self, Visitor):
        Visitor.visitDecOp(self)

##ABSTRATA##
class Assignment(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class AssignOp(Assignment):
    def __init__(self, ExpressionList, ASSIGN, ExpressionList1):
        self.Expression = ExpressionList
        self.ASSIGN = ASSIGN
        self.ExpressionList1 = ExpressionList1    
        
    def accept(self, Visitor):
        Visitor.visitAssignOp(self)

##ABSTRATA##
class ShortVarDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DeclShortVar(ShortVarDecl):
    def __init__(self, IdentifierList, ASSIGN, ExpressionList):
        self.IdentifierList = IdentifierList
        self.ASSIGN = ASSIGN
        self.ExpressionList = ExpressionList 
        
    def accept(self, Visitor):
        Visitor.visitDeclShortVar(self)

