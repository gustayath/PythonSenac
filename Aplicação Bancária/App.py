'''Variáveis globais'''
usuarios = []
session = []
saldo = []
login_sucesso = False

'''Definição da função saque'''
def saque(s, cpf):
    for conta in saldo:
        if conta ["saldo"] <= 0:
            print("Sem saldo para saque: ")
        elif conta["cpf"] == cpf:
            conta["saldo"] -= s
            return print(f"Seu saldo: {conta["saldo"]}")
            

'''Definição da função saldo'''
def add_saldo(s, cpf):
    for conta in saldo:
        if conta ["cpf"] == cpf:
            conta ["saldo"] += s
            return print(f"Seu saldo: {conta["saldo"]}")
    print("Conta de saldo não encontrada para este CPF. ")

'''Definição da função cadastro'''
def cadastrar():
    nome = input("===== Novo Usuário: ")
    senha = input("===== Senha: ")
    cpf = input("===== CPF: ")
    saldo.append({"saldo": 0.0, "cpf": cpf})
    usuarios.append({"usuario": nome, "senha": senha, "cpf": cpf, "saldo": saldo})
    print(f"\n========== Usuário cadastrado com sucesso! ==========")

'''Definição da função login'''
def login():
    senha = input("===== Senha: ")
    cpf = input("===== CPF: ")
    global login_sucesso
    login_sucesso = False
    for u in usuarios:
        if u["cpf"] == cpf and u["senha"] == senha:
            login_sucesso = True
            global session
            session = {"cpf": u["cpf"], "usuario": u["usuario"]}
            print(f"\n========== Acesso Liberado, seja bem-vindo '{u["usuario"]}' ==========")
            break
        print("===== Falha no login =====")
        break

'''Definição da função para troca de senha''' 
def trocar_senha():
    nome = input("===== Usuário: ")
    senha_atual = input("===== Senha atual: ")
    for user in usuarios:
        if user["usuario"] == nome and user["senha"] == senha_atual:
            user["senha"] = input("===== Nova senha: ")
            print("========== Senha atualizada ==========")
            return
    print("========== Dados inválidos. ==========")

'''Definição da função sistema, onde executará a aplicação'''
def sistema():
    while True:
        global login_sucesso
        global session
        if login_sucesso:
            print("\n 1. Adcionar saldo \n 2. Trocar Senha \n 3. Sair \n 4. Sacar")
            opcao = input("===== Escolha: ")

            match opcao:
                case "1":
                 if login_sucesso:
                    cpf = session ["cpf"]
                    saldo = float(input("===== Informe o valor do depósito: "))
                    add_saldo(saldo, cpf)
                case "2":
                    trocar_senha()
                case "3":
                    print("========== Saindo... ==========")
                    login_sucesso = False
                    session = {}
                    print(session)
                case "4":
                    saldo = float (input("Digite o valor que deseja sacar: R$"))
                    saque(saldo, cpf)
                case _:
                    print("========== Opção inválida. ==========")
        else:
            print("\n 1. Cadastrar \n 2. Login \n 3. Trocar Senha \n 4. Sair")
            opcao = input("===== Escolha: ")

            match opcao:
                case "1":
                    cadastrar()
                case "2":
                    login()
                case "3":
                    trocar_senha()
                case "4":
                    print("========== Saindo... ==========")
                    #global login_sucesso
                    break
                    print(login_sucesso)
                case _:
                    print("========== Opção inválida. ==========")
sistema()