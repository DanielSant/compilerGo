class Visitor():
    #FunctionDecl
    def visitDefinirFunc(self, definirFunc):
        print('func', end =' ')
        print(definirFunc.ID, end = ' ')
        definirFunc.Signature.accept(self)

    def visitDefinirFuncBody(self, definirFuncBody):
        print('func', end =' ')
        print(definirFuncBody.ID, end = ' ')
        definirFuncBody.Signature.accept(self)
        definirFuncBody.FunctionBody.accept(self)

    #Signature
    def visitDefinirParams(self, definirParams):
        definirParams.Parameters.accept(self)
    
    def visitDefinirParamsT(self, definirParamsT):
        definirParamsT.Params.accept(self)
        definirParamsT.Result.accept(self)
    
    #Result
    def visitDefinirTipo(self, definirTipo):
        definirTipo.Type.accept(self)
    
    #Type
    def visitTint(self, Tint):
        print('int', end = ' ')

    def visitTstring(self, Tstring):
        print('string', end = ' ')                 

    def visitTbool(self, Tbool):
        print('bool', end = ' ')

    def visitTbyte(self, Tbyte):
        print('byte', end = ' ')
    
    def visitTfloat(self, Tfloat):
        print('float', end = ' ')

    #Parameters    
    def visitDefinirParamsParameters(self, definirParams):
        print('(', end = ' ')
        print(')', end = ' ')
    
    def visitParams(self, params):
        print('(', end = ' ')
        params.ParameterList.accept(self)
        print(')', end = ' ')
    
    def visitParamsList(self, paramsList):
        print('(', end = ' ')
        paramsList.ParameterList.accept(self)
        print(',', end = ' ')
        print(')', end = ' ')
    
    #ParameterList
    def visitDefinirParamDecl(self, definirParamDecl):
        definirParamDecl.ParameterDecl.accept(self)
        definirParamDecl.ParameterList2.accept(self)
    
    #ParameterList2
    def visitCompParamsDecl(self, compParamsDecl):
        compParamsDecl.ParameterDecl.accept(self)
        compParamsDecl.ParameterDecList.accept(self)

    def visitCompoundParamDecl(self, compoundParamDecl):
        print(',', end = ' ')
        compoundParamDecl.ParameterList
    
    #ParameterDecl
    def visitParamDecl(self, paramDecl):
        paramDecl.Type.accept(self)
    
    def visitParamIdDecl(self, paramIdDecl):
        paramIdDecl.IdentifierList.accept(self)
        paramIdDecl.Type.accept(self)
    
    #FunctionBody
    def visitDefinirBlock(self, definirBlock):
        definirBlock.Block.accept(self)
    
    #Block
    def visitDefinirStatementL(self, statmentL):
        print('{', end = ' ')
        statmentL.StatementList.accept(self)
        print('}', end = ' ')

    #StatementList
    def visitCompoundStatmenteList(self, compoundStatmenteList):
        compoundStatmenteList.Statement.accept(self)
        print(';', end = ' ')
        compoundStatmenteList.StatementList2.accept(self)

    #StatementList2
    def visitCallBackStatementList(self, callBackStatementList):
        callBackStatementList.StatementList.accept(self)
    
    #Statement
    def visitStmtDeclaration(self, stmtDeclaration):
        stmtDeclaration.Declaration.accept(self)
    
    def visitStmtSimple(self, stmtSimple):
        stmtSimple.SimpleStmt.accept(self)
    
    def visitStmtReturn(self, stmtReturn):
        stmtReturn.ReturnStmt.accept(self)
    
    def visitStmtBreak(self, stmtBreak):
        stmtBreak.BreakStmt.accept(self)
    
    def visitStmtContinue(self, stmtContinue):
        stmtContinue.ContinueStmt.accept(self)
    
    def visitStmtBlock(self, stmtBlock):
        stmtBlock.Block.accept(self)
    
    def visitStmtIf(self, stmtIf):
        stmtIf.IfStmt.accept(self)
    
    def visitStmtSwitch(self, stmtSwitch):
        stmtSwitch.SwitchStmt.accept(self)
    
    def visitStmtFor(self, stmtFor):
        stmtFor.ForStmt.accept(self)

    #Declaration
    def visitDeclConst(self, declConst):
        declConst.ConstDecl.accept(self)
    
    def visitDeclType(self, declType):
        declType.TypeDecl.accept(self)
    
    def visitDeclVar(self, declVar):
        declVar.ConstVar.accept(self)
    
    #SimpleStmt
    def visitStmtExpression(self, stmtExpression):
        stmtExpression.Expression.accept(self)
    
    def visitStmtIncDec(self, stmtIncDec):
        stmtIncDec.IncDec.accept(self)
    
    def visitAssign(self, assign):
        assign.Assignment.accept(self)
    
    def visitDeclShortVar(self, declShortVar):
        declShortVar.ShortVarDecl.accept(self)
    
    #ReturnStmt
    def visitSimpleReturn(self, simpleReturn):
       print('return', end =' ')
    
    def visitExpReturn(self, expReturn):
        print('return', end =' ')
        expReturn.ExpressionList.accept(self)
    
    #BreakStmt
    def visitStmtBreack(self, stmtBreack):
        print('break', end =' ')

    #ContinueStmt
    def visitStmtContinue(self, stmtContinue):
        print('continue', end = ' ')
    
    #IfStmt
    def visitSimpleIf(self, simpleIf):
        print('if', end = ' ')
        simpleIf.Expression.accept(self)
        simpleIf.Block.accept(self)
    
    def visitIfElse(self, ifElse):
        print('if', end = ' ')
        ifElse.Expression.accept(self)
        ifElse.Block.accept(self)
        print('else', end = ' ')         #OBSERVAÇÃO -  Verificar linha 458 da GoAbstract
        ifElse.Block1.accept(self)
        
    def visitCompIfElse(self, compIfElse):
        print('if', end = ' ')
        compIfElse.Expression.accept(self)
        compIfElse.Block.accept(self)
        print('else', end = ' ')
        compIfElse.IfStmt.accept(self)

    #SwitchStmt
    def visitExprSwitch(self, exprSwitch):
        print('switch', end = ' ')
        exprSwitch.SimpleStmt.accept(self)
        print(';', end = ' ')
        exprSwitch.Expression.accept(self)
        print('{', end = ' ')
        exprSwitch.ExprCasaClauseList.accept(self)
        print('}', end = ' ')
    
    def visitExprSwitchNone(self, exprSwitchNone):
        print('switch', end = ' ')
        print('{', end = ' ')
        exprSwitchNone.ExprCaseClauseList.accept(self)
        print('}', end = ' ')
    
    def visitExprSwitchSimple(self, exprSwitchSimple):
        print('switch', end = ' ')
        exprSwitchSimple.SimpleStmt.accept(self)
        print('{', end = ' ')
        exprSwitchSimple.ExprCaseClauseList.accept(self)
        print('}', end = ' ')
    
    def visitExprSwitchExp(self, exprSwitchExp):
        print('switch', end = ' ')
        exprSwitchExp.Expression.accept(self)
        print('{', end = ' ')
        exprSwitchExp.ExprCaseClause.accept(self)
        print('}', end = ' ')

    #ExprCaseClauseList
    def visitCompoundCaseClase(self, compoundCaseClase):
        compoundCaseClase.ExprCaseClause.accept(self)
        compoundCaseClase.ExprCaseClauseList.accept(self)

    #ExprCase
    def visitExprCase(self, exprCase):
        exprCase.exprSwitchCase.accept(self)
        print(':', end = ' ')
        exprCase.StatmentList.accept(self)

    #ExprSwitchCase
    def visitCaseClauseExp(self, caseClauseExp):
        print('CASE', end = ' ')
        caseClauseExp.ExpressionList.accept(self)

    def visitCaseClause(self, caseClause):
        print('DEFAULT', end = ' ')

    #ForStmt
    def visitStmtFor(self, stmtFor):
        print('for', end = ' ')
        stmtFor.Condition.accept(self)
        stmtFor.Block.accept(self)

    def visitStmtForClause(self, stmtForClause):
        print('for', end = ' ')
        stmtForClause.ForClause.accept(self)
        stmtForClause.Block.accept(self)

    def visitStmtForRange(self, stmtForRange):
        print('for', end = ' ')
        stmtForRange.RangeClause.accept(self)
        stmtForRange.Block.accept(self)

    def visitStmtForBlock(self, stmtForBlock):
        print('for', end = ' ')
        stmtForBlock.Block.accept(self)

    #Condition
    def visitDefinirCondition(self, definirCondition):
        definirCondition.Expression.accept(self)

    #ForClause
    def visitClassicFor(self, classicFor):
        classicFor.InitStmt.accept(self)
        print(';', end = ' ')
        classicFor.Condition.accept(self)
        print(';', end = ' ')
        classicFor.PostStmt.accept(self)

    def visitInCoFor(self, inCoFor):
        inCoFor.InitStmt.accept(self)
        print(';', end = ' ')
        inCoFor.Condition.accept(self)

    def visitInitFor(self, initFor):
        initFor.InitStmt.accept(self)

    def visitCoPoFor(self, coPoFor):
        coPoFor.Condition.accept(self)
        print(';', end = ' ')
        coPoFor.PostStmt.accept(self)

    def visitConditionFor(self, conditionFor):
        conditionFor.Condition.accept(self)

    def visitInPoFor(self, inPoFor):
        inPoFor.InitStmt.accept(self)
        print(';', end = ' ')
        inPoFor.PostStmt.accept(self)

    def visitPostFor(self, postFor):
        postFor.PostStmt.accept(self)

    #InitStmt
    def visitStmtInit(self, stmtInit):
        stmtInit.SimpleStmt.accept(self)

    #PostStmt
    def visitStmtPost(self, stmtPost):
        stmtPost.SimpleStmt.accept(self)

    #RangeClause
    def visitDefinirRange(self, definirRange):
        print('range', end = ' ')
        definirRange.Expression.accept(self)

    def visitRangeExpList(self, rangeExpList):
        rangeExpList.ExpressionList.accept(self)
        print('=', end = ' ')
        print('range', end = ' ')
        rangeExpList.Expression.accept(self)

    def visitRangIDList(self, rangIDList):
        visitRangIDList.IdentifierList.accept(self)
        print('=', end = ' ')
        print('range', end = ' ')
        visitRangIDList.Expression.accept(self)

    #ConstDecl
    def visitSimpleConst(self, simpleConst):
        print('const', end = ' ')
        simpleConst.ConstSpec.accept(self)

    def visitCompConst(self, compConst):
        print('const', end = ' ')
        print('(', end = ' ')
        compConst.ConstSpecList.accept(self)
        print(')', end = ' ')

    #ConstSpecList
    def visitSimpleIdList(self, simpleIdList):
        simpleIdList.IdentifierList.accept(self)

    def visitListIdExp(self, listIdExp):
        listIdExp.IdentifierList.accept(self)
        print('=', end = ' ')
        listIdExp.ExpressionList.accept(self)

    def visitListTypeExp(self, listTypeExp):
        listTypeExp.IdentifierList.accept(self)
        listTypeExp.Type.accept(self)
        print('=', end = ' ')
        listTypeExp.ExpressionList.accept(self)
    
    #IdentfierList
    def visitDefinirID(self, definirID):
        print(definirID.ID, end = ' ')

    def visitDefinirIDList(self, definirIDList):
        print(definirIDList.ID, end = ' ')
        definirIDList.CompIDList.accept(self)

    #CompIDList
    def visitCompoundIDList(self, compoundIDList):
        print(',', end = ' ')
        print(compoundIDList.ID, end = ' ')
        compoundIDList.CompIDList2.accept(self)

    #CompIDList2
    def visitCallBackCompID(self, callBackCompID):
        callBackCompID.CompIDList.accept(self)

    #ExpressionList
    def visitCallExpList(self, callExpList):
        callExpList.Expression.accept(self)
        callExpList.ListExpr.accept(self)

    #ListExpr
    def visitCompoundExpList(self, compoundExpList):
        print(',', end = ' ')
        compoundExpList.Expression.accept(self)
        compoundExpList.ListExpr.accept(self)

    #TypeDecl
    def visitDefinirType(self, definirType):
        print('type', end = ' ')
        definirType.TypeSpec.accept(self)

    def visitCallTypeSpecList(self, callTypeSpecList):
        print('type', end = ' ')
        print('(', end = ' ')
        callTypeSpecList.TypeSpecList.accept(self)
        print(')', end = ' ')

    #TypeSpecList
    def visitCompTypeSpecList(self, compTypeSpecList):
        compTypeSpecList.TypeSpec.accept(self)
        print(';', end = ' ')
        compTypeSpecList.TypeSpecList.accept(self)

    #TypeSpec
    def visitSpecType(self, specType):
        print('id', end = ' ')
        specType.Type.accept(self)

    #VarDecl
    def visitDefinirVar(self, definirVar):
        print('var', end = ' ')
        definirVar.VarSpec.accept(self)

    def visitCompVar(self, compVar):
        print('var', end = ' ')
        print('(', end = ' ')
        compVar.VarSpecList.accept(self)
        print(')', end = ' ')

    #VarSpecList
    def visitCompoundVarSpec(self, compoundVarSpec):
        compoundVarSpec.VarSpec.accept(self)
        print(';', end = ' ')
        compoundVarSpec.VarSpecList

    #VarSpec
    def visitSpecVar(self, specVar):
        specVar.IdentifierList.accept(self)
        specVar.Type.accept(self)

    def visitClassicVarSpec(self, classicVarSpec):
        classicVarSpec.IdentifierList.accept(self)
        classicVarSpec.Type.accept(self)
        print('=', end = ' ')
        classicVarSpec.ExpressionList.accept(self)

    def visitSimpleVarSpec(self, simpleVarSpec):
        simpleVarSpec.IdentifierList.accept(self)
        print('=', end = ' ')
        simpleVarSpec.ExpressionList.accept(self)

    #Exp
    def visitOperadorOr(self, operadorOr):
        operadorOr.exp.accept(self)
        print(operadorOr.OR, end = ' ')
        operadorOr.exp1.accept(self)
    
    def visitCallExp1(self, callExp1):
        callExp1.exp1.accept(self)
    
    #Exp1
    def visitOperadorAnd(self, operadorAnd):
        operadorAnd.exp1.accept(self)
        print(operadorAnd.AND, end = ' ')
        operadorAnd.exp2.accept(self)
    
    def visitCallExp2(self, callExp2):
        callExp2.exp2.accept(self)

    #Exp2
    def visitOperadorIgual(self, operadorIgual):
        operadorIgual.exp2.accept(self)
        print(operadorIgual.EQUALS, end = ' ')
        operadorIgual.exp3.accept(self)

    def visitOpetadorDiferente(self, opetadorDiferente):
        opetadorDiferente.exp2.accept(self)
        print(opetadorDiferente.DIFERENTE, end = ' ')
        opetadorDiferente.exp3.accept(self)
    
    def visitOpetadorMenor(self, opetadorMenor):
        opetadorMenor.exp2.accept(self)
        print(opetadorMenor.LESS, end = ' ')
        opetadorMenor.exp3.accept(self)
    
    def visitOperadorMenorIgual(self, operadorMenorIgual):
        operadorMenorIgual.exp2.accept(self)
        print(operadorMenorIgual.LESS_EQUAL, end = ' ')
        operadorMenorIgual.exp3.accept(self)
    
    def visitOperadorMaior(self, operadorMaior):
        operadorMaior.exp2.accept(self)
        print(operadorMaior.GREATER, end = ' ')
        operadorMaior.exp3.accept(self)
    
    def visitOperadorMaiorIgual(self, operadorMaiorIgual):
        operadorMaiorIgual.exp2.accept(self)
        print(operadorMaiorIgual.GREATER_EQUAL, end = ' ')
        operadorMaiorIgual.exp3.accept(self)
    
    def visitCallExp3(self, callExp3):
        callExp3.exp3.accept(self)
    
    #Exp3
    def visitOperadorMais(self, operadorMais):
        operadorMais.exp3.accept(self)
        print(operadorMais.PLUS, end = ' ')
        operadorMais.exp4.accept(self)
    
    def visitOperadorMenos(self, operadorMenos):
        operadorMenos.exp3.accept(self)
        print(operadorMenos.MINUS, end = ' ')
        operadorMenos.exp4.accept(self)
    
    def visitOperadorPot(self, operadorPot):
        operadorPot.exp3.accept(self)
        print(operadorPot.POT, end = ' ')
        operadorPot.exp4.accept(self)
    
    def visitCallExp4(self, callExp4):
        callExp4.exp4.accept(self)
    
    #Exp4
    def visitOperadorVezes(self, operadorVezes):
        operadorVezes.exp4.accept(self)
        print(operadorVezes.TIMES, end = ' ')
        operadorVezes.exp5.accept(self)
    
    def visitOperadorDividir(self, operadorDividir):
        operadorDividir.exp4.accept(self)
        print(operadorDividir.DIVIDE, end = ' ')
        operadorDividir.exp5.accept(self)
    
    def visitOperadorMod(self, operadorMod):
        operadorMod.exp4.accept(self)
        print(operadorMod.MOD, end = ' ')
        operadorMod.exp5.accept(self)
    
    def visitCallExp5(self, callExp5):
        callExp5.exp5.accept(self)
    
    #Exp5
    def visitCallArguments(self, callArguments):
        callArguments.arguments.accept(self)
    
    def visitCallAssignment(self, callAssignment):
        callAssignment.assignment.accept(self)
    
    def visitCallNumber(self, callNumber):
        print(callNumber.NUMBER, end = ' ')
    
    def visitMostrarID(self, mostrarID):
        print(mostrarID.ID, end = ' ')
    
    #Arguments
    def visitCompoundExp(self, compoundExp):
        print(compoundExp.ID, end = ' ')
        compoundExp.ExpressionList.accept(self)
    
    def visitCallExp(self, callExp):
        callExp.exp.accept(self)

    #IncDec    
    def visitIncOp(self, incOp):
        incOp.Expression.accept(self)
        print('+', end = ' ')
        print('+', end = ' ')

    def visitDecOp(self, decOp):
        decOp.Expression.accept(self)
        print('-', end = ' ')
        print('-', end = ' ')

    #Assignment
    def visitAssignOp(self, assignOp):
        assignOp.ExpressionList.accept(self)
        print('=', end = ' ')
        assignOp.ExpressionList1.accept(self)

    #ShortVarDecl
    def visitDeclShortVar(self, declShortVar):
        declShortVar.IdentifierList.accept(self)
        print('=', end = ' ')
        declShortVar.ExpressionList.accept(self)


    

    


