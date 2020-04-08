class Visitor():
    def visitDefinirFunc(self, definirFunc):
        print('FUNC')
        print('ID')
        definirFunc.Signature.accept(self)

    def visitDefinirFuncBody(self, definirFuncBody):
        print('FUNC')
        print('ID')
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
        print('INT')

    def visitTstring(self, Tstring):
        print('STRING')                 #Observação Paramentro com Letra Maiúscula  #(Tint,Tstring,Tbool,Tfloat)

    def visitTbool(self, Tbool):
        print('BOOL')
    
    def visitTfloat(self, Tfloat):
        print('FLOAT')
    
    def visitDefinirParams(self, definirParams):
        print('LPAREN')
        print('RPAREN')
    
    def visitParams(self, params):
        print('LPAREN')
        params.ParameterList.accept(self)
        print('RPAREN')
    
    def visitParamsList(self, paramsList):
        print('LPAREN')
        paramsList.ParameterList.accept(self)
        print('COMMA')
        print('RPAREN')
    
    def visitDefinirParamDecl(self, definirParamDecl):
        definirParamDecl.ParameterDecl.accept(self)
    
    def visitCompParamsDecl(self, compParamsDecl):
        compParamsDecl.ParameterDecl.accept(self)
        compParamsDecl.ParameterDecList.accept(self)
    
    def visitDecParamComp(self, decParamComp):
        print('COMMA')
        decParamComp.ParameterDecl.accept(self)
    
    def visitDecListCompound(self, decListCompound):
        print('COMMA')
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
        print('LCHAVES')
        definirStatementL.StatmentList.accept(self)
        print('RCHAVES')
    
    def visitDefinirStatement(self, definirStatement):
        definirStatement.Statement.accept(self)
        print('SEMICOLON')
    
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

##Parada na linha 307 da GoAbstract.py
##Daniel vefiricar a linha deste codigo na linha 23 até a 33
##Deve dar continuidade na  -- def visitDeclConst