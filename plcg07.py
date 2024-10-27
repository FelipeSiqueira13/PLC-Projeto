import re

#A
#def doenca_total(listaDoentes, listaGenero):

#B
#def doenca_idade(listaDoentes, listaIdade): 

#C
#def doenca_Colesterol(listaDoentes, listaColesterol):

#D
#def doenca_batimento_tensao(listaDoentes, listaBatimento, listaTensao):

#E
#def criar_grafico(A,B,C,D):


def main():
    f = open("myheart.csv", "r")
    arcs = [] #idade, sexo, tensao, colesterol, batimento, temDoenca
    lista = {} #dicionario de listas que ligam as informações individuais
    nomes = f.readline()
    nome = re.split(",", nomes.rstrip('\n'))
    for n in nome:
        lista[n] = []
        arcs.append(n)
    max = len(arcs)
    for linha in f:
        info = re.split(",", linha.rstrip('\n'))
        for i in range(max):
            if info[i] == 'M' or info[i] == 'F':
                lista[arcs[i]].append(info[i])
            else:
                lista[arcs[i]].append(int(info[i]))
    f.close()

    print(lista)

main()