import ply.yacc as yacc
import ply.lex as lex
from GoLex import tokens
import GoAbstract as abstract

def p_functionDecl(p):
    '''functionDecl : FUNC ID signature
                    | FUNC ID signature functionBody'''
    if(len(p) == 4):
        p[0] = abstract.DefinirFunc(p[1], p[2], p[3])
    else:
        p[0] = abstract.DefinirFuncBody(p[1], p[2], p[3], p[4])

def p_signature(p):
    '''signature : parameters
                 | parameters result'''
    if(len(p) == 2):
        p[0] = abstract.DefinirParams(p[1])
    else:
        p[0] =  abstract.DefinirParamsT(p[1], p[2])

def p_result(p):
    '''result : type'''
    p[0] = abstract.DefinirTipo(p[1])

def p_type(p):
    '''type : INT
            | STRING
            | BOOL
            | BYTE
            | FLOAT'''
    if(p[1] == 'INT'):
        p[0] = abstract.Tint(p[1])
    elif(p[1] == 'STRING'):
        p[0] = abstract.Tstring(p[1])
    elif(p[1] == 'BOOL'):
        p[0] = abstract.Tbool(p[1])
    elif(p[1] == 'BYTE'):
        p[0] = abstract.Tbyte(p[1])
    elif(p[1] == 'FLOAT'):
        p[0] = abstract.Tfloat(p[1])

def p_parameters(p):
    '''parameters : LPAREN parameterList RPAREN
                  | LPAREN RPAREN'''
    if(len(p) == 4):
        p[0] = abstract.Params(p[1], p[2], p[3])
    else:
        p[0] = abstract.DefinirParamsParameters(p[1], p[2])

def p_parameterList(p):
    '''parameterList : parameterDecl parameterList_Mul
                     | parameterDecl'''
    if(len(p) == 3):
        p[0] = abstract.CompoundParamDecl(p[1], p[2])
    else:
        p[0] = abstract.CallParameterDecl(p[1])

def p_parameterList_Mul(p):
    '''parameterList_Mul : COMMA parameterDecl parameterList_Mul
                         | COMMA parameterDecl'''
    if(len(p) == 4):
        p[0] = abstract.CallBackParameterList_Mul(p[1], p[2], p[3])
    else:
        p[0] = abstract.EndParameterList_Mul(p[1], p[2])

def p_parameterDecl(p):
    '''parameterDecl : identifierList type
                     | type'''
    if(len(p) == 3):
        p[0] = abstract.ParamIdDecl(p[1], p[2])
    else:
        p[0] = abstract.ParamDecl(p[1])

def p_functionBody(p):
    '''functionBody : block'''
    p[0] = abstract.DefinirBlock(p[1])

def p_block(p):
    '''block : LCHAVES statementList RCHAVES
             | LCHAVES statementList RCHAVES functionDecl'''
    if(len(p) == 4):
        p[0] = abstract.DefinirStatementL(p[1], p[2], p[3])
    else:
        p[0] = abstract.MultFunc(p[1], p[2], p[3], p[4])

def p_statementList(p):
    '''statementList : statement SEMICOLON
                     | statement SEMICOLON statementList'''
    if(len(p) == 3):
        p[0] = abstract.DefinirStatement(p[1], p[2])
    else:
        p[0] = abstract.CompoundStatementList(p[1], p[2], p[3])

def p_statement(p):
    '''statement : declaration
                 | simpleStmt
                 | returnStmt
                 | breakStmt
                 | continueStmt
                 | block
                 | ifStmt
                 | switchStmt
                 | forStmt'''
    if(isinstance(p[1], abstract.Declaration)):
        p[0] = abstract.StmtDeclaration(p[1])
    elif(isinstance(p[1], abstract.SimpleStmt)):
        p[0] = abstract.StmtSimple(p[1])
    elif(isinstance(p[1], abstract.ReturnStmt)):
        p[0] = abstract.StmtReturn(p[1])
    elif(isinstance(p[1], abstract.BreakStmt)):
        p[0] = abstract.StmtBreak(p[1])
    elif(isinstance(p[1], abstract.ContinueStmt)):
        p[0] = abstract.StmtContinue(p[1])
    elif(isinstance(p[1], abstract.Block)):
        p[0] = abstract.StmtBlock(p[1])
    elif(isinstance(p[1], abstract.IfStmt)):
        p[0] = abstract.StmtIf(p[1])
    elif(isinstance(p[1], abstract.SwitchStmt)):
        p[0] = abstract.StmtSwitch(p[1])
    elif(isinstance(p[1], abstract.ForStmt)):
        p[0] = abstract.CallStmtFor(p[1])

def p_declaration(p):
    '''declaration : constDecl
                   | typeDecl
                   | varDecl'''
    if(isinstance(p[1], abstract.ConstDecl)):
        p[0] = abstract.DeclConst(p[1])
    elif(isinstance(p[1], abstract.TypeDecl)):
        p[0] = abstract.DeclType(p[1])
    elif(isinstance(p[1], abstract.VarDecl)):
        p[0] = abstract.DeclVar(p[1])

def p_simpleStmt(p): #condition vai para expression
    '''simpleStmt : condition
                  | incDec
                  | assignment
                  | shortVarDec'''
    if(isinstance(p[1], abstract.Condition)):
        p[0] = abstract.StmtCondition(p[1])
    elif(isinstance(p[1], abstract.IncDec)):
        p[0] = abstract.StmtIncDec(p[1])
    elif(isinstance(p[1], abstract.Assignment)):
        p[0] = abstract.Assign(p[1])
    elif(isinstance(p[1], abstract.ShortVarDecl)):
        p[0] = abstract.DeclShortVar(p[1])

def p_returnStmt(p):
    '''returnStmt : RETURN expressionList
                  | RETURN'''
    if(len(p) == 3):
        p[0] = abstract.ExpReturn(p[1], p[2])
    else:
        p[0] = abstract.SimpleReturn(p[1])

def p_breakStmt(p):
    '''breakStmt : BREAK'''
    p[0] = abstract.StmtBreak(p[1])

def p_continueStmt(p):
    '''continueStmt : CONTINUE'''
    p[0] = abstract.StmtContinue(p[1])

def p_ifStmt(p):
    '''ifStmt : IF expression block
              | IF expression block ELSE ifStmt
              | IF expression block ELSE block'''
    if(len(p) == 4):
        p[0] = abstract.SimpleIf(p[1], p[2], p[3])
    elif(isinstance(p[5], abstract.IfStmt)):
        p[0] = abstract.CompIfElse(p[1], p[2], p[3], p[4], p[5])
    elif(isinstance(p[5], abstract.Block)):
        p[0] = abstract.IfElse(p[1], p[2], p[3], p[4], p[5])

def p_switchStmt(p):
    '''switchStmt : SWITCH switchStmt_Head switchStmt_Body
                  | SWITCH switchStmt_Body'''
    if(len(p) == 4):
        p[0] = abstract.ExprSwitch(p[1], p[2], p[3])
    else:
        p[0] = abstract.ExprSwitchSimple(p[1], p[2])

def p_switchStmt_Head(p):
    '''switchStmt_Head : simpleStmt SEMICOLON expression
                       | simpleStmt SEMICOLON
                       | expression'''
    if(len(p) == 4):
        p[0] = abstract.ExprSwitchHead1(p[1], p[2], p[3])
    elif(len(p) == 3):
        p[0] = abstract.ExprSwitchHead2(p[1], p[2])
    else:
        p[0] = abstract.ExprSwitchHead3(p[1])
    
def p_switchStmt_Body(p):
    '''switchStmt_Body : LCHAVES exprCaseClauseList RCHAVES
                       | LCHAVES RCHAVES'''
    if(len(p) == 4):
        p[0] = abstract.ExprSwitchBody1(p[1], p[2], p[3])
    else:
        p[0] = abstract.ExprSwitchBody2(p[1], p[2])

def p_exprCaseClauseList(p):
    '''exprCaseClauseList : exprCaseClause exprCaseClauseList
                          | exprCaseClause'''
    if(len(p) == 3):
        p[0] = abstract.CompoundCaseClause1(p[1], p[2])
    else:
        p[0] = abstract.CompoundCaseClause2(p[1])

def p_exprCaseClause(p):
    '''exprCaseClause : exprSwitchCase COLON statementList'''
    p[0] = abstract.ExprCase(p[1], p[2], p[3])

def p_exprSwitchCase(p):
    '''exprSwitchCase : CASE expressionList
                      | DEFAULT'''
    if(len(p) == 3):
        p[0] = abstract.CaseClauseExp(p[1], p[2])
    else:
        p[0] = abstract.CaseClause(p[1])

def p_forStmt(p):
    '''forStmt : FOR condition block
               | FOR forClause block
               | FOR rangeClause block
               | FOR block'''

    if(isinstance(p[2], abstract.Condition)):
        p[0] = abstract.StmtFor(p[1], p[2], p[3])
    elif(isinstance(p[2], abstract.ForClause)):
        p[0] = abstract.StmtForClause(p[1], p[2], p[3])
    elif(isinstance(p[2], abstract.RangeClause)):
        p[0] = abstract.StmtForRange(p[1], p[2], p[3])
    elif(isinstance(p[2], abstract.Block)):
        p[0] = abstract.StmtForBlock(p[1], p[2])
    
def p_condition(p):
    '''condition : expression'''
    p[0] = abstract.DefinirCondition(p[1])

def p_forClause(p):
    '''forClause : initPostStmt SEMICOLON condition SEMICOLON initPostStmt
                 | SEMICOLON condition SEMICOLON'''

    if(len(p) == 6):
        p[0] = abstract.ClassicFor(p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = abstract.ClassicFor2(p[1], p[2], p[3])    

def p_initPostStmt(p):
    '''initPostStmt : simpleStmt'''
    p[0] = abstract.StmtInitPost(p[1])

def p_rangeClause(p):
    '''rangeClause : RANGE expression
                   | expressionList ASSIGN RANGE expression
                   | identifierList ASSIGN RANGE expression''' ### Mudei da original :=
    if(len(p) == 3):
        p[0] = abstract.DefinirRange(p[1], p[2])
    elif(isinstance(p[1], abstract.ExpressionList)):
        p[0] = abstract.RangeExpList(p[1], p[2], p[3], p[4])
    elif(isinstance(p[1], abstract.IdentifierList)):
        p[0] = abstract.RangeIDList(p[1], p[2], p[3], p[4])
    
def p_constDecl(p):
    '''constDecl : CONST constSpec
                 | CONST LPAREN constSpecList RPAREN'''
    
    if(len(p) == 3):
        p[0] = abstract.SimpleConst(p[1], p[2])
    else:
        p[0] = abstract.CompConst(p[1], p[2], p[3], p[4])

def p_constSpecList(p):
    '''constSpecList : constSpec SEMICOLON
                     | constSpec SEMICOLON constSpecList'''
    
    if(len(p) == 3):
        p[0] = abstract.CallConstSpec(p[1], p[2])
    else:
        p[0] = abstract.CompoundConstSpec(p[1], p[2], p[3])

def p_constSpec(p):
    '''constSpec : identifierList
                 | identifierList ASSIGN expressionList
                 | identifierList type ASSIGN expressionList''' 

    if(len(p) == 2):
        p[0] = abstract.SimpleIdList(p[1])
    elif(len(p) == 4):
        p[0] = abstract.ListIdExp(p[1], p[2], p[3])
    else:
        p[0] = abstract.ListIdTypeExp(p[1], p[2], p[3], p[4])

def p_identifierList(p):
    '''identifierList : ID compIDList
                      | ID'''
    
    if(len(p) == 3):
        p[0] = abstract.DefinirIDList(p[1], p[2])
    else:
        p[0] = abstract.DefinirID(p[1])

def p_compIDList(p):
    '''compIDList : COMMA ID compIDList
                  | COMMA ID'''
    if(len(p) == 4):
        p[0] = abstract.CompoundIDList(p[1], p[2], p[3])
    else:
        p[0] = abstract.EndCompID(p[1], p[2])

def p_expressionList(p):
    '''expressionList : expression listExpr
                      | expression'''
    if(len(p) == 3):
        p[0] = abstract.CallExpList(p[1], p[2])
    else:
        p[0] = abstract.DefinirExpList(p[1])

def p_listExpr(p):
    '''listExpr : COMMA expression listExpr
                | COMMA expression'''
    if(len(p) == 4):
        p[0] = abstract.CompoundExpList(p[1], p[2], p[3])
    else:
        p[0] = abstract.SimpleExpList(p[1], p[2])

def p_typeDecl(p):
    '''typeDecl : TYPE typeSpec
                | TYPE LPAREN typeSpecList RPAREN'''
    if(len(p) == 2):
        p[0] = abstract.DefinirType(p[1], p[2])
    else:
        p[0] = abstract.CallTypeSpecList(p[1], p[2], p[3], p[4])

def p_typeSpecList(p):
    '''typeSpecList : typeSpec SEMICOLON typeSpecList
                    | typeSpec SEMICOLON'''
    if(len(p) == 4):
        p[0] = abstract.CompTypeSpecList(p[1], p[2], p[3])
    else:
        p[0] = abstract.EndCompTypeSpec(p[1], p[2])

def p_typeSpec(p):
    '''typeSpec : ID type'''
    p[0] = abstract.SpecType(p[1], p[2])

def p_varDecl(p):
    '''varDecl : VAR varSpec
               | VAR LPAREN varSpecList RPAREN'''
    if(len(p) == 3):
        p[0] = abstract.DefinirVar(p[1], p[2])
    else:
        p[0] = abstract.CompVar(p[1], p[2], p[3], p[4])

def p_varSpecList(p):
    '''varSpecList : varSpec SEMICOLON varSpecList
                   | varSpec SEMICOLON'''
    if(len(p) == 4):
        p[0] = abstract.CompoundVarSpec(p[1], p[2], p[3])
    else:
        p[0] = abstract.EndCompVarSpec(p[1], p[2])

def p_varSpec(p):
    '''varSpec : identifierList type
               | identifierList type ASSIGN expressionList
               | identifierList ASSIGN expressionList'''
    if(len(p) == 3):
        p[0] = abstract.SpecVar(p[1], p[2])
    elif(len(p) == 5):
        p[0] = abstract.ClassicVarSpec(p[1], p[2], p[3], p[4])
    elif(len(p) == 4):
        p[0] = abstract.SimpleVarSpec(p[1], p[2], p[3])

def p_callFunc(p):
    '''callFunc : ID LPAREN expressionList RPAREN'''
    p[0] = abstract.SimpleCallFunc(p[1], p[2], p[3], p[4])

def p_incDec(p):
    '''incDec : expression DPLUS
              | expression DMINUS'''
    if(p[2] == 'DPLUS'):
        p[0] = abstract.IncOp(p[1], p[2])
    elif(p[2] == 'DMINUS'):
        p[0] = abstract.DecOp(p[1], p[2])

def p_assignment(p):
    '''assignment : expressionList ASSIGN expressionList'''
    p[0] = abstract.AssignOp(p[1], p[2], p[3])

def p_shortVarDec(p):
    '''shortVarDec : identifierList ASSIGN expressionList'''#Era para ser :=
    p[0] = abstract.DeclShortVarDef(p[1], p[2], p[3])

def p_exp(p):
    '''expression : expression OR exp1
                  | exp1'''
    if(len(p) == 4):
        p[0] = abstract.ExpressionOR(p[1], p[2], p[3])
    else:
        p[0] = abstract.CallExp1(p[1])

def p_exp1(p):
    '''exp1 : exp1 AND exp2
            | exp2'''
    if(len(p) == 4):
        p[0] = abstract.ExpressionAND(p[1], p[2], p[3])
    else:
        p[0] = abstract.CallExp2(p[1])

def p_exp2(p):
    '''exp2 : exp2 EQUALS exp3
            | exp2 DIFERENTE exp3
            | exp2 LESS exp3
            | exp2 LESS_EQUAL exp3
            | exp2 GREATER exp3
            | exp2 GREATER_EQUAL exp3
            | exp3'''
    if(len(p) == 2):
        p[0] = abstract.CallExp3(p[1])
    elif(p[2] == 'EQUALS'):
        p[0] = abstract.ExpressionEquals(p[1], p[2], p[3])
    elif(p[2] == 'DIFERENTE'):
        p[0] = abstract.ExpressionDiferente(p[1], p[2], p[3])
    elif(p[2] == 'LESS'):
        p[0] = abstract.ExpressionLess(p[1], p[2], p[3])
    elif(p[2] == 'LESS_EQUAL'):
        p[0] = abstract.ExpressionLessEqual(p[1], p[2], p[3])
    elif(p[2] == 'GREATER'):
        p[0] = abstract.ExpressionGreater(p[1], p[2], p[3])
    elif(p[2] == 'GREATER_EQUAL'):
        p[0] = abstract.ExpressionGreaterEqual(p[1], p[2], p[3])

def p_exp3(p):
    '''exp3 : exp4 PLUS exp3
            | exp4 MINUS exp3
            | exp4 POT exp3
            | exp4'''
    if(len(p) == 2):
        p[0] = abstract.CallExp4(p[1])
    elif(p[2] == 'PLUS'):
        p[0] = abstract.ExpressionPlus(p[1], p[2], p[3])
    elif(p[2] == 'MINUS'):
        p[0] = abstract.ExpressionMinus(p[1], p[2], p[3])
    elif(p[2] == 'POT'):
        p[0] = abstract.ExpressionPot(p[1], p[2], p[3])

def p_exp4(p):
    '''exp4 : exp5 TIMES exp4
            | exp5 DIVIDE exp4
            | exp5 MOD exp4
            | exp5'''
    if(len(p) == 2):
        p[0] = abstract.CallExp5(p[1])
    elif(p[2] == 'TIMES'):
        p[0] = abstract.ExpressionTimes(p[1], p[2], p[3])
    elif(p[2] == 'DIVIDE'):
        p[0] = abstract.ExpressionDivide(p[1], p[2], p[3])
    elif(p[2] == 'MOD'):
        p[0] = abstract.ExpressionMod(p[1], p[2], p[3])

def p_exp5(p):
    '''exp5 : NUMBER
            | callFunc
            | ID
            | LPAREN expression RPAREN'''

    if(p[1] == 'NUMBER'):
        p[0] = abstract.ExpressionNumber(p[1])
    elif(isinstance(p[1], abstract.CallFunc)):
        p[0] = abstract.ExpressionCallFunc(p[1])
    elif(p[1] == 'ID'):
        p[0] = abstract.ExpressionID(p[1])
    elif(len(p) == 4):
        p[0] = abstract.ExpressionParens(p[1], p[2], p[3])
    
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

#Execute

parser = yacc.yacc()

result = parser.parse(debug=True)

visit = abstract.Visitor.Visitor()

print('\n')

result.accept(visit)

print('\n')