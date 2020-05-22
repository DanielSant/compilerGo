from GoAbstractVisitor import GoAbstractVisitor
import GoSymbolTable as st
from GoVisitor import Visitor
import GoAbstract as sa

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
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
        print(definirFuncBody.ID)
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
        tipoExp = expReturn.ExpressionList.accept(self)
        scope = st.symbolTable[-1][st.SCOPE]
        bindable = st.getBindable(scope)
        if (tipoExp != bindable[st.TYPE]):
            expReturn.accept(self.printer)
            print('\t[Erro] O retorno da funcao', scope, 'eh do tipo', bindable[st.TYPE],end='')
            print(' no entanto, o retorno passado foi do tipo', tipoExp, '\n')
        st.endScope()

    def visitSimpleReturn(self, simpleReturn):
        print('visitSimpleReturn')
        pass
    
    # BreakStmt
    def visitStmtBreack(self, stmtBreack):
        print('visitStmtBreack')
        pass

    # ContinueStmt
    def visitStmtContinuePrint(self, stmtContinue):
        print('visitStmtContinuePrint')
        pass
    
    # Ifstmt
    def visitSimpleIf(self, simpleIf):
        print('visitSimpleIf')
        pass

    def visitCompIfElse(self, compIfElse):
        print('visitCompIfElse')
        pass
    
    def visitIfElse(self, ifElse):
        print('visitIfElse')
        pass
        
    # SwitchStmt
    def visitExprSwitch(self, exprSwitch):
        print('visitExprSwitch')
        pass
    
    # SwitchStmt_Head
    def visitExprSwitchSimple(self, exprSwitchSimple):
        print('visitExprSwitchSimple')
        pass

    # ExprSwitchHead1
    def visitExprSwitchHead1(self, exprSwitchHead1):
        print('visitExprSwitchHead1')
        pass
    
    # ExprSwitchHead2 
    def visitExprSwitchHead2(self, exprSwitchHead2):
        print('visitExprSwitchHead2')
        pass

    # ExprSwitchBody1
    def visitExprSwitchBody1(self, exprSwitchBody1):
        print('visitExprSwitchBody1')
        pass

    # ExprSwitchBody2
    def visitExprSwitchBody2(self, exprSwitchBody2):
        print('visitExprSwitchBody2')
        pass

    def visitExprSwitchExp(self, exprSwitchExp):
        print('visitExprSwitchExp')
        pass

    # ExprCaseClauseList
    def visitCompoundCaseClause1(self, compoundCaseClase1):
        print('visitCompoundCaseClause1')
        pass

    # ExprCaseClause
    def visitExprCase(self, exprCase):
        print('visitExprCase')
        pass

    # ExprSwitchCase
    def visitCaseClauseExp(self, caseClauseExp):
        print('visitCaseClauseExp')
        pass

    def visitCaseClause(self, caseClause):
        print('visitCaseClause')
        pass

    # ForStmt
    def visitStmtFor(self, stmtFor):
        print('visitStmtFor')
        pass

    def visitStmtForClause(self, stmtForClause):
        print('visitStmtForClause')
        pass

    def visitStmtForRange(self, stmtForRange):
        print('visitStmtForRange')
        pass

    def visitStmtForBlock(self, stmtForBlock):
        print('visitStmtForBlock')
        pass

    # Condition
    def visitDefinirCondition(self, definirCondition):
        print('visitDefinirCondition')
        pass
    # ForClause
    def visitClassicFor(self, classicFor):
        print('visitClassicFor')
        pass

    def visitclassicFor2(self, classicFor2):
        print('visitclassicFor2')
        pass

    # RangeClause
    def visitDefinirRange(self, definirRange):
        print('visitDefinirRange')
        pass

    def visitRangeExpList(self, rangeExpList):
        print('visitRangeExpList')
        pass

    def visitRangIDList(self, rangIDList):
        print('visitRangIDList')
        pass

    # ConstDecl
    def visitSimpleConst(self, simpleConst):
        print('visitSimpleConst')
        pass

    def visitCompConst(self, compConst):
        print('visitCompConst')
        pass

    # ConstSpecList
    def visitCallConstSpec(self, callConstSpec):
        print('visitCallConstSpec')
        pass

    def visitCompoundConstSpec(self, compoundConstSpec):
        print('visitCompoundConstSpec')
        pass

    def visitListIdExp(self, listIdExp):
        print('visitListIdExp')
        pass

    def visitListTypeExp(self, listTypeExp):
        print('visitListTypeExp')
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
        print('visitDefinirExpList')
        pass

    def visitCallExpList(self, callExpList):
        print('visitCallExpList')
        pass

    # ListExpr
    def visitSimpleExpList(self, simpleExpList):
        print('visitSimpleExpList')
        pass

    def visitCompoundExpList(self, compoundExpList):
        print('visitCompoundExpList')
        pass

    # TypeDecl
    def visitDefinirType(self, definirType):
        print('visitDefinirType')
        pass

    def visitCallTypeSpecList(self, callTypeSpecList):
        print('visitCallTypeSpecList')
        pass

    # TypeSpecList
    def visitCompTypeSpecList(self, compTypeSpecList):
        print('visitCompTypeSpecList')
        pass

    def visitEndCompTypeSpec(self, endCompTypeSpec):
        print('visitEndCompTypeSpec')
        pass

    # TypeSpec
    def visitSpecType(self, specType):
        print('visitSpecType')
        pass

    # VarDecl
    def visitDefinirVar(self, definirVar):
        print('visitDefinirVar')
        pass

    def visitCompVar(self, compVar):
        print('visitCompVar')
        pass

    # VarSpecList
    def visitCompoundVarSpec(self, compoundVarSpec):
        print('visitCompoundVarSpec')
        pass

    def visitEndCompVarSpec(self, endCompVarSpec):
        print('visitEndCompVarSpec')
        pass

    # VarSpec
    def visitSpecVar(self, specVar):
        print('visitSpecVar')
        pass

    def visitClassicVarSpec(self, classicVarSpec):
        print('visitClassicVarSpec')
        pass

    def visitSimpleVarSpec(self, simpleVarSpec):
        print('visitSimpleVarSpec')
        pass

    # CallFunc
    def visitSimpleCallFunc(self, simpleCallFunc):
        print('visitSimpleCallFunc')
        pass

    def visitCallParenFunc(self, callParenFunc):
        print('visitCallParenFunc')
        pass

    # IncDec
    def visitIncOp(self, incOp):
        print('visitIncOp')
        pass

    def visitDecOp(self, decOp):
        print('visitDecOp')
        pass

    # Assignment
    def visitAssignOp(self, assignOp):
        print('visitAssignOp')
        pass

    # ShortVarDec
    def visitDeclShortVarDef(self, declShortVar):
        print('visitDeclShortVarDef')
        pass
    
    # Expression
    def visitExpressionOR(self, expressionOR):
        print('visitExpressionOR')
        pass

    def visitCallExp1(self, callExp1):
        print('visitCallExp1')
        pass

    # Exp1
    def visitExpressionAND(self, expressionAND):
        print('visitExpressionAND')
        pass

    def visitCallExp2(self, callExp2):
        print('visitCallExp2')
        pass

    # Exp2
    def visitExpressionEquals(self, expressionEquals):
        print('visitExpressionEquals')
        pass

    def visitExpressionDiferente(self, expressionDiferente):
        print('visitExpressionDiferente')
        pass

    def visitExpressionLess(self, expressionLess):
        print('visitExpressionLess')
        pass

    def visitExpressionLessEqual(self, expressionLessEqual):
        print('visitExpressionLessEqual')
        pass

    def visitExpressionGreater(self, expressionGreater):
        print('visitExpressionGreater')
        pass

    def visitExpressionGreaterEqual(self, expressionGreaterEqual):
        print('visitExpressionGreaterEqual')
        pass

    def visitCallExp3(self, callExp3):
        print('visitCallExp3')
        pass

    # Exp3
    def visitExpressionPlus(self, expressionPlus):
        print('visitExpressionPlus')
        tipoExp1 = expressionPlus.Expr4.accept(self)
        tipoExp2 = expressionPlus.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionPlus.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            expressionPlus.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionPlus.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c

    def visitExpressionMinus(self, expressionMinus):
        print('visitExpressionMinus')
        tipoExp1 = expressionMinus.Expr4.accept(self)
        tipoExp2 = expressionMinus.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionMinus.accept(self.printer)
            print('\n\t[Erro] Subtracao invalida. A expressao ', end='')
            expressionMinus.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionMinus.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c

    def visitExpressionPot(self, expressionPot):
        print('visitExpressionPot')
        pass

    def visitCallExp4(self, callExp4):
        print('visitCallExp4')
        pass

    # Exp4
    def visitExpressionTimes(self, expressionTimes):
        print('visitExpressionTimes')
        tipoExp1 = expressionTimes.Expr4.accept(self)
        tipoExp2 = expressionTimes.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionTimes.accept(self.printer)
            print('\n\t[Erro] Multiplicacao invalida. A expressao ', end='')
            expressionTimes.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionTimes.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c
        pass

    def visitExpressionDivide(self, expressionDivide):
        print('visitExpressionDivide')
        pass

    def visitExpressionMod(self, expressionMod):
        print('visitExpressionMod')
        pass

    def visitPrintNumberID(self, printNumberID):
        print('visitPrintNumberID')
        if (printNumberID.numberOrId.isnumeric()):
            print('Numero')
            #print(isinstance(f, int))
        else:
            idName = st.getBindable(printNumberID.numberOrId)
            if (idName != None):
                return idName[st.TYPE]
            return None
        
    # Exp5
    def visitExpressionNumber(self, expressionNumber):
        print('visitExpressionNumber')
        pass

    def visitExpressionCallFunc(self, expressionCallFunc):
        print('visitExpressionCallFunc')
        pass

    def visitExpressionID(self, expressionID):
        print('visitExpressionID')
        pass

    def visitExpressionParens(self, expressionParens):
        print('visitExpressionParens')
        pass