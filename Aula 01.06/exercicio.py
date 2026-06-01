'''Define a função de Atendimento Médico'''
def aph():
    atendimento = int (input("O atendimento é para você ou para terceiros? \nDigite '1' se o atendimento é para você e '2' se o atendimento é para terceiros: " ))
    if atendimento == 1:
        print("Certo, localizamos seu endereço e estamos encaminhando uma equipe para o local.\nMantenha-se calmo.")
    else:
        print("Certo, mantenha a vítima imóvel e certifique-se de que a mesma continue respirando.\n A equipe já está a caminho de seu endereço! ")

'''Define a Função de combate a incêndio'''
def incendio():
    incendio = int (input("O incêndio é em um imóvel ou em algum veículo na estrada? \nDigite '1' para imóvel e '2' para veículo na estrada: "))
    if incendio == 1:
        print("Certo, certifique-se de que não tenha mais ninguém no imóvel e mantenha a calma. A equipe de combate está a caminho!")
    else:
        print("Certo, mantenha distância do veículo e aguarde a chegada da equipe de combate a incêndio! ")
       

while True:
    print("Bem-vindo(a) a central de atendimento! Esta solicitação está sendo rastreada para lhe atendermos com mais rapidez!")
    print("Escolha a opção de atendimento desejado:\n")
    print("[1] Atendimento médico\n[2] Combate a incêndio")
    
    opcao = int(input("Digite a opção desejada: "))
    
    match opcao:
        case 1:
            aph()
        case 2:
            incendio()
            break
    
    