def login():
    while True:
        login = "julio"
        password = "julio123"
        
        usuario = input("Digite o usuario: ")
        senha = input("Digite a senha: ")
        
        if usuario.strip().lower() == login and senha.strip().lower() == password:
            print("Acesso permitido")
            break
        elif usuario.strip().lower() != login and senha.strip().lower() == password:
            print("Usuario incorreto\nTente Novamente\n")
        elif usuario.strip().lower() == login and senha.strip().lower() != password:
            print("Senha incorreta\nTente Novamente\n")
        else:
            print("Senha e usuario errado\nTente novamente\n")
    
login()