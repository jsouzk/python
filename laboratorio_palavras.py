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

# Menu Contagens e Busca
def contagem(a):
    letra = input("Digite uma letra: ")
    print(f"Há {a.lower().count(letra)} letras '{letra}' na frase/palavra que você escreveu.")

def encontrar_posicao(a):
    l = input("Digite uma letra que deseja encontrar: ")
    
    for indice, letra in enumerate(a):
        if letra == (l):
            print(f"Há uma letra '{l}' na posição {indice} do vetor de caractere")
            
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
# Fim do Menu Contagens e Busca

# menu fatiamento e inversao
def fatiar_string(a):
    print(f"As tres primeras letras da string: {(a[0:3])}")
    print(f"Pegando do terceiro caractere até o final: {(a[2:])}") 
    print(f"Pegando um caractere a cada dois: {(a[::2])}")

def inverter_string(a):
    string_invertida = a[::-1]
    print(string_invertida)

def menu_fatiamento_inversao():
    
    algo = input("Digite algo: ")
    
    while True:
        print("1 - Fatiar string")
        print("2 - Inverter a string")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opções: "))
        
        if op == 1:
            fatiar_string(algo)
        elif op == 2:
            inverter_string(algo)
        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida. Tente Novamente")   
# fim do menu fatiamento e inversao

# menu substituicoes e remocoes
def eliminar_espacos(a):
    print(a.strip())
    
def eliminar_letras(a):
    remover_letra = input("Digite a letra que deseja remover: ")
    
    print(a.replace(remover_letra, ""))
    
def trocar_caractere(a):
    letra_substituir = input("Digite a letra que deseja substituir: ")
    letra_substituta = input("Digite a letra que deseja colocar no lugar: ")
    
    print(a.replace(letra_substituir, letra_substituta))
    
def menu_substituicoes_remocoes():
    
    algo = input("Digite algo: ")
    
    while True:
        print("1 - Trocar caractere")
        print("2 - Eliminar letras especificas")
        print("3 - Remover espaços que estao sobrando")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opçoes: "))
        
        if op == 1:
            trocar_caractere(algo)
        elif op == 2:
            eliminar_letras(algo)
        elif op == 3:
            eliminar_espacos(algo)
        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida. tente novamente")
# fim do menu substituicoes e remocoes

# menu verificação de conteudo
def menu_verificacao_conteudo():
    
    algo = input("Digite algo: ")
    
    while True:
        print("1 - Verificar se a string é composta somente por letras")
        print("2 - Verificar se a string é composta somente por numeros")
        print("3 - Verificar se string só tem espaços")
        print("4 - Verificar se todas as letras da string estão em minusculo")
        print("5 - Verificar se todas as letras da string estão em maiusculo")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opções: "))
        
        if op == 1:
            print(algo.isalpha())
        elif op == 2:
            print(algo.isdigit())
        elif op == 3:
            print(algo.isspace())
        elif op == 4:
            print(algo.islower())
        elif op == 5:
            print(algo.isupper())
        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida. Tente Novamente")        
# Fim do menu verificação de conteudo
def converter_string(a):
    lista = list(a)
    print(f"A lista da string ficará assim: {lista}")

def menu_conversao_lista():
    algo = input("Digite algo: ")
    
    while True:
        print("1 - Converter string para lista")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opções: "))
        
        if op == 1:
            converter_string(algo)
        elif op == 0:
            print("Saindo...")
            break
        else:
            print('Opção Invalida. Tente novamente')
# Fim do menu converter para lista
def unir_palavras(a):
    substituicao = input("Digite o que deseja colocar no lugar dos espaços das palavras que foram separadas: ")
    print(substituicao.join(a.split()))

def menu_divisao_juncao():
    algo = input("Digite algo: ")
    
    while True:
        print("1 - Separar em palavras")
        print("2 - Unir elas de formas diferentes")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opções: "))
        
        if op == 1:
            print(f"A separação da string ficara da seguinte forma: {algo.split()}")
        elif op == 2:
            unir_palavras(algo)
        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida. Tente Novamente.")
# Fim do menu divisao e juncao
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
            menu_fatiamento_inversao()
        elif escolha == 3:
            menu_substituicoes_remocoes()
        elif escolha == 4:
            menu_verificacao_conteudo()
        elif escolha == 5:
            menu_contagens_busca()
        elif escolha == 6:
            menu_conversao_lista()
        elif escolha == 7:
            menu_divisao_juncao()
        elif escolha == 0:
            print("Saindo...")
            break
        else:
            print("Opção Invalida")
        
menu()