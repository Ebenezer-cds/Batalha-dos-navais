# ===== MATRIZES DO JOGO (Aluno A) =====
# navios1/navios2: frota de cada jogador (0 = água, 1 = submarino, 2 = encouraçado, 3 = fragata, 4 = porta-aviões)
# tiros1/tiros2: tiros dados por cada jogador (. = não atirou, X = acertou, o = água)

navios1 = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]

navios2 = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]

tiros1 = [[".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."]]

tiros2 = [[".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "."]]

# ===== VARIÁVEIS DE CONTROLE =====
turno = 1


def todos_navios_afundados(navios, tiros):
    """Retorna True quando cada parte de navio já recebeu um acerto."""
    for linha in range(6):
        for coluna in range(6):
            if navios[linha][coluna] > 0 and tiros[linha][coluna] != "X":
                return False

    return True


# ===== REGRAS =====
print("======================= Bem-vindo ao batalha dos navais! ======================")
print("Aqui vai as regras do nosso jogo, você terá que adivinhar onde estão os navios do seu adversário, cada jogador tem 4 navios, sendo eles: 1 porta-aviões, 1 encouraçado, 1 submarino e 1 fragata.")
print("O tamanho de cada navio é o seguinte: porta-aviões = 4, fragata = 3, encouraçado = 2 e submarino = 1.")
print("Tem um regra especial, o navio encouraçado é blindado, ou seja, pra ele afundar, você precisa acertar ele 2 vezes.")
print("O tamanho do tabuleiro é de 6x6, sendo que cada jogador terá um tabuleiro para colocar seus navios e outro para tentar acertar os navios do adversário.")
print("Na tela vai aparecer o tabuleiro dos seus navios e, no tabuleiro da esquerda, os tiros que você deu no adversário.")
print("Símbolos: . = casa ainda não atirada | X = acertou um navio | o = água | ~ = água no seu tabuleiro | 1, 2, 3, 4 = partes dos seus navios (1 = submarino, 2 = encouraçado, 3 = fragata, 4 = porta-aviões).")
print("Como atirar: o jogo vai pedir primeiro a LINHA e depois a COLUNA, uma de cada vez.")
print("Digite apenas um número de 1 a 6 e aperte Enter. Não use vírgula, ponto nem espaço.")

# ===== POSICIONAMENTO DOS SUBMARINOS =====

# Cada jogador escolhe a posição do seu submarino
for jogador in range(1, 3):

    if jogador == 1:
        tabuleiro_atual = navios1
    else:
        tabuleiro_atual = navios2

    print("\nJogador", jogador, "- posicione seu submarino.")

    posicionado = False

    while posicionado == False:
        # Confere se a linha escolhida está entre 1 e 6
        linha_valida = False
        while linha_valida == False:
            entrada_linha = input("Digite a linha (1 a 6): ")
            for numero in range(1, 7):
                if entrada_linha == str(numero):
                    linha = numero - 1
                    linha_valida = True
            if linha_valida == False:
                print("Linha inválida! Digite um número de 1 a 6.")

        # Confere se a coluna escolhida está entre 1 e 6
        coluna_valida = False
        while coluna_valida == False:
            entrada_coluna = input("Digite a coluna (1 a 6): ")
            for numero in range(1, 7):
                if entrada_coluna == str(numero):
                    coluna = numero - 1
                    coluna_valida = True
            if coluna_valida == False:
                print("Coluna inválida! Digite um número de 1 a 6.")

        # Verifica se a casa está vazia
        if tabuleiro_atual[linha][coluna] == 0:
            tabuleiro_atual[linha][coluna] = 1
            posicionado = True
            print("Submarino posicionado com sucesso!")
        else:
            print("Essa posição já está ocupada! Escolha outra.")

    if jogador == 1:
        input("\nPasse a vez ao jogador 2 e pressione Enter.")
        print("\n" * 35)

print("\nPosicionamento dos submarinos concluído!")

# ===== POSICIONAMENTO DAS FRAGATAS =====

input("\nPasse a vez ao jogador 1 para posicionar a fragata e pressione Enter.")
print("\n" * 35)

for jogador in range(1, 3):
    if jogador == 1:
        tabuleiro_atual = navios1
    else:
        tabuleiro_atual = navios2

    print("\nJogador", jogador, "- posicione sua fragata de 3 casas.")
    posicionado = False

    while posicionado == False:
        linha_valida = False
        while linha_valida == False:
            entrada_linha = input("Linha inicial da fragata (1 a 6): ")
            for numero in range(1, 7):
                if entrada_linha == str(numero):
                    linha = numero - 1
                    linha_valida = True
            if linha_valida == False:
                print("Linha inválida! Digite um número de 1 a 6.")

        coluna_valida = False
        while coluna_valida == False:
            entrada_coluna = input("Coluna inicial da fragata (1 a 6): ")
            for numero in range(1, 7):
                if entrada_coluna == str(numero):
                    coluna = numero - 1
                    coluna_valida = True
            if coluna_valida == False:
                print("Coluna inválida! Digite um número de 1 a 6.")

        direcao_valida = False
        while direcao_valida == False:
            direcao = input("Direção (1 = horizontal, 2 = vertical): ")
            if direcao == "1" or direcao == "2":
                direcao_valida = True
            else:
                print("Direção inválida! Digite 1 ou 2.")

        # Verifica todas as casas antes de posicionar a fragata
        espaco_livre = True
        for parte in range(3):
            linha_parte = linha
            coluna_parte = coluna
            if direcao == "1":
                coluna_parte = coluna + parte
            else:
                linha_parte = linha + parte

            if linha_parte >= 6 or coluna_parte >= 6:
                espaco_livre = False
            elif tabuleiro_atual[linha_parte][coluna_parte] != 0:
                espaco_livre = False

        if espaco_livre == True:
            # Coloca as três partes da fragata na matriz
            for parte in range(3):
                if direcao == "1":
                    tabuleiro_atual[linha][coluna + parte] = 3
                else:
                    tabuleiro_atual[linha + parte][coluna] = 3

            posicionado = True
            print("Fragata posicionada com sucesso!")
        else:
            print("A fragata não cabe nessa posição ou existe outro navio no caminho. Tente novamente.")

    if jogador == 1:
        input("\nPasse a vez ao jogador 2 e pressione Enter.")
        print("\n" * 35)

input("\nFragatas posicionadas! Passe a vez ao jogador 1 para começar os tiros e pressione Enter.")
print("\n" * 35)

# ===== SEQUÊNCIA DE JOGADAS =====
# O fim da partida (vitória) será completado pelo Aluno B
# A exibição dos tabuleiros e a leitura do tiro são do Aluno A

fim_de_jogo = False

while fim_de_jogo == False:

    # Escolhe os tabuleiros do jogador da vez
    # tiros_recebidos = tiros que o ADVERSÁRIO já deu na frota deste jogador
    if turno == 1:
        tabuleiro_navios = navios1
        tabuleiro_tiros = tiros1
        navios_adversario = navios2
        tiros_recebidos = tiros2
    else:
        tabuleiro_navios = navios2
        tabuleiro_tiros = tiros2
        navios_adversario = navios1
        tiros_recebidos = tiros1

    # for aninhado: mostra a frota do jogador com os tiros que o adversário deu
    # (~ = água, número = parte do navio, X = parte atingida, o = tiro na água)
    print("\n========== JOGADOR", turno, "- SEU TABULEIRO DE NAVIOS ==========")
    print("   1 2 3 4 5 6")
    for i in range(6):
        print(i + 1, end="  ")
        for j in range(6):
            if tiros_recebidos[i][j] == "X":
                print("X", end=" ")
            elif tiros_recebidos[i][j] == "o":
                print("o", end=" ")
            elif tabuleiro_navios[i][j] == 0:
                print("~", end=" ")
            else:
                print(tabuleiro_navios[i][j], end=" ")
        print()

    # for aninhado: mostra os tiros que o jogador já deu
    print("\n========== JOGADOR", turno, "- SEU TABULEIRO DE TIROS ==========")
    print("   1 2 3 4 5 6")
    for i in range(6):
        print(i + 1, end="  ")
        for j in range(6):
            print(tabuleiro_tiros[i][j], end=" ")
        print()

    # ===== LEITURA DO TIRO =====
    atirou = False
    while atirou == False:

        # Lê a linha até ser válida (compara o texto com "1" a "6")
        linha_valida = False
        while linha_valida == False:
            entrada_linha = input("\nLinha do tiro (1 a 6): ")
            for numero in range(1, 7):
                if entrada_linha == str(numero):
                    linha = numero - 1
                    linha_valida = True
            if linha_valida == False:
                print("Linha inválida! Digite um número de 1 a 6.")

        # Lê a coluna até ser válida
        coluna_valida = False
        while coluna_valida == False:
            entrada_coluna = input("Coluna do tiro (1 a 6): ")
            for numero in range(1, 7):
                if entrada_coluna == str(numero):
                    coluna = numero - 1
                    coluna_valida = True
            if coluna_valida == False:
                print("Coluna inválida! Digite um número de 1 a 6.")

        # Casa já atirada? Se sim, pede outro tiro
        if tabuleiro_tiros[linha][coluna] != ".":
            print("Você já atirou nessa casa! Escolha outra.")
        else:
            if navios_adversario[linha][coluna] > 0:
                tabuleiro_tiros[linha][coluna] = "X"
                print("Acertou!")
            else:
                tabuleiro_tiros[linha][coluna] = "o"
                print("Água!")
            atirou = True

    if todos_navios_afundados(navios_adversario, tabuleiro_tiros):
        print("\nJogador", turno, "venceu! Todos os navios adversários foram afundados.")
        fim_de_jogo = True
    else:
        # Troca de jogador e esconde a tela
        input("\nAperte Enter e passe a vez ao outro jogador.")
        print("\n" * 35)
        turno = 3 - turno
