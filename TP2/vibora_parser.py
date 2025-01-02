import ply.yacc as yacc
import sys

from vibora_lex import tokens

def p_programa(p):
    'programa : declaracoes linhas'
    parser.assembly = f'{p[1]} START\n {p[2]}STOP'

def p_programa2(p):
    'programa : linhas'
    parser.assembly = f'START\n {p[1]}STOP'

def p_declaracoes(p):
    'declaracoes : declaracao'
    p[0] = f'{p[1]}'

def p_declaracoes2(p):
    'declaracoes : declaracoes declaracao'
    p[0] = f'{p[1]}{p[2]}'

def p_declaracao(p):
    'declaracao : inteiro VAR ";"'
    if p[2] not in p.parser.registers:
        p.parser.registers.update({p[2]: p.parser.gp})
        p[0] = f'PUSHI 0\n'
        p.parser.ints.append(p[2])
        p.parser.gp += 1
    else:
        print("Error: Variavel já existe.")
        parser.exito = False

def p_decaracao2(p):
    'declaracao : inteiro VAR "=" NUM ";"'
    if p[2] not in p.parser.registers:
        p.parser.registers.update({p[2]: p.parser.gp})
        p[0] = f'PUSHI {p[4]}\n'
        p.parser.ints.append(p[2])
        p.parser.gp += 1
    else:
        print("Error: Variavel já existe.")
        parser.exito = False


def p_linhas(p):
    'linhas : linha'
    p[0] = f'{p[1]}'

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

def p_atribuicao(p):
    'atribuicao : VAR "=" expressao ";"'
    p[0] = f'{p[3]} STOREG {p.parser.registers.get(p[1])}\n'

def p_expressao(p):
    'expressao : NUM'
    p[0] = f'PUSHI {p[1]}\n'

def p_expressao2(p):
    'expressao : VAR'
    p[0] = f'PUSHG {p.parser.registers.get(p[1])}\n'

def p_expressao3(p):
    'expressao : expressao "+" expressao'
    p[0] = f'{p[1]}{p[3]} ADD\n'
    
def p_expressao4(p):
    'expressao : expressao "-" expressao'
    p[0] = f'{p[1]}{p[3]} SUB\n'

def p_expressao5(p):
    'expressao : expressao "*" expressao'
    p[0] = f'{p[1]}{p[3]} MUL\n'

def p_expressao6(p):
    'expressao : expressao "/" expressao'
    p[0] = f'{p[1]}{p[3]} DIV\n'

def p_expressao7(p):
    'expressao :  "(" expressao ")"'
    p[0] = f'{p[2]}'

def p_cler(p):
    'cler : VAR "=" ler "(" TEXTO ")" ";"'
    p[0] = f'PUSHS {p[5]}\n WRITES\n READ\n STOREG {p.parser.registers.get(p[1])}\n'

def p_cescreva(p):
    'cescreva : escreva "(" escrevatexto ")" ";" '
    p[0] = f'{p[3]}'

def p_cse(p):
    'cse : se "(" condicoes ")" entao linhas csezinho'
    p.parser.elses += 1
    p[0] = f'{p[3]}JZ else{p.parser.elses}\n{p[6]}\nJUMP fim{p.parser.elses} else{p.parser.elses}: \n{p[7]} fim{p.parser.elses}: \n'

def p_csezinho(p):
    'csezinho : senao se "(" condicoes ")" entao linhas csezinho'
    p.parser.elses += 1
    p[0] = f'{p[3]}JZ else{p.parser.elses}\n{p[6]}\nJUMP fim{p.parser.elses} else{p.parser.elses}: \n{p[7]} fim{p.parser.elses}: \n'

def p_csezinho2(p):
    'csezinho : senao linhas fim'
    p[0] = f'{p[2]}'
    
def p_csezinho3(p):
    'csezinho : fim'
    p[0] = f''

def p_cenquanto(p):
    'cenquanto : enquanto "(" condicoes ")" faz linhas fim'
    p.parser.enquantos += 1
    p[0] = f'inicioloop{p.parser.enquantos}:\n {p[3]}JZ fimloop{p.parser.enquantos}\n{p[6]} JUMP inicioloop{p.parser.enquantos}\n fimloop{p.parser.enquantos}\n'

def p_condicoes(p):
    'condicoes : condicao'
    p[0] = f'{p[1]}'

def p_condicoes2(p):
    'condicoes : condicoes e condicoes'
    p[0] = f'{p[1]}{p[3]} AND\n'

def p_condicoes3(p):
    'condicoes : condicoes ou condicoes'
    p[0] = f'{p[1]}{p[3]} OR\n'

def p_condicoes4(p):
    'condicoes : "(" condicoes ")"'
    p[0] = f'{p[2]}'

def p_condicao(p):
    'condicao : expressao comparacao expressao'
    p[0] = f'{p[1]}{p[3]}{p[2]}'

def p_comparacao(p):
    'comparacao : =='
    p[0] = f'EQUAL\n'
    
def p_comparacao2(p):
    'comparacao : <'
    p[0] = f'INF\n'

def p_comparacao3(p):
    'comparacao : >'
    p[0] = f'SUP\n'

def p_comparacao4(p):
    'comparacao :  <='
    p[0] = f'INFEQ\n'

def p_comparacao5(p):
    'comparacao :  >='
    p[0] = f'SUPEQ\n'

def p_comparacao6(p):
    'comparacao : !='
    p[0] = f'EQUAL\nNOT\n'

def p_escrevatexto(p):
    'escrevatexto : escrevatexto "," escrevatextofinal'
    p[0] = f'{p[1]} PUSHS " " \n WRITES \n{p[3]}'

def p_textvar2(p):
    'escrevatexto : escrevatextofinal'
    p[0] = f'{p[1]} PUSHS "\n"\n WRITES \n'

def p_final(p):
    'escrevatextofinal : VAR'
    p[0] = f'PUSHG {p.parser.registers.get(p[1])}\n WRITEI\n'

def p_final2(p):
    'escrevatextofinal : TEXTO'
    p[0] = f'PUSHS {p[1]}\n WRITES\n'

def p_error(p):
    print("Syntax error in input!")
    parser.exito = False

parser = yacc.yacc(debug=True)
parser.exito = True
parser.registers = {}
parser.ints = []
parser.elses = 0
parser.enquantos = 0
parser.gp = 0
parser.assembly = ""


fonte = ""
for linha in sys.stdin:
    fonte += linha

parse = parser.parse(fonte)

if parse.exito:
    print("terminou com sucesso")

try:
    with open('.\PLC-Projeto\TP2\E1.txt','r') as file:
        inp = file.read()
        parser.parse(inp)
        if parser.success:
            with open('.\PLC-Projeto\TP2\E1.vm', 'w') as output:
                output.write(parser.assembly)
                print(parser.assembly)
        else:
            print("<><><><><><><><><><><><><><><><><><><><><><><>")
            print("Erro")
            print("<><><><><><><><><><><><><><><><><><><><><><><>")
except KeyboardInterrupt:
    print()