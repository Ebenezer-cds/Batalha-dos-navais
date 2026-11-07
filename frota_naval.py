# =====================================================================
# BATALHA NAVAL NO TERMINAL (6x6, dois jogadores)
# Disciplina: Coding | UNINASSAU
# Codigo criado por: Héber Ebenézer, Valderso Leando e Carlos Felix.
# Como o programa funciona, em resumo:
#   1. Cria quatro matrizes 6x6 (navios e tiros de cada jogador)
#   2. Mostra as regras
#   3. Cada jogador posiciona seus 4 navios (um por vez)
#   4. Os jogadores se alternam atirando até alguém afundar toda a frota
#   5. Mostra o tabuleiro de cada jogador.
# O trabalho foi sem def, funções, bibliotecas, import, break, return e qualquer outro recurso que não foi ensinado até o momento.
# Só usamos o conteúdo permitido: variáveis, operadores, if/elif/else,
# while, for, range(), matrizes (lista de listas), print(), input() e str().
# =====================================================================


# ===== MATRIZES DO JOGO =====
# Cada tabuleiro é uma matriz 6x6 (lista de listas) declarada por extenso.
# Para acessar uma casa usamos matriz[i][j]: i = linha e j = coluna.
# Os índices vão de 0 a 5, mas para o jogador mostramos de 1 a 6.
# navios1 / navios2: frota de cada jogador
#   0 = água | 1 = submarino | 2 = encouraçado | 3 = fragata | 4 = porta-aviões
# tiros1 / tiros2: tiros que cada jogador já deu no adversário
#   "." = ainda não atirou | "X" = acertou um navio | "o" = o tiro acertou na água
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
# turno guarda de quem é a vez (número inteiro: 1 ou 2)
turno = 1

# ===== REGRAS =====
# Mensagens que explicam o jogo e os símbolos que aparecem na tela
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
# O laço "for jogador" repete o bloco duas vezes: primeiro para o jogador 1
# e depois para o jogador 2. Assim não precisamos copiar o código duas vezes.
for jogador in range(1, 3):
    # Escolhe em qual matriz de navios vamos escrever (a do jogador da vez)
    # Toda vez que for a vez do jogador 1 vai escrever na matriz navios1.
    if jogador == 1:
        tabuleiro_atual = navios1
    # Toda vez que for a vez do jogador 2 vai escrever na matriz navios2.
    else:
        tabuleiro_atual = navios2

    print("\nJogador", jogador, "- posicione seu submarino.")
    # posicionado é um booleano: só vira True quando o navio foi colocado
    posicionado = False
    # Repete até o jogador escolher uma posição válida
    while posicionado == False:
        # for aninhado: mostra o seu tabuleiro com os navios já posicionados (~ = água)
        print("\n   1 2 3 4 5 6")
        for i in range(6):
            print(i + 1, end="  ")
            for j in range(6):
                if tabuleiro_atual[i][j] == 0:
                    print("~", end=" ")
                else:
                    print(tabuleiro_atual[i][j], end=" ")
            print()

        # VALIDAÇÃO DA LINHA
        # linha_valida: booleana que indica se o que foi digitado é válido.
        # Começa False e só vira True se o texto digitado for "1", "2", ..., "6"
        linha_valida = False
        while linha_valida == False:
            # entrada_linha: texto digitado pelo jogador (input sempre devolve texto)
            entrada_linha = input("Digite a linha (1 a 6): ")
            # numero: variável do for, vai de 1 até 6. Comparamos o texto digitado com str(numero) Letra, campo vazio, 0 e 7 não batem e são recusados.
            for numero in range(1, 7):
                if entrada_linha == str(numero):
                    # linha: índice da matriz (0 a 5). O jogador digita 1 a 6, então subtraímos 1.
                    linha = numero - 1
                    linha_valida = True
            if linha_valida == False:
                print("Linha inválida! Digite um número de 1 a 6.")

        # VALIDAÇÃO DA COLUNA
        # coluna_valida, entrada_coluna e coluna funcionam como as variáveis da linha.
        coluna_valida = False
        while coluna_valida == False:
            # entrada_coluna: texto digitado pelo jogador (input sempre devolve texto)
            entrada_coluna = input("Digite a coluna (1 a 6): ")
            for numero in range(1, 7):
                if entrada_coluna == str(numero):
                    coluna = numero - 1
                    coluna_valida = True
            if coluna_valida == False:
                print("Coluna inválida! Digite um número de 1 a 6.")

        # Só posiciona se a casa estiver livre (0 = água).
        # Sair do tabuleiro já é impedido pela validação acima (só aceita 1 a 6).
        # Este if impede que o navio fique em cima de outro navio.
        if tabuleiro_atual[linha][coluna] == 0:
            tabuleiro_atual[linha][coluna] = 1
            posicionado = True
            print("Submarino posicionado com sucesso!")

            # for aninhado: mostra o tabuleiro já com o submarino
            print("\n   1 2 3 4 5 6")
            for i in range(6):
                print(i + 1, end="  ")
                for j in range(6):
                    if tabuleiro_atual[i][j] == 0:
                        print("~", end=" ")
                    else:
                        print(tabuleiro_atual[i][j], end=" ")
                print()
        else:
            print("Essa posição já está ocupada! Escolha outra.")

    # Depois do jogador 1, esconde a tela para o jogador 2 não ver os navios.
    # print("\n" * 35) imprime 35 linhas vazias, empurrando o texto antigo para cima.
    if jogador == 1:
        input("\nPasse a vez ao jogador 2 e pressione Enter.")
        print("\n" * 35)

print("\nPosicionamento dos submarinos concluído!")

# ===== POSICIONAMENTO DAS FRAGATAS =====
# A fragata ocupa 3 casas em linha. Por isso, além da linha e da coluna
# inicial, o jogador escolhe a direção (horizontal ou vertical).
# As variáveis jogador, tabuleiro_atual, posicionado, linha_valida, coluna_valida,
# entrada_linha, entrada_coluna, linha e coluna são as mesmas do bloco anterior,
# só recebem novos valores.

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
        # for aninhado: mostra o seu tabuleiro com os navios já posicionados (~ = água)
        print("\n   1 2 3 4 5 6")
        for i in range(6):
            print(i + 1, end="  ")
            for j in range(6):
                if tabuleiro_atual[i][j] == 0:
                    print("~", end=" ")
                else:
                    print(tabuleiro_atual[i][j], end=" ")
            print()

        # Lê a linha inicial até ser válida
        linha_valida = False
        while linha_valida == False:
            entrada_linha = input("Linha inicial da fragata (1 a 6): ")
            for numero in range(1, 7):
                if entrada_linha == str(numero):
                    linha = numero - 1
                    linha_valida = True
            if linha_valida == False:
                print("Linha inválida! Digite um número de 1 a 6.")

        # Lê a coluna inicial até ser válida
        coluna_valida = False
        while coluna_valida == False:
            entrada_coluna = input("Coluna inicial da fragata (1 a 6): ")
            for numero in range(1, 7):
                if entrada_coluna == str(numero):
                    coluna = numero - 1
                    coluna_valida = True
            if coluna_valida == False:
                print("Coluna inválida! Digite um número de 1 a 6.")

        # direcao_valida: booleana, só vira True se a direção digitada for válida.
        # direcao: texto digitado ("1" = horizontal, "2" = vertical).
        direcao_valida = False
        while direcao_valida == False:
            direcao = input("Direção (1 = horizontal, 2 = vertical): ")
            if direcao == "1" or direcao == "2":
                direcao_valida = True
            else:
                print("Direção inválida! Digite 1 ou 2.")

        # Verifica todas as casas antes de posicionar a fragata.
        # espaco_livre: booleana que começa True e vira False se QUALQUER parte
        # da fragata sair do tabuleiro ou bater em outro navio.
        # parte: variável do for (0, 1 e 2), indica qual parte da fragata está
        # sendo testada. linha_parte e coluna_parte guardam a posição dessa parte:
        # na horizontal a coluna aumenta, na vertical a linha aumenta.
        espaco_livre = True
        for parte in range(3):
            linha_parte = linha
            coluna_parte = coluna
            if direcao == "1":
                coluna_parte = coluna + parte
            else:
                linha_parte = linha + parte

            # Passou do tabuleiro (índice 6 ou mais)? Ou a casa já está ocupada?
            if linha_parte >= 6 or coluna_parte >= 6:
                espaco_livre = False
            elif tabuleiro_atual[linha_parte][coluna_parte] != 0:
                espaco_livre = False

        if espaco_livre == True:
            # Coloca as três partes da fragata na matriz (número 3)
            for parte in range(3):
                if direcao == "1":
                    tabuleiro_atual[linha][coluna + parte] = 3
                else:
                    tabuleiro_atual[linha + parte][coluna] = 3

            posicionado = True
            print("Fragata posicionada com sucesso!")

            # for aninhado: mostra o tabuleiro já com a fragata
            print("\n   1 2 3 4 5 6")
            for i in range(6):
                print(i + 1, end="  ")
                for j in range(6):
                    if tabuleiro_atual[i][j] == 0:
                        print("~", end=" ")
                    else:
                        print(tabuleiro_atual[i][j], end=" ")
                print()
        else:
            print("A fragata não cabe nessa posição ou existe outro navio no caminho. Tente novamente.")

    if jogador == 1:
        input("\nPasse a vez ao jogador 2 e pressione Enter.")
        print("\n" * 35)


# ===== POSICIONAMENTO DO ENCOURAÇADO E PORTA-AVIÕES =====
# range(2, 5, 2) gera apenas 2 e 4: o tamanho do encouraçado e do porta-aviões.
# tipo_navio: variável inteira do for. Ela é o tamanho do navio e também o
# número gravado na matriz (2 = encouraçado, 4 = porta-aviões).
# nome_navio: texto usado só para mostrar o nome do navio nas mensagens.
# O resto do bloco funciona como o da fragata, só que com tipo_navio casas.
for tipo_navio in range(2, 5, 2):
    if tipo_navio == 2:
        nome_navio = "encouraçado"
    else:
        nome_navio = "porta-aviões"

    input("\nPasse a vez ao jogador 1 para posicionar o " + nome_navio + " e pressione Enter.")
    print("\n" * 35)

    for jogador in range(1, 3):
        if jogador == 1:
            tabuleiro_atual = navios1
        else:
            tabuleiro_atual = navios2

        print("\nJogador", jogador, "- posicione seu", nome_navio, "de", tipo_navio, "casas.")
        posicionado = False

        while posicionado == False:
            # for aninhado: mostra o seu tabuleiro com os navios já posicionados (~ = água)
            print("\n   1 2 3 4 5 6")
            for i in range(6):
                print(i + 1, end="  ")
                for j in range(6):
                    if tabuleiro_atual[i][j] == 0:
                        print("~", end=" ")
                    else:
                        print(tabuleiro_atual[i][j], end=" ")
                print()

            # Lê a linha, a coluna e a direção até serem válidas (mesmo método da fragata)
            linha_valida = False
            while linha_valida == False:
                entrada_linha = input("Linha inicial (1 a 6): ")
                for numero in range(1, 7):
                    if entrada_linha == str(numero):
                        linha = numero - 1
                        linha_valida = True
                if linha_valida == False:
                    print("Linha inválida! Digite um número de 1 a 6.")

            coluna_valida = False
            while coluna_valida == False:
                entrada_coluna = input("Coluna inicial (1 a 6): ")
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

            # Verifica se todas as casas estão livres e dentro do tabuleiro
            # (o for repete tipo_navio vezes: 2 casas ou 4 casas)
            espaco_livre = True
            for parte in range(tipo_navio):
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
                # Grava o número do navio (tipo_navio) em cada casa que ele ocupa
                for parte in range(tipo_navio):
                    if direcao == "1":
                        tabuleiro_atual[linha][coluna + parte] = tipo_navio
                    else:
                        tabuleiro_atual[linha + parte][coluna] = tipo_navio

                posicionado = True
                print("Navio posicionado com sucesso!")

                # for aninhado: mostra o tabuleiro já com o navio
                print("\n   1 2 3 4 5 6")
                for i in range(6):
                    print(i + 1, end="  ")
                    for j in range(6):
                        if tabuleiro_atual[i][j] == 0:
                            print("~", end=" ")
                        else:
                            print(tabuleiro_atual[i][j], end=" ")
                    print()
            else:
                print("Não há espaço livre nessa posição. Escolha outra.")

        if jogador == 1:
            input("\nPasse a vez ao jogador 2 e pressione Enter.")
            print("\n" * 35)

input("\nTodos os navios foram posicionados! Passe a vez ao jogador 1 para começar os tiros e pressione Enter.")
print("\n" * 35)


# ===== SEQUÊNCIA DE JOGADAS =====
# Este while é a partida: cada volta é uma jogada de um jogador.
# fim_de_jogo: variável booleana. Fica False durante a partida e vira True
# quando alguém afunda toda a frota do adversário, encerrando o while.
fim_de_jogo = False

while fim_de_jogo == False:

    # Escolhe as matrizes do jogador da vez. Todas apontam para as matrizes
    # originais (não são cópias):
    #   tabuleiro_navios  = a frota do jogador da vez
    #   tabuleiro_tiros   = os tiros que o jogador da vez já deu
    #   navios_adversario = a frota do adversário (onde ele vai atirar)
    #   tiros_recebidos   = os tiros que o ADVERSÁRIO já deu na frota deste jogador
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

    # EXIBIÇÃO DA FROTA DO JOGADOR
    # Por que não usar só print(navios1)? Porque o print(navios1) funciona e
    # não dá erro, mas mostra a matriz "crua", no formato do Python:
    #   [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], ...]
    # Isso aparece com colchetes e vírgulas, com 0 no lugar da água, sem os números
    # de linha e coluna e sem os tiros do adversário (que ficam em outra matriz,
    # tiros_recebidos). Para desenhar o tabuleiro do jeito que queremos, usamos um
    # for aninhado, que visita as casas uma por uma e decide o que imprimir em cada.
    #
    # for aninhado: o laço de fora (i) percorre as LINHAS e, para cada linha, o
    # laço de dentro (j) percorre as COLUNAS. i e j são variáveis inteiras (0 a 5).
    # Para cada casa: se o adversário atirou nela, mostra X (acertou) ou o (água);
    # senão mostra ~ (água) ou o número do navio.
    print("\n========== JOGADOR", turno, "- SEU TABULEIRO DE NAVIOS ==========")
    print("   1 2 3 4 5 6")
    for i in range(6):
        # i + 1 é o número da linha mostrado para o jogador (1 a 6).
        # end="  " evita pular de linha, para as casas ficarem na mesma linha.
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
        # print() vazio pula para a próxima linha do tabuleiro.
        print()

    # for aninhado: mostra os tiros que o jogador já deu (mesma ideia de cima,
    # mas aqui basta imprimir o que está na matriz de tiros)
    print("\n========== JOGADOR", turno, "- SEU TABULEIRO DE TIROS ==========")
    print("   1 2 3 4 5 6")
    for i in range(6):
        print(i + 1, end="  ")
        for j in range(6):
            print(tabuleiro_tiros[i][j], end=" ")
        print()

    # ===== LEITURA DO TIRO =====
    # atirou: booleana que só vira True quando o jogador deu um tiro válido
    # (em uma casa ainda não atirada). Se for False, o while pede outro tiro.
    atirou = False
    while atirou == False:

        # Lê a linha do tiro até ser válida (mesmo método com str(numero))
        linha_valida = False
        while linha_valida == False:
            entrada_linha = input("\nLinha do tiro (1 a 6): ")
            for numero in range(1, 7):
                if entrada_linha == str(numero):
                    linha = numero - 1
                    linha_valida = True
            if linha_valida == False:
                print("Linha inválida! Digite um número de 1 a 6.")

        # Lê a coluna do tiro até ser válida
        coluna_valida = False
        while coluna_valida == False:
            entrada_coluna = input("Coluna do tiro (1 a 6): ")
            for numero in range(1, 7):
                if entrada_coluna == str(numero):
                    coluna = numero - 1
                    coluna_valida = True
            if coluna_valida == False:
                print("Coluna inválida! Digite um número de 1 a 6.")

        # Casa já atirada? Se não for "." é porque já tem X ou o. Então pede outro tiro.
        if tabuleiro_tiros[linha][coluna] != ".":
            print("Você já atirou nessa casa! Escolha outra.")
        else:
            # Se na frota do adversário há um navio (número maior que 0), acertou
            if navios_adversario[linha][coluna] > 0:
                tabuleiro_tiros[linha][coluna] = "X"
                print("Acertou!")
            else:
                tabuleiro_tiros[linha][coluna] = "o"
                print("Água!")
            atirou = True

    # VERIFICAÇÃO DE VITÓRIA (for aninhado)
    # restantes: variável inteira que funciona como um contador. Começa em 0 e
    # conta quantas partes de navio do adversário ainda NÃO foram atingidas.
    restantes = 0
    # O for de fora percorre as linhas (i) e o de dentro as colunas (j),
    # visitando todas as 36 casas da frota do adversário.
    for i in range(6):
        for j in range(6):
            # Cada casa é testada com duas condições ligadas por "and":
            #   1) navios_adversario[i][j] > 0   -> a casa tem parte de um navio
            #   2) tabuleiro_tiros[i][j] != "X"  -> e ainda não foi acertada
            # Quando as duas são verdadeiras, soma 1 no contador.
            if navios_adversario[i][j] > 0 and tabuleiro_tiros[i][j] != "X":
                restantes = restantes + 1

    # Se não sobrou nenhuma parte de navio sem acerto, todos foram afundados
    if restantes == 0:
        print("\nJogador", turno, "venceu! Todos os navios adversários foram afundados.")
        fim_de_jogo = True
    else:
        # Troca de jogador e esconde a tela
        input("\nAperte Enter e passe a vez ao outro jogador.")
        print("\n" * 35)
        # turno = 3 - turno alterna o jogador da vez entre 1 e 2:
        #   se turno é 1, então 3 - 1 = 2 (passa para o jogador 2)
        #   se turno é 2, então 3 - 2 = 1 (volta para o jogador 1)
        turno = 3 - turno