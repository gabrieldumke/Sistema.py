import os
from pathlib import Path

#Identificando arquivo de textos na pasta#
def escanear_pastas(pastas_inicial):
    arquivos = os.listdir(pastas_inicial)
    lista_arquivos = []

    for arquivo in arquivos:
        lista_arquivos.append(arquivo)
    return lista_arquivos

#Definindo o caminho da pasta#
caminho = input("Coloque o endereço da pasta: ").strip()
palavra = 0
#Laço de repetição para pesquisa e definindo palavra a ser procurada#
while (palavra != 'exit'):
    palavra = input("\nDigite a palavra para busca ou exit para encerrar: ").lower()
    #Saida do laço de repetição e fim das buscas.#
    if palavra == 'exit':
        print("Fim das buscas.")
        break

    pasta = escanear_pastas(caminho)

    lista_texto = []
    lista_texto2 = []
#Lendo arquivos da pasta#
    for arquivo in pasta:
        temp = []
        arquivo_aberto = caminho + "/" + arquivo
        arq = open(arquivo_aberto, 'r')
        temp.append(arquivo)
        temp.append(arq.read().lower())
        lista_texto2.append(temp)
        arq.close()
#Voltando a linha inicial do arquivo e procurando ''palavra''
    for linha in lista_texto2:
        if palavra in linha[1]:
            lista_texto.append(linha[0])
    
    
#Retirando as repetições da lista de arquivos em que a palavra aparece#
    lista_texto_definitiva = []

    for arquivo in lista_texto:
        if (arquivo in lista_texto_definitiva):
            pass
        else:
            lista_texto_definitiva.append(arquivo)
#Imprimindo na tela#
    if lista_texto == []:
        print("\n")
        print("-" * 60)
        print(f"\nNão existe a palavra {palavra} nos arquivos de texto.\n")
    else:
        print(f"\nA lista de arquivos que contém a palavra {palavra} no texto é:\n")
        print("-" * 60)

    for i in lista_texto_definitiva:
        print(i)
    print("-" * 60)

