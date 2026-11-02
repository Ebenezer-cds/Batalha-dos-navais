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
turno = 1


def exibir_tabuleiro(tabuleiro, titulo, substituir_agua=False):
    """Exibe um tabuleiro 6x6 com cabeçalhos de linha e coluna."""
    print("\n==========", titulo, "==========")
    print("   1 2 3 4 5 6")

    for indice_linha, linha in enumerate(tabuleiro, start=1):
        print(indice_linha, end="  ")

        for casa in linha:
            if substituir_agua and casa == 0:
                print("~", end=" ")
            else:
                print(casa, end=" ")

        print()


def ler_coordenada(tipo):
    """Lê uma linha ou coluna válida e retorna seu índice no tabuleiro."""
    while True:
        entrada = input("Digite a " + tipo + " (1 a 6): ")

        if entrada in ["1", "2", "3", "4", "5", "6"]:
            return int(entrada) - 1

        print(tipo.capitalize() + " inválida! Digite um número de 1 a 6.")


print ("======================= Bem-vindo ao batalha dos navais! ======================")
print ("Aqui vai as regras do nosso jogo, você terá que adivinhar onde estão os navios do seu adversário, cada jogador tem 4 navios, sendo eles: 1 porta-aviões, 1 encouraçado, 1 submarino e 1 fragata.")
print ("O tamanho de cada navio é o seguinte: porta-aviões = 4, fragata = 3, encouraçado = 2 e submarino = 1.")
print ("Tem um regra especial, o navio encouraçado é blindado, ou seja, pra ele afundar, você precisa acertar ele 2 vezes.")
print ("O tamanho do tabuleiro é de 6x6, sendo que cada jogador terá um tabuleiro para colocar seus navios e outro para tentar acertar os navios do adversário.")
print ("Na tela vai aparecer o tabuleiro dos seus navios e, no tabuleiro da esquerda, os tiros que você deu no adversário.")
print ("Símbolos: . = casa ainda não atirada | X = acertou um navio | o = água | ~ = água no seu tabuleiro | 1, 2, 3, 4 = partes dos seus navios (1 = submarino, 2 = encouraçado, 3 = fragata, 4 = porta-aviões).")
print ("Como atirar: o jogo vai pedir primeiro a LINHA e depois a COLUNA, uma de cada vez.")
print ("Digite apenas um número de 1 a 6 e aperte Enter. Não use vírgula, ponto nem espaço.")

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
        linha = ler_coordenada("linha")
        coluna = ler_coordenada("coluna")

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

# ===== EXIBIÇÃO DOS TABULEIROS =====

# Identifica os tabuleiros do jogador atual
if turno == 1:
    tabuleiro_navios = navios1
    tabuleiro_tiros = tiros1
else:
    tabuleiro_navios = navios2
    tabuleiro_tiros = tiros2

# Exibe os tabuleiros do jogador atual
exibir_tabuleiro(tabuleiro_navios, "SEU TABULEIRO DE NAVIOS", True)
exibir_tabuleiro(tabuleiro_tiros, "SEU TABULEIRO DE TIROS")
