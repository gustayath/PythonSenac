'''if simples para teste de indentação'''

temperatura = int (input("Qual a temperatura?"))
if temperatura >= 25:
    print("Está calor!")
else:
     print("Está frio!")

'''Variáveis, explicitando ou casting'''
x = float(5.10)
print(type(x))

'''Desafio if else, par ou impar'''
numero = int (input("Digite um número: "))
if numero % 2:
     print("Este número é ímpar!")
else: 
     print("Este número é par!")

'''Desafio login'''
login = input("Digite o nome do usuário: ")
senha = int(input("Digite sua senha: "))
if login == "Gustavo" and senha == 1234:
     print("Login feito")
else:
     print("Acesso negado")