lista_clientes = []

nome_produto = []
preco_produto = []
quantidade_produto = []


def Menu():
    while True:
        print("\n ----- Bem vindo a Loja -----")
        print("1 - Entrar como administrador")
        print("2 - Entrar como cliente")
        print("0 - Sair")
        
        op = int(input("Digite uma das opcoes: "))
        
        if op == 1:
            print("Menu administrador")
        elif op == 2:
            print("Menu Cliente")
        elif op == 0:
            break
        else:
            print("Opcao Invalida")
            continue

# Comprar Produto
def comprar_produto(nome, quantidade):
    for indice, conteudo in enumerate(nome_produto):
        print(f"ID: {indice + 1} \t Nome: {conteudo} \t Telefone: {preco_produto[indice]} \t CPF: {quantidade_produto[indice]}")
        
        nome = input("Digite o ID do produto em que deseja comprar: ")
        
        if nome not in nome_produto:
            print("O produto que voce digitou nao existe...")
        else:
            print("Produto encontrado")
            quantidade = int(input("Digite a quantidade em deseja comprar: "))
            
            quantidade_produto.append(quantidade)
    
# Fim do Comprar Produto

# Listar Produto
def listar_produto():
    for indice, conteudo in enumerate(nome_produto):
        print(f"ID: {indice + 1} \t Nome: {conteudo} \t Telefone: {preco_produto[indice]} \t CPF: {quantidade_produto[indice]}")
        
# Fim Listar Produto

# Cadastro de Produtos
def adicionar_produto(nome, preco, quantidade):
    while True:
        nome = input("Digite o nome do produto a ser cadastrado: ")
        preco = float(input("Digite o preco: "))
        quantidade = int(input("Digite a quantidade: "))
        
        nome_produto.append(nome)
        preco_produto.append(preco)
        quantidade_produto.append(quantidade)
        
        print(f"{nome} cadastrado com sucesso no estoque!")
        
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao)"))
        
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opcao Invalida")
            continue
# Fim do cadastro de produtos

# Cadastro de Clientes
def cadastrar_cliente(nome):
    while True:
        nome = input("Digite o nome do cliente a ser cadastrado: ")
        
        lista_clientes.append(nome)

        print(f"{nome} cadastrado com sucesso!")
        
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao)"))
        
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opcao Invalida")
            continue
# Fim do cadastro de clientes

# Menus 
def cliente():
    while True:
        print("\n ----- Menu do Cliente -----")
        print("1 - Comprar Produto")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opcoes: "))
        
        if op == 1:
            print("Comprar Produto")
        elif op == 0:
            break
        else:
            print("Opcao Invalida")
            continue
            
def administrador():
    while True:
        print("\n ----- Menu do Administrador -----")
        print("1 - Cadastrar Produto (estoque)")
        print("2 - Vender Produto")
        print("3 - Listar Produtos")
        print("4 - Listar Clientes")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opcoes: "))
        
        if op == 1:
            print("Cadastrar Produto")
        elif op == 2:
            print("Vender Produto")
        elif op == 3:
            print("Listar Produto")
        elif op == 4:
            print("Listar Clientes")
        elif op == 0:
            break
        else:
            print("Opcao Invalida")
            continue