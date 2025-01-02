import ply.lex as lex
import sys

literals = [';' , '=', '<', '>','(',')',',','!','+','-','*','/']

tokens = (
    # Tipos da linguagem
    'NUM', 'TEXTO', 'VAR',

    #declarações
    'inteiro',

    # Funções
    'se', 'enquanto', 'ler', 'escreva', 'entao', 'fim', 'senao_se', 'senao',

    # Operações Lógicas
    'e', 'ou', 'nao', 'maior', 'maior_igual', 'menor', 'menor_igual', 'igual', 'diferente', 'E_parentese', 'D_parentese'

    # Operações Aritiméticas
    'soma', 'subtracao', 'multiplicacao', 'divisao'
)

    # Tipos
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

    # Declarações

def t_inteiro(t):
    r'inteiro'
    return t

    # Funções

def t_se(t):
    r'se'
    return t

def t_enquanto(t):
    r'enquanto'
    return t

def t_ler(t):
    r'ler'
    return t

def t_escreva(t):
    r'escreva'
    return t

def t_senao_se(t):
    r'senao se'
    return t

def t_senao(t):
    r'senao'
    return t

def t_entao(t):
    r'entao'
    return t

def t_fim(t):
    r'fim'
    return t

    #Operações Lógicas

def t_e(t):
    r'e'
    return t

def t_ou(t):
    r'ou'
    return t

def t_nao(t):
    r'nao'
    return t

t_maior = r'>'
t_maior_igual = r'>='
t_menor = r'<'
t_menor_igual = r'<='
t_igual = r'='
t_diferente = r'!='
    
def t_E_parentese(t):
    r'\('
    return t

def t_D_parentese(t):
    r'\)'
    return t


    # Operações Aritiméticas

def t_soma(t):
    r'\+'
    return t

def t_subtracao(t):
    r'\-'
    return t

def t_multiplicacao(t):
    r'\*'
    return t

def t_divisao(t):
    r'\/'
    return t


t_ignore = ' \n\t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
