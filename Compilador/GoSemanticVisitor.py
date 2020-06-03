from GoAbstractVisitor import GoAbstractVisitor
import GoSymbolTable as st
from GoVisitor import Visitor
import GoAbstract as sa
import GoLex as lex

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    elif (type1 == st.BOOL and type2 == st.BOOL):
        return st.BOOL
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
        if(parametrosRetorno[0] != None):
            for k in range(0, len(parametrosRetorno[0:-1]), 2):
                st.addVar(parametrosRetorno[0:-1][k], parametrosRetorno[0:-1][k+1])

        definirFuncBody.FunctionBody.accept(self)
        st.varCheck(st.endScope())
        # print('Last symbol table:', st.symbolTable)

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

    def visitDefinirParamsParameters(self, definirParams):
        return [None]

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
    # def visitStmtDeclaration(self, stmtDeclaration):
    #     print('visitStmtDeclaration')
    #     pass

    # def visitStmtSimple(self, stmtSimple):
    #     print('visitStmtSimple')
    #     pass

    # def visitStmtReturn(self, stmtReturn):
    #     print('visitStmtReturn')
    #     pass
    
    # def visitStmtBreak(self, stmtBreak):
    #     print('visitStmtBreak')
    #     pass
    
    # def visitStmtContinue(self, stmtContinue):
    #     print('visitStmtContinue')
    #     pass
    
    # def visitStmtIf(self, stmtIf):
    #     print('visitStmtIf')
    #     pass
    
    # def visitStmtSwitch(self, stmtSwitch):
    #     print('visitStmtSwitch')
    #     pass
    
    # def visitCallStmtFor(self, stmtFor):
    #     print('visitCallStmtFor')
    #     pass

    # Declaration
    # def visitDeclConst(self, declConst):
    #     print('visitDeclConst')
    #     pass
    
    # def visitDeclType(self, declType):
    #     print('visitDeclType')
    #     pass
    
    # def visitDeclVar(self, declVar):
    #     print('visitDeclVar')
    #     pass
    
    # SimpleStmt
    # def visitStmtCondition(self, stmtCondition):
    #     print('visitStmtCondition')
    #     pass

    # def visitStmtIncDec(self, stmtIncDec):
    #     print('visitStmtIncDec')
    #     pass
    
    # def visitAssign(self, assign):
    #     print('visitAssign')
    #     pass
    
    # ReturnStmt
    def visitExpReturn(self, expReturn):
        print('visitExpReturn')
        tipoExp = expReturn.ExpressionList.accept(self)

        # Volta ao escopo que tem o tipo de retorno.
        for indice in reversed(range(len(st.symbolTable))):
            scope = st.symbolTable[indice][st.SCOPE]    
            bindable = st.getBindable(scope)
            if (bindable != None):
                break

        if (tipoExp != bindable[st.TYPE]):
            expReturn.accept(self.printer)
            print('\n\t[Erro]: O retorno da funcao', scope, 'eh do tipo', bindable[st.TYPE],end='')
            print(' no entanto, o retorno passado foi do tipo', tipoExp, '\n')

    def visitSimpleReturn(self, simpleReturn):
        print('visitSimpleReturn')
        st.endScope()
    
    # BreakStmt
    def visitStmtBreack(self, stmtBreack):
        print('visitStmtBreack')
        # endScope?
        pass

    # ContinueStmt
    def visitStmtContinuePrint(self, stmtContinue):
        print('visitStmtContinuePrint')
        # endScope?
        pass
    
    # Ifstmt
    def visitSimpleIf(self, simpleIf):
        print('visitSimpleIf')
        st.beginScope(st.IF)
        simpleIf.Expression.accept(self)
        simpleIf.Block.accept(self)
        st.varCheck(st.endScope())
        
    def visitCompIfElse(self, compIfElse):
        print('visitCompIfElse')
        st.beginScope(st.IF)
        compIfElse.Expression.accept(self)
        compIfElse.Block.accept(self)
        st.varCheck(st.endScope())
        compIfElse.IfStmt.accept(self)

    def visitIfElse(self, ifElse):
        print('visitIfElse')
        st.beginScope(st.IF)
        ifElse.Expression.accept(self)
        ifElse.Block.accept(self)
        st.varCheck(st.endScope())
        st.beginScope(st.ELSE)
        ifElse.Block1.accept(self)
        st.varCheck(st.endScope())
        
    # SwitchStmt
    def visitExprSwitch(self, exprSwitch):
        print('visitExprSwitch')
        st.beginScope(st.SWITCH)
        tipo = exprSwitch.switchStmt_Head.accept(self)
        st.symbolTable[-1][st.SWITCHTYPE] = tipo
        exprSwitch.switchStmt_Body.accept(self)
        st.varCheck(st.endScope())
    
    # SwitchStmt_Head
    def visitExprSwitchSimple(self, exprSwitchSimple):
        print('visitExprSwitchSimple')
        st.beginScope(st.SWITCH)
        st.symbolTable[-1][st.SWITCHTYPE] = ''
        exprSwitchSimple.switchStmt_Body.accept(self)
        st.varCheck(st.endScope())

    # ExprSwitchHead1
    def visitExprSwitchHead1(self, exprSwitchHead1):
        print('visitExprSwitchHead1')
        exprSwitchHead1.simpleStmt.accept(self)
        return exprSwitchHead1.expression.accept(self)
    
    # ExprSwitchHead2 
    def visitExprSwitchHead2(self, exprSwitchHead2):
        print('visitExprSwitchHead2')
        return exprSwitchHead2.simpleStmt.accept(self)

    # ExprSwitchBody1
    def visitExprSwitchBody1(self, exprSwitchBody1):
        print('visitExprSwitchBody1')
        exprSwitchBody1.exprCaseClauseList.accept(self)

    # ExprSwitchBody2
    def visitExprSwitchBody2(self, exprSwitchBody2):
        print('visitExprSwitchBody2')
        # this body is empty
        pass

    # def visitExprSwitchExp(self, exprSwitchExp):
    #     print('visitExprSwitchExp')
    #     pass

    # ExprCaseClauseList
    def visitCompoundCaseClause1(self, compoundCaseClase1):
        print('visitCompoundCaseClause1')
        compoundCaseClase1.ExprCaseClause.accept(self)
        compoundCaseClase1.ExprCaseClauseList.accept(self)

    # ExprCaseClause
    def visitExprCase(self, exprCase):
        print('visitExprCase')
        exprCase.ExprSwitchCase.accept(self)
        exprCase.StatementList.accept(self)

    # ExprSwitchCase
    def visitCaseClauseExp(self, caseClauseExp):
        print('visitCaseClauseExp')
        caseType = caseClauseExp.ExpressionList.accept(self)
        switchType = st.symbolTable[-1][st.SWITCHTYPE]
        if (switchType != '' and switchType != caseType):
            caseClauseExp.accept(self.printer)
            print('\n\t[ERRO] case eh do tipo', caseType, 'quando deveria ser do tipo', switchType)

    def visitCaseClause(self, caseClause):
        print('visitCaseClause')
        # print do case
        pass

    # ForStmt
    def visitStmtFor(self, stmtFor):
        print('visitStmtFor')
        st.beginScope(st.FOR)
        stmtFor.Condition.accept(self)
        stmtFor.Block.accept(self)
        st.varCheck(st.endScope())

    def visitStmtForClause(self, stmtForClause):
        print('visitStmtForClause')
        st.beginScope(st.FOR)
        stmtForClause.ForClause.accept(self)
        stmtForClause.Block.accept(self)
        st.varCheck(st.endScope())
        
    def visitStmtForRange(self, stmtForRange):
        print('visitStmtForRange')
        st.beginScope(st.FOR)
        stmtForRange.RangeClause.accept(self)
        stmtForRange.Block.accept(self)
        st.varCheck(st.endScope())

    def visitStmtForBlock(self, stmtForBlock):
        print('visitStmtForBlock')
        st.beginScope(st.FOR)
        stmtForBlock.Block.accept(self)
        st.varCheck(st.endScope())

    # Condition
    def visitDefinirCondition(self, definirCondition):
        print('visitDefinirCondition')
        tipo = definirCondition.Expression.accept(self)
        if(tipo in st.TiposPrimitivos):
            return tipo
        else:
            definirCondition.accept(self.printer)
            print('\n\t[Erro]: Condicao invalida')

    # ForClause
    def visitClassicFor(self, classicFor):
        print('visitClassicFor')
        classicFor.initPostStmt.accept(self)
        classicFor.Condition.accept(self)
        classicFor.initPostStmt1.accept(self)

    def visitclassicFor2(self, classicFor2):
        print('visitclassicFor2')
        classicFor2.Condition.accept(self)

    # RangeClause
    def visitDefinirRange(self, definirRange):
        print('visitDefinirRange')
        if (definirRange.Expression.accept(self) != st.STRING):
            definirRange.accept(self.printer)
            print('\n\t[ERRO] Declaracao do range precisa ser do tipo string')

    def visitRangeExpList(self, rangeExpList):
        print('visitRangeExpList')
        left = rangeExpList.ExpressionList.accept(self)
        right = rangeExpList.Expression.accept(self)

        if (type(left) is list):
            if (left[0] in st.TiposPrimitivos and left[0] != st.INT):
                rangeExpList.accept(self.printer)
                print('\n\t [ERRO] O tipo da primeira variavel precisa ser inteiro.')
            elif(left[0] != st.INT):
                st.addVar(left[0], st.INT)

            if (left[1] in st.TiposPrimitivos and left[1] != st.STRING):
                rangeExpList.accept(self.printer)
                print('\n\t [ERRO] O tipo da segunda variavel precisa ser string.')
            elif(left[1] != st.STRING):
                st.addVar(left[1], st.STRING)

        elif(left in lex.reserved and left != st.STRING):
            rangeExpList.accept(self.printer)
            print('\n\t[ERRO] Variavel precisa ser do tipo string.')
        elif(left != st.STRING):
            st.addVar(left, st.STRING)
            
        if (right != st.STRING):
            rangeExpList.accept(self.printer)
            print('\n\t[ERRO] Declaracao range precisa ser do tipo string')

    # ConstDecl
    def visitSimpleConst(self, simpleConst):
        print('visitSimpleConst')
        simpleConst.ConstSpec.accept(self)

    def visitCompConst(self, compConst):
        print('visitCompConst')
        compConst.constSpecList.accept(self)

    # ConstSpecList
    def visitCallConstSpec(self, callConstSpec):
        print('visitCallConstSpec')
        callConstSpec.ConstSpec.accept(self)

    def visitCompoundConstSpec(self, compoundConstSpec):
        print('visitCompoundConstSpec')
        compoundConstSpec.ConstSpec.accept(self)
        compoundConstSpec.ConstSpecList.accept(self)

    def visitListIdExp(self, listIdExp):
        print('visitListIdExp')
        idList = listIdExp.IdentifierList.accept(self)
        expList = listIdExp.ExpressionList.accept(self)

        if(type(expList) is not list):
            expList = [expList]

        if(len(idList) != len(expList)):
            listIdExp.accept(self.printer)
            print('[Erro]: ', len(idList), 'constantes mas', len(expList), 'valores')
        else:
            for i in range(len(idList)):
                st.addVar(idList[i], expList[i])
                st.symbolTable[-1][idList[i]][st.CONST] = 'const'

    def visitListTypeExp(self, listTypeExp):
        print('visitListTypeExp')
        listTypeExp.IdentifierList.accept(self)
        tipo = listTypeExp.Type
        listTypeExp.ExpressionList.accept(self)
    
    # IdentifierList
    def visitDefinirIDList(self, definirIDList):
        print('visitDefinirIDList')
        listIDs = definirIDList.CompIDList.accept(self)
        return [definirIDList.ID] + listIDs
    
    def visitDefinirID(self, definirID): # ok
        print('visitDefinirID')
        return [definirID.ID]

    # CompIDList
    def visitCompoundIDList(self, compoundIDList):
        return [compoundIDList.ID] + compoundIDList.CompIDList.accept(self)

    def visitEndCompID(self, compoundIDList):
        return [compoundIDList.ID]

    # ExpressionList
    # def visitDefinirExpList(self, definirExpList):
    #     print('visitDefinirExpList')
    #     pass

    def visitCallExpList(self, callExpList):
        print('visitCallExpList')
        return [callExpList.Expression.accept(self)] + callExpList.ListExpr.accept(self)

    # ListExpr
    def visitSimpleExpList(self, simpleExpList):
        print('visitSimpleExpList')
        return [simpleExpList.Expression.accept(self)]

    def visitCompoundExpList(self, compoundExpList):
        print('visitCompoundExpList')
        return [compoundExpList.Expression.accept(self)] + compoundExpList.ListExpr.accept(self)

    # TypeDecl
    def visitDefinirType(self, definirType):
        print('visitDefinirType')
        definirType.TypeSpec.accept(self)

    def visitCallTypeSpecList(self, callTypeSpecList):
        print('visitCallTypeSpecList')
        callTypeSpecList.TypeSpecList.accept(self)

    # TypeSpecList
    def visitCompTypeSpecList(self, compTypeSpecList):
        print('visitCompTypeSpecList')
        compTypeSpecList.TypeSpec.accept(self)
        compTypeSpecList.TypeSpecList.accept(self)

    def visitEndCompTypeSpec(self, endCompTypeSpec):
        print('visitEndCompTypeSpec')
        endCompTypeSpec.TypeSpec.accept(self)

    # TypeSpec
    def visitSpecType(self, specType):
        print('visitSpecType')
        identifier = specType.ID
        tipo = specType.Type

    # VarDecl
    def visitDefinirVar(self, definirVar):
        print('visitDefinirVar')
        definirVar.VarSpec.accept(self)

    def visitCompVar(self, compVar):
        print('visitCompVar')
        compVar.VarSpecList.accept(self)

    # VarSpecList
    def visitCompoundVarSpec(self, compoundVarSpec):
        print('visitCompoundVarSpec')
        compoundVarSpec.VarSpec.accept(self)
        compoundVarSpec.VarSpecList.accept(self)

    def visitEndCompVarSpec(self, endCompVarSpec):
        print('visitEndCompVarSpec')
        endCompVarSpec.VarSpec.accept(self)

    # VarSpec
    def visitSpecVar(self, specVar):
        print('visitSpecVar')
        variaveis = specVar.IdentifierList.accept(self)
        tipo = specVar.Type
        for k in range(len(variaveis)):
            st.addVar(variaveis[k], tipo)

    def visitClassicVarSpec(self, classicVarSpec):
        print('visitClassicVarSpec')
        variaveis = classicVarSpec.IdentifierList.accept(self)
        tipo = classicVarSpec.Type

        for k in range(len(variaveis)):
            st.addVar(variaveis[k], tipo)

        expressao = classicVarSpec.ExpressionList.accept(self)

        if(type(expressao) != type([])):
            if(expressao != tipo):
                classicVarSpec.accept(self.printer)
                print('\n\t[Erro]: Atribuicao nao compativel')
        else: 
            for i in range (len(expressao)):
                if(expressao[i] != tipo):
                    classicVarSpec.accept(self.printer)
                    print('\n\t[Erro]: Atribuicao nao compativel')
                    break

    def visitSimpleVarSpec(self, simpleVarSpec):
        print('visitSimpleVarSpec')
        variavel = simpleVarSpec.IdentifierList.accept(self)
        tipo = simpleVarSpec.ExpressionList.accept(self)
        for x in range(len(variavel)):
            st.addVar(variavel[x], tipo)

    # CallFunc
    def visitSimpleCallFunc(self, simpleCallFunc):
        print('visitSimpleCallFunc')
        idFunc = simpleCallFunc.ID
        bindable = st.getBindable(idFunc)
        params = []
        for i in range(1, len(bindable[st.PARAMS]), 2):
            params.append(bindable[st.PARAMS][i])
        
        paramsCall = simpleCallFunc.ExpressionList.accept(self)
        
        if(type(paramsCall) is not list):
            paramsCall = [paramsCall]

        if(params != paramsCall):
            simpleCallFunc.accept(self.printer)
            print('\n\t[Erro]: Parametros incompativeis')

        return bindable[st.TYPE]

    def visitCallParenFunc(self, callParenFunc):
        print('visitCallParenFunc')
        idFunc = callParenFunc.ID
        bindable = st.getBindable(idFunc)
        return bindable[st.TYPE]

    # IncDec
    def visitIncOp(self, incOp):
        print('visitIncOp')
        tipo = incOp.Expression.accept(self) 
        if(tipo != st.INT):
            incOp.accept(self.printer)
            print('\n\t[Erro]: Variavel a ser incrementada deve ser do tipo inteiro')

    def visitDecOp(self, decOp):
        print('visitDecOp')
        tipo = decOp.Expression.accept(self)
        if(tipo != st.INT):
            decOp.accept(self.printer)
            print('\n\t[Erro]: Variavel a ser decrementada deve ser do tipo inteiro')

    # Assignment
    def visitAssignOp(self, assignOp):
        print('visitAssignOp')
        listaExp = assignOp.ExpressionList.accept(self) # lado esquerdo
        
        listaExp1 = assignOp.ExpressionList1.accept(self) # lado direito   
        
        if(listaExp not in st.TiposPrimitivos):
            bindable = st.getBindable(listaExp)
            if(st.CONST in bindable):
                assignOp.accept(self.printer)
                print('\n\t[Erro]: Atribuicao invalida de constante')
        if(listaExp1 not in st.TiposPrimitivos):
            bindable = st.getBindable(listaExp1)
            if(st.TYPE in bindable):
                listaExp1 = bindable[st.TYPE]
            if(listaExp != listaExp1):
                assignOp.accept(self.printer)
                print('\n\t[Erro]: Tipo de atribuicao invalida')

        

    # ShortVarDecl
    def visitDefinirShortVar(self, shortVar):
        print('visitShortVarDecl')
        variaveis = shortVar.IdentifierList.accept(self)
        tipos = shortVar.ExpressionList.accept(self)
        if(type(variaveis) is list and type(tipos) is list):
            if(len(variaveis) == len(tipos)):
                for k in range(len(variaveis)):
                    if(variaveis[k] in lex.reserved):
                        shortVar.accept(self.printer)
                        print('\n\t[Erro]: Declaracao invalida')
                    else:
                        for k in range(len(variaveis)):
                            if(tipos[k] in st.TiposPrimitivos):
                                st.addVar(variaveis[k], tipos[k])
                            else:
                                shortVar.accept(self.printer)
                                print('\n\t[Erro]: Declaracao invalida')
            else:
                shortVar.accept(self.printer)
                print('\n\t[Erro]: Declaracao invalida')
        elif(type(variaveis) is list):
            shortVar.accept(self.printer)
            print('\n\t[Erro]: Declaracao invalida')
        elif(variaveis in lex.reserved):
            shortVar.accept(self.printer)
            print('\n\t[Erro]: Declaracao invalida')
        elif(tipos in st.TiposPrimitivos):
            st.addVar(variaveis, tipos)
        else:
            shortVar.accept(self.printer)
            print('\n\t[Erro]: Declaracao invalida')
        
    # Expression
    def visitExpressionOR(self, expressionOR):
        print('visitExpressionOR')
        tipoExp1 = expressionOR.Exp.accept(self)
        tipoExp2 = expressionOR.Exp1.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c != st.BOOL):
            expressionOR.accept(self.printer)
            print('\n\t[Erro]: Comparacao invalida. A expressao ', end='')
            expressionOR.Exp.accept(self.printer)
            print('eh do tipo', tipoExp1, 'e a expressao ', end='')
            expressionOR.Exp1.accept(self.printer)
            print('eh do tipo', tipoExp2, 'onde ambas deveriam ser do tipo', st.BOOL, '\n')
        return c
    
    # def visitCallExp1(self, callExp1):
    #     print('visitCallExp1')
    #     pass

    # Exp1
    def visitExpressionAND(self, expressionAND):
        print('visitExpressionAND')
        tipoExp1 = expressionAND.Expr1.accept(self)
        tipoExp2 = expressionAND.Expr2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c != st.BOOL):
            expressionAND.accept(self.printer)
            print('\n\t[Erro]: Comparacao invalida. A expressao ', end='')
            expressionAND.Expr1.accept(self.printer)
            print('eh do tipo', tipoExp1, 'e a expressao ', end='')
            expressionAND.Expr2.accept(self.printer)
            print('eh do tipo', tipoExp2, 'onde ambas deveriam ser do tipo', st.BOOL, '\n')
        return c

    # def visitCallExp2(self, callExp2):
    #     print('visitCallExp2')
    #     pass

    # Exp2
    def visitExpressionEquals(self, expressionEquals):
        print('visitExpressionEquals')
        tipoExp2 = expressionEquals.Expr2.accept(self)
        tipoExp3 = expressionEquals.Expr3.accept(self)
        c = coercion(tipoExp2, tipoExp3)
        if (c == None):
            expressionEquals.accept(self.printer)
            print('\n\t[Erro]: Comparação invalida. A expressao ', end='')
            expressionEquals.Expr2.accept(self.printer)
            print(' eh do tipo', tipoExp2, 'enquanto a expressao ', end='')
            expressionEquals.Expr3.accept(self.printer)
            print(' eh do tipo', tipoExp3, 'quando deveriam ser do mesmo tipo\n')
        return c

    def visitExpressionDiferente(self, expressionDiferente):
        print('visitExpressionDiferente')
        tipoExp1 = expressionDiferente.Expr2.accept(self) 
        tipoExp2 = expressionDiferente.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionDiferente.accept(self.printer)
            print('\n\t[Erro]: Comparação invalida. A expressao ', end='')
            expressionDiferente.Expr2.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionDiferente.Expr3.accept(self.printer)
            print(' eh do tipo', tipoExp2, 'quando deveriam ser do mesmo tipo\n')
        return c

    def visitExpressionLess(self, expressionLess):
        print('visitExpressionLess')
        tipoExp1 = expressionLess.Expr2.accept(self)
        tipoExp2 = expressionLess.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionLess.accept(self.printer)
            print('\n\t[Erro]: Comparação invalida. A expressao ', end='')
            expressionLess.Expr2.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionLess.Expr3.accept(self.printer)
            print(' eh do tipo', tipoExp2, 'quando deveriam ser do mesmo tipo\n')
        return c

    def visitExpressionLessEqual(self, expressionLessEqual):
        print('visitExpressionLessEqual')
        tipoExp1 = expressionLessEqual.Expr2.accept(self)
        tipoExp2 = expressionLessEqual.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionLessEqual.accept(self.printer)
            print('\n\t[Erro]: Comparação invalida. A expressao ', end='')
            expressionLessEqual.Expr2.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionLessEqual.Expr3.accept(self.printer)
            print(' eh do tipo', tipoExp2, 'quando deveriam ser do mesmo tipo\n')
        return c

    def visitExpressionGreater(self, expressionGreater):
        print('visitExpressionGreater')
        tipoExp1 = expressionGreater.Expr2.accept(self)
        tipoExp2 = expressionGreater.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionGreater.accept(self.printer)
            print('\n\t[Erro]: Comparação invalida. A expressao ', end='')
            expressionGreater.Expr2.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionGreater.Expr3.accept(self.printer)
            print(' eh do tipo', tipoExp2, 'quando deveriam ser do mesmo tipo\n')
        return c

    def visitExpressionGreaterEqual(self, expressionGreaterEqual):
        print('visitExpressionGreaterEqual')
        tipoExp1 = expressionGreaterEqual.Expr2.accept(self)
        tipoExp2 = expressionGreaterEqual.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionGreaterEqual.accept(self.printer)
            print('\n\t[Erro]: Comparação invalida. A expressao ', end='')
            expressionGreaterEqual.Expr2.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionGreaterEqual.Expr3.accept(self.printer)
            print(' eh do tipo', tipoExp2, 'quando deveriam ser do mesmo tipo\n')
        return c

    # def visitCallExp3(self, callExp3):
    #     print('visitCallExp3')
    #     pass

    # Exp3
    def visitExpressionPlus(self, expressionPlus):
        print('visitExpressionPlus')
        tipoExp1 = expressionPlus.Expr4.accept(self)
        tipoExp2 = expressionPlus.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionPlus.accept(self.printer)
            print('\n\t[Erro]: Soma invalida. A expressao ', end='')
            expressionPlus.Expr4.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionPlus.Expr3.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c

    def visitExpressionMinus(self, expressionMinus):
        print('visitExpressionMinus')
        tipoExp1 = expressionMinus.Expr4.accept(self)
        tipoExp2 = expressionMinus.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionMinus.accept(self.printer)
            print('\n\t[Erro]: Subtracao invalida. A expressao ', end='')
            expressionMinus.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionMinus.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c

    # def visitCallExp4(self, callExp4):
    #     print('visitCallExp4')
    #     pass

    # Exp4
    def visitExpressionTimes(self, expressionTimes):
        print('visitExpressionTimes')
        tipoExp1 = expressionTimes.Expr4.accept(self)
        tipoExp2 = expressionTimes.Expr3.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionTimes.accept(self.printer)
            print('\n\t[Erro]: Multiplicacao invalida. A expressao ', end='')
            expressionTimes.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionTimes.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c

    def visitExpressionDivide(self, expressionDivide):
        print('visitExpressionDivide')
        tipoExp1 = expressionDivide.Expr5.accept(self)
        tipoExp2 = expressionDivide.Expr4.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            expressionDivide.accept(self.printer)
            print('\n\t[Erro]: Divisao invalida. A expressao ', end='')
            expressionDivide.Expr5.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionDivide.Expr4.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c

    def visitExpressionMod(self, expressionMod):
        print('visitExpressionMod')
        tipoExp1 = expressionMod.Expr5.accept(self)
        tipoExp2 = expressionMod.Expr4.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c != st.INT):
            expressionMod.accept(self.printer)
            print('\n\t[Erro]: Operacao de Mod invalida. A expressao ', end='')
            expressionMod.Expr5.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            expressionMod.Expr4.accept(self.printer)
            print(' eh do tipo', tipoExp2, 'quando deveriam ser do tipo int\n')
        return c

    def visitPrintNumberID(self, printNumberID):
        print('visitPrintNumberID')
        if (isinstance(printNumberID.numberOrId, int)):
            return st.INT
        elif (printNumberID.numberOrId == 'true' or printNumberID.numberOrId == 'false'):
            return st.BOOL
        elif (printNumberID.numberOrId[0] == '\"'):
            return st.STRING
        else:
            idName = st.getBindable(printNumberID.numberOrId)
            if (idName != None):
                if(st.CONST in idName):
                    return printNumberID.numberOrId
                return idName[st.TYPE]
            return printNumberID.numberOrId
        
    # Exp5
    # def visitExpressionNumber(self, expressionNumber):
    #     print('visitExpressionNumber')
    #     pass

    def visitExpressionCallFunc(self, expressionCallFunc):
        print('visitExpressionCallFunc')
        return expressionCallFunc.callFunc.accept(self)
        
    # def visitExpressionID(self, expressionID):
    #     print('visitExpressionID')
    #     pass

    def visitExpressionParens(self, expressionParens):
        print('visitExpressionParens')
        expressionParens.expression.accept(self)