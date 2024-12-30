import ply.lex as lex
import sys

literals = [';' , '=', '<', '>','(',')',',','!','+','-','*','/']

tokens = (
    'NUM',
    'TEXTO',
    'VAR'
)

def get_lexer():
    def t_TEXTO(t):
        r'\"[^"]*\"'
        return t

        
    def t_NUM(t):
        r'[0-9]+'
        #t.value = int(t.value) 
        return t
        
    def t_VAR(t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        return t
    
    t_ignore = ' \n\t'

    def t_error(t):
        print('Illegal character: ', t.value[0])
        t.lexer.skip(1)

    return lex.lex()
