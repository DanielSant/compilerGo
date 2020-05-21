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
    def visitDefinirFunc(self, definirFunc):
        parametrosRetorno = definirFunc.Signature.accept(self)
        print(definirFunc.ID)
        st.addFunction(definirFunc.ID, parametrosRetorno[0:-1], parametrosRetorno[-1])
        # Tera codigo aqui

    def visitDefinirFuncBody(self, definirFuncBody):
        print(definirFuncBody.ID)
        parametrosRetorno = definirFuncBody.Signature.accept(self)
        # st.addFunction(definirFuncBody.ID, parametrosRetorno[0:-1], parametrosRetorno[-1])
        definirFuncBody.FunctionBody.accept(self)
        # Tera codigo aqui

    # Signature
    def visitDefinirParamsT(self, definirParamsT):
        print('visitDefinirParamsT')
        parametros = {}
        if (definirParamsT.Params != None):
            parametros = definirParamsT.Params.accept(self)
        
        tipoRetorno = definirParamsT.Result.accept(self)
        print(parametros, tipoRetorno)
        return [parametros] + tipoRetorno

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
        print("visitParams")
        return params.ParameterList.accept(self)

    def visitParamsList(self, paramsList): # Lista de parametros
        print("visitParamsList")
        return paramsList.ParameterList.accept(self)

    # ParameterList
    def visitCompParamsDecl(self, compParamsDecl):
        parametros = compParamsDecl.ParameterDecl.accept(self)
        parametrosMult = compParamsDecl.ParameterList_Mul.accept(self)
        print("visitCompParamsDecl", parametros, parametrosMult)
        return parametros + parametrosMult

    # ParameterList_Mul
    def visitCallBackParameterList_Mul(self, callBackParameterList_Mul):
        parametro = callBackParameterList_Mul.ParameterDecl.accept(self)
        parametroMul = callBackParameterList_Mul.ParameterList_Mul1.accept(self)
        print('visitCallBackParameterList_Mul', parametro, parametroMul)
        return parametro + parametroMul

    def visitEndParameterList_Mul(self, endParameterList_Mul):
        print('visitEndParameterList_Mul')
        return endParameterList_Mul.ParameterDecl.accept(self)

    # ParameterDecl
    def visitParamIdDecl(self, paramIdDecl): # ok
        listaIDs = paramIdDecl.IdentifierList.accept(self)
        tipo = paramIdDecl.Type
        print('tipo', tipo)
        print('visitParamIdDecl', listaIDs, tipo)
        return listaIDs + [tipo]

    def visitParamDecl(self, paramDecl):
        print("visitParamDecl")
        st.addVar(paramDecl.ID)

    # Block
    def visitDefinirStatementL(self, definirStatementL):
        pass

    def visitMultFunc(self, multFunc):
        pass

    # StatementList
    def visitDefinirStatement(self, definirStatement):
        pass

    def visitCompoundStatmenteList(self, compoundStatmenteList):
        pass

    # Statement
    def visitStmtDeclaration(self, stmtDeclaration):
        pass

    def visitStmtSimple(self, stmtSimple):
        pass

    def visitStmtReturn(self, stmtReturn):
        pass
    
    def visitStmtBreak(self, stmtBreak):
        pass
    
    def visitStmtContinue(self, stmtContinue):
        pass
    
    def visitStmtBlock(self, stmtBlock):
        pass
    
    def visitStmtIf(self, stmtIf):
        pass
    
    def visitStmtSwitch(self, stmtSwitch):
        pass
    
    def visitCallStmtFor(self, stmtFor):
        pass

    # Declaration
    def visitDeclConst(self, declConst):
        pass
    
    def visitDeclType(self, declType):
        pass
    
    def visitDeclVar(self, declVar):
        pass
    
    # SimpleStmt
    def visitStmtCondition(self, stmtCondition):
        pass

    def visitStmtIncDec(self, stmtIncDec):
        pass
    
    def visitAssign(self, assign):
        pass
    
    def visitDeclShortVar(self, declShortVar):
        pass
    
    # ReturnStmt
    def visitExpReturn(self, expReturn):
        pass

    def visitSimpleReturn(self, simpleReturn):
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
        print('visitDefinirIDList', definirIDList.ID, listIDs)
        return [definirIDList.ID] + listIDs
    
    def visitDefinirID(self, definirID): # ok
        print('visitDefinirID')
        return [definirID.ID]

    # CompIDList
    def visitCompoundIDList(self, compoundIDList):
        print('visitCompoundIDList', compoundIDList.ID)
        return [compoundIDList.ID] + compoundIDList.CompIDList.accept(self)

    def visitEndCompID(self, compoundIDList):
        print('visitEndCompID', compoundIDList.ID)
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