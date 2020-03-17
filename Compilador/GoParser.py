m_functionDecl(p):
    '''functionDecl : FUNC ID signature
                    | FUNC ID signature functionBody'''

m_signature(p):
    '''signature : parameters
                 | parameters result'''

m_result(p):
    '''result : type'''

m_type(p):
    '''type : INT
            | STRING