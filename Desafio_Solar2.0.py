nomes_pacotes = ["Essencial", "Premium", "Luxo" ]
valores_pacotes = [2000, 3500, 5000]
limites_convidados = [50, 100, 150]

nomes_depoimentos = ["Julio", "José", "Maria"]
depoimentos = ["Lugar lindo e atendimento impecável!", "Festa perfeita do início ao fim!", "Ambiente maravilhoso, recomendo muito!"]

nomes = []
emails = []
mensagens = []

contador_visitas = 0

def ver_pacotes():
    global nomes_pacotes, valores_pacotes
    print("\n ----- Pacotes Disponiveis -----")
    for indice, conteudo in enumerate(nomes_pacotes):
        print(f"{indice + 1}. \t Nome do pacote: {conteudo} \t Valor do pacote: R${valores_pacotes[indice]}")

def calcular_orcamentos(pacote_escolhido, numero_convidados):
    global valores_pacotes, limites_convidados
    valor_base = valores_pacotes[pacote_escolhido]
    limite = limites_convidados[pacote_escolhido]
    
    if numero_convidados > limite:
        limite_excedido = numero_convidados - limite
        valor_total = valor_base + (limite_excedido * 30)
    else:
        valor_total = valor_base
    return valor_total

def simular_orcamentos():
    global limites_convidados
    while True:
        ver_pacotes()
        
        pacote_escolhido = int(input("\nDigite o pacote que deseja: "))
        if pacote_escolhido < 1 or pacote_escolhido > len(nomes_pacotes):
            print("O número do pacote que você digitou não existe.")
            continue
        
        numero_convidados = int(input("Digite a quantidade de convidados: "))
        if numero_convidados < 0:
            print("Quantidade de convidados inválida.")
            continue
        
        valor_total = calcular_orcamentos(pacote_escolhido - 1, numero_convidados)
        
        print(f"O valor estimado para o pacote {nomes_pacotes[pacote_escolhido - 1]} é de: R${valor_total}")
        
        if numero_convidados > limites_convidados[pacote_escolhido - 1]:
            limite_excedido = numero_convidados - limites_convidados[pacote_escolhido - 1]
            print(f"{limite_excedido} convidados adicionais foram cobrados")
            
            comprar = int(input("\nDeseja comprar esse pacote? (1 - Sim / 2 - Nao): "))
            if comprar == 1:
                print("\n ----- Formas de Pagamento -----")
                print("1 - Dinheiro")
                print("2 - Cartao de Credito")
                print("3 - Cartao de Debito")
                print("4 - Pix")
                
                forma_pagamento = int(input("Escolha a forma de pagamento: "))
                
                if forma_pagamento == 1:
                    valor_pago = float(input("Digite o valor entregue: R$"))
                    
                    if valor_pago < valor_total:
                        print("Valor insuficiente. Compra cancelada.")
                    else:
                        troco = valor_pago - valor_total
                        print(f"Compra confirmada! Troco: {troco:.2f}")
                elif forma_pagamento == 2 or forma_pagamento == 3 or forma_pagamento == 4:
                    print("Compra realizada")
                else:
                    print("Forma de pagamento invalida. Compra cancelada")
                
        continuar = int(input("Deseja continuar a simular orcamentos? (1 - Sim / 2 - Não): "))
        if continuar == 1:
            print("Continuando...")
        elif continuar == 2:
            break
        else:
            print("Opção inválida")

def ver_depoimentos():
    global nomes_depoimentos, depoimentos
    print("\n ----- Depoimentos ----- ")
    for indice, conteudo in enumerate(nomes_depoimentos):
        print(f"{indice + 1}. {conteudo} - {depoimentos[indice]}")
        
def enviar_mensagem(n, e, msg):
    global nomes, emails, mensagens
    nomes.append(n)
    emails.append(e)
    mensagens.append(msg)
    print("Mensagem enviada com sucesso")

def listar_mensagens():
    global nomes, mensagens
    if not nomes:
        print("\nAinda não há nenhuma mensagem...")
        return
    print("\n ----- Mensagens Enviadas ----- ")
    for indice, conteudo in enumerate(nomes):
        print(f"{indice + 1}. Nome da Pessoa: {conteudo} - {mensagens[indice]}")

def adicionar_depoimento(user, depoi):
    global nomes_depoimentos, depoimentos
    nomes_depoimentos.append(user)
    depoimentos.append(depoi)
    print("Depoimento enviado com sucesso")
    

def menu():
    global contador_visitas
    contador_visitas = contador_visitas + 1
    while True:
        print("\n ----- Solar das Estrelas -----")
        print("1 - Ver pacotes disponiveis")
        print("2 - Simular orcamento")
        print("3 - Ver depoimento")
        print("4 - Enviar mensagem de contato")
        print("5 - Listar mensagens")
        print("6 - Adicionar depoimento")
        print("0 - Sair")
        
        op = int(input("Escolha uma das opcoes: "))
        
        if op == 1:
            ver_pacotes()
        elif op == 2:
            simular_orcamentos()
        elif op == 3:
            ver_depoimentos()
        elif op == 4:
            while True:
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                mensagem = input("Digite sua mensagem: ")
                enviar_mensagem(nome, email, mensagem)
                
                continuar = int(input("Deseja continuar a enviar mensagens? (1 - Sim / 2 - Nao): "))
                
                if continuar == 1:
                    print("Continuando...")
                elif continuar == 2:
                    break
                else:
                    print("Opção Invalida")
        elif op == 5:
            listar_mensagens(usuario, depoimento)
        elif op == 6:
            usuario = input("Digite seu nome: ")
            depoimento = input("Digite seu depoimento: ")
            adicionar_depoimento(usuario, depoimento)
        elif op == 0:
            print("Saindo do sistema...")
            print(f"O sistema foi acessado {contador_visitas} vezes.")
            break
        else:
            print("Opção Invalida")
            
menu()