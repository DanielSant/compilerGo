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
        p[0] = abstract.StmtFor(p[1])

def p_declaration(p):
    '''declaration : constDecl
                   | typeDecl
                   | varDecl'''

def p_simpleStmt(p): #condition vai para expression
    '''simpleStmt : condition
                  | incDec
                  | assignment
                  | shortVarDec'''

def p_returnStmt(p):
    '''returnStmt : RETURN expressionList
                  | RETURN'''

def p_breakStmt(p):
    '''breakStmt : BREAK'''

def p_continueStmt(p):
    '''continueStmt : CONTINUE'''

def p_ifStmt(p):
    '''ifStmt : IF expression block
              | IF expression block ELSE ifStmt
              | IF expression block ELSE block'''

def p_switchStmt(p):
    '''switchStmt : SWITCH switchStmt_Head switchStmt_Body
                  | SWITCH switchStmt_Body'''

def p_switchStmt_Head(p):
    '''switchStmt_Head : simpleStmt SEMICOLON expression
                       | simpleStmt SEMICOLON
                       | expression'''
    
def p_switchStmt_Body(p):
    '''switchStmt_Body : LCHAVES exprCaseClauseList RCHAVES
                       | LCHAVES RCHAVES'''

def p_exprCaseClauseList(p):
    '''exprCaseClauseList : exprCaseClause exprCaseClauseList
                          | exprCaseClause'''

def p_exprCaseClause(p):
    '''exprCaseClause : exprSwitchCase COLON statementList'''

def p_exprSwitchCase(p):
    '''exprSwitchCase : CASE expressionList
                      | DEFAULT'''

def p_forStmt(p):
    '''forStmt : FOR condition block
               | FOR forClause block
               | FOR rangeClause block
               | FOR block'''

def p_condition(p):
    '''condition : expression'''

def p_forClause(p):
    '''forClause : initPostStmt SEMICOLON condition SEMICOLON initPostStmt
                 | SEMICOLON condition SEMICOLON'''

def p_initPostStmt(p):
    '''initPostStmt : simpleStmt'''

def p_rangeClause(p):
    '''rangeClause : RANGE expression
                  | expressionList ASSIGN RANGE expression
                  | identifierList ASSIGN RANGE expression''' ### Mudei da original :=

def p_constDecl(p):
    '''constDecl : CONST constSpec
                 | CONST LPAREN constSpecList RPAREN'''

def p_constSpecList(p):
    '''constSpecList : constSpec SEMICOLON
                     | constSpec SEMICOLON constSpecList'''

def p_constSpec(p):
    '''constSpec : identifierList
                 | identifierList ASSIGN expressionList
                 | identifierList type ASSIGN expressionList''' 

def p_identifierList(p):
    '''identifierList : ID compIDList
                      | ID'''

def p_compIDList(p):
    '''compIDList : COMMA ID compIDList
                  | COMMA ID'''

def p_expressionList(p):
    '''expressionList : expression listExpr
                      | expression'''

def p_listExpr(p):
    '''listExpr : COMMA expression listExpr
                | COMMA expression'''

def p_typeDecl(p):
    '''typeDecl : TYPE typeSpec
                | TYPE LPAREN typeSpecList RPAREN'''

def p_typeSpecList(p):
    '''typeSpecList : typeSpec SEMICOLON typeSpecList
                    | typeSpec SEMICOLON'''

def p_typeSpec(p):
    '''typeSpec : ID type'''

def p_varDecl(p):
    '''varDecl : VAR varSpec
               | VAR LPAREN varSpecList RPAREN'''

def p_varSpecList(p):
    '''varSpecList : varSpec SEMICOLON varSpecList
                   | varSpec SEMICOLON'''

def p_varSpec(p):
    '''varSpec : identifierList type
               | identifierList type ASSIGN expressionList
               | identifierList ASSIGN expressionList'''

def p_callFunc(p):
    '''callFunc : ID LPAREN expressionList RPAREN'''

def p_incDec(p):
    '''incDec : expression DPLUS
              | expression DMINUS'''

def p_assignment(p):
    '''assignment : expressionList ASSIGN expressionList'''

def p_shortVarDec(p):
    '''shortVarDec : identifierList ASSIGN expressionList'''#Era para ser :=

def p_exp(p):
    '''expression : expression OR exp1
                  | exp1'''

def p_exp1(p):
    '''exp1 : exp1 AND exp2
            | exp2'''

def p_exp2(p):
    '''exp2 : exp2 EQUALS exp3
            | exp2 DIFERENTE exp3
            | exp2 LESS exp3
            | exp2 LESS_EQUAL exp3
            | exp2 GREATER exp3
            | exp2 GREATER_EQUAL exp3
            | exp3'''

def p_exp3(p):
    '''exp3 : exp4 PLUS exp3
            | exp4 MINUS exp3
            | exp4 POT exp3
            | exp4'''

def p_exp4(p):
    '''exp4 : exp5 TIMES exp4
            | exp5 DIVIDE exp4
            | exp5 MOD exp4
            | exp5'''

def p_exp5(p):
    '''exp5 : NUMBER
            | callFunc
            | ID
            | LPAREN expression RPAREN'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

#Execute

parser = yacc.yacc()

result = parser.parse(debug=True)

#visit = abstract.Visitor.Visitor()

print('\n')

#result.accept(visit)

print('\n')