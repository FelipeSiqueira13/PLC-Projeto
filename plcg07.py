import re
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
            lista[arcs[i]].append(info[i])
    
    print(lista)
    #temos que transformar os numeros em INT
    generoDoenca = {"M":0, "F":0}
    for i in range(len(lista[arcs[0]])):
        print(lista[arcs[5]][i])
        if(lista[arcs[5]][i]) == "1":
            generoDoenca[lista[arcs[1]][i]]+=1
    print(generoDoenca)


main()