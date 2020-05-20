#INICIO DA CONSTRUÇÃO SEMÂNTICO 
#Objetivo dessa arquivo (CLASSE) criar uma molde para todos visitantes.
#SUA COMPOSIÇÃO
#Metodos de visita para uma dos elemento concretos que possui na linguagem.
#@ABSTRACTMETHOD: O uso desse decorador exige que a metaclasse da classe
# seja ABCMeta ou seja derivada dela. Uma classe que possui
# uma metaclasse derivada ABCMeta não pode ser instanciada,
# a menos que todos os seus métodos e propriedades
# abstratos sejam substituídos. 

from abc import abstractmethod
from abc import ABCMeta

class GoAbstractVisitor(metaclass=ABCMeta):
    # FunctionDecl
    @abstractmethod
    def visitDefinirFunc(self, definirFunc):
        pass

    @abstractmethod
    def visitDefinirFuncBody(self, definirFuncBody):
        pass

    # Signature
    @abstractmethod
    def visitDefinirParamsT(self, definirParamsT):
        pass

    # Result
    @abstractmethod
    def visitDefinirTipo(self, definirTipo):
        pass
    
    # Type
    @abstractmethod
    def visitTint(self, Tint):
        pass

    @abstractmethod
    def visitTstring(self, Tstring):
        pass

    @abstractmethod
    def visitTbool(self, Tbool):
        pass

    @abstractmethod
    def visitTbyte(self, Tbyte):
        pass

    @abstractmethod
    def visitTfloat(self, Tfloat):
        pass

    # Parameters
    @abstractmethod
    def visitParams(self, params):
        pass

    @abstractmethod
    def visitParamsList(self, paramsList):
        pass

    @abstractmethod
    def visitDefinirParamsParameters(self, definirParams):
        pass

    # ParameterList
    @abstractmethod
    def visitCompParamsDecl(self, compParamsDecl):
        pass

    
    # ParameterList_Mul
    @abstractmethod
    def visitCallBackParameterList_Mul(self, callBackParameterList_Mul):
        pass
    
    @abstractmethod
    def visitEndParameterList_Mul(self, endParameterList_Mul):
        pass

    # ParameterDecl
    @abstractmethod
    def visitParamIdDecl(self, paramIdDecl):
        pass

    @abstractmethod
    def visitParamDecl(self, paramDecl):
        pass

    # Block
    @abstractmethod
    def visitDefinirStatementL(self, definirStatementL):
        pass

    @abstractmethod
    def visitMultFunc(self, multFunc):
        pass

    # StatementList
    @abstractmethod
    def visitDefinirStatement(self, definirStatement):
        pass

    @abstractmethod
    def visitCompoundStatmenteList(self, compoundStatmenteList):
       pass

    # Statement
    @abstractmethod
    def visitStmtDeclaration(self, stmtDeclaration):
        pass
    
    @abstractmethod
    def visitStmtSimple(self, stmtSimple):
        pass

    @abstractmethod
    def visitStmtReturn(self, stmtReturn):
        pass

    @abstractmethod
    def visitStmtBreak(self, stmtBreak):
        pass

    @abstractmethod
    def visitStmtContinue(self, stmtContinue):
        pass

    @abstractmethod
    def visitStmtBlock(self, stmtBlock):
        pass

    @abstractmethod
    def visitStmtIf(self, stmtIf):
        pass
    
    @abstractmethod
    def visitStmtSwitch(self, stmtSwitch):
        pass

    @abstractmethod
    def visitCallStmtFor(self, stmtFor):
        pass
    
    # Declaration
    @abstractmethod
    def visitDeclConst(self, declConst):
        pass

    @abstractmethod
    def visitDeclType(self, declType):
        pass

    @abstractmethod
    def visitDeclVar(self, declVar):
        pass

    # SimpleStmt
    @abstractmethod
    def visitStmtCondition(self, stmtCondition):
        pass

    @abstractmethod
    def visitStmtIncDec(self, stmtIncDec):
        pass

    @abstractmethod
    def visitAssign(self, assign):
        pass

    @abstractmethod
    def visitDeclShortVar(self, declShortVar):
        pass

    # ReturnStmt
    @abstractmethod
    def visitExpReturn(self, expReturn):
        pass

    @abstractmethod
    def visitSimpleReturn(self, simpleReturn):
        pass

    # BreakStmt
    @abstractmethod
    def visitStmtBreack(self, stmtBreack):
        pass

    # ContinueStmt
    @abstractmethod
    def visitStmtContinuePrint(self, stmtContinue):
        pass

    # Ifstmt
    @abstractmethod
    def visitSimpleIf(self, simpleIf):
        pass

    @abstractmethod
    def visitCompIfElse(self, compIfElse):
        pass

    @abstractmethod
    def visitIfElse(self, ifElse):
        pass
    
    # SwitchStmt
    @abstractmethod
    def visitExprSwitch(self, exprSwitch):
        pass

    # SwitchStmt_Head
    @abstractmethod
    def visitExprSwitchSimple(self, exprSwitchSimple):
        pass

    # ExprSwitchHead1
    @abstractmethod
    def visitExprSwitchHead1(self, exprSwitchHead1):
        pass

    # ExprSwitchHead2 
    @abstractmethod
    def visitExprSwitchHead2(self, exprSwitchHead2):
        pass

    # ExprSwitchBody1
    @abstractmethod
    def visitExprSwitchBody1(self, exprSwitchBody1):
        pass

    # ExprSwitchBody2
    @abstractmethod
    def visitExprSwitchBody2(self, exprSwitchBody2):
        pass

    @abstractmethod
    def visitExprSwitchExp(self, exprSwitchExp):
        pass
    
    # ExprCaseClauseList
    @abstractmethod
    def visitCompoundCaseClause1(self, compoundCaseClase1):
        pass

    # ExprCaseClause
    @abstractmethod
    def visitExprCase(self, exprCase):
        pass

    # ExprSwitchCase
    @abstractmethod
    def visitCaseClauseExp(self, caseClauseExp):
        pass

    @abstractmethod
    def visitCaseClause(self, caseClause):
        pass

    # ForStmt
    @abstractmethod
    def visitStmtFor(self, stmtFor):
        pass
    
    @abstractmethod
    def visitStmtForClause(self, stmtForClause):
        pass

    @abstractmethod
    def visitStmtForRange(self, stmtForRange):
        pass

    @abstractmethod
    def visitStmtForBlock(self, stmtForBlock):
        pass

    # Condition
    @abstractmethod
    def visitDefinirCondition(self, definirCondition):
        pass

    # ForClause
    @abstractmethod
    def visitClassicFor(self, classicFor):
        pass

    @abstractmethod
    def visitclassicFor2(self, classicFor2):
        pass

    # RangeClause
    @abstractmethod
    def visitDefinirRange(self, definirRange):
        pass

    @abstractmethod
    def visitRangeExpList(self, rangeExpList):
        pass

    @abstractmethod
    def visitRangIDList(self, rangIDList):
        pass

    # ConstDecl
    @abstractmethod
    def visitSimpleConst(self, simpleConst):
        pass

    @abstractmethod
    def visitCompConst(self, compConst):
        pass

    # ConstSpecList
    @abstractmethod
    def visitCallConstSpec(self, callConstSpec):
        pass

    @abstractmethod
    def visitCompoundConstSpec(self, compoundConstSpec):
        pass

    @abstractmethod
    def visitListIdExp(self, listIdExp):
        pass

    @abstractmethod
    def visitListTypeExp(self, listTypeExp):
        pass

     # IdentifierLis
    @abstractmethod
    def visitDefinirIDList(self, definirIDList):
        pass

    @abstractmethod
    def visitDefinirID(self, definirID):
        pass

    # CompIDList
    @abstractmethod
    def visitCompoundIDList(self, compoundIDList):
        pass

    @abstractmethod
    def visitEndCompID(self, compoundIDList):
        pass

    # ExpressionList
    @abstractmethod
    def visitDefinirExpList(self, definirExpList):
        pass

    @abstractmethod
    def visitCallExpList(self, callExpList):
        pass

     # ListExpr
    @abstractmethod
    def visitSimpleExpList(self, simpleExpList):
        pass

    @abstractmethod
    def visitCompoundExpList(self, compoundExpList):
        pass

    # TypeDecl
    @abstractmethod
    def visitDefinirType(self, definirType):
        pass

    @abstractmethod
    def visitCallTypeSpecList(self, callTypeSpecList):
        pass

    # TypeSpecList
    @abstractmethod
    def visitCompTypeSpecList(self, compTypeSpecList):
        pass

    @abstractmethod
    def visitEndCompTypeSpec(self, endCompTypeSpec):
        pass

    # TypeSpec
    @abstractmethod
    def visitSpecType(self, specType):
        pass

    # VarDecl
    @abstractmethod
    def visitDefinirVar(self, definirVar):
        pass

    @abstractmethod
    def visitCompVar(self, compVar):
        pass

    # VarSpecList
    @abstractmethod
    def visitCompoundVarSpec(self, compoundVarSpec):
        pass

    @abstractmethod
    def visitEndCompVarSpec(self, endCompVarSpec):
        pass

    # VarSpec
    @abstractmethod
    def visitSpecVar(self, specVar):
        pass

    @abstractmethod
    def visitClassicVarSpec(self, classicVarSpec):
        pass

    @abstractmethod
    def visitSimpleVarSpec(self, simpleVarSpec):
        pass

    # CallFunc
    @abstractmethod
    def visitSimpleCallFunc(self, simpleCallFunc):
        pass

    @abstractmethod
    def visitCallParenFunc(self, callParenFunc):
        pass

    # IncDec
    @abstractmethod
    def visitIncOp(self, incOp):
        pass

    @abstractmethod
    def visitDecOp(self, decOp):
        pass

    # Assignment
    @abstractmethod
    def visitAssignOp(self, assignOp): #observacao
        pass

    # ShortVarDec
    @abstractmethod
    def visitDeclShortVarDef(self, declShortVar):
        pass

    # Expression
    @abstractmethod
    def visitExpressionOR(self, expressionOR):
        pass

    @abstractmethod
    def visitCallExp1(self, callExp1):
        pass

    # Exp1
    @abstractmethod
    def visitExpressionAND(self, expressionAND):
        pass

    # Exp1
    #@abstractmethod
    #def visitExpressionAND(self, expressionAND):
    #    pass
    #ATENÇÃO -  DOIS METODOS IGUAIS -  EXP1 

    # Exp2
    @abstractmethod
    def visitExpressionEquals(self, expressionEquals):
        pass

    @abstractmethod
    def visitExpressionDiferente(self, expressionDiferente):
        pass

    @abstractmethod
    def visitExpressionLess(self, expressionLess):
        pass

    @abstractmethod
    def visitExpressionLessEqual(self, expressionLessEqual):
        pass
    
    @abstractmethod
    def visitExpressionGreater(self, expressionGreater):
        pass

    @abstractmethod
    def visitExpressionGreaterEqual(self, expressionGreaterEqual):
        pass

    @abstractmethod
    def visitCallExp3(self, callExp3):
        pass

    # Exp3
    @abstractmethod
    def visitExpressionPlus(self, expressionPlus):
        pass
    
    @abstractmethod
    def visitExpressionMinus(self, expressionMinus):
        pass

    @abstractmethod
    def visitExpressionPot(self, expressionPot):
        pass

    @abstractmethod
    def visitCallExp4(self, callExp4):
        pass

    # Exp4
    @abstractmethod
    def visitExpressionTimes(self, expressionTimes):
        pass

    @abstractmethod
    def visitExpressionDivide(self, expressionDivide):
        pass

    @abstractmethod
    def visitExpressionMod(self, expressionMod):
        pass

    @abstractmethod
    def visitPrintNumberID(self, printNumberID):
        pass

    # Exp5
    @abstractmethod
    def visitExpressionNumber(self, expressionNumber):
        pass

    @abstractmethod
    def visitExpressionCallFunc(self, expressionCallFunc):
        pass

    @abstractmethod
    def visitExpressionID(self, expressionID):
        pass

    @abstractmethod
    def visitExpressionParens(self, expressionParens):
        pass










    



























