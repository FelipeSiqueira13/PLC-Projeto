import ply.lex as lex
import ply.yacc as yacc
import sys

def gramar():

    """
    programa : declaracoes linhas
    declaracoes : declaracao | declaracoes declaracao
    declaracao : 'inteiro' VAR ';' | 'inteiro' VAR '=' NUM ';'
    linhas : linha | linhas linha
    linha : comando | atribuicao
    comando : cescreva | cse | cenquanto | cler
    atribuicao : VAR '=' expressao ';'
    expressao : NUM | VAR | expressao '+' expressao | expressao '-' expressao | expressao '*' expressao 
              | expressao '/' expressao | '(' expressao ')'
    cler : VAR '=' 'ler''('TEXTO')'';'
    cescreva : 'escreva''(' textvar ')'';'
    cse : 'se''('condicoes')' 'entao' linhas cse2
    cse2 :  'senao se''('condicoes')' 'entao' linhas cse2 | 'senao' linhas 'fim' | 'fim' 
    cenquanto : 'enquanto''('condicoes')' 'faz' linhas 'fim'
    condicoes : condicao | condicoes 'e' condicoes | condicoes 'ou' condicoes | '(' condicoes ')'
    condicao : expressao comparacao expressao
    comparacao : '=''=' | '<' | '>' | '<''=' | '>''=' | '!''='
    textvar : textvar',' final | final
    final : VAR | TEXTO
    TEXTO : ".*"
    VAR : [a-zA-Z][a-zA-Z0-9]*
    NUM : [0-9]+
    """
