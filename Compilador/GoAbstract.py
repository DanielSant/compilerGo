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
# class DefinirParams(Signature):
#     def __init__(self, Parameters):
#         self.Parameters = Parameters

#     def accept(self, Visitor):
#         Visitor.visitDefinirParams(self)

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
    def __init__(self, LPAREN, ParameterList, RPAREN):
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

class CompoundParamDecl(ParameterList):
    def __init__(self, ParameterDecl, ParameterList_Mul):
        self.ParameterDecl = ParameterDecl
        self.ParameterList_Mul = ParameterList_Mul

    def accept(self, Visitor):
        Visitor.visitCompParamsDecl(self)

# class CallParameterDecl(ParameterList):
#     def __init__(self, ParameterDecl):
#         self.ParameterDecl = ParameterDecl

#     def accept(self, Visitor):
#         Visitor.visitCallParameterDecl(self)

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
# class DefinirBlock(FunctionBody):
#     def __init__(self, Block):
#         self.Block = Block
    
#     def accept(self, Visitor):
#         Visitor.visitDefinirBlock(self)

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

class CallStmtFor(Statement):
    def __init__(self, ForStmt):
        self.ForStmt = ForStmt

    def accept(self, Visitor):
        Visitor.visitCallStmtFor(self)

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

# class ExprSwitchHead3(SwitchStmt_Head):
#     def __init__(self, expression):
#         self.expression = expression

#     def accept(self, Visitor):
#         Visitor.visitExprSwitchHead3(self)

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
        Visitor.visitCompoundCaseClause1(self)

# class CompoundCaseClause2(ExprCaseClauseList):
#     def __init__(self, ExprCaseClause):
#         self.ExprCaseClause = ExprCaseClause
    
#     def accept(self, Visitor):
#         Visitor.visitCompoundCaseClause2(self)

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
    def __init__(self, FOR, Condition, Block):
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
# class DefinirCondition(Condition):
#     def __init__(self, Expression):
#         self.Expression = Expression

#     def accept(self, Visitor):
#         Visitor.visitDefinirCondition(self)

##ABSTRATA##
class ForClause(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ClassicFor(ForClause):
    def __init__(self, initPostStmt, SEMICOLON, Condition, SEMICOLON1, initPostStmt1):
        self.initPostStmt = initPostStmt
        self.SEMICOLON = SEMICOLON
        self.Condition = Condition
        self.SEMICOLON1 = SEMICOLON1
        self.initPostStmt1 = initPostStmt1

    def accept(self, Visitor):
        Visitor.visitClassicFor(self)

class ClassicFor2(ForClause):
    def __init__(self,SEMICOLON, Condition, SEMICOLON1):
        self.SEMICOLON = SEMICOLON
        self.Condition = Condition
        self.SEMICOLON1 = SEMICOLON1

    def accept(self, Visitor):
        Visitor.visitclassicFor2(self)

##ABSTRATA##
class InitPostStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
# class StmtInitPost(InitPostStmt):
#     def __init__(self, SimpleStmt):
#         self.SimpleStmt = SimpleStmt

#     def accept(self, Visitor):
#         Visitor.visitStmtInitPost(self)

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
# class SimpleIdList(ConstSpec):
#     def __init__(self, IdentifierList):
#         self.IdentifierList = IdentifierList

#     def accept(self, Visitor):
#         Visitor.visitSimpleIdList(self)

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

class DefinirID(IdentifierList):
    def __init__(self, ID):
        self.ID = ID
        
    def accept(self, Visitor):
        Visitor.visitDefinirID(self)

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

class EndCompID(CompIDList):
    def __init__(self, COMMA, ID):
        self.COMMA = COMMA
        self.ID = ID

    def accept(self, Visitor):
        Visitor.visitEndCompID(self)

##ABSTRATA##
class ExpressionList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CallExpList(ExpressionList):
    def __init__(self, Expression, ListExpr):
        self.Expression = Expression
        self.ListExpr = ListExpr

    def accept(self, Visitor):
        Visitor.visitCallExpList(self)


# class DefinirExpList(ExpressionList):
#     def __init__(self, Expression):
#         self.Expression = Expression

#     def accept(self, Visitor):
#         Visitor.visitDefinirExpList(self)

##ABSTRATA##
class ListExpr(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompoundExpList(ListExpr):
    def __init__(self, COMMA, Expression, ListExpr):
        self.COMMA = COMMA
        self.Expression = Expression
        self.ListExpr = ListExpr

    def accept(self, Visitor):
        Visitor.visitCompoundExpList(self)

class SimpleExpList(ListExpr):
    def __init__(self, COMMA, Expression):
        self.COMMA = COMMA
        self.Expression = Expression

    def accept(self, Visitor):
        Visitor.visitSimpleExpList(self)

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

class EndCompTypeSpec(TypeSpecList):
    def __init__(self, TypeSpec, SEMICOLON):
        self.TypeSpec = TypeSpec
        self.SEMICOLON = SEMICOLON

    def accept(self, Visitor):
        Visitor.visitEndCompTypeSpec(self)

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

class EndCompVarSpec(VarSpecList):
    def __init__(self, VarSpec, SEMICOLON):
        self.VarSpec = VarSpec
        self.SEMICOLON = SEMICOLON

    def accept(self, Visitor):
        Visitor.visitEndCompVarSpec(self)

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
class CallFunc(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class SimpleCallFunc(CallFunc):
    def __init__(self, ID, LPAREN, ExpressionList, RPAREN):
        self.ID = ID
        self.LPAREN = LPAREN
        self.ExpressionList = ExpressionList
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitSimpleCallFunc(self)

##ABSTRATA##
class IncDec(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class IncOp(IncDec):
    def __init__(self, Expression, DPLUS):
        self.Expression = Expression
        self.DPLUS = DPLUS
        
    def accept(self, Visitor):
        Visitor.visitIncOp(self)

class DecOp(IncDec):
    def __init__(self, Expression, DMINUS):
        self.Expression = Expression
        self.DMINUS = DMINUS
        
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
        self.ExpressionList = ExpressionList
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
class DeclShortVarDef(ShortVarDecl):
    def __init__(self, IdentifierList, ASSIGN, ExpressionList):
        self.IdentifierList = IdentifierList
        self.ASSIGN = ASSIGN
        self.ExpressionList = ExpressionList    ##observar
        
    def accept(self, Visitor):
        Visitor.visitDeclShortVarDef(self)

##ABSTRATA##
class Expression(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionOR(Expression):
    def __init__(self, Exp, OR, Exp1):
        self.Exp = Exp
        self.OR = OR
        self.Exp1 = Exp1

    def accept(self, Visitor):
        Visitor.visitExpressionOR(self)

# class CallExp1(Expression):
#     def __init__(self, Exp1):
#         self.Exp1 = Exp1

#     def accept(self, Visitor):
#         Visitor.visitCallExp1(self)

##ABSTRATA##
class Exp1(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionAND(Exp1):
    def __init__(self, Expr1, AND, Expr2):
        self.Expr1 = Expr1
        self.AND = AND
        self.Exp2 = Exp2

    def accept(self, Visitor):
        Visitor.visitExpressionAND(self)

# class CallExp2(Exp1):
#     def __init__(self, Expr2):
#         self.Expr2 = Expr2

#     def accept(self, Visitor):
#         Visitor.visitCallExp2(self)

##ABSTRATA##
class Exp2(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionEquals(Exp2):
    def __init__(self, Expr2, EQUALS, Expr3):
        self.Expr2 = Expr2
        self.EQUALS = EQUALS
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionEquals(self)

class ExpressionDiferente(Exp2):
    def __init__(self, Expr2, DIFERENTE, Expr3):
        self.Expr2 = Expr2
        self.DIFERENTE = DIFERENTE
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionDiferente(self)

class ExpressionLess(Exp2):
    def __init__(self, Expr2, LESS, Expr3):
        self.Expr2 = Expr2
        self.LESS = LESS
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionLess(self)

class ExpressionLessEqual(Exp2):
    def __init__(self, Expr2, LESS_EQUAL, Expr3):
        self.Expr2 = Expr2
        self.LESS_EQUAL = LESS_EQUAL
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionLessEqual(self)

class ExpressionGreater(Exp2):
    def __init__(self, Expr2, GREATER, Expr3):
        self.Expr2 = Expr2
        self.GREATER = GREATER
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionGreater(self)

class ExpressionGreaterEqual(Exp2):
    def __init__(self, Expr2, GREATER_EQUAL, Expr3):
        self.Expr2 = Expr2
        self.GREATER_EQUAL = GREATER_EQUAL
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionGreaterEqual(self)

# class CallExp3(Exp2):
#     def __init__(self, Expr3):
#         self.Expr3 = Expr3

#     def accept(self, Visitor):
#         Visitor.visitCallExp3(self)

##ABSTRATA##
class Exp3(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionPlus(Exp3):
    def __init__(self, Expr4, PLUS, Expr3):
        self.Expr4 = Expr4
        self.PLUS = PLUS
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionPlus(self)

class ExpressionMinus(Exp3):
    def __init__(self, Expr4, MINUS, Expr3):
        self.Expr4 = Expr4
        self.MINUS = MINUS
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionMinus(self)

class ExpressionPot(Exp3):
    def __init__(self, Expr4, POT, Expr3):
        self.Expr4 = Expr4
        self.POT = POT
        self.Expr3 = Expr3

    def accept(self, Visitor):
        Visitor.visitExpressionPot(self)

# class CallExp4(Exp3):
#     def __init__(self, Expr4):
#         self.Expr4 = Expr4

#     def accept(self, Visitor):
#         Visitor.visitCallExp4(self)

##ABSTRATA##
class Exp4(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionTimes(Exp4):
    def __init__(self, Expr5, TIMES, Expr4):
        self.Expr5 = Expr5
        self.TIMES = TIMES
        self.Expr4 = Expr4

    def accept(self, Visitor):
        Visitor.visitExpressionTimes(self)

class ExpressionDivide(Exp4):
    def __init__(self, Expr5, DIVIDE, Expr4):
        self.Expr5 = Expr5
        self.DIVIDE = DIVIDE
        self.Expr4 = Expr4

    def accept(self, Visitor):
        Visitor.visitExpressionDivide(self)

class ExpressionMod(Exp4):
    def __init__(self, Expr5, MOD, Expr4):
        self.Expr5 = Expr5
        self.MOD = MOD
        self.Expr4 = Expr4
    
    def accept(self, Visitor):
        Visitor.visitExpressionMod(self)

class CallExp5(Exp4):
    def __init__(self, Expr5):
        self.Expr5 = Expr5

    def accept(self, Visitor):
        Visitor.visitCallExp5(self)

##ABSTRATA##
class Exp5(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
# class ExpressionNumber(Exp5):
#     def __init__(self, number):
#         self.number = number

#     def accept(self, Visitor):
#         Visitor.visitExpressionNumber(self)

class ExpressionCallFunc(Exp5):
    def __init__(self, callFunc):
        self.callFunc = callFunc

    def accept(self, Visitor):
        Visitor.visitExpressionCallFunc(self)

# class ExpressionID(Exp5):
#     def __init__(self, id):
#         self.id = id

#     def accept(self, Visitor):
#         Visitor.visitExpressionID(self)

class ExpressionParens(Exp5):
    def __init__(self, LPAREN, expression, RPAREN):
        self.LPAREN = LPAREN
        self.expression = expression
        self.RPAREN = RPAREN

    def accept(self, Visitor):
        Visitor.visitExpressionParens(self)

class PrintNumberID(Exp5):
    def __init__(self, numberOrId):
        self.numberOrId = numberOrId

    def accept(self, Visitor):
        Visitor.visitPrintNumberID(self)