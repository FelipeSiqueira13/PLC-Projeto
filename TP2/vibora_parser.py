import ply.yacc as yacc
import sys

from vibora_lex import tokens
def get_parser():
    def p_programa(p):
        f'programa : declaracoes linhas'

    def p_declaracoes(p):
        f'declaracoes : declaracao'

    def p_declaracoes2(p):
        f'declaracoes : declaracoes declaracao'

    def p_declaracao(p):
        f'declaracao : "inteiro" VAR ;'

    def p_decaracao2(p):
        f'declaracao : "inteiro" atribuicao'

    def p_linhas(p):
        f'linhas : linha'

    def p_linhas2(p):
        f'linhas : linhas linha'

    def p_linha(p):
        f'linha : atribuicao'

    def p_linha2(p):
        f'linha : comando'

    def p_comando(p):
        f'comando : cescreva'

    def p_comando2(p):
        f'comando : cse '

    def p_comando3(p):
        f'comando : cenquanto'

    def p_comando4(p):
        f'comando : cler'

    def p_atribuicao(p):
        f'atribuicao : VAR "=" expressao ";" '

    def p_expressao(p):
        f'expressao : NUM '

    def p_expressao2(p):
        f'expressao : VAR '
    
    def p_expressao3(p):
        f'expressao : expressao "+" expressao '

    def p_expressao4(p):
        f'expressao : expressao "-" expressao'

    def p_expressao5(p):
        f'expressao : expressao "*" expressao'

    def p_expressao6(p):
        f'expressao : expressao "/" expressao '

    def p_expressao7(p):
        f'expressao :  "(" expressao ")'

    def p_cler(p):
        f'cler : VAR "=" "ler" ( TEXTO ) ";" '

    def p_cescreva(p):
        f'cescreva : "escreva" ( textvar ) ";" '

    def p_cse(p):
        f'cse : "se" ( condicoes ) "entao" linhas csezinho '

    def p_csezinho(p):
        f'csezinho : "senao se" ( condicoes ) "entao" linhas csezinho'

    def p_csezinho2(p):
        f'csezinho : "senao" linhas "fim" '
        
    def p_csezinho3(p):
        f'csezinho : "fim" '

    def p_cenquanto(p):
        f'cenquanto : "enquanto" ( condicoes ) "faz" linhas "fim" '

    def p_condicoes(p):
        f'condicoes : condicao '
    
    def p_condicoes2(p):
        f'condicoes : condicoes "e" condicoes '

    def p_condicoes3(p):
        f'condicoes : condicoes "ou" condicoes '

    def p_condicoes4(p):
        f'condicoes : "(" condicoes ")" '

    def p_condicao(p):
        f'condicao : expressao comparacao expressao '

    def p_comparacao(p):
        f'comparacao : "=" '
        
    def p_comparacao2(p):
        f'comparacao : "<" '

    def p_comparacao3(p):
        f'comparacao : ">" '

    def p_comparacao4(p):
        f'comparacao :  "<="  '

    def p_comparacao5(p):
        f'comparacao :  ">=" '
    
    def p_comparacao6(p):
        f'comparacao : "!=" '

    def p_textvar(p):
        f'textvar : textvar "," final '

    def p_textvar2(p):
        f'textvar : final '

    def p_final(p):
        f'final : VAR '
    
    def p_final2(p):
        f'final : TEXTO '

    def p_error(p):
        print("Syntax error in input!")
        parser.exito = False

    parser = yacc.yacc()
    parser.exito = True

    fonte = ""
    for linha in sys.stdin:
        fonte += linha

    parse = parser.parse(fonte)

    if parse.exito:
        print("terminou com sucesso")