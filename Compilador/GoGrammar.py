import ply.yacc as yacc
import ply.lex as lex
from GoLex import tokens
import GoAbstract as abstract

# precedence = (
#     ('left', 'AND', 'OR'),
#     ('nonassoc', 'LCHAVES', 'RCHAVES', 'COMMA', 'EQUALS', 'DIFERENTE', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL'),
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
#     ('left', 'MOD')
# )

def p_functionDecl(p):
    '''functionDecl : FUNC ID signature
                    | FUNC ID signature functionBody'''

def p_signature(p):
    '''signature : parameters
                 | parameters result'''

def p_result(p):
    '''result : type'''

def p_type(p):
    '''type : INT
            | STRING
            | BOOL
            | BYTE
            | FLOAT'''

#| LPAREN parameterList COMMA RPAREN
def p_parameters(p):
    '''parameters : LPAREN parameterList RPAREN
                  | LPAREN RPAREN'''

def p_parameterList(p):
    '''parameterList : parameterDecl parameterList_Mul
                     | parameterDecl'''

def p_parameterList_Mul(p):
    '''parameterList_Mul : COMMA parameterDecl parameterList_Mul
                         | COMMA parameterDecl'''

def p_parameterDecl(p):
    '''parameterDecl : identifierList type
                     | type'''

def p_functionBody(p):
    '''functionBody : block'''

def p_block(p):
    '''block : LCHAVES statementList RCHAVES'''

def p_statementList(p):
    '''statementList : statement SEMICOLON
                     | statement SEMICOLON statementList'''

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
              | IF expression block ELSE block''' ###OBERVAÇÃO VERIFICAR SER ESTAR CORRETO A CONSTRUÇÃO

def p_switchStmt(p):
    '''switchStmt : SWITCH switchStmt_Head switchStmt_Body
      | SWITCH switchStmt_Body
    '''

def p_switchStmt_Head(p):
  '''
    switchStmt_Head : simpleStmt SEMICOLON expression
      | simpleStmt SEMICOLON
      | expression
  '''
    
def p_switchStmt_Body(p):
  '''
    switchStmt_Body : LCHAVES exprCaseClauseList RCHAVES
      | LCHAVES RCHAVES
  '''

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
    '''forClause : initStmt SEMICOLON condition SEMICOLON postStmt
                 | initStmt
                 | initStmt SEMICOLON postStmt'''

def p_initStmt(p):
    '''initStmt : postStmt'''

def p_postStmt(p):
    '''postStmt : simpleStmt'''

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
                      | ID
    '''

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

# def p_expression(p):
#     '''expression : unaryExpr
#                   | expression binary_op expression'''

# def p_unaryExpr(p):
#     '''unaryExpr : NUMBER
#                  | ID arguments
#                  | LPAREN expression RPAREN''' #Talvez teremos que modificar

def p_arguments(p): # Não precisa de abstrata e concreta?
    '''arguments : parameters'''

# def p_binary_op(p):
#     '''binary_op : OR
#                  | AND
#                  | rel_op  
#                  | add_op
#                  | mul_op'''

# def p_rel_op(p):
#     '''rel_op : EQUALS
#               | DIFERENTE
#               | LESS
#               | LESS_EQUAL
#               | GREATER
#               | GREATER_EQUAL'''

# def p_add_op(p):
#     '''add_op : PLUS
#               | MINUS'''

# def p_mul_op(p):
#     '''mul_op : TIMES
#               | DIVIDE
#               | MOD'''

def p_incDec(p):
    '''incDec : expression PLUS PLUS
           | expression MINUS MINUS'''

def p_assignment(p):
    '''assignment : expressionList ASSIGN expressionList'''
def p_shortVarDec(p):
    '''shortVarDec : identifierList ASSIGN expressionList'''#Era para ser :=
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

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
            | ID arguments
            | LPAREN expression RPAREN'''

#Execute

parser = yacc.yacc()

result = parser.parse(debug=True)

#visit = abstract.Visitor.Visitor()

print('\n')

#result.accept(visit)

print('\n')