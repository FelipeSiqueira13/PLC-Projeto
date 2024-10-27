import re
import matplotlib
import matplotlib.pyplot as plt

#A
def doenca_total(lista):
    generoTotal= {"M":0, "F":0}

    generoDoenca = {"M":0, "F":0}

    generoTotal["M"] = len(re.findall(f'[0-9]+,M,[0-9]+,[0-9]+,[0-9]+,[0-1]',lista))

    generoDoenca["M"] = len(re.findall(f'[0-9]+,M,[0-9]+,[0-9]+,[0-9]+,1',lista))

    generoTotal["F"] = len(re.findall(f'[0-9]+,F,[0-9]+,[0-9]+,[0-9]+,[0-1]',lista))

    generoDoenca["F"] = len(re.findall(f'[0-9]+,F,[0-9]+,[0-9]+,[0-9]+,1',lista))

    doencaTotal = round((generoDoenca["F"] + generoDoenca["M"])/(generoTotal["F"]+generoTotal["M"])*100,2)

    doencaM = round((generoDoenca["M"]/generoTotal["M"])*100,2)

    doencaF = round((generoDoenca["F"]/generoTotal["F"])*100,2)

    return ((generoDoenca["F"] + generoDoenca["M"]),doencaTotal, doencaM, doencaF)

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
        estatisticas[escalao] = round((escaloes[escalao]["doentes"]/escaloes[escalao]["total"])*100,2)
    
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

        escalao = str(i)+'\n-\n'+str(i+9)
        escaloes[escalao] = {}
        escaloes[escalao]["doentes"] = len(re.findall(regularDoente,lista))
        escaloes[escalao]["total"] = len(re.findall(regularTotal,lista))
        if escaloes[escalao]["total"] == 0:
            estatisticas[escalao] = "Sem informação"
        else:
            estatisticas[escalao] = round((escaloes[escalao]["doentes"]/escaloes[escalao]["total"])*100,2)
    
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
            estatisticasTensao[escalao] = "Sem informação"
        else:
            estatisticasTensao[escalao] = round((escaloesTensao[escalao]["doentes"]/escaloesTensao[escalao]["total"])*100,2)
    
        i+=10

    x = []
    y = []
    for i in estatisticasTensao:
        x.append(i)
        y.append(estatisticasTensao[i])
    
    plt.plot(x,y)

    plt.xlabel("Tensão")
    plt.ylabel("Doença")

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('fig1.png', dpi=100)
    plt.close()
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
            estatisticasBatimento[escalao] = "Sem informação"
        else:
            estatisticasBatimento[escalao] = round((escaloesBatimento[escalao]["doentes"]/escaloesBatimento[escalao]["total"])*100,2)
    
        i+=10
    
    x = []
    y = []
    for i in estatisticasBatimento:
        x.append(i)
        y.append(estatisticasBatimento[i])
    
    plt.plot(x,y)

    plt.xlabel("Batimento")
    plt.ylabel("Doença")

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('fig2.png', dpi=100)
    plt.close()

    


#E
def criar_grafico(estatisticasIdade,estatisticasColesterol):
    x = []
    y = []
    for i in estatisticasIdade:
        x.append(i)
        y.append(estatisticasIdade[i])
    
    plt.bar(x,y)

    plt.xlabel("Idade")
    plt.ylabel("Doença")

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('fig3.png', dpi=100)
    plt.close()

    x = []
    y = []
    for i in estatisticasColesterol:
        if estatisticasColesterol[i] != "Sem informação":
            x.append(i)
            y.append(estatisticasColesterol[i])
    
    plt.bar(x,y)

    plt.xlabel("Colesterol")
    plt.ylabel("Doença")

    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('fig4.png', dpi=100)

    plt.close()

def main(): #[0-9]+,[MF],[0-9]+,[0-9]+,[0-9]+,[0,1]
    f = open("myheart.csv", "r")
    lista = f.read()
    f.close()


    (totalDoentes,doencaTotal, doencaM, doencaF) = doenca_total(lista)
    #print("doença total é ", doencaTotal)
    #print("doença M é ", doencaM)
    #print("doença F é ", doencaF)


    estatisticasIdade = doenca_idade(lista)

    mudaraquiIdade = ""

    for i in estatisticasIdade:
        mudaraquiIdade += "<tr><td>"+i+"</td><td>"+str(estatisticasIdade[i])+"</td></tr>"


    estatisticasColesterol = doenca_Colesterol(lista)
  
    mudaraquiColesterol = ""

    for i in estatisticasColesterol:
        mudaraquiColesterol += "<tr><td>"+i+"</td><td>"+str(estatisticasColesterol[i])+"</td></tr>"

    #print(estatisticasColesterol)

    doenca_batimento_tensao(lista)

    criar_grafico(estatisticasIdade,estatisticasColesterol)


    ficheirohtml = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>G07 - Apresentação PLC</title>
            <style>
            body{{
                background-color: rgb(63, 63, 201);
            }}
            main{{
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.425);
                width: 80%;
                padding: 20px;
                margin: auto;
                text-align: center;
            }}
            p{{
                text-align: left;
                font-size: 120%;
            }}
            table, th, td {{
                border: 1px solid black;
            }}
            </style>
        </head>
        <body>
            <main>
                <h1>Apresentação PLC</h1>
                <p style="text-align: center;">Felipe Siqueira Espinheira a102513</p>
                <p style="text-align: center;">Hugo Simões Marques a102934</p>
                <p style="text-align: center;">José Afonso da Silva Miranda a102933</p>

                <h2>A) Doença e Géneros</h2>
                <p>O numero total de pessoas doentes é: {totalDoentes}.</p>
                <p>A percentagem de doentes no total é: {doencaTotal}.</p>
                <p>A percentagem doentes do género masculino: {doencaM}.</p>
                <p>A percentagem doentes do género feminino: {doencaF}.</p>

                <h2>B) Distribuição por escalão de idade</h2>
                <table style="width:100%">
                    <tr>
                    <th>Idade</th>
                    <th>Percentagem de doentes</th>
                    </tr>
                    {mudaraquiIdade}
                </table>
                <h2>C) Distribuição por escalão de colesterol</h2>
                    <table style="width:100%">
                        <tr>
                        <th>Colesterol</th>
                        <th>Percentagem de doentes</th>
                        </tr>
                        {mudaraquiColesterol}
                    </table>
                <h2>D) Distribuição por tensão e Distribuição de Batimentos</h2>
                    <p>A correlação entre doença e tensão é fraca, com um aumento não muito significativo da % de pessoas com doença nos escalões mais altos, isto pode ser devido à falta de dados.</p>
                    <p>No outro lado, a correlação entre batimento e doença é notável, com uma diminuição da percentagem de pessoas doentes quanto mais alta é o seu batimento.</p>
                    <picture>
                        <img src="fig1.png">
                        <img src="fig2.png">
                    </picture>
                <h2>E) Gráficos para a distribuiçãoda B e C</h2>
                <p>Os índices onde não  existe informação não estão representados no gráfico.</p>
                <picture>
                    <img src="fig3.png">
                    <img src="fig4.png">
                </picture>
            </main>
        </body>
        </html>"""
    
    with open("index.html", "w", encoding="utf-8") as html_file:
        html_file.write(ficheirohtml)

    print("Página HTML 'index.html' gerada com sucesso!")

main()