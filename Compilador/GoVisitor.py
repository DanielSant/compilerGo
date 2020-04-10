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
        print('\,', end = ' ')
        print(')', end = ' ')
    
    def visitDefinirParamDecl(self, definirParamDecl):
        definirParamDecl.ParameterDecl.accept(self)
    
    def visitCompParamsDecl(self, compParamsDecl):
        compParamsDecl.ParameterDecl.accept(self)
        compParamsDecl.ParameterDecList.accept(self)
    
    def visitDecParamComp(self, decParamComp):
        print('\,', end = ' ')
        decParamComp.ParameterDecl.accept(self)
    
    def visitDecListCompound(self, decListCompound):
        print('\,', end = ' ')
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
        print('(', end = ' ')
        definirStatementL.StatmentList.accept(self)
        print(')', end = ' ')
    
    def visitDefinirStatement(self, definirStatement):
        definirStatement.Statement.accept(self)
        print('\;', end = ' ')
    
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
    

##Parada na linha 307 da GoAbstract.pyc