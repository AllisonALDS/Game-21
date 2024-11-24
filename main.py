import random

def cartas():
    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return random.choice(card)

def singleplayer():
    cartas_atual = 0
    cartas_atual_maquina = 0

    print(f"--- MODO SINGLEPLAYER ---")
    print(f"Voce começou com {cartas_atual}")
    while True:

            
            print(f"Pontuação : {cartas_atual}")
            escolher = int(input("Deseja Pegar uma Carta? 1- Sim / 2- Não"))
            if escolher == 1:
                cartas_atual = cartas_atual + cartas()
            elif escolher == 2:
                while True:     
                    if cartas_atual_maquina < 17:
                        cartas_atual_maquina = cartas_atual_maquina + cartas()
                    else:
                        break
                if cartas_atual > cartas_atual_maquina:
                    print(f"\nSeus Pontos: {cartas_atual}")
                    print(f"Pontos Maquinas: {cartas_atual_maquina}")
                    print("Voce Venceu! \n")
                    break
                elif cartas_atual < cartas_atual_maquina:
                    print(f"\nSeus Pontos: {cartas_atual}")
                    print(f"Pontos Maquinas: {cartas_atual_maquina}")
                    print("Maquina Venceu! \n")
                    break
                else:
                    print(f"\nSeus Pontos: {cartas_atual}")
                    print(f"Pontos Maquinas: {cartas_atual_maquina}")
                    print("Empate! \n")
                    break

def multiplayer():
    pass

def jogar():
    while True:     
        print("BEM VINDO AO JOGO 21")
        op = int(input("1- Multiplayer 2- Singleplayer"))
        if op == 1:
            multiplayer()
        elif op == 2:
            singleplayer()
        else:
            continue

jogar()