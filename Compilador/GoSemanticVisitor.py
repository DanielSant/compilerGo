from GoAbstractVisitor import AbstractVisitor
import GoSymbolTable as st
from GoVisitor import Visitor
import GoAbstract as sa

def coercion(type1, type2):
    if (type in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')

    # FunctionDecl
    def visitDefinirFunc(self, definirFunc):
        parametrosRetorno = definirFunc.Signature.accept(self)
        st.addFunction(definirFunc.ID, parametrosRetorno[0:-1], parametrosRetorno[-1])

    def visitDefinirFuncBody(self, definirFuncBody):
        parametrosRetorno = definirFuncBody.Signature.accept(self)
        st.addFunction(definirFuncBody.ID, parametrosRetorno[0:-1], parametrosRetorno[-1])
        definirFuncBody.FunctionBody.accept(self)

    # Signature
    def visitDefinirParamsT(self, definirParamsT)
        parametros = {}
        if (definirParamsT.Params != None):
            parametros = definirParamsT.Params.accept(self)
        
        tipoRetorno = definirParamsT.Result.accept(self)
        return [parametros] + tipoRetorno

    # Result
    def visitDefinirTipo(self, definirTipo)
        return definirTipo.Type

    # Type
    # def visitTint()

    # def visitTstring()

    # def visitTbool()

    # def visitTbyte()

    # def visitTfloat()

    # Parameters
    def visitParams(self, params): # Unico parametro
        params.ParameterList.accept(self)

    def visitParamsList(self, paramsList): # Lista de parametros
        paramsList.ParameterList.accept(self)

    # ParameterList
    def visitCompParamsDecl(self, compParamsDecl):
        compParamsDecl.ParameterDecl.accept(self)
        compParamsDecl.ParameterList_Mul.accept(self)

    # ParameterList_Mul
    def visitCallBackParameterList_Mul(self, callBackParameterList_Mul)

    def visitEndParameterList_Mul(self, endParameterList_Mul)

    # ParameterDecl
    def visitParamIdDecl(self, paramIdDecl):
        nomeFuncao = paramIdDecl.IdentifierList.accept(self)
        # st.addVar(None, paramIdDecl.Type)

    def visitParamDecl(self, paramDecl):
        st.addVar(paramDecl.ID)

    # Block
    def visitDefinirStatementL(self, definirStatementL)

    def visitMultFunc(self, multFunc)

    # StatementList
    def visitDefinirStatement(self, definirStatement)

    def visitCompoundStatmenteList(self, compoundStatmenteList)

    # Statement
    def visitStmtDeclaration(self, stmtDeclaration)

    def visitStmtSimple(self, stmtSimple)

    def visitStmtReturn(self, stmtReturn)
    
    def visitStmtBreak(self, stmtBreak)
    
    def visitStmtContinue(self, stmtContinue)
    
    def visitStmtBlock(self, stmtBlock)
    
    def visitStmtIf(self, stmtIf)
    
    def visitStmtSwitch(self, stmtSwitch)
    
    def visitCallStmtFor(self, stmtFor)

    # Declaration
    def visitDeclConst(self, declConst)
    
    def visitDeclType(self, declType)
    
    def visitDeclVar(self, declVar)
    
    # SimpleStmt
    def visitStmtCondition(self, stmtCondition)

    def visitStmtIncDec(self, stmtIncDec)
    
    def visitAssign(self, assign)
    
    def visitDeclShortVar(self, declShortVar)
    
    # ReturnStmt
    def visitExpReturn(self, expReturn)

    def visitSimpleReturn(self, simpleReturn)
    
    # BreakStmt
    def visitStmtBreack(self, stmtBreack)

    # ContinueStmt
    def visitStmtContinuePrint(self, stmtContinue)
    
    # Ifstmt
    def visitSimpleIf(self, simpleIf)

    def visitCompIfElse(self, compIfElse)
    
    def visitIfElse(self, ifElse)
        
    # SwitchStmt
    def visitExprSwitch(self, exprSwitch)
    
    # SwitchStmt_Head
    def visitExprSwitchSimple(self, exprSwitchSimple)

    # ExprSwitchHead1
    def visitExprSwitchHead1(self, exprSwitchHead1)
    
    # ExprSwitchHead2 
    def visitExprSwitchHead2(self, exprSwitchHead2)

    # ExprSwitchBody1
    def visitExprSwitchBody1(self, exprSwitchBody1)

    # ExprSwitchBody2
    def visitExprSwitchBody2(self, exprSwitchBody2)

    def visitExprSwitchExp(self, exprSwitchExp)

    # ExprCaseClauseList
    def visitCompoundCaseClause1(self, compoundCaseClase1)

    # ExprCaseClause
    def visitExprCase(self, exprCase)

    # ExprSwitchCase
    def visitCaseClauseExp(self, caseClauseExp)

    def visitCaseClause(self, caseClause)

    # ForStmt
    def visitStmtFor(self, stmtFor)

    def visitStmtForClause(self, stmtForClause)

    def visitStmtForRange(self, stmtForRange)

    def visitStmtForBlock(self, stmtForBlock)

    # Condition
    def visitDefinirCondition(self, definirCondition)
    # ForClause
    def visitClassicFor(self, classicFor)

    def visitclassicFor2(self, classicFor2)

    # RangeClause
    def visitDefinirRange(self, definirRange)

    def visitRangeExpList(self, rangeExpList)

    def visitRangIDList(self, rangIDList)

    # ConstDecl
    def visitSimpleConst(self, simpleConst)

    def visitCompConst(self, compConst)

    # ConstSpecList
    def visitCallConstSpec(self, callConstSpec)

    def visitCompoundConstSpec(self, compoundConstSpec)

    def visitListIdExp(self, listIdExp)

    def visitListTypeExp(self, listTypeExp)
    
    # IdentifierList
    def visitDefinirIDList(self, definirIDList)
    
    def visitDefinirID(self, definirID)

    # CompIDList
    def visitCompoundIDList(self, compoundIDList)

    def visitEndCompID(self, compoundIDList)
    # ExpressionList
    def visitDefinirExpList(self, definirExpList)

    def visitCallExpList(self, callExpList)

    # ListExpr
    def visitSimpleExpList(self, simpleExpList)

    def visitCompoundExpList(self, compoundExpList)

    # TypeDecl
    def visitDefinirType(self, definirType)

    def visitCallTypeSpecList(self, callTypeSpecList)

    # TypeSpecList
    def visitCompTypeSpecList(self, compTypeSpecList)

    def visitEndCompTypeSpec(self, endCompTypeSpec)

    # TypeSpec
    def visitSpecType(self, specType)

    # VarDecl
    def visitDefinirVar(self, definirVar)

    def visitCompVar(self, compVar)

    # VarSpecList
    def visitCompoundVarSpec(self, compoundVarSpec)

    def visitEndCompVarSpec(self, endCompVarSpec)

    # VarSpec
    def visitSpecVar(self, specVar)

    def visitClassicVarSpec(self, classicVarSpec)

    def visitSimpleVarSpec(self, simpleVarSpec)

    # CallFunc
    def visitSimpleCallFunc(self, simpleCallFunc)

    def visitCallParenFunc(self, callParenFunc)

    # IncDec
    def visitIncOp(self, incOp)

    def visitDecOp(self, decOp)

    # Assignment
    def visitAssignOp(self, assignOp)

    # ShortVarDec
    def visitDeclShortVarDef(self, declShortVar)
    
    # Expression
    def visitExpressionOR(self, expressionOR)

    def visitCallExp1(self, callExp1)

    # Exp1
    def visitExpressionAND(self, expressionAND)

    def visitCallExp2(self, callExp2)

    # Exp2
    def visitExpressionEquals(self, expressionEquals)

    def visitExpressionDiferente(self, expressionDiferente)

    def visitExpressionLess(self, expressionLess)

    def visitExpressionLessEqual(self, expressionLessEqual)

    def visitExpressionGreater(self, expressionGreater)

    def visitExpressionGreaterEqual(self, expressionGreaterEqual)

    def visitCallExp3(self, callExp3)

    # Exp3
    def visitExpressionPlus(self, expressionPlus)

    def visitExpressionMinus(self, expressionMinus)

    def visitExpressionPot(self, expressionPot)

    def visitCallExp4(self, callExp4)

    # Exp4
    def visitExpressionTimes(self, expressionTimes)

    def visitExpressionDivide(self, expressionDivide)

    def visitExpressionMod(self, expressionMod)

    def visitPrintNumberID(self, printNumberID)

    # Exp5
    def visitExpressionNumber(self, expressionNumber)

    def visitExpressionCallFunc(self, expressionCallFunc)

    def visitExpressionID(self, expressionID)

    def visitExpressionParens(self, expressionParens)