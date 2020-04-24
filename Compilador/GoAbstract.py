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
class Params(Parameters):
    def __init__(self,LPAREN,ParameterList,RPAREN):
        self.LPAREN = LPAREN
        self.ParameterList = ParameterList
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitParams(self)

class DefinirParamsParameters(Parameters):
    def __init__(self,LPAREN,RPAREN):
        self.LPAREN = LPAREN
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitDefinirParamsParameters(self)

##ABSTRATA##
class ParameterList(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

class CompoundParamDecl(ParameterList): ##PRECISA OBSERVAR ISSO
    def __init__(self, ParameterDecl, ParameterList_Mul):
        self.ParameterDecl = ParameterDecl
        self.ParameterList_Mul = ParameterList_Mul

    def accept(self, Visitor):
        Visitor.visitCompParamsDecl(self)

class CallParameterDecl(ParameterList):
    def __init__(self, ParameterDecl):
        self.ParameterDecl = ParameterDecl

    def accept(self, Visitor):
        Visitor.visitCallParameterDecl(self)

##ABSTRATA##
class ParameterList_Mul(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCREATA##
class CallBackParameterList_Mul(ParameterList_Mul):
    def __init__(self, COMMA, ParameterDecl, ParameterList_Mul1):
        self.COMMA = COMMA
        self.ParameterDecl = ParameterDecl
        self.ParameterList_Mul1 = ParameterList_Mul1

    def accept(self, Visitor):
        Visitor.visitCallBackParameterList_Mul(self)

class EndParameterList_Mul(ParameterList_Mul):
    def __init__(self, COMMA, ParameterDecl):
        self.COMMA = COMMA
        self.ParameterDecl = ParameterDecl
    
    def accept(self, Visitor):
        Visitor.visitEndParameterList_Mul(self)

##ABSTRATA##
class ParameterDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ParamIdDecl(ParameterDecl):
    def __init__(self, IdentifierList, Type):
        self.IdentifierList = IdentifierList
        self.Type = Type

    def accept(self, Visitor):
        Visitor.visitParamIdDecl(self)

class ParamDecl(ParameterDecl):
    def __init__(self, Type):
        self.Type = Type

    def accept(self, Visitor):
        Visitor.visitParamDecl(self)

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
    def __init__(self, LCHAVES, StatementList, RCHAVES):
        self.LCHAVES = LCHAVES
        self.StatementList = StatementList
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitDefinirStatementL(self)

class MultFunc(Block):
    def __init__(self, LCHAVES, StatementList, RCHAVES, FunctionDecl):
        self.LCHAVES = LCHAVES
        self.StatementList = StatementList
        self.RCHAVES = RCHAVES
        self.FunctionDecl = FunctionDecl

    def accept(self, Visitor):
        Visitor.visitMultFunc(self)

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

class CompoundStatementList(StatementList):
    def __init__(self, statement, SEMICOLON, statementList):
        self.statement = statement
        self.SEMICOLON = SEMICOLON
        self.statementList = statementList

    def accept(self, Visitor):
        Visitor.visitCompoundStatmenteList(self)

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
    def __init__(self, VarDecl):
        self.VarDecl = VarDecl

    def accept(self, Visitor):
        Visitor.visitDeclVar(self)

##ABSTRATA##
class SimpleStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

class StmtCondition(SimpleStmt):
    def __init__(self, Condition):
        self.Condition = Condition

    def accept(self, Visitor):
        Visitor.visitStmtCondition(self)

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
class ExpReturn(ReturnStmt):
    def __init__(self,RETURN, ExpressionList):
        self.RETURN = RETURN
        self.ExpressionList = ExpressionList
    
    def accept(self, Visitor):
        Visitor.visitExpReturn(self)

class SimpleReturn(ReturnStmt):
    def __init__(self,RETURN):
        self.RETURN = RETURN

    def accept(self, Visitor):
        Visitor.visitSimpleReturn(self)

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

class CompIfElse(IfStmt):
    def __init__(self, IF, Expression, Block, ELSE, IfStmt):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
        self.ELSE = ELSE
        self.IfStmt = IfStmt

    def accept(self, Visitor):
        Visitor.visitCompIfElse(self)

class IfElse(IfStmt):
    def __init__(self, IF, Expression, Block, ELSE, Block1):
        self.IF = IF
        self.Expression = Expression
        self.Block = Block
        self.ELSE = ELSE
        self.Block1 = Block1

    def accept(self, Visitor):
        Visitor.visitIfElse(self)

##ABSTRATA##
class SwitchStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExprSwitch(SwitchStmt):
    def __init__(self, SWITCH, switchStmt_Head, switchStmt_Body):
        self.SWITCH = SWITCH
        self.switchStmt_Head = switchStmt_Head
        self.switchStmt_Body = switchStmt_Body

    def accept(self, Visitor):
        Visitor.visitExprSwitch(self)

class ExprSwitchSimple(SwitchStmt):
    def __init__(self, SWITCH, switchStmt_Body):
        self.SWITCH = SWITCH
        self.switchStmt_Body = switchStmt_Body

    def accept(self, Visitor):
        Visitor.visitExprSwitchSimple(self)

##ABSTRATA
class SwitchStmt_Head(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA
class ExprSwitchHead1(SwitchStmt_Head):
    def __init__(self, simpleStmt, SEMICOLON, expression):
        self.simpleStmt = simpleStmt
        self.SEMICOLON = SEMICOLON
        self.expression = expression

    def accept(self, Visitor):
        Visitor.visitExprSwitchHead1(self)

class ExprSwitchHead2(SwitchStmt_Head):
    def __init__(self, simpleStmt, SEMICOLON):
        self.simpleStmt = simpleStmt
        self.SEMICOLON = SEMICOLON

    def accept(self, Visitor):
        Visitor.visitExprSwitchHead2(self)

class ExprSwitchHead3(SwitchStmt_Head):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, Visitor):
        Visitor.visitExprSwitchHead3(self)

##ABSTRATA
class SwitchStmt_Body(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA
class ExprSwitchBody1(SwitchStmt_Body):
    def __init__(self, LCHAVES, exprCaseClauseList, RCHAVES):
        self.LCHAVES = LCHAVES
        self.exprCaseClauseList = exprCaseClauseList
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitchBody1(self)

class ExprSwitchBody2(SwitchStmt_Body):
    def __init__(self, LCHAVES, RCHAVES):
        self.LCHAVES = LCHAVES
        self.RCHAVES = RCHAVES

    def accept(self, Visitor):
        Visitor.visitExprSwitchBody2(self)

##ABSTRATA
class ExprCaseClauseList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA
class CompoundCaseClause1(ExprCaseClauseList):
    def __init__(self, ExprCaseClause, ExprCaseClauseList):
        self.ExprCaseClause = ExprCaseClause
        self.ExprCaseClauseList = ExprCaseClauseList

    def accept(self, Visitor):
        Visitor.visitCompoundCaseClase(self)

class CompoundCaseClause2(ExprCaseClauseList):
    def __init__(self, ExprCaseClause):
        self.ExprCaseClause = ExprCaseClause
    
    def accept(self, Visitor):
        Visitor.visitCompoundCaseClause2(self)

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

class InitFor(ForClause):
    def __init__(self, InitStmt):
        self.InitStmt = InitStmt

    def accept(self, Visitor):
        Visitor.visitInitFor(self)

class InPoFor(ForClause):
    def __init__(self, InitStmt, SEMICOLON, PostStmt):
        self.InitStmt = InitStmt
        self.SEMICOLON = SEMICOLON
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
    def __init__(self, PostStmt):
        self.PostStmt = PostStmt

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
    def __init__(self, CONST, LPAREN, constSpecList, RPAREN):
        self.CONST = CONST
        self.LPAREN = LPAREN
        self.constSpecList = constSpecList
        self.RPAREN = RPAREN
    
    def accept(self, Visitor):
        Visitor.visitCompConst(self)

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

##CONCRETA##
class CompoundIDList(CompIDList):
    def __init__(self, COMMA, ID, CompIDList):
        self.COMMA = COMMA
        self.ID = ID
        self.CompIDList = CompIDList

    def accept(self, Visitor):
        Visitor.visitCompoundIDList(self)

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
        Visitor.visitCallExpList(self)

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

##CONCRETA##
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
class Expression(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExprUnary(Expression):
	def __init__(self, UnaryExpr):
		self.UnaryExpr = UnaryExpr

	def accept(self, Visitor):
		Visitor.visitExprUnary(self)

class DefinirExp(Expression):
	def __init__(self, Expression, binary_op, Expression1):
		self.Expression = Expression
		self.binary_op =  binary_op
		self.Expression1 = Expression1

	def accept(self, Visitor):
		Visitor.visitDefinirExp(self)

##ABSTRATA##
class UnaryExpr(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
	    pass

##CONCRETA##
class UnaryExprNumber(UnaryExpr):
    def __init__(self, NUMBER):
        self.NUMBER = NUMBER

    def accept(self, Visitor):
        Visitor.visitUnaryExprNumber(self)

class UnaryExprID(UnaryExpr):
    def __init__(self, ID, Arguments):
        self.ID = ID
        self.Arguments = Arguments

    def accept(self, Visitor):
        Visitor.visitUnaryExprID(self)

class UnaryExprParen(UnaryExpr):
    def __init__(self, LPAREN, Expression, RPAREN):
        self.LPAREN = LPAREN
        self.Expression = Expression
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitUnaryExprParen(self)

##ABSTRATA##
class Binary_op(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class OpOr(Binary_op):
	def __init__(self, OR):
		self.OR = OR

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
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class IqualsOp(Rel_op):
	def __init__(self, EQUALS):
		self.EQUALS = EQUALS

	def accept(self, Visitor):
		Visitor.visitEqualsOp(self)

class DifereOp(Rel_op):
    def __init__(self, DIFERENTE):
        self.DIFERENTE = DIFERENTE
        
    def accept(self, Visitor):
        Visitor.visitDifereOp(self)

class MenorOp(Rel_op):
    def __init__(self, LESS):
        self.LESS = LESS
        
    def accept(self, Visitor):
        Visitor.visitMenorOp(self)

class MenorIgualOp(Rel_op):
    def __init__(self, LESS_EQUAL):
        self.LESS_EQUAL = LESS_EQUAL
        
    def accept(self, Visitor):
        Visitor.visitMenorIgualOp(self)

class MaiorOp(Rel_op):
    def __init__(self, GREATER):
        self.GREATER = GREATER
        
    def accept(self, Visitor):
        Visitor.visitMaiorOp(self)  

class MaiorIgual(Rel_op):
    def __init__(self, GREATER_EQUAL):
        self.GREATER_EQUAL = GREATER_EQUAL
        
    def accept(self, Visitor):
        Visitor.visitMaiorIgualOp(self)

##ABSTRATA##
class Add_op(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class MaisOp(Add_op):
	def __init__(self,PLUS):
		self.PLUS = PLUS

	def accept(self, Visitor):
		Visitor.visitMaisOp(self)

class MenosOp(Add_op):
    def __init__(self,MINUS):
        self.MINUS = MINUS
        
    def accept(self, Visitor):
        Visitor.visitMenosOp(self)
    
##ABSTRATA##
class Mul_op(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class VezesOp(Mul_op):
	def __init__(self,TIMES):
		self.TIMES =  TIMES

	def accept(self, Visitor):
		Visitor.visitVezesOp(self)

class DivideOp(Mul_op):
    def __init__(self,DIVIDE):
        self.DIVIDE = DIVIDE
        
    def accept(self, Visitor):
        Visitor.visitDivideOp(self)

class ModOp(Mul_op):
    def __init__(self,MOD):
        self.MOD = MOD
    
    def accept(self, Visitor):
        Visitor.visitModOp(self)

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
        self.ExpressionList1 = ExpressionList1    ##observar
        
    def accept(self, Visitor):
        Visitor.visitAssignOp(self)

##ABSTRATA##
class ShortVarDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DeclShortVarDef(ShortVarDecl):
    def __init__(self, IdentifierList, ASSIGN, ExpressionList):
        self.IdentifierList = IdentifierList
        self.ASSIGN = ASSIGN
        self.ExpressionList = ExpressionList    ##observar
        
    def accept(self, Visitor):
        Visitor.visitDeclShortVarDef(self)