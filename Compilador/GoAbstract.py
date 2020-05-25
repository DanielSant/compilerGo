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
    def __init__(self, ID, Signature):
        self.ID = ID
        self.Signature = Signature

    def accept(self, Visitor):
        return Visitor.visitDefinirFunc(self)

class DefinirFuncBody(FunctionDecl):
    def __init__(self, ID, Signature, FunctionBody):
        self.ID = ID
        self.Signature = Signature
        self.FunctionBody = FunctionBody

    def accept(self, Visitor):
        return Visitor.visitDefinirFuncBody(self)

##ABSTRATA##
class Signature(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

class DefinirParamsT(Signature):
	def __init__(self, Params, Result):
		self.Params = Params
		self.Result = Result

	def accept(self, Visitor):
		return Visitor.visitDefinirParamsT(self)

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
		return Visitor.visitDefinirTipo(self)

##ABSTRATA##
class Type(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##ABSTRATA##
class Parameters(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class Params(Parameters):
    def __init__(self, ParameterList):
        self.ParameterList = ParameterList

    def accept(self, Visitor):
        return Visitor.visitParams(self)

class DefinirParamsParameters(Parameters):
    def __init__(self):
        pass

    def accept(self, Visitor):
        return Visitor.visitDefinirParamsParameters(self)

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
        return Visitor.visitCompParamsDecl(self)

##ABSTRATA##
class ParameterList_Mul(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCREATA##
class CallBackParameterList_Mul(ParameterList_Mul):
    def __init__(self, ParameterDecl, ParameterList_Mul1):
        self.ParameterDecl = ParameterDecl
        self.ParameterList_Mul1 = ParameterList_Mul1

    def accept(self, Visitor):
        return Visitor.visitCallBackParameterList_Mul(self)

class EndParameterList_Mul(ParameterList_Mul):
    def __init__(self, ParameterDecl):
        self.ParameterDecl = ParameterDecl
    
    def accept(self, Visitor):
        return Visitor.visitEndParameterList_Mul(self)

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
        return Visitor.visitParamIdDecl(self)

class ParamDecl(ParameterDecl):
    def __init__(self, Type):
        self.Type = Type

    def accept(self, Visitor):
        return Visitor.visitParamDecl(self)

##ABSTRATA##
class Block(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirStatementL(Block):
    def __init__(self, StatementList):
        self.StatementList = StatementList

    def accept(self, Visitor):
        return Visitor.visitDefinirStatementL(self)

class MultFunc(Block):
    def __init__(self, StatementList, FunctionDecl):
        self.StatementList = StatementList
        self.FunctionDecl = FunctionDecl

    def accept(self, Visitor):
        return Visitor.visitMultFunc(self)

##ABSTRATA##
class StatementList(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class DefinirStatement(StatementList): ##PRECISA OBSERVAR ISSO
    def __init__ (self, Statement):
        self.Statement = Statement

    def accept(self, Visitor):
        return Visitor.visitDefinirStatement(self)

class CompoundStatementList(StatementList):
    def __init__(self, statement, statementList):
        self.statement = statement
        self.statementList = statementList

    def accept(self, Visitor):
        return Visitor.visitCompoundStatmenteList(self)

##ABSTRATA##
class Statement(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##ABSTRATA##
class Declaration(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##ABSTRATA##
class SimpleStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##ABSTRATA##
class ReturnStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpReturn(ReturnStmt):
    def __init__(self, ExpressionList):
        self.ExpressionList = ExpressionList
    
    def accept(self, Visitor):
        return Visitor.visitExpReturn(self)

class SimpleReturn(ReturnStmt):
    def __init__(self):
        pass

    def accept(self, Visitor):
        return Visitor.visitSimpleReturn(self)

 ##ABSTRATA##
class BreakStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class StmtBreak(BreakStmt):
    def __init__(self):
        pass

    def accept(self, Visitor):
        return Visitor.visitStmtBreack(self)

##ABSTRATA##
class ContinueStmt(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class StmtContinuePrint(ContinueStmt):
    def __init__(self):
        pass

    def accept(self, Visitor):
        return Visitor.visitStmtContinuePrint(self)

##ABSTRATA##
class IfStmt(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class SimpleIf(IfStmt):
    def __init__(self, Expression, Block):
        self.Expression = Expression
        self.Block = Block

    def accept(self, Visitor):
        return Visitor.visitSimpleIf(self)

class CompIfElse(IfStmt):
    def __init__(self, Expression, Block, IfStmt):
        self.Expression = Expression
        self.Block = Block
        self.IfStmt = IfStmt

    def accept(self, Visitor):
        return Visitor.visitCompIfElse(self)

class IfElse(IfStmt):
    def __init__(self, Expression, Block, Block1):
        self.Expression = Expression
        self.Block = Block
        self.Block1 = Block1

    def accept(self, Visitor):
        return Visitor.visitIfElse(self)

##ABSTRATA##
class SwitchStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExprSwitch(SwitchStmt):
    def __init__(self, switchStmt_Head, switchStmt_Body):
        self.switchStmt_Head = switchStmt_Head
        self.switchStmt_Body = switchStmt_Body

    def accept(self, Visitor):
        return Visitor.visitExprSwitch(self)

class ExprSwitchSimple(SwitchStmt):
    def __init__(self, switchStmt_Body):
        self.switchStmt_Body = switchStmt_Body

    def accept(self, Visitor):
        return Visitor.visitExprSwitchSimple(self)

##ABSTRATA
class SwitchStmt_Head(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA
class ExprSwitchHead1(SwitchStmt_Head):
    def __init__(self, simpleStmt, expression):
        self.simpleStmt = simpleStmt
        self.expression = expression

    def accept(self, Visitor):
        return Visitor.visitExprSwitchHead1(self)

class ExprSwitchHead2(SwitchStmt_Head):
    def __init__(self, simpleStmt):
        self.simpleStmt = simpleStmt

    def accept(self, Visitor):
        return Visitor.visitExprSwitchHead2(self)

##ABSTRATA
class SwitchStmt_Body(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA
class ExprSwitchBody1(SwitchStmt_Body):
    def __init__(self, exprCaseClauseList):
        self.exprCaseClauseList = exprCaseClauseList

    def accept(self, Visitor):
        return Visitor.visitExprSwitchBody1(self)

class ExprSwitchBody2(SwitchStmt_Body):
    def __init__(self):
        pass

    def accept(self, Visitor):
        return Visitor.visitExprSwitchBody2(self)

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
        return Visitor.visitCompoundCaseClause1(self)

##ABSTRATA##
class ExprCaseClause(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class ExprCase(ExprCaseClause):
    def __init__(self, ExprSwitchCase, StatementList):
        self.ExprSwitchCase = ExprSwitchCase
        self.StatementList = StatementList
    
    def accept(self, Visitor):
        return Visitor.visitExprCase(self)

##ABSTRATA##
class ExprSwitchCase(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CaseClauseExp(ExprSwitchCase):
    def __init__(self, ExpressionList):
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        return Visitor.visitCaseClauseExp(self)

class CaseClause(ExprSwitchCase):
    def __init__(self):
        pass

    def accept(self, Visitor):
        return Visitor.visitCaseClause(self)

##ABSTRATA##
class ForStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class StmtFor(ForStmt):
    def __init__(self, Condition, Block):
        self.Condition = Condition
        self.Block = Block

    def accept(self, Visitor):
        return Visitor.visitStmtFor(self)

class StmtForClause(ForStmt):
    def __init__(self, ForClause, Block):
        self.ForClause = ForClause
        self.Block = Block

    def accept(self, Visitor):
        return Visitor.visitStmtForClause(self)

class StmtForRange(ForStmt):
    def __init__(self, RangeClause, Block):
        self.RangeClause = RangeClause
        self.Block = Block

    def accept(self, Visitor):
        return Visitor.visitStmtForRange(self)

class StmtForBlock(ForStmt):
    def __init__(self, Block):
        self.Block = Block

    def accept(self, Visitor):
        return Visitor.visitStmtForBlock(self)

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
        return Visitor.visitDefinirCondition(self)

##ABSTRATA##
class ForClause(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ClassicFor(ForClause):
    def __init__(self, initPostStmt, Condition, initPostStmt1):
        self.initPostStmt = initPostStmt
        self.Condition = Condition
        self.initPostStmt1 = initPostStmt1

    def accept(self, Visitor):
        return Visitor.visitClassicFor(self)

class ClassicFor2(ForClause):
    def __init__(self, Condition):
        self.Condition = Condition

    def accept(self, Visitor):
        return Visitor.visitclassicFor2(self)

##ABSTRATA##
class InitPostStmt(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##ABSTRATA##
class RangeClause(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirRange(RangeClause):
    def __init__(self, Expression):
        self.Expression = Expression

    def accept(self, Visitor):
        return Visitor.visitDefinirRange(self)

class RangeExpList(RangeClause): 
    def __init__(self, ExpressionList, Expression):
        self.ExpressionList = ExpressionList
        self.Expression = Expression

    def accept(self, Visitor):
        return Visitor.visitRangeExpList(self)

##ABSTRATA##
class ConstDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class SimpleConst(ConstDecl):
    def __init__ (self, ConstSpec):
        self.ConstSpec = ConstSpec

    def accept(self, Visitor):
        return Visitor.visitSimpleConst(self)

class CompConst(ConstDecl):
    def __init__(self, constSpecList):
        self.constSpecList = constSpecList
    
    def accept(self, Visitor):
        return Visitor.visitCompConst(self)

##ABSTRATA##
class ConstSpecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CallConstSpec(ConstSpecList):
    def __init__(self, ConstSpec):
        self.ConstSpec = ConstSpec

    def accept(self, Visitor):
        return Visitor.visitCallConstSpec(self)

class CompoundConstSpec(ConstSpecList):
    def __init__(self, ConstSpec, ConstSpecList):
        self.ConstSpec = ConstSpec
        self.ConstSpecList = ConstSpecList

    def accept(self, Visitor):
        return Visitor.visitCompoundConstSpec(self)

##ABSTRATA##
class ConstSpec(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

class ListIdExp(ConstSpec):
    def __init__(self, IdentifierList, ExpressionList):
        self.IdentifierList = IdentifierList
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        return Visitor.visitListIdExp(self)

class ListIdTypeExp(ConstSpec):
    def __init__(self, IdentifierList, Type, ExpressionList):
        self.IdentifierList = IdentifierList
        self.Type = Type
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        return Visitor.visitListTypeExp(self)

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
        return Visitor.visitDefinirIDList(self)

class DefinirID(IdentifierList):
    def __init__(self, ID):
        self.ID = ID
        
    def accept(self, Visitor):
        return Visitor.visitDefinirID(self)

##ABSTRATA
class CompIDList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompoundIDList(CompIDList):
    def __init__(self, ID, CompIDList):
        self.ID = ID
        self.CompIDList = CompIDList

    def accept(self, Visitor):
        return Visitor.visitCompoundIDList(self)

class EndCompID(CompIDList):
    def __init__(self, ID):
        self.ID = ID

    def accept(self, Visitor):
        return Visitor.visitEndCompID(self)

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
        return Visitor.visitCallExpList(self)

##ABSTRATA##
class ListExpr(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompoundExpList(ListExpr):
    def __init__(self, Expression, ListExpr):
        self.Expression = Expression
        self.ListExpr = ListExpr

    def accept(self, Visitor):
        return Visitor.visitCompoundExpList(self)

class SimpleExpList(ListExpr):
    def __init__(self, Expression):
        self.Expression = Expression

    def accept(self, Visitor):
        return Visitor.visitSimpleExpList(self)

##ABSTRATA##
class TypeDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DefinirType(TypeDecl): 
    def __init__(self, TypeSpec):
        self.TypeSpec = TypeSpec

    def accept(self, Visitor):
        return Visitor.visitDefinirType(self)

class CallTypeSpecList(TypeDecl):
    def __init__(self, TypeSpecList):
        self.TypeSpecList = TypeSpecList

    def accept(self, Visitor):
        return Visitor.visitCallTypeSpecList(self)

##ABSTRATA##
class TypeSpecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompTypeSpecList(TypeSpecList):
    def __init__(self, TypeSpec, TypeSpecList):
        self.TypeSpec = TypeSpec
        self.TypeSpecList = TypeSpecList

    def accept(self, Visitor):
        return Visitor.visitCompTypeSpecList(self)

class EndCompTypeSpec(TypeSpecList):
    def __init__(self, TypeSpec):
        self.TypeSpec = TypeSpec

    def accept(self, Visitor):
        return Visitor.visitEndCompTypeSpec(self)

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
	    return Visitor.visitSpecType(self)

##ABSTRATA##
class VarDecl(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, Visitor):
		pass

##CONCRETA##
class DefinirVar(VarDecl):
	def __init__(self, VarSpec):
		self.VarSpec = VarSpec

	def accept(self, Visitor):
		return Visitor.visitDefinirVar(self)

class CompVar(VarDecl):
    def __init__(self, VarSpecList):
        self.VarSpecList = VarSpecList
        
    def accept(self, Visitor):
        return Visitor.visitCompVar(self)

##ABSTRATA##
class VarSpecList(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class CompoundVarSpec(VarSpecList):
    def __init__(self, VarSpec, VarSpecList):
        self.VarSpec = VarSpec
        self.VarSpecList = VarSpecList

    def accept(self, Visitor):
        return Visitor.visitCompoundVarSpec(self)

class EndCompVarSpec(VarSpecList):
    def __init__(self, VarSpec):
        self.VarSpec = VarSpec

    def accept(self, Visitor):
        return Visitor.visitEndCompVarSpec(self)

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
		return Visitor.visitSpecVar(self)

class ClassicVarSpec(VarSpec):
	def __init__(self, IdentifierList, Type, ExpressionList):
		self.IdentifierList = IdentifierList
		self.Type = Type
		self.ExpressionList = ExpressionList

	def accept(self, Visitor):
		return Visitor.visitClassicVarSpec(self)

class SimpleVarSpec(VarSpec):
	def __init__(self, IdentifierList, ExpressionList):
		self.IdentifierList = IdentifierList
		self.ExpressionList = ExpressionList

	def accept(self, Visitor):
		return Visitor.visitSimpleVarSpec(self)

##ABSTRATA##
class CallFunc(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class SimpleCallFunc(CallFunc):
    def __init__(self, ID, ExpressionList):
        self.ID = ID
        self.ExpressionList = ExpressionList

    def accept(self, Visitor):
        return Visitor.visitSimpleCallFunc(self)

class CallParenFunc(CallFunc):
    def __init__(self, ID):
        self.ID = ID

    def accept(self, Visitor):
        return Visitor.visitCallParenFunc(self)

##ABSTRATA##
class IncDec(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class IncOp(IncDec):
    def __init__(self, Expression):
        self.Expression = Expression
        
    def accept(self, Visitor):
        return Visitor.visitIncOp(self)

class DecOp(IncDec):
    def __init__(self, Expression):
        self.Expression = Expression
        
    def accept(self, Visitor):
        return Visitor.visitDecOp(self)

##ABSTRATA##
class Assignment(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class AssignOp(Assignment):
    def __init__(self, ExpressionList, ExpressionList1):
        self.ExpressionList = ExpressionList
        self.ExpressionList1 = ExpressionList1
        
    def accept(self, Visitor):
        return Visitor.visitAssignOp(self)

##ABSTRATA##
class ShortVarDecl(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class DeclShortVarDef(ShortVarDecl):
    def __init__(self, IdentifierList, ExpressionList):
        self.IdentifierList = IdentifierList
        self.ExpressionList = ExpressionList  
        
    def accept(self, Visitor):
        return Visitor.visitDeclShortVarDef(self)

##ABSTRATA##
class Expression(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionOR(Expression):
    def __init__(self, Exp, Exp1):
        self.Exp = Exp
        self.Exp1 = Exp1

    def accept(self, Visitor):
        return Visitor.visitExpressionOR(self)

##ABSTRATA##
class Exp1(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionAND(Exp1):
    def __init__(self, Expr1, Expr2):
        self.Expr1 = Expr1
        self.Expr2 = Expr2

    def accept(self, Visitor):
        return Visitor.visitExpressionAND(self)

##ABSTRATA##
class Exp2(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionEquals(Exp2):
    def __init__(self, Expr2, Expr3):
        self.Expr2 = Expr2
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionEquals(self)

class ExpressionDiferente(Exp2):
    def __init__(self, Expr2, Expr3):
        self.Expr2 = Expr2
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionDiferente(self)

class ExpressionLess(Exp2):
    def __init__(self, Expr2, Expr3):
        self.Expr2 = Expr2
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionLess(self)

class ExpressionLessEqual(Exp2):
    def __init__(self, Expr2, Expr3):
        self.Expr2 = Expr2
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionLessEqual(self)

class ExpressionGreater(Exp2):
    def __init__(self, Expr2, Expr3):
        self.Expr2 = Expr2
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionGreater(self)

class ExpressionGreaterEqual(Exp2):
    def __init__(self, Expr2, Expr3):
        self.Expr2 = Expr2
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionGreaterEqual(self)

##ABSTRATA##
class Exp3(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionPlus(Exp3):
    def __init__(self, Expr4, Expr3):
        self.Expr4 = Expr4
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionPlus(self)

class ExpressionMinus(Exp3):
    def __init__(self, Expr4, Expr3):
        self.Expr4 = Expr4
        self.Expr3 = Expr3

    def accept(self, Visitor):
        return Visitor.visitExpressionMinus(self)
        

##ABSTRATA##
class Exp4(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

##CONCRETA##
class ExpressionTimes(Exp4):
    def __init__(self, Expr5, Expr4):
        self.Expr5 = Expr5
        self.Expr4 = Expr4

    def accept(self, Visitor):
        return Visitor.visitExpressionTimes(self)

class ExpressionDivide(Exp4):
    def __init__(self, Expr5, Expr4):
        self.Expr5 = Expr5
        self.Expr4 = Expr4

    def accept(self, Visitor):
        return Visitor.visitExpressionDivide(self)

class ExpressionMod(Exp4):
    def __init__(self, Expr5, Expr4):
        self.Expr5 = Expr5
        self.Expr4 = Expr4
    
    def accept(self, Visitor):
        return Visitor.visitExpressionMod(self)

class CallExp5(Exp4):
    def __init__(self, Expr5):
        self.Expr5 = Expr5

    def accept(self, Visitor):
        return Visitor.visitCallExp5(self)

##ABSTRATA##
class Exp5(metaclass=ABCMeta):
    @abstractclassmethod
    def accept(self, Visitor):
        pass

class ExpressionCallFunc(Exp5):
    def __init__(self, callFunc):
        self.callFunc = callFunc

    def accept(self, Visitor):
        return Visitor.visitExpressionCallFunc(self)

class ExpressionParens(Exp5):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, Visitor):
        return Visitor.visitExpressionParens(self)

class PrintNumberID(Exp5):
    def __init__(self, numberOrId):
        self.numberOrId = numberOrId

    def accept(self, Visitor):
        return Visitor.visitPrintNumberID(self)