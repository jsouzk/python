lista_clientes = []

nomes_produtos = []
precos_produtos = []
quantidades_produtos = []

nome = str
quantidade = int
preco = float




# Cadastrar Clientes
# Implementar um sistema que registre clientes.
def cadastrar_cliente(nome):
    while True:
        nome = input("Digite o nome do cliente a ser cadastrado: ")
        
        lista_clientes.append(nome)

        print(f"{nome} cadastrado com sucesso!")
        
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao): "))
        
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opcao Invalida")
            continue
# Fim da funcao onde cadastramos clientes

# Cadastrar Produtos
# Criar um sistema para adicionar produtos ao estoque.
def cadastrar_produto(nome, quantidade, preco):
    while True:
        nome = input("Digite o nome do produto a ser cadastrado: ")
        
        if nome in nomes_produtos:
            print("Produto já cadastrado. Por favor, insira um nome diferente.")
            continue
        
        preco = float(input("Digite o preço do produto: "))
        
        if preco <= 0:
            print("Preço invalido, digite um valor acima de 0.")
            continue
        
        quantidade = int(input("Digite a quantidade do produto: "))
        
        nomes_produtos.append(nome)
        precos_produtos.append(preco)
        quantidades_produtos.append(quantidade)

        print(f"{nome} cadastrado com sucesso no estoque")
        print(f"Valor total: {quantidade * preco}")
        
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao): "))
        
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opcao Invalida")
            continue
# Fim da funcao onde cadastramos produtos

# Comprar Produtos (Repor estoque)
# Criar uma funcionalidade que permita aumentar o estoque de um produto existente
def comprar_produto(nome, quantidade):
    while True:
        nome = input("Digite o nome do produto a ser comprado: ")
        
        if nome not in nomes_produtos:
            print("Produto não encontrado.")
            continue
        
        for indice, conteudo in enumerate(nomes_produtos):
            if conteudo == nome:
                quantidade = int(input("Digite a quantidade a ser comprada: "))
                quantidades_produtos[indice] = quantidades_produtos[indice] + quantidade
                print(f"{quantidade} unidades de {nome} compradas com sucesso!")
                
            
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao): "))
        
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opcao Invalida")
            continue
# Fim da funcao onde compramos produtos para repor o estoque

# Vender Produtos
# Criar uma funcionalidade que permita vender um produto e diminuir seu estoque.
# Pode retornar True se a venda for bem-sucedida e False caso contrário.
def vender_produto(nome, quantidade):
    while True:
        nome = input("Digite o nome do produto a ser vendido: ")
        
        if nome not in nomes_produtos:
            print("Produto não encontrado.")
            continue
        
        for indice, conteudo in enumerate(nomes_produtos):
            if conteudo == nome:
                quantidade = int(input("Digite a quantidade a ser vendida: "))
                
                if quantidade <= 0:
                    print("Quantidade inválida. Por favor, insira um valor positivo.")
                    continue
                
                if quantidade > quantidades_produtos[indice]:
                    print(" A venda não pode ser realizada. Estoque insuficiente.")
                    return False
                
                
                quantidades_produtos[indice] = quantidades_produtos[indice] - quantidade
                print(f"{quantidade} unidades de {nome} vendidas com sucesso!")
                print(f"Valor total: {quantidade * precos_produtos[indice]}")
                return True
                
        
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao): "))
        
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opcao Invalida")
            continue
# Fim da funcao onde vendemos produtos

# Listar Clientes
def listar_clientes():
    if not lista_clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("\nLista de Clientes:")
        for indice, conteudo in enumerate(lista_clientes):
            print(f"ID {indice + 1}: {conteudo}")
# Fim da funcao onde listamos clientes

# Listar Produtos
def listar_produtos():
    if not nomes_produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos:")
        for indice, conteudo in enumerate(nomes_produtos):
            print(f"Nome do produto: {conteudo} \t Preço: {precos_produtos[indice]} R$ \t Quantidade disponivel: {quantidades_produtos[indice]}")
# Fim da funcao onde listamos produtos

# Buscar Produto
# Deve retornar o produto encontrado ou None caso não exista
def buscar_produto(nome):
    nome = input("Digite o nome do produto: ")
    if nome not in nomes_produtos:
        print("Produto não encontrado.")
        return None
    else:
        indice = nomes_produtos.index(nome)
        print(f"Produto encontrado: {nome} \t Preço: {precos_produtos[indice]} \t Quantidade: {quantidades_produtos[indice]}")
        return nome
# Fim da funcao onde buscamos produtos

# Menu interativo
def menu():
    while True:
        print("\n ----- Menu da Loja -----")
        print("1 - Cadastrar Produto")
        print("2 - Comprar produto (Repôr estoque)")
        print("3 - Vender produto")
        print("4 - Listar Produtos")
        print("5 - Cadastrar Cliente")
        print("6 - Listar Clientes")
        print("7 - Buscar Produto")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opções: "))
        
        if op == 0:
            break
        elif op == 1:
            cadastrar_produto(nome, preco, quantidade)
        elif op == 2:
            comprar_produto(nome, quantidade)
        elif op == 3:
            vender_produto(nome, quantidade)
        elif op == 4:
            listar_produtos()
        elif op == 5:
            cadastrar_cliente(nome)
        elif op == 6:
            listar_clientes()
        elif op == 7:
            buscar_produto(nome)
        else:
            print("Opção inválida. Tente novamente.")

menu()