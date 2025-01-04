import ply.lex as lex
import sys

literals = [';' , '=',',']

tokens = (
    # Tipos da linguagem
    'NUM', 'TEXTO', 'VAR', 'chamada',

    #declarações
    'DECINTEIRO', 'def',

    # Funções
    'se', 'enquanto', 'faz', 'ler', 'escreva', 'entao', 'fim', 'senaose', 'senao', 'retorna',

    # Operações Lógicas
    'e', 'ou', 'maior', 'maior_igual', 'menor', 'menor_igual', 'igual', 'diferente', 'E_parentese', 'D_parentese',

    # Operações Aritiméticas
    'soma', 'subtracao', 'multiplicacao', 'divisao', 'mod'
)


    # Declarações
def t_DECINTEIRO(t):
    r'inteiro'
    return t

    # Tipos
def t_TEXTO(t):
    r'\"[^"]*\"'
    return t
    

    # Funções


def t_enquanto(t):
    r'enquanto'
    return t

def t_faz(t):
    r'faz'
    return t

def t_ler(t):
    r'ler'
    return t

def t_escreva(t):
    r'escreva'
    return t

def t_senaose(t):
    r'senaose'
    return t

def t_senao(t):
    r'senao'
    return t

def t_se(t):
    r'se'
    return t

def t_entao(t):
    r'entao'
    return t

def t_fim(t):
    r'fim'
    return t

def t_retorna(t):
    r'retorna'
    return t

def t_def(t):
    r'def'
    return t

    #Operações Lógicas

def t_e(t):
    r'e'
    return t

def t_ou(t):
    r'ou'
    return t

t_maior = r'>'
t_maior_igual = r'>='
t_menor = r'<'
t_menor_igual = r'<='
t_igual = r'=='
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

def t_mod(t):
    r'%'
    return t

def t_chamada(t):
    r'[a-zA-Z][a-zA-Z0-9]*\(\)'
    return t

def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_NUM(t):
    r'-?[0-9]+'
    return t

t_ignore = ' \n\t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()

#if __name__ == "__main__":
#    with open(f'.\\TP2\\Programas\\menoresque.vbr', "r") as f:
#        data = f.read()
#    lexer.input(data)
#    for token in lexer:
#        print(token)

