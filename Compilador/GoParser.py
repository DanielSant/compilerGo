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
    '''parameters : LPAREN parameterList COMMA RPAREN''' 

def m_parameterList(p):
    '''parameterList : parameterDecl COMMA parameterDecl'''

def m_parameterDecl(p):
