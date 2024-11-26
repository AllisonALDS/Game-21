import random

def cartas():
    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return random.choice(card)

def singleplayer():
    cartas_atual = 0
    cartas_atual_maquina = 0
    cartasd = []



    print(f"--- MODO SINGLEPLAYER ---")
    print(f"Voce começou com {cartas_atual}")
    while True:

            print(f"Pontuação : {cartas_atual}")
            escolher = int(input("Deseja Pegar uma Carta? 1- Sim / 2- Não"))
            if escolher == 1:
                carta_sorteada = cartas()
                cartasd.append(carta_sorteada)
                print(f"Cartas Atual: {cartasd}")
                cartas_atual = cartas_atual + carta_sorteada
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
    players = 0
    jogadores = []
    pontuacao = []
    jogador_vencedor = 0
    pontuacao_maior = 0

    print(f"--- MODO Multiplayer ---")
    qtd_players = int(input("Quantidade de Jogadores: "))
    players = qtd_players

    for a in range(0, players + 1):
        num = 0
        pontuacao.append(num)

    for o in range(1, players + 1):
        jogadores.append(o)

    for i in range(0, players):


        while True:

            print(f"Turno do Jogador {jogadores[i]}")
            print(f"Pontuação : {pontuacao[i]}")

            escolher = int(input("Deseja Pegar uma Carta? 1- Sim / 2- Não"))
            if escolher == 1:
                carta_sorteada = cartas()
                pontuacao[i] += carta_sorteada
            elif escolher == 2:
                break

            if pontuacao[i] <= 21 and pontuacao[i] > pontuacao_maior:
                jogador_vencedor = jogadores[i] 
                pontuacao_maior = pontuacao[i]
            elif pontuacao[i] > 21:
                print("Voce Estorou! ")
                break


    for k, p in zip(jogadores, pontuacao):
        print(f"Jogador: {k} pontuação {p}")
            

    print(f"--- VENCEDOR --  \nJogador: {jogador_vencedor} : Pontuação: {pontuacao_maior}")

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