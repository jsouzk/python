lista_clientes = []

nome_produtos = []
precos_produtos = []
quantidades_produtos = []

# Cadastro de Clientes
def cadastrar_cliente():
    while True:
        nome = input("Digite o nome do cliente a ser cadastrado: ")
        
        if nome in lista_clientes:
            print("Ja tem um cliente cadastrado com esse nome. Insira um nome diferente.")
            continue
        
        lista_clientes.append(nome)
        
        print(f"{nome} cadastrado com sucesso!")
        
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao): "))
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
# Fim da função onde cadastramos clientes

# Cadastro de Produtos no estoque
def adicionar_produto():
    while True:
        nome = input("Digite o nome do produto que sera cadastrado: ")
        
        if nome in nome_produtos:
            print("Este produto ja esta cadastrado. Digite um nome diferente.")
            continue
        
        preco = float(input("Digite o preço do produto: "))
        
        if preco < 0:
            print("Preço inválido. O valor nao pode ser negativo.")
            continue
        
        quantidade = int(input("Digite a quantidade do produto: "))
        
        nome_produtos.append(nome)
        precos_produtos.append(preco)
        quantidades_produtos.append(quantidade)
        
        print(f"{nome} cadastrado com sucesso")
        
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao): "))
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
# Fim da função onde cadastramos produtos no estoque

# Compras de produtos para reposição de estoque
def comprar_produto():
    while True:
        print("\n ----- Reposição de Estoque ----- \n")
        listar_produtos()

        nome = input("Digite o nome do produto que será comprado para reposição de estoque: ")

        if nome not in nome_produtos:
            print("Produto não encontrado.")
            continue

        for indice, conteudo in enumerate(nome_produtos):
            if conteudo == nome:
                quantidade = int(input("Digite a quantidade a ser comprada para o estoque: "))
                quantidades_produtos[indice] = quantidades_produtos[indice] + quantidade
                print(f"{quantidade} unidades de {nome} compradas.")
                print(f"Quantidade atualizada no estoque : {quantidades_produtos[indice]} unidades.")
                break

        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Não): "))
        if continuar == 1:
            continue
        elif continuar == 2:
            break
        else:
            print("Opção inválida.")
# Fim da função onde compramos produtos para reposição de estoque

# Vendas de produtos
def vender_produto():
    while True:
        print("\n ----- Vendas de Produtos ----- \n")
        for indice, conteudo in enumerate(nome_produtos):
            print(f"Nome do produto: {conteudo} \t Preço: {precos_produtos[indice]} R$ \t Quantidade disponivel: {quantidades_produtos[indice]}")
        
        nome = input("Digite o nome do produto que sera vendido: ")
        
        if nome not in nome_produtos:
            print("Produto não encontrado.")
            continue
        
        for indice, conteudo in enumerate(nome_produtos):
            if conteudo == nome:
                quantidade = int(input("Digite a quantidade a ser vendida: "))
                
                if quantidade > quantidades_produtos[indice]:
                    print("Quantidade insuficiente em estoque.")
                    return False
                elif quantidade <= 0:
                    print("Quantidade inválida. Por favor, insira um valor positivo.")
                    continue
                else:
                    print(f"Valor total a ser pago: {quantidade * precos_produtos[indice]} R$")
                    
                    print("\n ----- Formas de Pagamento -----")
                    print("1 - Dinheiro")
                    print("2 - Cartão de Crédito")
                    print("3 - Cartão de Débito")
                    print("4 - Pix")
                    
                    forma_pagamento = int(input("Escolha a forma de pagamento: "))
                    
                    if forma_pagamento == 2:
                        print("Pago com cartão de crédito.")
                    elif forma_pagamento == 3:
                        print("Pago com cartão de débito.")
                    elif forma_pagamento == 4:
                        print("Pago com Pix.")
                    elif forma_pagamento == 1:
                        dinheiro = float(input("Digite o valor pago em dinheiro: "))
                        valor_total = quantidade * precos_produtos[indice]
                        
                        if dinheiro < valor_total:
                            print("Falta de dinheiro. A venda não pode ser realizada.")
                            continue
                        elif dinheiro > valor_total:
                            troco = dinheiro - valor_total
                            print(f"Troco: {troco} R$")
                    else:
                        print("Forma de pagamento inválida. Tente novamente.")
                        continue
                    # Atualiza a quantidade do produto vendido
                    quantidades_produtos[indice] = quantidades_produtos[indice] - quantidade
                    print(f"{quantidade} unidades de {nome} vendidas com sucesso!")
                    return True
                
        continuar = int(input("Deseja continuar? (1 - Sim / 2 - Nao): "))
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opcao Invalida")
            continue

# Fim da função onde vendemos produtos 

# Listar Clientes
def listar_clientes():
    if not lista_clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("\nLista de Clientes:")
        for indice, conteudo in enumerate(lista_clientes):
            print(f"ID {indice + 1}: {conteudo}")
# Fim da função onde listamos clientes

# Listar Produtos
def listar_produtos():
    if not nome_produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos:")
        for indice, conteudo in enumerate(nome_produtos):
            print(f"Nome do produto: {conteudo} \t Preço: {precos_produtos[indice]} R$ \t Quantidade disponivel: {quantidades_produtos[indice]}")

def buscar_produto():
    print("\nLista de Produtos:")
    for indice, conteudo in enumerate(nome_produtos):
        print(f"Nome do produto: {conteudo} \t Preço: {precos_produtos[indice]} R$ \t Quantidade disponivel: {quantidades_produtos[indice]}")

    nome = input("Digite o nome do produto que deseja buscar no estoque: ")

    for indice, conteudo in enumerate(nome_produtos):
        if conteudo == nome:
            print(f"Produto encontrado: {conteudo} \t Preço: {precos_produtos[indice]} R$ \t Quantidade disponivel: {quantidades_produtos[indice]}")
            return conteudo

    print("Produto não encontrado.")
    return None
# Fim da função onde buscamos produtos

# Menu Principal
def menu():
    while True:
        print("\n ----- Menu Principal -----")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Comprar Produto para Reposição de Estoque")
        print("4 - Vender Produto")
        print("5 - Listar Clientes")
        print("6 - Listar Produtos")
        print("7 - Buscar Produto")
        print("8 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            adicionar_produto()
        elif opcao == 3:
            comprar_produto()
        elif opcao == 4:
            vender_produto()
        elif opcao == 5:
            listar_clientes()
        elif opcao == 6:
            listar_produtos()
        elif opcao == 7:
            buscar_produto()
        elif opcao == 8:
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
    


            
                        