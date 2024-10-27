import re
import matplotlib

#A
def doenca_total(lista):
    generoTotal= {"M":0, "F":0}

    generoDoenca = {"M":0, "F":0}

    generoTotal["M"] = len(re.findall(f'[0-9]+,M,[0-9]+,[0-9]+,[0-9]+,[0-1]',lista))

    generoDoenca["M"] = len(re.findall(f'[0-9]+,M,[0-9]+,[0-9]+,[0-9]+,1',lista))

    generoTotal["F"] = len(re.findall(f'[0-9]+,F,[0-9]+,[0-9]+,[0-9]+,[0-1]',lista))

    generoDoenca["F"] = len(re.findall(f'[0-9]+,F,[0-9]+,[0-9]+,[0-9]+,1',lista))

    doencaTotal = (generoDoenca["F"] + generoDoenca["M"])/(generoTotal["F"]+generoTotal["M"])*100

    doencaM = (generoDoenca["M"]/generoTotal["M"])*100

    doencaF = (generoDoenca["F"]/generoTotal["F"])*100

    return (doencaTotal, doencaM, doencaF)

#B
def doenca_idade(lista):
    escaloes = {}
    estatisticas = {}

    for i in range(8):
        x,y = (5,9),3+int(i/2)
        if i%2 == 0:
            x = (0,4)
        regularTotal = f'[' + str(y) +']['+ str(x[0]) +'-'+str(x[1])+'],[MF],[0-9]+,[0-9]+,[0-9]+,[0-1]'
        regularDoente = f'[' + str(y) +']['+ str(x[0]) +'-'+str(x[1])+'],[MF],[0-9]+,[0-9]+,[0-9]+,1'
        escalao = str(y)+str(x[0])+'-'+str(y)+str(x[1])

        escaloes[escalao] = {}

        escaloes[escalao]["doentes"] = len(re.findall(regularDoente,lista))
        escaloes[escalao]["total"] = len(re.findall(regularTotal,lista))
        estatisticas[escalao] = (escaloes[escalao]["doentes"]/escaloes[escalao]["total"])*100
    
    return estatisticas


#C
def doenca_Colesterol(lista):
    dividido = re.split(',|\n',lista)
    menor = int(dividido[9])
    maior = menor
    i = 15
    while(i<len(dividido)):
        if int(dividido[i]) != 0 and int(dividido[i]) < menor:
            menor = int(dividido[i])
        if int(dividido[i]) > maior:
            maior = int(dividido[i])
        i+=6
    
    escaloes = {}
    estatisticas = {}

    i = menor
    while(i <= maior):
        if(i <= 90):
            regularTotal = f'[0-9]+,[MF],[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[' + str(int((i+9)/10)) +']['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,[0-1]'
            regularDoente = f'[0-9]+,[MF],[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[' + str(int((i+9)/10)) +']['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,1'
        elif(i < 100):
            regularTotal = f'[0-9]+,[MF],[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[1][0]['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,[0-1]'
            regularDoente = f'[0-9]+,[MF],[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[1][0]['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,1'
        else:
            regularTotal = f'[0-9]+,[MF],[0-9]+,([' + str(int(i/100)) +'][' + str(int((i/10))%10) +']['+  str(int(i%10)) +'-'+ str(9)+']|'+'[' + str(int((i+9)/100)) +'][' + str(int(((i+9)/10)%10)) +']['+  str(0) +'-'+str((i-1)%10)+']),[0-9]+,[0-1]'
            regularDoente = f'[0-9]+,[MF],[0-9]+,([' + str(int(i/100)) +'][' + str(int((i/10))%10) +']['+  str(int(i%10)) +'-'+ str(9)+']|'+'[' + str(int((i+9)/100)) +'][' + str(int(((i+9)/10)%10)) +']['+  str(0) +'-'+str((i-1)%10)+']),[0-9]+,1'

        escalao = str(i)+'-'+str(i+9)
        escaloes[escalao] = {}
        escaloes[escalao]["doentes"] = len(re.findall(regularDoente,lista))
        escaloes[escalao]["total"] = len(re.findall(regularTotal,lista))
        if escaloes[escalao]["total"] == 0:
            estatisticas[escalao] = -1
        else:
            estatisticas[escalao] = (escaloes[escalao]["doentes"]/escaloes[escalao]["total"])*100
    
        i+=10


    return estatisticas

#D
def doenca_batimento_tensao(lista):
    dividido = re.split(',|\n',lista)
    menor = int(dividido[8])
    maior = menor
    i = 14
    while(i<len(dividido)):
        if int(dividido[i]) != 0 and int(dividido[i]) < menor:
            menor = int(dividido[i])
        if int(dividido[i]) > maior:
            maior = int(dividido[i])
        i+=6
    
    escaloesTensao = {}
    estatisticasTensao = {}

    i = menor
    while(i <= maior):
        if(i <= 90):
            regularTotal = f'[0-9]+,[MF],([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[' + str(int((i+9)/10)) +']['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,[0-9]+,[0-1]'
            regularDoente = f'[0-9]+,[MF],([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[' + str(int((i+9)/10)) +']['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,[0-9]+,1'
        elif(i < 100):
            regularTotal = f'[0-9]+,[MF],([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[1][0]['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,[0-9]+,[0-1]'
            regularDoente = f'[0-9]+,[MF],([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[1][0]['+  str(0) +'-'+str((i+9)%10)+']),[0-9]+,[0-9]+,1'
        else:
            regularTotal = f'[0-9]+,[MF],([' + str(int(i/100)) +'][' + str(int((i/10))%10) +']['+  str(int(i%10)) +'-'+ str(9)+']|'+'[' + str(int((i+9)/100)) +'][' + str(int(((i+9)/10)%10)) +']['+  str(0) +'-'+str((i-1)%10)+']),[0-9]+,[0-9]+,[0-1]'
            regularDoente = f'[0-9]+,[MF],([' + str(int(i/100)) +'][' + str(int((i/10))%10) +']['+  str(int(i%10)) +'-'+ str(9)+']|'+'[' + str(int((i+9)/100)) +'][' + str(int(((i+9)/10)%10)) +']['+  str(0) +'-'+str((i-1)%10)+']),[0-9]+,[0-9]+,1'

        escalao = str(i)+'-'+str(i+9)
        escaloesTensao[escalao] = {}
        escaloesTensao[escalao]["doentes"] = len(re.findall(regularDoente,lista))
        escaloesTensao[escalao]["total"] = len(re.findall(regularTotal,lista))
        if escaloesTensao[escalao]["total"] == 0:
            estatisticasTensao[escalao] = -1
        else:
            estatisticasTensao[escalao] = (escaloesTensao[escalao]["doentes"]/escaloesTensao[escalao]["total"])*100
    
        i+=10

    #batimento

    menor = int(dividido[10])
    maior = menor
    i = 16
    while(i<len(dividido)):
        if int(dividido[i]) != 0 and int(dividido[i]) < menor:
            menor = int(dividido[i])
        if int(dividido[i]) > maior:
            maior = int(dividido[i])
        i+=6
    
    escaloesBatimento = {}
    estatisticasBatimento = {}

    i = menor
    while(i <= maior):
        if(i <= 90):
            regularTotal = f'[0-9]+,[MF],[0-9]+,[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[' + str(int((i+9)/10)) +']['+  str(0) +'-'+str((i+9)%10)+']),[0-1]'
            regularDoente = f'[0-9]+,[MF],[0-9]+,[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[' + str(int((i+9)/10)) +']['+  str(0) +'-'+str((i+9)%10)+']),1'
        elif(i < 100):
            regularTotal = f'[0-9]+,[MF],[0-9]+,[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[1][0]['+  str(0) +'-'+str((i+9)%10)+']),[0-1]'
            regularDoente = f'[0-9]+,[MF],[0-9]+,[0-9]+,([' + str(int(i/10)) +']['+  str(i%10) +'-'+ str(9)+']|'+'[1][0]['+  str(0) +'-'+str((i+9)%10)+']),1'
        else:
            regularTotal = f'[0-9]+,[MF],[0-9]+,[0-9]+,([' + str(int(i/100)) +'][' + str(int((i/10))%10) +']['+  str(int(i%10)) +'-'+ str(9)+']|'+'[' + str(int((i+9)/100)) +'][' + str(int(((i+9)/10)%10)) +']['+  str(0) +'-'+str((i-1)%10)+']),[0-1]'
            regularDoente = f'[0-9]+,[MF],[0-9]+,[0-9]+,([' + str(int(i/100)) +'][' + str(int((i/10))%10) +']['+  str(int(i%10)) +'-'+ str(9)+']|'+'[' + str(int((i+9)/100)) +'][' + str(int(((i+9)/10)%10)) +']['+  str(0) +'-'+str((i-1)%10)+']),1'

        escalao = str(i)+'-'+str(i+9)
        escaloesBatimento[escalao] = {}
        escaloesBatimento[escalao]["doentes"] = len(re.findall(regularDoente,lista))
        escaloesBatimento[escalao]["total"] = len(re.findall(regularTotal,lista))
        if escaloesBatimento[escalao]["total"] == 0:
            estatisticasBatimento[escalao] = -1
        else:
            estatisticasBatimento[escalao] = (escaloesBatimento[escalao]["doentes"]/escaloesBatimento[escalao]["total"])*100
    
        i+=10
    


#E
#def criar_grafico(A,B,C,D):


def main(): #[0-9]+,[MF],[0-9]+,[0-9]+,[0-9]+,[0,1]
    f = open("myheart.csv", "r")
    lista = f.read()
    f.close()


    (doencaTotal, doencaM, doencaF) = doenca_total(lista)
    #print("doença total é ", doencaTotal)
    #print("doença M é ", doencaM)
    #print("doença F é ", doencaF)


    estatisticasIdade = doenca_idade(lista)
    #print(estatisticasIdade)

    estatisticasColesterol = doenca_Colesterol(lista)
    #print(estatisticasColesterol)

    doenca_batimento_tensao(lista)

main()