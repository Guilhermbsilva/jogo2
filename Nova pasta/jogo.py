import random

palavras = ["pintos" , "buceta", "recebe", "coisar", "cagado"]

def jogo():

    print("ADIVINHE A PALAVRA!\nSUA PALAVRA TEM 6 LETRAS!")

    adivinhar = random.choice(palavras)
    print(adivinhar)
    tentativa = input()

    for i in list(adivinhar):
        if i == 6:
            break
        for j in list(tentativa):
            if j == 6:
                break

    certas = [elemento for elemento in adivinhar if elemento in tentativa]
    
    while list(tentativa) != list(adivinhar):
            
        if tentativa[0] == adivinhar[0]:
            print(tentativa[0] , "🟩")
    
        if tentativa[0] != adivinhar[0] and tentativa[0] in list(certas):
            print(tentativa[0], "🟧")

        if tentativa[0] not in certas and tentativa[0] != adivinhar[0]:
            print(tentativa[0], "🟥")

        if tentativa[1] == adivinhar[1]:
            print(tentativa[1] , "🟩")

        if tentativa[1] != adivinhar[1] and tentativa[1] in list(certas):
            print(tentativa[1], "🟧")

        if tentativa[1] not in certas and tentativa[1] != adivinhar[1]:
            print(tentativa[1], "🟥")

        if tentativa[2] == adivinhar[2]:
            print(tentativa[2] , "🟩")

        if tentativa[2] != adivinhar[2] and tentativa[2] in list(certas):
            print(tentativa[2], "🟧")

        if tentativa[2] not in certas and tentativa[2] != adivinhar[2]:
            print(tentativa[2], "🟥") 

        if tentativa[3] == adivinhar[3]:
            print(tentativa[3] , "🟩")

        if tentativa[3] != adivinhar[3] and tentativa[3] in list(certas):
            print(tentativa[3], "🟧")

        if tentativa[3] not in certas and tentativa[3] != adivinhar[3]:
            print(tentativa[3], "🟥")

        if tentativa[4] == adivinhar[4]:
            print(tentativa[4] , "🟩")

        if tentativa[4] != adivinhar[4] and tentativa[4] in list(certas):
            print(tentativa[4], "🟧")

        if tentativa[4] not in certas and tentativa[4] != adivinhar[4]:
            print(tentativa[4], "🟥")

        if tentativa[5] == adivinhar[5]:
            print(tentativa[5] , "🟩")

        if tentativa[5] != adivinhar[5] and tentativa[5] in list(certas):
            print(tentativa[5], "🟧")

        if tentativa[5] not in certas and tentativa[5] != adivinhar[5]:
            print(tentativa[5], "🟥")
        
        if list(tentativa) != list(adivinhar):
            tentativa = input()
            


def menu():

    print("======= BEM VINDO AO TERMO =======")
    print("======= ESCOLHA UMA OPÇÃO: =======")
    print("========== 1 - JOGAR =============\n========== 2 - SAIR ==============\n")

    escolha = int(input())
    if escolha == 1:
        jogo()
    else:
        print("Saindo...")
        exit()

menu()