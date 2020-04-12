class Visitor():
    def visitDefinirFunc(self, definirFunc):
        print('func', end =' ')
        print(definirFunc.ID, end = ' ')
        definirFunc.Signature.accept(self)

    def visitDefinirFuncBody(self, definirFuncBody):
        print('func', end =' ')
        print(definirFuncBody.ID, end = ' ')
        definirFuncBody.Signature.accept(self)
        definirFuncBody.FunctionBody.accept(self)

    def visitDefinirParams(self, definirParams):
        definirParams.Parameters.accept(self)
    
    def visitDefinirParamsT(self, definirParamsT):
        definirParamsT.Params.accept(self)
        definirParamsT.Result.accept(self)
    
    def visitDefinirTipo(self, definirTipo):
        definirTipo.Type.accept(self)
    
    def visitTint(self, Tint):
        print('int', end = ' ')

    def visitTstring(self, Tstring):
        print('string', end = ' ')                 #Observação Paramentro com Letra Maiúscula  #(Tint,Tstring,Tbool,Tfloat)

    def visitTbool(self, Tbool):
        print('bool', end = ' ')

    def visitTbyte(self, Tbyte):
        print('byte', end = ' ')
    
    def visitTfloat(self, Tfloat):
        print('float', end = ' ')
    
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
    
    def visitDefinirParamDecl(self, definirParamDecl):
        definirParamDecl.ParameterDecl.accept(self)
    
    def visitCompParamsDecl(self, compParamsDecl):
        compParamsDecl.ParameterDecl.accept(self)
        compParamsDecl.ParameterDecList.accept(self)
    
    def visitDecParamComp(self, decParamComp):
        print(',', end = ' ')
        decParamComp.ParameterDecl.accept(self)
    
    def visitDecListCompound(self, decListCompound):
        print(',', end = ' ')
        decListCompound.ParameterDecl.accept(self)
        decListCompound.ParameterDecList.accept(self)
    
    def visitParamDecl(self, paramDecl):
        paramDecl.Type.accept(self)
    
    def visitParamIdDecl(self, paramIdDecl):
        paramIdDecl.IdentifierList.accept(self)
        paramIdDecl.Type.accept(self)
    
    def visitDefinirBlock(self, definirBlock):
        definirBlock.Block.accept(self)
    
    def visitDefinirStatementL(self, definirStatementL):
        print('{', end = ' ')
        definirStatementL.StatmentList.accept(self)
        print('}', end = ' ')
    
    def visitDefinirStatement(self, definirStatement):
        definirStatement.Statement.accept(self)
        print(';', end = ' ')

    def visitCompoundStatmenteList(self, compoundStatmenteList):
        compoundStatmenteList.Statement.accept(self)
        print(';', end = ' ')
        compoundStatmenteList.StatementList.accept(self)
    
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

    def visitDeclConst(self, declConst):
        declConst.ConstDecl.accept(self)
    
    def visitDeclType(self, declType):
        declType.TypeDecl.accept(self)
    
    def visitDeclVar(self, declVar):
        declVar.ConstVar.accept(self)
    
    def visitStmtEmpty(self, stmtEmpty):
        stmtEmpty.None.accept(self)       #Duvidas -  Verificar linha 355 da GoAbstract
        
    def visitStmtExpression(self, stmtExpression):
        stmtExpression.Expression.accept(self)
    
    def visitStmtIncDec(self, stmtIncDec):
        stmtIncDec.IncDec.accept(self)
    
    def visitAssign(self, assign):
        assign.Assignment.accept(self)
    
    def visitDeclShortVar(self, declShortVar):
        declShortVar.ShortVarDecl.accept(self)
    
    def visitSimpleReturn(self, simpleReturn):
       print('return', end =' ')
    
    def visitExpReturn(self, expReturn):
        print('return', end =' ')
        expReturn.ExpressionList.accept(self)
    
    def visitStmtBreack(self, stmtBreack):
        print('break', end =' ')

    def visitStmtContinue(self, stmtContinue):
        print('continue'= end = ' ')
    
    def visitSimpleIf(self, simpleIf):
        print('if', end = ' ')
        simpleIf.Expression.accept(self)
        simpleIf.Block.accept(self)
    
    def visitIfElse(self, ifElse):
        print('if', end = ' ')
        ifElse.Expression.accept(self)
        ifElse.Block.accept(self)
        print('else', end = ' ')         #OBSERVAÇÃO -  Verificar linha 458 da GoAbstract
    
    def visitCompIfElse(self, compIfElse):
        print('if', end = ' ')
        compIfElse.Expression.accept(self)
        compIfElse.Block.accept(self)
        print('else', end = ' ')
        compIfElse.IfStmt.accept(self)

    def visitExprSwitch(self, exprSwitch):
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

    def visitCallExprCaseClause(self, callExprCaseClause):
        callExprCaseClause.ExprCaseClause.accept(self)

    def visitCompoundCaseClase(self, compoundCaseClase):
        compoundCaseClase.ExprCaseClause.accept(self)
        compoundCaseClase.ExprCaseClauseList.accept(self)

    def visitEmptyCaseClause(self, emptyCaseClause):
        print(' ') #OBSERVAÇÃO: NONE É VAZIO?

    def visitExprCase(self, exprCase):
        exprCase.exprSwitchCase.accept(self)
        print(':', end = ' ')
        exprCase.StatmentList.accept(self)

    def visitCaseClauseExp(self, caseClauseExp):
        print('CASE', end = ' ')
        caseClauseExp.ExpressionList.accept(self)

    def visitCaseClause(self, caseClause):
        print('DEFAULT', end = ' ')

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

    def visitDefinirCondition(self, definirCondition):
        definirCondition.Expression.accept(self)

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

    def visitStmtInit(self, stmtInit):
        stmtInit.SimpleStmt.accept(self)

    def visitStmtPost(self, stmtPost):
        stmtPost.SimpleStmt.accept(self)

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

    def visitSimpleConst(self, simpleConst):
        print('const', end = ' ')
        simpleConst.ConstSpec.accept(self)

    def visitCompConst(self, compConst):
        print('const', end = ' ')
        print('(', end = ' ')
        compConst.ConstSpec.accept(self)
        print(')', end = ' ')

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
    
    def visitCallConstSpec(self, callConstSpec):
        callConstSpec.ConstSpec.accept(self)
        print(';', end = ' ')

    def visitCompoundConstSpec(self, compoundConstSpec):
        compoundConstSpec.ConstSpec.accept(self)
        print(';', end = ' ')
        compoundConstSpec.ConstSpecList.accept(self)

    def visitDefinirIDList(self, definirIDList):
        print(definirIDList.ID, end = ' ')
        definirIDList.CompIDList.accept(self)

    def visitDoubleID(self, doubleID):
        print(',', end = ' ')
        print(doubleID.ID, end = ' ')

    def visitCompoundIDList(self, compoundIDList):
        print(',', end = ' ')
        print(compoundIDList.ID, end = ' ')
        compoundIDList.CompIDList.accept(self)

    def visitSimpleID(self, simpleID):
        print(' ', end = ' ')

    def visitDefinirExpList(self, definirExpList):
        definirExpList.Expression.accept(self)

    def visitCallExpList(self, callExpList):
        callExpList.Expression.accept(self)
        callExpList.ListExpr.accept(self)

    def visitSimpleExpList(self, simpleExpList):
        print(',', end = ' ')
        simpleExpList.Expression.accept(self)

    def visitCompoundExpList(self, compoundExpList):
        print(',', end = ' ')
        compoundExpList.Expression.accept(self)
        compoundExpList.ListExpr.accept(self)

    def visitDefinirType(self, definirType):
        print('type', end = ' ')
        definirType.TypeSpec.accept(self)

    def visitCallTypeSpecList(self, callTypeSpecList):
        print('type', end = ' ')
        print('(', end = ' ')
        callTypeSpecList.callTypeSpecList.accept(self)
        print(')', end = ' ')

    def visitTypeSpecDouble(self, typeSpecDouble):
        typeSpecDouble.TypeSpec.accept(self)
        print(';', end = ' ')

    def visitCompTypeSpecList(self, compTypeSpecList):
        compTypeSpecList.TypeSpec.accept(self)
        print(';', end = ' ')
        compTypeSpecList.TypeSpecList.accept(self)

    def visitTypeSpecSimple(self, typeSpecSimple):
        print(' ', end = ' ')

    def visitSpecType(self, specType):
        print('id', end = ' ')
        specType.Type.accept(self)

    def visitDefinirVar(self, definirVar):
        print('var', end = ' ')
        definirVar.VarSpec.accept(self)

    def visitCompVar(self, compVar):
        print('var', end = ' ')
        print('(', end = ' ')
        compVar.VarSpecList.accept(self)
        print(')', end = ' ')

    def visitVarDef(self, varDef):
        varDef.VarSpec.accept(self)
        print(';', end = ' ')
    
    def visitCompoundVarSpec(self, compoundVarSpec):
        compoundVarSpec.VarSpec.accept(self)
        print(';', end = ' ')
        compoundVarSpec.VarSpecList

    def visitSimpleVar(self, simpleVar):
        print(' ', end = ' ')

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

    def visitDefinirExp(self, definirExp):
        definirExp.Expression.accept(self)
        definirExp.binary_op.accept(self)
        definirExp.Expression.accept(self)

    def visitExprUnary(self, exprUnary):
        exprUnary.UnaryExpr.accept(self)

    def visitUnaryExprNumber(self, unaryExprNumber):
        print(unaryExprNumber.NUMBER, end = ' ')

    def visitUnaryExprID(self, unaryExprID):
        print(unaryExprID.ID, end = ' ')

    def visitUnaryExprParen(self, unaryExprParen):
        print('(', end = ' ')
        unaryExprParen.Expression.accept(self)
        print(')', end = ' ')

    def visitOpOr(self, opOr):
        print('||', end = ' ')

    def visitOpAnd(self, opAnd):
        print('&&', end = ' ')

    def visitOpRel(self, opRel):
        opRel.rel_op.accept(self)

    def visitOpAdd(self, opAdd):
        opAdd.add_op.accept(self)

    def visitOpMul(self, opMul):
        opMul.mul_op.accept(self)

    def visitEqualsOp(self, equalsOp):
        print('==', end = ' ')

    def visitDifereOp(self, difereOp):
        print('!=', end = ' ')

    def visitMenorOp(self, menorOp):
        print('<', end = ' ')

    def visitMenorIgualOp(self, menorIgualOp):
        print('<=', end = ' ')

    def visitMaiorOp(self, maiorOp):
        print('>', end = ' ')        

    def visitMaiorIgualOp(self, maiorIgualOp):
        print('>=', end = ' ')

    def visitMaisOp(self, maisOp):
        print('+', end = ' ')

    def visitMenosOp(self, menosOp):
        print('-', end = ' ')

    def visitVezesOp(self, vezesOp):
        print('*', end = ' ')

    def visitDivideOp(sel, divideOp):
        print('/', end = ' ')

    def visitModOp(self, modOp):
        print('%', end = ' ')

    def visitIncOp(self, incOp):
        incOp.Expression.accept(self)
        print('+', end = ' ')
        print('+', end = ' ')

    def visitDecOp(self, decOp):
        decOp.Expression.accept(self)
        print('-', end = ' ')
        print('-', end = ' ')

    def visitAssignOp(self, assignOp):
        assignOp.ExpressionList.accept(self)
        print('=', end = ' ')
        assignOp.ExpressionList.accept(self)

    def visitDeclShortVar(self, declShortVar):
        declShortVar.IdentifierList.accept(self)
        print('=', end = ' ')
        declShortVar.ExpressionList.accept(self)


    

    


