import ply.yacc as yacc
import os
import re

from vibora_lex import tokens

precedence = (
    ('left', 'e', 'ou'),
    ('left', 'igual', 'diferente'),
    ('left', 'menor', 'maior', 'menor_igual', 'maior_igual'),
    ('left', 'soma', 'subtracao'),
    ('left', 'multiplicacao', 'divisao'),
    ('right', 'elevado'),
    ('right', '='),
)

def p_programa(p):
    'programa : declaracoes funcoes linhas'
    parser.assembly = f'{p[1]}\nSTART\nJUMP main\n{p[2]}\nmain:\n{p[3]}\nSTOP'

def p_declaracoes(p):
    'declaracoes :'
    p[0] = f''

def p_declaracoes2(p):
    'declaracoes : declaracoes declaracao'
    p[0] = f'{p[1]}{p[2]}'

def p_declaracao(p):
    'declaracao : DECINTEIRO VAR ";"'
    if p[2] not in p.parser.registers:
        p.parser.registers.update({p[2]: p.parser.gp})
        p[0] = f'PUSHI 0\n'
        p.parser.gp += 1
    else:
        print("Error: Variavel já existe.")
        parser.exito = False

def p_decaracao2(p):
    'declaracao : DECINTEIRO VAR "=" NUM ";"'
    if p[2] not in p.parser.registers:
        p.parser.registers.update({p[2]: p.parser.gp})
        p[0] = f'PUSHI {p[4]}\n'
        p.parser.gp += 1
    else:
        print("Error: Variavel já existe.")
        parser.exito = False

def p_funcoes(p):
    'funcoes : funcoes funcao'
    p[0] = f'{p[1]}{p[2]}'

def p_funcoes2(p):
    'funcoes :'
    p[0] = f''

def p_funcao(p):
    'funcao : def chamada linhas retorna expressao ";" fim'
    if p[2] not in p.parser.funcoesComRetorno:
        p.parser.funcoesComRetorno.update({p[2]: p.parser.funcoes})
        p[0] = f'func{p.parser.funcoes}:\n{p[3]}{p[5]}RETURN\n'
        p.parser.funcoes += 1
    else:
        print("Error: Funçao ou variavel já existe.")
        parser.exito = False

def p_funcao2(p):
    'funcao : def chamada linhas retorna ";" fim'
    if p[2] not in p.parser.funcoesSemRetorno:
        p.parser.funcoesSemRetorno.update({p[2]: p.parser.funcoes})
        p[0] = f'func{p.parser.funcoes}:\n{p[3]}RETURN\n'
        p.parser.funcoes += 1
    else:
        print("Error: Funçao ou variavel já existe.")
        parser.exito = False

def p_linhas(p):
    'linhas :'
    p[0] = f''

def p_linhas2(p):
    'linhas : linhas linha'
    p[0] = f'{p[1]}{p[2]}'

def p_linha(p):
    'linha : atribuicao'
    p[0] = f'{p[1]}'

def p_linha2(p):
    'linha : comando'
    p[0] = f'{p[1]}'

def p_comando(p):
    'comando : cescreva'
    p[0] = f'{p[1]}'

def p_comando2(p):
    'comando : cse'
    p[0] = f'{p[1]}'

def p_comando3(p):
    'comando : cenquanto'
    p[0] = f'{p[1]}'

def p_comando4(p):
    'comando : cler'
    p[0] = f'{p[1]}'

def p_comando5(p):
    'comando : cfuncao'
    p[0] = f'{p[1]}'

def p_atribuicao(p):
    'atribuicao : VAR "=" expressao ";"'
    p[0] = f'{p[3]}STOREG {p.parser.registers.get(p[1])}\n'

def p_expressao(p):
    'expressao : NUM'
    p[0] = f'PUSHI {p[1]}\n'

def p_expressao2(p):
    'expressao : VAR'
    p[0] = f'PUSHG {p.parser.registers.get(p[1])}\n'

def p_expressao3(p):
    'expressao : expressao soma expressao'
    p[0] = f'{p[1]}{p[3]}ADD\n'
    
def p_expressao4(p):
    'expressao : expressao subtracao expressao'
    p[0] = f'{p[1]}{p[3]}SUB\n'

def p_expressao5(p):
    'expressao : expressao multiplicacao expressao'
    p[0] = f'{p[1]}{p[3]}MUL\n'

def p_expressao6(p):
    'expressao : expressao divisao expressao'
    p[0] = f'{p[1]}{p[3]}DIV\n'

def p_expressao7(p):
    'expressao : expressao mod expressao'
    p[0] = f'{p[1]}{p[3]}MOD\n'

def p_expressao8(p):
    'expressao :  abs expressao abs'
    p.parser.preDef += 1
    p[0] = f'{p[2]}DUP 1\nPUSHI 0\nINF\nJZ fimPreDef{p.parser.preDef}\nPUSHI -1\nMUL\nfimPreDef{p.parser.preDef}:\n'

def p_expressao9(p):
    'expressao : expressao elevado expressao'
    p.parser.preDef += 1
    p[0] = f'{p[1]}DUP 1\n{p[3]}PUSHI 1\nSUB\ninicioloopPreDef{p.parser.preDef}:\nDUP 1\nJZ fimloopPreDef{p.parser.preDef}\nSWAP\nPUSHSP\nPUSHI -2\nPADD\nLOAD 0\nMUL\nSWAP\nPUSHI 1\nSUB\nJUMP inicioloopPreDef{p.parser.preDef}\nfimloopPreDef{p.parser.preDef}:\nPOP 1\nSWAP\nPOP 1\n'

def p_expressao10(p):
    'expressao :  E_parentese expressao D_parentese'
    p[0] = f'{p[2]}'

def p_expressao11(p):
    'expressao :  subtracao expressao'
    p[0] = f'{p[2]}PUSHI -1\nMUL\n'

def p_expressao12(p):
    'expressao : chamada'
    if p[1] in p.parser.funcoesComRetorno:
        p[0] = f'PUSHA func{p.parser.funcoesComRetorno.get(p[1])}\nCALL\n'
    else:
        print("Error: Esta funçao nao existe ou nao tem retorno")
        parser.exito = False

def p_cfuncao(p):
    'cfuncao : chamada ";"'
    if p[1] in p.parser.funcoesSemRetorno:
        p[0] = f'PUSHA func{p.parser.funcoesSemRetorno.get(p[1])}\nCALL\n'
    else:
        print("Error: Esta funçao nao existe ou tem retorno")
        parser.exito = False

def p_cler(p):
    'cler : VAR "=" ler E_parentese TEXTO D_parentese ";"'
    p[0] = f'PUSHS {p[5]}\nWRITES\nPUSHS "\\n"\nWRITES\nREAD\nATOI\nSTOREG {p.parser.registers.get(p[1])}\n'

def p_cescreva(p):
    'cescreva : escreva E_parentese escrevatexto D_parentese ";" '
    p[0] = f'{p[3]}PUSHS"\\n"\nWRITES\n'

def p_cse(p):
    'cse : se E_parentese condicoes D_parentese entao linhas csezinho'
    p.parser.elses += 1
    p[0] = f'{p[3]}JZ else{p.parser.elses}\n{p[6]}JUMP fim{p.parser.elses}\nelse{p.parser.elses}:\n{p[7]}fim{p.parser.elses}:\n'

def p_csezinho(p):
    'csezinho : senaose E_parentese condicoes D_parentese entao linhas csezinho'
    p.parser.elses += 1
    p[0] = f'{p[3]}JZ else{p.parser.elses}\n{p[6]}JUMP fim{p.parser.elses}\nelse{p.parser.elses}:\n{p[7]}fim{p.parser.elses}:\n'

def p_csezinho2(p):
    'csezinho : senao linhas fim'
    p[0] = f'{p[2]}'
    
def p_csezinho3(p):
    'csezinho : fim'
    p[0] = f''

def p_cenquanto(p):
    'cenquanto : enquanto E_parentese condicoes D_parentese faz linhas fim'
    p.parser.enquantos += 1
    p[0] = f'inicioloop{p.parser.enquantos}:\n{p[3]}JZ fimloop{p.parser.enquantos}\n{p[6]}JUMP inicioloop{p.parser.enquantos}\nfimloop{p.parser.enquantos}:\n'

def p_condicoes(p):
    'condicoes : condicao'
    p[0] = f'{p[1]}'

def p_condicoes2(p):
    'condicoes : condicoes e condicoes'
    p[0] = f'{p[1]}{p[3]}AND\n'

def p_condicoes3(p):
    'condicoes : condicoes ou condicoes'
    p[0] = f'{p[1]}{p[3]}OR\n'

def p_condicoes4(p):
    'condicoes : nao E_parentese condicoes D_parentese'
    p[0] = f'{p[3]}NOT\n'

def p_condicoes5(p):
    'condicoes : E_parentese condicoes D_parentese'
    p[0] = f'{p[2]}'

def p_condicao(p):
    'condicao : expressao comparacao expressao'
    p[0] = f'{p[1]}{p[3]}{p[2]}'

def p_comparacao(p):
    'comparacao : igual'
    p[0] = f'EQUAL\n'
    
def p_comparacao2(p):
    'comparacao : menor'
    p[0] = f'INF\n'

def p_comparacao3(p):
    'comparacao : maior'
    p[0] = f'SUP\n'

def p_comparacao4(p):
    'comparacao :  menor_igual'
    p[0] = f'INFEQ\n'

def p_comparacao5(p):
    'comparacao :  maior_igual'
    p[0] = f'SUPEQ\n'

def p_comparacao6(p):
    'comparacao : diferente'
    p[0] = f'EQUAL\nNOT\n'

def p_escrevatexto(p):
    'escrevatexto : escrevatexto "," escrevatextofinal'
    p[0] = f'{p[1]}PUSHS " "\nWRITES\n{p[3]}'

def p_textvar2(p):
    'escrevatexto : escrevatextofinal'
    p[0] = f'{p[1]}'

def p_final(p):
    'escrevatextofinal : condicoes'
    p[0] = f'{p[1]}WRITEI\n'

def p_final2(p):
    'escrevatextofinal : expressao'
    p[0] = f'{p[1]}WRITEI\n'

def p_final3(p):
    'escrevatextofinal : TEXTO'
    p[0] = f'PUSHS {p[1]}\nWRITES\n'


def p_error(p):
    if p:
        # Use p.lexer.lexdata para acessar o contexto
        print(f"Syntax error at token {p.type}, value '{p.value}', line {getattr(p, 'lineno', 'unknown')}")
        print(f"Parser context: \n{p.lexer.lexdata[:p.lexpos]} << ERROR HERE >> {p.lexer.lexdata[p.lexpos:]}")
    else:
        print("Syntax error at EOF")



parser = yacc.yacc(debug=True)
parser.exito = True
parser.registers = {}
parser.funcoesComRetorno = {}
parser.funcoesSemRetorno = {}
parser.elses = 0
parser.enquantos = 0
parser.preDef = 0
parser.gp = 0
parser.funcoes = 1

parser.assembly = ""

folder_path = f'.\\TP2\\Programas'

files = os.listdir(folder_path)

if len(files) > 1:

    i = 0

    escolha = "Ficheiros encontrados em Programas: \n"

    for file in files:
        escolha += str(i) + " : " + file + "\n" 
        i += 1

    print(escolha)
    escolhido = int(input(f"Que programa deseja rodar? (escolha um numero de 0 a {i-1})"))

    while (escolhido < 0 or escolhido >= i):
        print(f"Numero escolhido nao esta entre 0 e {i-1}.")
        escolhido = int(input(f"Que programa deseja rodar? (escolha um numero de 0 a {i-1})"))

    ficheiro = files[escolhido]

elif len(files) == 1:
    print("Encontrado um unico ficheiro, convertendo.")
    ficheiro = files[0]

else:
    print("Nenhum ficheiro encontrado.")



file_path = os.path.join(folder_path, ficheiro)
with open(file_path, 'r') as f:
    inp = f.read()
    parser.parse(inp)
    if parser.exito:
        nomeDoFicheiro = re.search(r'(.+)\.vbr',ficheiro)
        with open(f'.\\TP2\\Saidas\\{nomeDoFicheiro.group(1)}.vm', 'w') as output:
            print("Codigo gerado com sucesso.")
            output.write(parser.assembly)
    else:
        print("-------------------------------------------------------------")
        print("Erro")
        print("-------------------------------------------------------------")


#with open(r'.\TP2\Programas\idoso.vbr','r') as file:
#    inp = file.read()
#    parser.parse(inp)
#    if parser.exito:
#        with open(r'.\TP2\Saidas\idoso.vm', 'w') as output:
#            output.write(parser.assembly)
#            print(parser.assembly)
#    else:
#        print("<><><><><><><><><><><><><><><><><><><><><><><>")
#        print("Erro")
#        print("<><><><><><><><><><><><><><><><><><><><><><><>")