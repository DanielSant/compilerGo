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
    
    def visitTfloat(self, Tfloat):
        print('float', end = ' ')
    
    def visitDefinirParams(self, definirParams):
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

#Para na Linha 525 da GoAbstract.py
