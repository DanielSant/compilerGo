import ply.yacc as yacc
import ply.lex as lex
from GoLex import tokens
import GoAbstract as abstract

def p_functionDecl(p):
    '''functionDecl : FUNC ID signature
                    | FUNC ID signature functionBody'''
    if (len(p) == 4):
        p[0] = abstract.DefinirFunc(p[1], p[2], p[3])
    else:
        p[0] = abstract.DefinirFuncBody(p[1], p[2], p[3], p[4])

def p_signature(p):
    '''signature : parameters
                 | parameters result'''
    if (len(p) == 2):
        p[0] = abstract.DefinirParams(p[1])
    else:
        p[0] = abstract.DefinirParamsT(p[1], p[2])

def p_result(p):
    '''result : type'''
    p[0] = abstract.DefinirTipo(p[1])

def p_type(p):
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

def p_parameters(p):
    '''parameters : LPAREN parameterList RPAREN
                  | LPAREN parameterList COMMA RPAREN 
                  | LPAREN RPAREN'''
    if (len(p) == 4):
        p[0] = abstract.Params(p[1], p[2], p[3])
    elif (len(p) == 5):
        p[0] = abstract.ParamsList(p[1], p[2], p[3], p[4])
    elif (len(p) == 3):
        p[0] = abstract.DefinirParamsParameters(p[1], p[2])

def p_parameterList(p):
    '''parameterList : parameterDecl parameterList2'''
    p[0] = abstract.DefinirParamDecl(p[1], p[2])

def p_parameterList2(p):
    '''parameterList2 : parameterDecl parameterDecList'''
    p[0] = abstract.CompoundParamDecl(p[1], p[2])

def p_parameterDecList(p):
    '''parameterDecList : COMMA parameterList2
                        | empty'''
    if (len(p) == 3):
        p[0] = abstract.DecParamComp(p[1], p[2])
    else:
        p[0] = p[1]

def p_parameterDecl(p):
    '''parameterDecl : identifierList TYPE
                     | TYPE'''
    if (len(p) == 3):
        p[0] = abstract.ParamIdDecl(p[1], p[2])
    else:
        p[0] = abstract.ParamDecl(p[1])

def p_functionBody(p):
    '''functionBody : block'''
    p[0] = abstract.DefinirBlock(p[1])

def p_block(p):
    '''block : LCHAVES statementList RCHAVES'''
    p[0] = abstract.DefinirStatementL(p[1], p[2], p[3])

def p_statementList(p):
    '''statementList : statement SEMICOLON statementList2'''
    p[0] = abstract.CompoundStatementList(p[1], p[2], p[3])

def p_statementList2(p):
    '''statementList2 : statementList
                      | empty'''

    if (isinstance(p[1], abstract.StatementList)):
        p[0] = abstract.CallBackStatementList(p[1])
    else:
        p[0] = p[1]

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

def p_declaration(p):
    '''declaration : constDecl
                   | typeDecl
                   | varDecl'''
    if (isinstance(p[1], abstract.ConstDecl)):
        p[0] = abstract.DeclConst(p[1])
    elif (isinstance(p[1], abstract.TypeDecl)):
        p[0] = abstract.DeclType(p[1])
    elif (isinstance(p[1], abstract.VarDecl)):
        p[0] = abstract.DeclVar(p[1])

def p_simpleStmt(p): # Verificar mudançar no arguments
    '''simpleStmt : empty
                  | ID arguments
                  | inc
                  | assignment
                  | shortVarDec'''
    if (isinstance(p[1], abstract.ConstDecl)):
        p[0] = p[1]
    elif (isinstance(p[1], abstract.Expression)):
        p[0] = abstract.StmtExpression(p[1])
    elif (isinstance(p[1], abstract.IncDec)):
        p[0] = abstract.StmtIncDec(p[1])
    elif (isinstance(p[1], abstract.Assignment)):
        p[0] = abstract.Assign(p[1])
    elif (isinstance(p[1], abstract.ShortVarDecl)):
        p[0] = abstract.DeclShortVar(p[1])

def p_returnStmt(p):
    '''returnStmt : RETURN expressionList
                  | RETURN'''
    if (len(p) == 3):
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
              | IF expression block ELSE block''' ###OBERVAÇÃO VERIFICAR SER ESTAR CORRETO A CONSTRUÇÃO
    if (len(p) == 4):
        p[0] = abstract.SimpleIf(p[1], p[2], p[3])
    elif (isinstance(p[5], abstract.IfStmt)):
        p[0] = abstract.CompIfElse(p[1], p[2], p[3], p[4], p[5])
    elif (isinstance(p[5], abstract.Block)):
        p[0] = abstract.IfElse(p[1], p[2], p[3], p[4], p[5]) 

def p_switchStmt(p):
    '''switchStmt : SWITCH simpleStmt SEMICOLON expression LCHAVES exprCaseClauseList RCHAVES
                  | SWITCH LCHAVES exprCaseClauseList RCHAVES
                  | SWITCH simpleStmt LCHAVES exprCaseClauseList RCHAVES
                  | SWITCH expression LCHAVES exprCaseClauseList RCHAVES'''
    if (len(p) == 8):
        p[0] = abstract.ExprSwitch(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    elif (len(p) == 5):
        p[0] = abstract.ExprSwitchNone(p[1], p[2], p[3], p[4])
    elif (isinstance(p[2], abstract.SimpleStmt)):
        p[0] = abstract.ExprSwitchSimple(p[1], p[2], p[3], p[4], p[5])
    elif (isinstance(p[2], abstract.Expression)):
        p[0] = abstract.ExprSwitchExp(p[1], p[2], p[3], p[4], p[5])

def p_exprCaseClauseList(p):
    '''exprCaseClauseList : exprCaseClause exprCaseClauseList
                          | empty'''
    if(len(p) == 3):
        p[0] = abstract.CompoundCaseClause(p[1], p[2])
    else:
        p[0] = p[1]

def p_empty(p): # Big observação
    '''empty :'''
    p[0] = None

def p_exprCaseClause(p):
    '''exprCaseClause : exprSwitchCase COLON statementList'''
    p[0] = abstract.ExprCase(p[1], p[2], p[3])

def p_exprSwitchCase(p):
    '''exprSwitchCase : CASE expressionList
                      | DEFAULT'''
    if (len(p) == 3):
        p[0] = abstract.CaseClauseExp(p[1], p[2])
    else:
        p[0] = abstract.CaseClause(p[1])

def p_forStmt(p):
    '''forStmt : FOR condition block
               | FOR forClause block
               | FOR rangeClause block
               | FOR block'''
    if (isinstance(p[2], abstract.Condition)):
        p[0] = abstract.StmtFor(p[1], p[2], p[3])
    elif (isinstance(p[2], abstract.ForClause)):
        p[0] = abstract.StmtForClause(p[1], p[2], p[3])
    elif (isinstance(p[2], abstract.RangeClause)):
        p[0] = abstract.StmtForRange(p[1], p[2], p[3])
    elif (len(p) == 3):
        p[0] = abstract.StmtForBlock(p[1], p[2])

def p_condition(p):
    '''condition : expression'''
    p[0] = abstract.DefinirCondition(p[1])

def p_forClause(p):
    '''forClause : initStmt SEMICOLON condition SEMICOLON postStmt
                 | initStmt SEMICOLON condition
                 | initStmt
                 | condition SEMICOLON postStmt
                 | condition
                 | initStmt SEMICOLON postStmt
                 | postStmt''' ###OBSERVA A CONSTRUÇÃO
    if (len(p) == 6):
        p[0] = abstract.ClassicFor(p[1], p[2], p[3], p[4], p[5])
    elif (isinstance(p[3], abstract.Condition) and len(p) == 4):
        p[0] = abstract.InCoFor(p[1], p[2], p[3])
    elif (isinstance(p[1], abstract.InitStmt) and len(p) == 2):
        p[0] = abstract.InitFor(p[1])
    elif (isinstance(p[1], abstract.Condition) and len(p) == 4):
        p[0] = abstract.CoPoFor(p[1], p[2], p[3])
    elif (isinstance(p[1], abstract.Condition) and len(p) == 2):
        p[0] = abstract.ConditionFor(p[1])
    elif (isinstance(p[3], abstract.PostStmt) and len(p) == 4):
        p[0] = abstract.InPoFor(p[1], p[2], p[3])
    elif (isinstance(p[1], abstract.PostStmt)):
        p[0] = abstract.PostFor(p[1])

def p_initStmt(p):
    '''initStmt : simpleStmt'''
    p[0] = abstract.StmtInit(p[1])

def p_postStmt(p):
    '''postStmt : simpleStmt'''
    p[0] = abstract.StmtPost(p[1])

def p_rangeClause(p):
    '''rangeClause : RANGE expression
                  | expressionList ASSIGN RANGE expression
                  | identifierList ASSIGN RANGE expression''' ### Mudei da original :=
    if (len(p) == 2):
        p[0] = abstract.DefinirRange(p[1], p[2])
    elif (isinstance(p[1], abstract.ExpressionList)):
        p[0] = abstract.RangeExpList(p[1], p[2], p[3], p[4])
    elif (isinstance(p[1], abstract.IdentifierList)):
        p[0] = abstract.visitRangIDList(p[1], p[2], p[3], p[4])

def p_constDecl(p):
    '''constDecl : CONST constSpec
                 | CONST LPAREN constSpecList RPAREN'''
    if (len(p) == 3):
        p[0] = abstract.SimpleConst(p[1], p[2])
    else:
        p[0] = abstract.CompConst(p[1], p[2], p[3], p[4])

def p_constSpecList(p):
    '''constSpecList : constSpec SEMICOLON constSpecList
                     | empty'''
    if(len(p) == 4):
        p[0] = abstract.CompoundConstSpec(p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_constSpec(p): # Cabe mudanças para melhorar
    '''constSpec : identifierList
                 | identifierList ASSIGN expressionList
                 | identifierList type ASSIGN expressionList''' ###Verificar ser estar correta 
    if (len(p) == 2):
        p[0] = abstract.SimpleIdList(p[1])
    elif (len(p) == 4):
        p[0] = abstract.ListIdExp(p[1], p[2], p[3])
    elif (len(p) == 5):
        p[0] = abstract.ListIdTypeExp(p[1], p[2], p[3], p[4])

def p_identifierList(p):
    '''identifierList : ID
                      | ID compIDList'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = abstract.DefinirIDList(p[1], p[2])

def p_compIDList(p):
    '''compIDList : COMMA ID compIDList2'''
    p[0] = abstract.CompoundIDList(p[1], p[2], p[3])

def p_compIDList2(p):
    '''compIDList2 : compIDList
                   | empty'''
    if (isinstance(p[1], abstract.CompIDList)):
        p[0] = abstract.CallBackCompID(p[1])
    else:
        p[0] = p[1]

def p_expressionList(p):
    '''expressionList : expression listExpr'''

def p_listExpr(p):
    '''listExpr : COMMA expression listExpr
                | empty'''

def p_typeDecl(p):
    '''typeDecl : TYPE typeSpec
                | TYPE LPAREN typeSpecList RPAREN'''
    if (len(p) == 3):
        p[0] = abstract.DefinirType(p[1], p[2])
    else:
        p[0] = abstract.CallTypeSpecList(p[1], p[2], p[3], p[4])

def p_typeSpecList(p):
    '''typeSpecList : typeSpec SEMICOLON typeSpecList
                    | empty'''
    

def p_typeSpec(p):
    '''typeSpec : ID type'''
    p[0] = abstract.SpecType(p[1], p[2])

def p_varDecl(p):
    '''varDecl : VAR varSpec
               | VAR LPAREN varSpecList RPAREN'''
    if (len(p) == 3):
        p[0] = abstract.DefinirVar(p[1], p[2])
    else:
        p[0] = abstract.CompVar(p[1], p[2], p[3], p[4])

def p_varSpecList(p):
    '''varSpecList : varSpec SEMICOLON varSpecList
                   | empty'''
    

def p_varSpec(p):
    '''varSpec : identifierList type
               | identifierList type ASSIGN expressionList
               | identifierList ASSIGN expressionList'''
    if (len(p) == 3):
        p[0] = abstract.SpecVar(p[1], p[2])
    elif (len(p) == 5):
        p[0] = abstract.ClassicVarSpec(p[1], p[2], p[3], p[4])
    else:
        p[0] = abstract.SimpleVarSpec(p[1], p[2], p[3])



def p_exp(p):
    '''exp : exp OR exp1
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
    '''exp3 : exp3 PLUS exp4
            | exp3 MINUS exp4
            | exp3 POT exp4
            | exp4'''

def p_exp4(p):
    '''exp4 : exp4 TIMES exp5
            | exp4 DIVIDE exp5
            | exp4 MOD exp5
            | exp5'''

def p_exp5(p):
    '''exp5 : arguments
            | assigment
            | Number
            | ID'''

def p_arguments(p): # Implementar
    '''arguments : ID ExpressionList
                 | exp'''



def p_inc(p):
    '''inc : expression PLUS PLUS
           | expression MINUS MINUS'''
    if (p[2] == 'PLUS'):
        p[0] = abstract.IncOp(p[1], p[2], p[3])
    else:
        p[0] = abstract.DecOp(p[1], p[2], p[3])

def p_assignment(p):
    '''assignment : expressionList ASSIGN exp'''
    p[0] = abstract.AssignOp(p[1], p[2], p[3])

def p_shortVarDec(p):
    '''shortVarDec : identifierList ASSIGN expressionList'''#Era para ser :=
    p[0] = abstract.DeclShortVar(p[1], p[2], p[3])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

#Execute

parser = yacc.yacc(debug=True)

result = parser.parse(debug=True)

visit = abstract.Visitor.Visitor()

print('\n')

result.accept(visit)

print('\n')