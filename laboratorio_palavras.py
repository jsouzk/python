string = []

# Transformaçao de caixa
def deixar_maiuscula(f):
    print(f.upper())

def deixar_minuscula(f):
    print(f.lower())

def capitalizar(f):
    print(f.capitalize())

def estilo_titulo(f):
    print(f.title())

def menu_tranformacao_de_caixa():
    frase = input("Digite algo: ")
    while True:

        print("1 - Deixar tudo em maiusculo")
        print("2 - Deixar tudo em minusculas")
        print("3 - Capitalizar")
        print("4 - Aplicar o estilo titulo")
        print("0 - Sair")

        op = int(input("Escolha uma das opções: "))

        if op == 1:
            deixar_maiuscula(frase)
        elif op == 2:
            deixar_minuscula(frase)
        elif op == 3:
            capitalizar(frase)
        elif op == 4:
            estilo_titulo(frase)
        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida")
# Fim da transformação de caixa
def contagem(a):
    letra = input("Digite uma letra: ")
    print(f"Há {a.count(letra)} letras '{letra}' na frase/palavra que você escreveu.")

def encontrar_posicao(a):
    letra = input("Digite uma letra que deseja encontrar: ")
    posicao = a.find(letra)
    print(f"A letra {letra} se encontra na posição {posicao} do vetor de caracteres.")

def menu_contagens_busca():
    algo = input("Digite algo: ")
    while True:
        print("1 - Contagem de caractere")
        print("2 - Encontrar posição de certo caractere")
        print("0 - Sair")

        op = int(input("Digite uma das opções acima: "))
        
        if op == 1:
            contagem(algo)
        elif op == 2:
            encontrar_posicao(algo)
        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida")

def menu():
    while True:
        print("\n----- Menu -----")
        print("1 - Transformações de caixa")
        print("2 - Fatiamento e inversão")
        print("3 - Substituições e remoções")
        print("4 - Verificações de conteudo")
        print("5 - Contagens e busca")
        print("6 - Conversão para lista")
        print("7 - Divisão e junçao de palavras")
        print("0 - Sair")

        escolha = int(input("Digite uma das opçoes acima: "))
        if escolha == 1:
            menu_tranformacao_de_caixa()
        elif escolha == 2:
            print("fatiamento e inversao")
        elif escolha == 3:
            print("d")
        elif escolha == 4:
            print("kfj")
        elif escolha == 5:
            print("def")
        elif escolha == 6:
            print("dwsd")
        elif escolha == 7:
            print("ddw")
        elif escolha == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida")
        
menu()