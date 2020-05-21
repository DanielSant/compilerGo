from GoAbstractVisitor import GoAbstractVisitor
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

class GoSemanticVisitor(GoAbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')

    # FunctionDecl
    def visitDefinirFuncBody(self, definirFuncBody):
        parametrosRetorno = definirFuncBody.Signature.accept(self)
        st.addFunction(definirFuncBody.ID, parametrosRetorno[0:-1], parametrosRetorno[-1])
        st.beginScope(definirFuncBody.ID)
        for k in range(0, len(parametrosRetorno[0:-1]), 2):
            st.addVar(parametrosRetorno[0:-1][k], parametrosRetorno[0:-1][k+1])

        # print('symbolTable', st.symbolTable)
        definirFuncBody.FunctionBody.accept(self)

    # Signature
    def visitDefinirParamsT(self, definirParamsT): # ok
        parametros = {}
        if (definirParamsT.Params != None):
            parametros = definirParamsT.Params.accept(self)
        
        tipoRetorno = definirParamsT.Result.accept(self)
        return parametros + tipoRetorno

    # Result
    def visitDefinirTipo(self, definirTipo):
        return [definirTipo.Type]

    # Type
    # def visitTint()

    # def visitTstring()

    # def visitTbool()

    # def visitTbyte()

    # def visitTfloat()

    # Parameters
    def visitParams(self, params): # Unico parametro
        return params.ParameterList.accept(self)

    def visitParamsList(self, paramsList): # Lista de parametros
        return paramsList.ParameterList.accept(self)

    # ParameterList
    def visitCompParamsDecl(self, compParamsDecl):
        parametros = compParamsDecl.ParameterDecl.accept(self)
        parametrosMult = compParamsDecl.ParameterList_Mul.accept(self)
        return parametros + parametrosMult

    # ParameterList_Mul
    def visitCallBackParameterList_Mul(self, callBackParameterList_Mul):
        parametro = callBackParameterList_Mul.ParameterDecl.accept(self)
        parametroMul = callBackParameterList_Mul.ParameterList_Mul1.accept(self)
        return parametro + parametroMul

    def visitEndParameterList_Mul(self, endParameterList_Mul):
        return endParameterList_Mul.ParameterDecl.accept(self)

    # ParameterDecl
    def visitParamIdDecl(self, paramIdDecl): # ok
        listaIDs = paramIdDecl.IdentifierList.accept(self)
        tipo = paramIdDecl.Type
        for k in range(len(listaIDs)+len(listaIDs)):
            if(k%2 != 0):
                listaIDs.insert(k, tipo)

        return listaIDs

    # Block
    def visitDefinirStatementL(self, definirStatementL):
        definirStatementL.StatementList.accept(self)

    def visitMultFunc(self, multFunc):
        multFunc.StatementList.accept(self)
        multFunc.FunctionDecl.accept(self)

    # StatementList
    def visitDefinirStatement(self, definirStatement):
        print('visitDefinirStatement')
        definirStatement.Statement.accept(self)

    def visitCompoundStatmenteList(self, compoundStatmenteList):
        print('visitCompoundStatmenteList')
        compoundStatmenteList.statement.accept(self)
        compoundStatmenteList.statementList.accept(self)

    # Statement
    def visitStmtDeclaration(self, stmtDeclaration):
        print('visitStmtDeclaration')
        pass

    def visitStmtSimple(self, stmtSimple):
        print('visitStmtSimple')
        pass

    def visitStmtReturn(self, stmtReturn):
        print('visitStmtReturn')
        pass
    
    def visitStmtBreak(self, stmtBreak):
        print('visitStmtBreak')
        pass
    
    def visitStmtContinue(self, stmtContinue):
        print('visitStmtContinue')
        pass
    
    def visitStmtBlock(self, stmtBlock):
        print('visitStmtBlock')
        pass
    
    def visitStmtIf(self, stmtIf):
        print('visitStmtIf')
        pass
    
    def visitStmtSwitch(self, stmtSwitch):
        print('visitStmtSwitch')
        pass
    
    def visitCallStmtFor(self, stmtFor):
        print('visitCallStmtFor')
        pass

    # Declaration
    def visitDeclConst(self, declConst):
        print('visitDeclConst')
        pass
    
    def visitDeclType(self, declType):
        print('visitDeclType')
        pass
    
    def visitDeclVar(self, declVar):
        print('visitDeclVar')
        pass
    
    # SimpleStmt
    def visitStmtCondition(self, stmtCondition):
        print('visitStmtCondition')
        pass

    def visitStmtIncDec(self, stmtIncDec):
        print('visitStmtIncDec')
        pass
    
    def visitAssign(self, assign):
        print('visitAssign')
        pass
    
    def visitDeclShortVar(self, declShortVar):
        print('visitDeclShortVar')
        pass
    
    # ReturnStmt
    def visitExpReturn(self, expReturn):
        print('visitExpReturn')
        expReturn.ExpressionList.accept(self)
        pass

    def visitSimpleReturn(self, simpleReturn):
        print('visitSimpleReturn')
        pass
    
    # BreakStmt
    def visitStmtBreack(self, stmtBreack):
        pass

    # ContinueStmt
    def visitStmtContinuePrint(self, stmtContinue):
        pass
    
    # Ifstmt
    def visitSimpleIf(self, simpleIf):
        pass

    def visitCompIfElse(self, compIfElse):
        pass
    
    def visitIfElse(self, ifElse):
        pass
        
    # SwitchStmt
    def visitExprSwitch(self, exprSwitch):
        pass
    
    # SwitchStmt_Head
    def visitExprSwitchSimple(self, exprSwitchSimple):
        pass

    # ExprSwitchHead1
    def visitExprSwitchHead1(self, exprSwitchHead1):
        pass
    
    # ExprSwitchHead2 
    def visitExprSwitchHead2(self, exprSwitchHead2):
        pass

    # ExprSwitchBody1
    def visitExprSwitchBody1(self, exprSwitchBody1):
        pass

    # ExprSwitchBody2
    def visitExprSwitchBody2(self, exprSwitchBody2):
        pass

    def visitExprSwitchExp(self, exprSwitchExp):
        pass

    # ExprCaseClauseList
    def visitCompoundCaseClause1(self, compoundCaseClase1):
        pass

    # ExprCaseClause
    def visitExprCase(self, exprCase):
        pass

    # ExprSwitchCase
    def visitCaseClauseExp(self, caseClauseExp):
        pass

    def visitCaseClause(self, caseClause):
        pass

    # ForStmt
    def visitStmtFor(self, stmtFor):
        pass

    def visitStmtForClause(self, stmtForClause):
        pass

    def visitStmtForRange(self, stmtForRange):
        pass

    def visitStmtForBlock(self, stmtForBlock):
        pass

    # Condition
    def visitDefinirCondition(self, definirCondition):
        pass
    # ForClause
    def visitClassicFor(self, classicFor):
        pass

    def visitclassicFor2(self, classicFor2):
        pass

    # RangeClause
    def visitDefinirRange(self, definirRange):
        pass

    def visitRangeExpList(self, rangeExpList):
        pass

    def visitRangIDList(self, rangIDList):
        pass

    # ConstDecl
    def visitSimpleConst(self, simpleConst):
        pass

    def visitCompConst(self, compConst):
        pass

    # ConstSpecList
    def visitCallConstSpec(self, callConstSpec):
        pass

    def visitCompoundConstSpec(self, compoundConstSpec):
        pass

    def visitListIdExp(self, listIdExp):
        pass

    def visitListTypeExp(self, listTypeExp):
        pass
    
    # IdentifierList
    def visitDefinirIDList(self, definirIDList):
        listIDs = definirIDList.CompIDList.accept(self)
        return [definirIDList.ID] + listIDs
    
    def visitDefinirID(self, definirID): # ok
        return [definirID.ID]

    # CompIDList
    def visitCompoundIDList(self, compoundIDList):
        return [compoundIDList.ID] + compoundIDList.CompIDList.accept(self)

    def visitEndCompID(self, compoundIDList):
        return [compoundIDList.ID]

    # ExpressionList
    def visitDefinirExpList(self, definirExpList):
        pass

    def visitCallExpList(self, callExpList):
        pass

    # ListExpr
    def visitSimpleExpList(self, simpleExpList):
        pass

    def visitCompoundExpList(self, compoundExpList):
        pass

    # TypeDecl
    def visitDefinirType(self, definirType):
        pass

    def visitCallTypeSpecList(self, callTypeSpecList):
        pass

    # TypeSpecList
    def visitCompTypeSpecList(self, compTypeSpecList):
        pass

    def visitEndCompTypeSpec(self, endCompTypeSpec):
        pass

    # TypeSpec
    def visitSpecType(self, specType):
        pass

    # VarDecl
    def visitDefinirVar(self, definirVar):
        pass

    def visitCompVar(self, compVar):
        pass

    # VarSpecList
    def visitCompoundVarSpec(self, compoundVarSpec):
        pass

    def visitEndCompVarSpec(self, endCompVarSpec):
        pass

    # VarSpec
    def visitSpecVar(self, specVar):
        pass

    def visitClassicVarSpec(self, classicVarSpec):
        pass

    def visitSimpleVarSpec(self, simpleVarSpec):
        pass

    # CallFunc
    def visitSimpleCallFunc(self, simpleCallFunc):
        pass

    def visitCallParenFunc(self, callParenFunc):
        pass

    # IncDec
    def visitIncOp(self, incOp):
        pass

    def visitDecOp(self, decOp):
        pass

    # Assignment
    def visitAssignOp(self, assignOp):
        pass

    # ShortVarDec
    def visitDeclShortVarDef(self, declShortVar):
        pass
    
    # Expression
    def visitExpressionOR(self, expressionOR):
        pass

    def visitCallExp1(self, callExp1):
        pass

    # Exp1
    def visitExpressionAND(self, expressionAND):
        pass

    def visitCallExp2(self, callExp2):
        pass

    # Exp2
    def visitExpressionEquals(self, expressionEquals):
        pass

    def visitExpressionDiferente(self, expressionDiferente):
        pass

    def visitExpressionLess(self, expressionLess):
        pass

    def visitExpressionLessEqual(self, expressionLessEqual):
        pass

    def visitExpressionGreater(self, expressionGreater):
        pass

    def visitExpressionGreaterEqual(self, expressionGreaterEqual):
        pass

    def visitCallExp3(self, callExp3):
        pass

    # Exp3
    def visitExpressionPlus(self, expressionPlus):
        pass

    def visitExpressionMinus(self, expressionMinus):
        pass

    def visitExpressionPot(self, expressionPot):
        pass

    def visitCallExp4(self, callExp4):
        pass

    # Exp4
    def visitExpressionTimes(self, expressionTimes):
        pass

    def visitExpressionDivide(self, expressionDivide):
        pass

    def visitExpressionMod(self, expressionMod):
        pass

    def visitPrintNumberID(self, printNumberID):
        pass

    # Exp5
    def visitExpressionNumber(self, expressionNumber):
        pass

    def visitExpressionCallFunc(self, expressionCallFunc):
        pass

    def visitExpressionID(self, expressionID):
        pass

    def visitExpressionParens(self, expressionParens):
        pass