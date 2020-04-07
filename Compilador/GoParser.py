def m_functionDecl(p):
    '''functionDecl : FUNC ID signature
                    | FUNC ID signature functionBody'''

def m_signature(p):
    '''signature : parameters
                 | parameters result'''

def m_result(p):
    '''result : type'''

def m_type(p):
    '''type : INT
            | STRING
            | BOOL
            | BYTE
            | FLOAT'''

def m_parameters(p):
    '''parameters : LPAREN parameterList RPAREN
                  | LPAREN parameterList COMMA RPAREN 
                  | LPAREN RPAREN''' 

def m_parameterList(p):
    '''parameterList : parameterDecl
                     | parameterDecl parameterDecList '''

def m_paramterDecList(p):
    '''parameterDecList : COMMA parameterDecl
                        | COMMA parameterDecl parameterDecList'''

def m_parameterDecl(p):
    '''parameterDecl : identifier TYPE'''

def m_functionBody(p):
    '''functionBody : block'''

def m_block(p):
    '''block : LCHAVES statementList RCHAVES'''

def m_statementList(p):
    '''statementList : declaration
                     | simpleStmt
                     | returnStmt
                     | breakStmt
                     | continueStmt
                     | block  
                     | ifStmt
                     | switchStmt
                     | forStmt'''

def m_declaration(p):
    '''declaration : constDecl
                   | typeDecl
                   | varDecl'''

def m_simpleStmt(p):
    '''simpleStmt : empty
                  | expression
                  | incDec
                  | assignment
                  | shortVarDecl'''

def m_returnStmt(p):
    '''returnStmt : RETURN expressionList'''

def m_breakStmt(p):
    '''breakStmt : BREAK'''

def m_continueStmt(p):
    '''continueStmt : CONTINUE'''

def m_ifStmt(p):
    '''ifStmt : IF expressionBlock ELSE if ifStmt
              | IF expressionBlock ELSE if block ''' ###OBERVAÇÃO VERIFICAR SER ESTAR CORRETO A CONSTRUÇÃO

def m_switchStmt(p):
    '''switchStmt : SWITCH simpleStmt SEMICOLON expression LCHAVES exprCaseClause RCHAVES'''

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
                 | CONST LPAREN constSpec SEMICOLON RPAREN'''

def m_constSpec(p):
    '''constSpec : identifierList
                 | identifierList ASSIGN expressionList
                 | identifierList type ASSIGN expressionList''' ###Verificar ser estar correta 

def m_identifierList(p):
    '''identifierList : ID COMMA ID'''

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

def m_spec(p):
    '''spec : identifierList type
            | identifierList type ASSIGN expressionList
            | identifierList ASSIGN expressionList''''

def m_expression(p):
    '''expression : unaryExpr
                  | expression binary_op expression'''

def m_unaryExpr(p):
    '''unaryExpr : Number
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
              | LELESS_EQUAL
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
