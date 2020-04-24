class Visitor():
    # FunctionDecl
    def visitDefinirFunc(self, definirFunc):
        print('func', end =' ')
        print(definirFunc.ID, end = ' ')
        definirFunc.Signature.accept(self)

    def visitDefinirFuncBody(self, definirFuncBody):
        print('func', end =' ')
        print(definirFuncBody.ID, end = ' ')
        definirFuncBody.Signature.accept(self)
        definirFuncBody.FunctionBody.accept(self)

    # Signature
    def visitDefinirParams(self, definirParams):
        definirParams.Parameters.accept(self)
    
    def visitDefinirParamsT(self, definirParamsT):
        definirParamsT.Params.accept(self)
        definirParamsT.Result.accept(self)
    
    # Result
    def visitDefinirTipo(self, definirTipo):
        #definirTipo.Type.accept(self)
        pass
    
    # Type
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
    
    # Parameters
    def visitParams(self, params):
        print('(', end = ' ')
        params.ParameterList.accept(self)
        print(')', end = ' ')

    def visitParamsList(self, paramsList):
        print('(', end = ' ')
        paramsList.ParameterList.accept(self)
        print(',', end = ' ')
        print(')', end = ' ')

    def visitDefinirParamsParameters(self, definirParams):
        print('(', end = ' ')
        print(')', end = ' ')
    
    # ParameterList
    def visitCompParamsDecl(self, compParamsDecl):
        compParamsDecl.ParameterDecl.accept(self)
        compParamsDecl.ParameterList_Mul.accept(self)

    def visitCallParameterDecl(self, callParameterDecl):
        callParameterDecl.ParameterDecl.accept(self)

    # ParameterList_Mul
    def visitCallBackParameterList_Mul(self, callBackParameterList_Mul):
        print(',', end = ' ')
        callBackParameterList_Mul.ParameterDecl.accept(self)
        callBackParameterList_Mul.ParameterList_Mul1.accept(self)

    def visitEndParameterList_Mul(self, endParameterList_Mul):
        print(',', end = ' ')
        endParameterList_Mul.ParameterDecl.accept(self)

    # ParameterDecl
    def visitParamIdDecl(self, paramIdDecl):
        paramIdDecl.IdentifierList.accept(self)
        paramIdDecl.Type.accept(self)

    def visitParamDecl(self, paramDecl):
        paramDecl.Type.accept(self)

    # FunctionBody
    def visitDefinirBlock(self, definirBlock):
        definirBlock.Block.accept(self)
    
    # Block
    def visitDefinirStatementL(self, definirStatementL):
        print('{', end = ' ')
        definirStatementL.StatementList.accept(self)
        print('}', end = ' ')

    def visitMultFunc(self, multFunc):
        print('{', end = ' ')
        multFunc.StatementList.accept(self)
        print('}', end = ' ')
        multFunc.FunctionDecl.accept(self)
    
    # StatementList
    def visitDefinirStatement(self, definirStatement):
        definirStatement.Statement.accept(self)
        print(';', end = ' ')

    def visitCompoundStatmenteList(self, compoundStatmenteList):
        compoundStatmenteList.Statement.accept(self)
        print(';', end = ' ')
        compoundStatmenteList.StatementList.accept(self)
    
    # Statement
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

    # Declaration
    def visitDeclConst(self, declConst):
        declConst.ConstDecl.accept(self)
    
    def visitDeclType(self, declType):
        declType.TypeDecl.accept(self)
    
    def visitDeclVar(self, declVar):
        declVar.ConstVar.accept(self)
    
    # SimpleStmt
    def visitStmtCondition(self, stmtCondition):
        stmtConditio.Condition.accept(self)

    def visitStmtIncDec(self, stmtIncDec):
        stmtIncDec.IncDec.accept(self)
    
    def visitAssign(self, assign):
        assign.Assignment.accept(self)
    
    def visitDeclShortVar(self, declShortVar):
        declShortVar.ShortVarDecl.accept(self)
    
    # ReturnStmt
    def visitExpReturn(self, expReturn):
        print('return', end =' ')
        expReturn.ExpressionList.accept(self)

    def visitSimpleReturn(self, simpleReturn):
       print('return', end =' ')
    
    # BreakStmt
    def visitStmtBreack(self, stmtBreack):
        print('break', end =' ')

    # ContinueStmt
    def visitStmtContinue(self, stmtContinue):
        print('continue', end = ' ')
    
    # Ifstmt
    def visitSimpleIf(self, simpleIf):
        print('if', end = ' ')
        simpleIf.Expression.accept(self)
        simpleIf.Block.accept(self)

    def visitCompIfElse(self, compIfElse):
        print('if', end = ' ')
        compIfElse.Expression.accept(self)
        compIfElse.Block.accept(self)
        print('else', end = ' ')
        compIfElse.IfStmt.accept(self)
    
    def visitIfElse(self, ifElse):
        print('if', end = ' ')
        ifElse.Expression.accept(self)
        ifElse.Block.accept(self)
        print('else', end = ' ')         
        ifElse.Block1.accept(self)
        
    # SwitchStmt
    def visitExprSwitch(self, exprSwitch):
        print('switch', end = ' ')
        exprSwitch.switchStmt_Head.accept(self)
        exprSwitch.switchStmt_Body.accept(self)
    
    # SwitchStmt_Head
    def visitExprSwitchSimple(self, exprSwitchSimple):
        print('switch', end = ' ')
        exprSwitchSimple.switchStmt_Body.accept(self)
    
    # SwitchStmt_Body
    def visitExprSwitchSimple(self, exprSwitchSimple):
        print('switch', end = ' ')
        exprSwitchSimple.SimpleStmt.accept(self)
        print('{', end = ' ')
        exprSwitchSimple.ExprCaseClauseList.accept(self)
        print('}', end = ' ')

    # ExprSwitchHead1
    def visitExprSwitchHead1(self, exprSwitchHead1):
        exprSwitchHead1.simpleStmt.accept(self)
        print(';', end = ' ')
        exprSwitchHead1.expression.accept(self)
    
    # ExprSwitchHead2 
    def visitExprSwitchHead2(self, exprSwitchHead2):
        exprSwitchHead2.simpleStmt.accept(self)
        print(';', end = ' ')

    # ExprSwitchHead3
    def visitExprSwitchHead3(self, exprSwitchHead3):
        exprSwitchHead3.expression.accept(self)

    # ExprSwitchBody1
    def visitExprSwitchBody1(self, exprSwitchBody1):
        print('(', end  = ' ')
        exprSwitchBody1.exprCaseClauseList.accept(self)
        print(')', end  = ' ')

    # ExprSwitchBody2
    def visitExprSwitchBody2(self, exprSwitchBody2):
        print('(', end  = ' ')
        print(')', end  = ' ')

    def visitExprSwitchExp(self, exprSwitchExp):
        print('switch', end = ' ')
        exprSwitchExp.Expression.accept(self)
        print('{', end = ' ')
        exprSwitchExp.ExprCaseClause.accept(self)
        print('}', end = ' ')

    # ExprCaseClauseList
    def visitCompoundCaseClase1(self, compoundCaseClase1):
        compoundCaseClase1.ExprCaseClause.accept(self)
        compoundCaseClase1.ExprCaseClauseList.accept(self)

    def visitCompoundCaseClase2(self, compoundCaseClase2):
        compoundCaseClase2.ExprCaseClause.accept(self)

    # ExprCaseClause
    def visitExprCase(self, exprCase):
        exprCase.exprSwitchCase.accept(self)
        print(':', end = ' ')
        exprCase.StatmentList.accept(self)

    # ExprSwitchCase
    def visitCaseClauseExp(self, caseClauseExp):
        print('CASE', end = ' ')
        caseClauseExp.ExpressionList.accept(self)

    def visitCaseClause(self, caseClause):
        print('DEFAULT', end = ' ')

    # ForStmt
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

    # Condition
    def visitDefinirCondition(self, definirCondition):
        definirCondition.Expression.accept(self)

    # ForClause
    def visitClassicFor(self, classicFor):
        classicFor.InitStmt.accept(self)
        print(';', end = ' ')
        classicFor.Condition.accept(self)
        print(';', end = ' ')
        classicFor.PostStmt.accept(self)

    def visitInitFor(self, initFor):
        initFor.InitStmt.accept(self)

    def visitInPoFor(self, inPoFor):
        inPoFor.InitStmt.accept(self)
        print(';', end = ' ')
        inPoFor.PostStmt.accept(self)

    # InitStmt
    def visitStmtInit(self, stmtInit):
        stmtInit.PostStmt.accept(self)

    # PostStmt
    def visitStmtPost(self, stmtPost):
        stmtPost.SimpleStmt.accept(self)

    # RangeClause
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

    # ConstDecl
    def visitSimpleConst(self, simpleConst):
        print('const', end = ' ')
        simpleConst.ConstSpec.accept(self)

    def visitCompConst(self, compConst):
        print('const', end = ' ')
        print('(', end = ' ')
        compConst.constSpecList.accept(self)
        print(')', end = ' ')

    # ConstSpecList
    def visitCallConstSpec(self, callConstSpec):
        callConstSpec.ConstSpec.accept(self)
        print(';', end = ' ')

    def visitCompoundConstSpec(self, compoundConstSpec):
        compoundConstSpec.ConstSpec.accept(self)
        print(';', end = ' ')
        compoundConstSpec.ConstSpecList.accept(self)

    # ConstSpec
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
    
    # IdentifierList
    def visitDefinirIDList(self, definirIDList):
        print(definirIDList.ID, end = ' ')
        #definirIDList.CompIDList.accept(self)

    # CompIDList
    def visitCompoundIDList(self, compoundIDList):
        print(',', end = ' ')
        print(compoundIDList.ID, end = ' ')
        compoundIDList.CompIDList.accept(self)

    # ExpressionList
    def visitDefinirExpList(self, definirExpList):
        definirExpList.Expression.accept(self)

    def visitCallExpList(self, callExpList):
        callExpList.Expression.accept(self)
        callExpList.ListExpr.accept(self)

    # ListExpr
    def visitSimpleExpList(self, simpleExpList):
        print(',', end = ' ')
        simpleExpList.Expression.accept(self)

    def visitCompoundExpList(self, compoundExpList):
        print(',', end = ' ')
        compoundExpList.Expression.accept(self)
        compoundExpList.ListExpr.accept(self)

    # TypeDecl
    def visitDefinirType(self, definirType):
        print('type', end = ' ')
        definirType.TypeSpec.accept(self)

    def visitCallTypeSpecList(self, callTypeSpecList):
        print('type', end = ' ')
        print('(', end = ' ')
        callTypeSpecList.callTypeSpecList.accept(self)
        print(')', end = ' ')

    # TypeSpecList
    def visitCompTypeSpecList(self, compTypeSpecList):
        compTypeSpecList.TypeSpec.accept(self)
        print(';', end = ' ')
        compTypeSpecList.TypeSpecList.accept(self)

    # TypeSpec
    def visitSpecType(self, specType):
        print('id', end = ' ')
        specType.Type.accept(self)

    # VarDecl
    def visitDefinirVar(self, definirVar):
        print('var', end = ' ')
        definirVar.VarSpec.accept(self)

    def visitCompVar(self, compVar):
        print('var', end = ' ')
        print('(', end = ' ')
        compVar.VarSpecList.accept(self)
        print(')', end = ' ')

    # VarSpecList
    def visitCompoundVarSpec(self, compoundVarSpec):
        compoundVarSpec.VarSpec.accept(self)
        print(';', end = ' ')
        compoundVarSpec.VarSpecList

    # VarSpec
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

    # Expression
    def visitExprUnary(self, exprUnary):
        exprUnary.UnaryExpr.accept(self)

    def visitDefinirExp(self, definirExp):
        definirExp.Expression.accept(self)
        definirExp.binary_op.accept(self)
        definirExp.Expression1.accept(self)

    # UnaryExpr
    def visitUnaryExprNumber(self, unaryExprNumber):
        print(unaryExprNumber.NUMBER, end = ' ')

    def visitUnaryExprID(self, unaryExprID):
        print(unaryExprID.ID, end = ' ')
        unaryExprID.Arguments.accept(self)

    def visitUnaryExprParen(self, unaryExprParen):
        print('(', end = ' ')
        unaryExprParen.Expression.accept(self)
        print(')', end = ' ')

    # Arguments

    # BinaryOp
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

    # RelOp
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

    # AddOp
    def visitMaisOp(self, maisOp):
        print('+', end = ' ')

    def visitMenosOp(self, menosOp):
        print('-', end = ' ')

    #MulOp
    def visitVezesOp(self, vezesOp):
        print('*', end = ' ')

    def visitDivideOp(sel, divideOp):
        print('/', end = ' ')

    def visitModOp(self, modOp):
        print('%', end = ' ')

    # IncDec
    def visitIncOp(self, incOp):
        incOp.Expression.accept(self)
        print('+', end = ' ')
        print('+', end = ' ')

    def visitDecOp(self, decOp):
        decOp.Expression.accept(self)
        print('-', end = ' ')
        print('-', end = ' ')

    # Assignment
    def visitAssignOp(self, assignOp):
        assignOp.ExpressionList.accept(self)
        print('=', end = ' ')
        assignOp.ExpressionList1.accept(self)

    # ShortVarDec
    def visitDeclShortVarDef(self, declShortVar):
        declShortVar.IdentifierList.accept(self)
        print('=', end = ' ')
        declShortVar.ExpressionList.accept(self)