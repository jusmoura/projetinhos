import random

caverna = {
    1: [2, 6], 2: [1, 3, 7], 3: [2, 4, 8], 4: [3, 5, 9],
    5: [4, 10], 6: [1, 7], 7: [2, 6, 8, 12], 8: [3, 7, 9, 13],
    9: [4, 8, 10, 14], 10: [5, 9, 15], 11: [6, 12, 16], 12: [7, 11, 13, 17],
    13: [8, 12, 14, 18], 14: [9, 13, 15, 19], 15: [10, 14, 20],
    16: [11, 17], 17: [12, 16, 18], 18: [13, 17, 19],
    19: [14, 18, 20], 20: [15, 19]
}

player = random.randint(1, 20)
wumpus = random.randint(1, 20)
while wumpus == player:
    wumpus = random.randint(1, 20)

pits = random.sample([i for i in range(1, 21) if i != player and i != wumpus], 2)
bats = random.sample([i for i in range(1, 21) if i != player and i != wumpus and i not in pits], 2)

salas_visitadas = set()

def mostrar_caverna():
    for i in range(1, 21):
        simbolo = f"{i:02}"
        if i == player:
            simbolo = "P"
        elif i in salas_visitadas:
            simbolo = "X"
        
        print(f"{simbolo:^4}", end="") 
        if i % 5 == 0:
            print()  

def jogar():
    global player, wumpus, pits, bats
    flechas = 5
    print("Bem-vindo ao Wumpus!")
    
    while True:
        print(f"\nVocê está na sala {player}. Salas conectadas: {caverna[player]}")
        mostrar_caverna()
        print(f"Flechas restantes: {flechas}")

        salas_visitadas.add(player)
        
        if len(salas_visitadas) == 1:
            print("Iniciando sua aventura...")

        if any(adj in caverna[player] for adj in [wumpus]):
            print("Você sente um fedor terrível.")
        if any(adj in caverna[player] for adj in pits):
            print("Você sente uma brisa vinda de uma sala próxima.")
        if any(adj in caverna[player] for adj in bats):
            print("Você ouve um bater de asas.")

        ação = input("Você deseja (M)over ou (A)tacar? ").strip().upper()

        if ação == 'M':
            destino = int(input("Para qual sala deseja se mover? "))
            if destino in caverna[player]:
                player = destino
                if player == wumpus:
                    print("O Wumpus te devorou! Fim de jogo.")
                    break
                elif player in pits:
                    print("Você caiu em um buraco sem fundo! Fim de jogo.")
                    break
                elif player in bats:
                    print("Morcegos te pegaram e te jogaram em outra sala!")
                    player = random.randint(1, 20)
            else:
                print("Movimento inválido.")
        elif ação == 'A':
            if flechas == 0:
                print("Você não tem mais flechas!")
                continue
            alvo = int(input("Para qual sala deseja atirar a flecha? "))
            flechas -= 1
            if alvo == wumpus:
                print("Você acertou o Wumpus! Parabéns, você venceu!")
                break
            else:
                print("Errou! O Wumpus acordou...")
                if random.random() < 0.75:
                    wumpus = random.choice(caverna[wumpus])
                    print("O Wumpus se moveu!")
                else:
                    print("O Wumpus ficou onde está.")
                if flechas == 0:
                    print("Você usou todas as suas flechas! Fim de jogo.")
                    break
        else:
            print("Comando inválido.")

if __name__ == "__main__":
    jogar()
