#Exercício de cadastro com Match Case e While

#Função CADASTRO
def cadastro(n):
    print(f"Usuário '{n}' cadastrado com sucesso!")

#Função LOGIN
def login():
    print("Você efetuou o login! ")

#Função SAIR
def sair():
    print("Você saiu! ")

while True:
    print("BEM VINDO AO SITE X \n")
    print("ESCOLHA UMA OPÇÃO DE CADASTRO \n")
    print("[1] CADASTRO \n[2] LOGIN \n[3] SAIR")

    opcao = int (input("Digite a opção desejada: "))

    match opcao:
        case 1:
            nome = input("Qual seu nome? ")
            cadastro(nome)
        case 2:
            login()
        case 3:
            break
            sair()