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

def menu_fatiamento_inversao():
    algo = input("Digite algo: ")
    while True:
        print("1 - Fatiamento")
        

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
        elif escolha == 8:
            print("Saindo...")
            break
        else:
            print("Opção Invalida")
        
menu()