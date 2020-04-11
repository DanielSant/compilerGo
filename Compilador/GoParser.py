import ply.yacc as yacc
import ply.lex as lex
from GoLex import tokens
import GoAbstract as abstract

def m_functionDecl(p):
    '''functionDecl : FUNC ID signature
                    | FUNC ID signature functionBody'''
    if (len(p) == 4):
        p[0] = abstract.DefinirFunc(p[1], p[2], p[3])
    else:
        p[0] = abstract.DefinirFuncBody(p[1], p[2], p[3], p[4])

def m_signature(p):
    '''signature : parameters
                 | parameters result'''
    if (len(p) == 2):
        p[0] = abstract.DefinirParams(p[1])
    else:
        p[0] = abstract.DefinirParamsT(p[1], p[2])

def m_result(p):
    '''result : type'''
    p[0] = abstract.DefinirTipo(p[1])

def m_type(p):
    '''type : INT
            | STRING
            | BOOL
            | BYTE
            | FLOAT'''
    if ('INT'):
        p[0] = abstract.Tint(p[1])
    elif ('STRING'):
        p[0] = abstract.Tstring(p[1])
    elif ('BOOL'):
        p[0] = abstract.Tbool(p[1])
    elif ('BYTE'):
        p[0] = abstract.Tbyte(p[1])
    elif ('FLOAT'):
        p[0] = abstract.Tfloat(p[1])

def m_parameters(p):
    '''parameters : LPAREN parameterList RPAREN
                  | LPAREN parameterList COMMA RPAREN 
                  | LPAREN RPAREN'''
    if (len(p) == 4):
        p[0] = abstract.Params(p[1], p[2], p[3])
    elif (len(p) == 5):
        p[0] = abstract.ParamsList(p[1], p[2], p[3], p[4])
    elif (len(p) == 3):
        p[0] = abstract.DefinirParamsParameters(p[1], p[2])

def m_parameterList(p):
    '''parameterList : parameterDecl
                     | parameterDecl parameterDecList'''
    if (len(p) == 2):
        p[0] = abstract.DefinirParamDecl(p[1])
    else:
        p[0] = abstract.CompoundParamDecl(p[1], p[2])

def m_paramterDecList(p):
    '''parameterDecList : COMMA parameterDecl
                        | COMMA parameterDecl parameterDecList'''
    if (len(p) == 3):
        p[0] = abstract.DecParamComp(p[1], p[2])
    else:
        p[0] = abstract.DecListCompound(p[1], p[2], p[3])

def m_parameterDecl(p):
    '''parameterDecl : identifierList TYPE
                     | TYPE'''
    if (len(p) == 3):
        p[0] = abstract.ParamIdDecl(p[1], p[2])
    else:
        p[0] = abstract.ParamDecl(p[1])

def m_functionBody(p):
    '''functionBody : block'''
    p[0] = abstract.DefinirBlock(p[1])

def m_block(p):
    '''block : LCHAVES statementList RCHAVES'''
    p[0] = abstract.DefinirStatementL(p[1], p[2], p[3])

def m_statementList(p):
    '''statementList : statement SEMICOLON
                     | statement SEMICOLON statementList'''
    if (len(p) == 3):
        p[0] = abstract.DefinirStatement(p[1], p[2])
    else:
        p[0] = abstract.CompoundStatementList(p[1], p[2], p[3])

def m_statement(p):
    '''statementList : declaration
                     | simpleStmt
                     | returnStmt
                     | breakStmt
                     | continueStmt
                     | block
                     | ifStmt
                     | switchStmt
                     | forStmt'''
    if (isinstance(p[1], abstract.Declaration)):
        p[0] = abstract.StmtDeclaration(p[1])
    elif (isinstance(p[1], abstract.SimpleStmt)):
        p[0] = abstract.StmtSimple(p[1])
    elif (isinstance(p[1], abstract.ReturnStmt)):
        p[0] = abstract.StmtReturn(p[1])
    elif (isinstance(p[1], abstract.BreakStm)):
        p[0] = abstract.StmtBreak(p[1])
    elif (isinstance(p[1], abstract.ContinueStmt)):
        p[0] = abstract.StmtContinue(p[1])
    elif (isinstance(p[1], abstract.Block)):
        p[0] = abstract.StmtBlock(p[1])
    elif (isinstance(p[1], abstract.IfStmt)):
        p[0] = abstract.StmtIf(p[1])
    elif (isinstance(p[1], abstract.SwitchStmt)):
        p[0] = abstract.StmtSwitch(p[1])
    elif (isinstance(p[1], abstract.ForStmt)):
        p[0] = abstract.StmtFor(p[1])

def m_declaration(p):
    '''declaration : constDecl
                   | typeDecl
                   | varDecl'''
    if (isinstance(p[1], abstract.ConstDecl)):
        p[0] = abstract.DeclConst(p[1])
    elif (isinstance(p[1], abstract.TypeDecl)):
        p[0] = abstract.DeclType(p[1])
    elif (isinstance(p[1], abstract.VarDecl)):
        p[0] = abstract.DeclVar(p[1])

def m_simpleStmt(p):
    '''simpleStmt : empty
                  | expression
                  | incDec
                  | assignment
                  | shortVarDecl'''
    if (isinstance(p[1], abstract.ConstDecl)):
        p[0] = abstract.StmtEmpty(p[1])
    elif (isinstance(p[1], abstract.Expression)):
        p[0] = abstract.StmtExpression(p[1])
    elif (isinstance(p[1], abstract.IncDec)):
        p[0] = abstract.StmtIncDec(p[1])
    elif (isinstance(p[1], abstract.Assignment)):
        p[0] = abstract.Assign(p[1])
    elif (isinstance(p[1], abstract.ShortVarDecl)):
        p[0] = abstract.DeclShortVar(p[1])

def m_returnStmt(p):
    '''returnStmt : RETURN expressionList
                  | RETUNR'''
    if (len(p) == 3):
        p[0] = abstract.ExpReturn(p[1], p[2])
    else:
        p[0] = abstract.SimpleReturn(p[1])

def m_breakStmt(p):
    '''breakStmt : BREAK'''
    p[0] = abstract.StmtBreak(p[1])

def m_continueStmt(p):
    '''continueStmt : CONTINUE'''
    p[0] = abstract.StmtContinue(p[1])

def m_ifStmt(p):
    '''ifStmt : IF expression block
              | IF expression block ELSE ifStmt
              | IF expression block ELSE block''' ###OBERVAÇÃO VERIFICAR SER ESTAR CORRETO A CONSTRUÇÃO
    if (len(p) == 4):
        p[0] = abstract.SimpleIf(p[1], p[2], p[3])
    elif (isinstance(p[5], abstract.IfStmt)):
        p[0] = abstract.CompIfElse(p[1], p[2], p[3], p[4], p[5])
    elif (isinstance(p[5], abstract.Block)):
        p[0] = abstract.IfElse(p[1], p[2], p[3], p[4], p[5]) 

def m_switchStmt(p):
    '''switchStmt : SWITCH simpleStmt SEMICOLON expression LCHAVES exprCaseClauseList RCHAVES
                  | SWITCH LCHAVES exprCaseClauseList RCHAVES
                  | SWITCH simpleStmt LCHAVES exprCaseClauseList RCHAVES
                  | SWITCH expression LCHAVES exprCaseClauseList RCHAVES'''
    if (len(p) == 8):
        p[0] = abstract.

def m_exprCaseClauseList(p):
    '''exprCaseClauseList : exprCaseClause
                          | exprCaseClause ExprCaseClauseList
                          | empty'''
def m_empty(p):
    '''empty :'''
    pass

def m_exprCaseClause(p):
    '''exprCaseClause : exprSwitchCase COLON statementList'''

def m_exprSwitchCase(p):
    '''exprSwitchCase : CASE expressionList
                      | DEFAULT'''

def m_forStmt(p):
    '''forStmt : FOR condition block
               | FOR forClause block
               | FOR rangeClause block
               | FOR block'''

def m_condition(p):
    '''condition : expresison'''

def m_forClause(p):
    '''forClause : initStmt SEMICOLON condition SEMICOLON postStmt
                 | initStmt SEMICOLON condition
                 | initStmt
                 | condition SEMICOLON postStmt
                 | condition
                 | initStmt SEMICOLON postStmt
                 | postStmt''' ###OBSERVA A CONSTRUÇÃO

def m_initStmt(p):
    '''initStmt : simpleStmt'''

def m_postStmt(p):
    '''postStmt : simpleStmt'''

def m_rangeClause(p):
    '''rangeClaus : RANGE expression
                  | expressionList ASSIGN RANGE expression
                  | identifierList ASSIGN RANGE expression''' ### Mudei da original :=

def m_constDecl(p):
    '''constDecl : CONST constSpec
                 | CONST LPAREN constSpecList RPAREN'''

def m_constSpecList(p):
    '''constSpecList : constSpec SEMICOLON
                     | constSpec SEMICOLON constSpecList'''

def m_constSpec(p):
    '''constSpec : identifierList
                 | identifierList ASSIGN expressionList
                 | identifierList type ASSIGN expressionList''' ###Verificar ser estar correta 


def m_identifierList(p):
    '''identifierList : ID compIDList'''

def m_compIDList(p):
    '''compIDList : COMMA ID
                  | COMMA ID compIDList
                  | empty'''

def m_expressionList(p):
    '''expressionList : expression 
                      | expression listExpr'''

def m_listExpr(p):
    '''listExpr : COMMA expression
                | COMMA expression listExpr'''


def m_typeDecl(p):
    '''typeDecl : TYPE typeSpec
                | TYPE LPAREN typeSpecList RPAREN'''

def m_typeSpecList(p):
    '''typeSpecList : typeSpec SEMICOLON
                    | typeSpec SEMICOLON typeSpecList
                    | empty'''

def m_typeSpec(p):
    '''typeSpec : ID type'''

def m_varDecl(p):
    '''varDecl : VAR varSpec
               | VAR LPAREN varSpecList RPAREN'''

def m_varSpecList(p):
    '''varSpecList : varSpec SEMICOLON
                   | varSpec SEMICOLON varSpecList
                   | empty'''

def m_varSpec(p):
    '''varSpec : identifierList type
               | identifierList type ASSIGN expressionList
               | identifierList ASSIGN expressionList''''

def m_expression(p):
    '''expression : unaryExpr
                  | expression binary_op expression'''

def m_unaryExpr(p):
    '''unaryExpr : NUMBER
                 | ID
                 | LPAREN expression RPAREN''' #Talvez teremos que modificar

def m_binary_op(p):
    '''binary_op : OR
                 | AND
                 | rel_op  
                 | add_op
                 | mul_op'''

def m_rel_op(p):
    '''rel_op : EQUALS
              | DIFERENTE
              | LESS
              | LESS_EQUAL
              | GREATER
              | GREATER_EQUAL'''

def m_add_op(p):
    '''add_op : PLUS
              | MINUS'''

def m_mul_op(p):
    '''mul_op : TIMES
              | DIVIDE
              | MOD'''              

def m_inc(p):
    '''inc : expression PLUS PLUS
           | expression MINUS MINUS'''

def m_assignment(p):
    '''assignment : expressionList ASSIGN expressionList'''

def m_shortVarDec(p):
    '''shortVarDec : identifierLis ASSIGN expressionList'''#Era para ser :=
