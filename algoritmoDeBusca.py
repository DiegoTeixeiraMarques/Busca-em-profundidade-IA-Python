# Algoritmo busca em profundidade

estadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
estadoInicial = [[2, 8, 3], [1, 6, 0], [7, 4, 5]]
fechados = []
pai = 0
no = 1
abertos = [(pai, no, estadoInicial)]
caminhoSucesso = []
caminhoSucesso.append(estadoInicial)

def mostrar_campo(campo):
    for item in campo:
        print(item)

def duplicar_campo(X):
    X1 = [[0,0,0],[0,0,0],[0,0,0]]
    l = 0
    c = 0
    filhos = []
    for linha in X:
        for coluna in linha:
            X1[l][c] = X[l][c]
            c = c + 1
        c = 0
        l = l + 1
    return X1

def verifica_se_filho_existe(X):
    for item in fechados:
        if (item == X):
            return True

    for item in abertos:
        if (item[2] == X):
            return True

def gerarFilhos(X):
    X1 = X[2]
    Y = X
    l = 0
    c = 0
    for linha in X1:
        for coluna in linha:
            if(X1[l][c] == 0):
                lin = l
                col = c
            c = c + 1
        c = 0
        l = l + 1

    if (col > 0):
        X2 = duplicar_campo(X1)       
        X2[lin][col] = X2[lin][col - 1]
        X2[lin][col - 1] = 0
        if (verifica_se_filho_existe(X2)):
            pass
        else:
            idFilho = str(Y[1]) + '1'
            abertos.append((Y[1], int(idFilho), X2))
            caminhoSucesso.append((Y[1], int(idFilho), X2))
            #mostrar_campo(X2)
            #print('----------------')
    if (col < 2):
        X2 = duplicar_campo(X1)       
        X2[lin][col] = X2[lin][col + 1]
        X2[lin][col + 1] = 0
        if (verifica_se_filho_existe(X2)):
            pass
        else:
            idFilho = str(Y[1]) + '2'
            abertos.append((Y[1], int(idFilho), X2))
            caminhoSucesso.append((Y[1], int(idFilho), X2))
            #mostrar_campo(X2)
            #print('----------------')
    if (lin > 0):
        X2 = duplicar_campo(X1)       
        X2[lin][col] = X2[lin - 1][col]
        X2[lin - 1][col] = 0
        if (verifica_se_filho_existe(X2)):
            pass
        else:
            idFilho = str(Y[1]) + '3'
            abertos.append((Y[1], int(idFilho), X2))
            caminhoSucesso.append((Y[1], int(idFilho), X2))
            #mostrar_campo(X2)
            #print('----------------')
    if (lin < 2):
        X2 = duplicar_campo(X1)       
        X2[lin][col] = X2[lin + 1][col]
        X2[lin + 1][col] = 0
        if (verifica_se_filho_existe(X2)):
            pass
        else:
            idFilho = str(Y[1]) + '4'
            abertos.append((Y[1], int(idFilho), X2))
            caminhoSucesso.append((Y[1], int(idFilho), X2))
            #mostrar_campo(X2)
            #print('----------------')
   
def loop():
    print('Olá, aguarde enquanto eu procuro uma solução para este problema...')
    print("")
    while abertos != []:
        X = abertos[0]
        abertos.pop(0)
        if X[2] == estadoFinal:
            print('Encontrei a solução!')
            print("")
            fechados.insert(0, X[2])
            #mostrar_campo(X[2])
            #print('Pai: ', X[0])
            #print('ID: ', X[1])

            solucao = []
            solucao.insert(0, X)

            while solucao[0][0] != 1:
                #print(solucao[0][0])
                #input("-->")
                for item in caminhoSucesso:
                    if item[1] == X[0]:
                        solucao.insert(0, item)
                        #print('X antes: ', X)
                        X = item
                        #print('X depois: ', X)
            #print(solucao)
            input("Tecle ENTER, veja o estado inicial e em seguida a solução!")
            print("")
            mostrar_campo(estadoInicial)
            for n in range(0, len(solucao)-1):
                input("Tecle ENTER para proxima jogada!")
                print("")
                daVez = solucao[n]
                mostrar_campo(daVez[2])
            input("Tecle ENTER para proxima jogada!")
            print("")
            mostrar_campo(estadoFinal)
            break

        else:
            fechados.insert(0, X[2])
            gerarFilhos(X)


print("Olá, eu sou especialista em revolver quebra cabeças.")
print("Utilizo um algorítmo de busca em profundidade para descobrir o passo a passo para solução.")
print("")
print("Vamos testar?")
print("")
input("Tecle ENTER para prosseguir")
print("")

print("Veja, este é o estado inicial...")
print("")
mostrar_campo(estadoInicial)
print("")

print("Vou buscar uma solução para chegar neste estado...")
print("")
mostrar_campo(estadoFinal)
print("")

input("Tecle Enter para conferir!")



loop()





