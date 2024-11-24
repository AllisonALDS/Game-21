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

        if cartas_atual > 21:
            print("Voce Estorou! Maquina Venceu ")
            break
        elif cartas_atual < 21:
            
            print(f"Pontuação : {cartas_atual}")
            escolher = int(input("Deseja Pegar uma Carta? 1- Sim / 2- Não"))
            if escolher == 1:
                cartas_atual = cartas_atual + cartas()
            elif escolher == 2:
                pass

def multiplayer():
    pass

def jogar():
    while True:     
        op = int(input("1- Multiplayer 2- Singleplayer"))
        if op == 1:
            multiplayer()
        elif op == 2:
            singleplayer()
        else:
            continue

jogar()