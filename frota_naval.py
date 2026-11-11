# =====================================================================
# BATALHA NAVAL NO TERMINAL (6x6, dois jogadores)
# Disciplina: Coding | UNINASSAU - Centro Universitário Maurício de Nassau
# Professor: M.Sc. Tiago Martins Ribeiro
# Código desenvolvido por: Héber Ebenézer, Valderso Leandro e Carlos Felix.
#
# RESUMO DAS DIRETRIZES E RESTRIÇÕES PEDAGÓGICAS ATENDIDAS:
#   1. Não utiliza funções nem procedimentos próprios (sem def e sem return).
#   2. Não utiliza módulos ou bibliotecas externas (sem nenhum import).
#   3. Não utiliza tratamento de exceções (sem try/except); validações feitas
#      por comparação direta com strings válidas via while e laços for.
#   4. Não utiliza métodos de conveniência de listas ou strings (sem .isdigit(),
#      sem .append(), sem dicionários e sem listas fora das matrizes).
#   5. Não utiliza comando break (todo o fluxo é controlado por variáveis booleanas).
#   6. Utiliza matrizes 6x6 declaradas por extenso e for aninhado para:
#      - Exibição gráfica dos tabuleiros;
#      - Reinício/limpeza das matrizes para novas partidas;
#      - Verificação de vitória e contagem de partes de navios restantes.
#   7. Possui Menu Interativo com opções numéricas e tratamento de opções inválidas.
#   8. Possui Sistema de Placar mantido em memória entre as partidas.
# =====================================================================


# =====================================================================
# BLOCO 1: DECLARAÇÃO DAS MATRIZES E VARIÁVEIS DE CONTROLE
# =====================================================================

# Matrizes 6x6 declaradas por extenso (lista de listas).
# Acesso: matriz[linha][coluna], com índices internos de 0 a 5.
#
# Tabuleiros de navios (frota de cada jogador):
#   0 = água | 1 = submarino | 2 = encouraçado | 3 = fragata | 4 = porta-aviões
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

# Tabuleiros de tiros (registro dos disparos dados contra o oponente):
#   "." = casa ainda não alvejada | "X" = tiro certeiro em navio | "o" = tiro na água
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

# Variáveis acumuladoras do placar geral (mantidas entre as partidas)
placar_jogador1 = 0
placar_jogador2 = 0
total_partidas = 0

# executando_programa: variável booleana que mantém o laço do menu principal ativo
executando_programa = True


# =====================================================================
# BLOCO 2: MENU PRINCIPAL INTERATIVO
# =====================================================================

while executando_programa == True:
    print("\n" + "=" * 65)
    print("        BATALHA DOS NAVAIS - MENU PRINCIPAL (TERMINAL 6x6)")
    print("=" * 65)
    print("1 - Iniciar nova partida")
    print("2 - Ver regras do jogo e símbolos")
    print("3 - Exibir placar geral")
    print("0 - Sair do jogo")
    print("=" * 65)

    # Validação da opção do menu sem try/except:
    # A variável opcao_valida inicia como False. A leitura recebe uma string
    # e compara com as alternativas permitidas ("1", "2", "3", "0"). Qualquer letra,
    # espaço em branco ou número fora dessa lista mantém opcao_valida como False.
    opcao_valida = False
    while opcao_valida == False:
        opcao_menu = input("Escolha uma opção (0, 1, 2 ou 3): ")
        if opcao_menu == "0" or opcao_menu == "1" or opcao_menu == "2" or opcao_menu == "3":
            opcao_valida = True
        else:
            print("Opção inválida! Digite apenas 0, 1, 2 ou 3.")

    # -----------------------------------------------------------------
    # OPÇÃO 0: SAIR DO JOGO
    # -----------------------------------------------------------------
    if opcao_menu == "0":
        print("\nObrigado por jogar Batalha Naval! Encerrando o programa...")
        executando_programa = False

    # -----------------------------------------------------------------
    # OPÇÃO 2: REGRAS DO JOGO E GUIA DE EMBARCAÇÕES
    # -----------------------------------------------------------------
    elif opcao_menu == "2":
        print("\n" + "=" * 65)
        print("                        REGRAS DO JOGO")
        print("=" * 65)
        print("1. OBJETIVO:")
        print("   Descobrir e afundar todos os navios da frota adversária.")
        print("   A partida continua até que um dos jogadores destrua completamente")
        print("   a frota oponente (não há empate).")
        print("\n2. OS TABULEIROS:")
        print("   Cada jogador possui um tabuleiro 6x6 para dispor seus navios")
        print("   e um tabuleiro 6x6 de tiros para registrar seus disparos.")
        print("\n3. A FROTA NAVAL (4 navios por jogador, total de 10 partes):")
        print("   - Porta-aviões : ocupa 4 casas (identificado pelo número 4)")
        print("   - Fragata      : ocupa 3 casas (identificado pelo número 3)")
        print("   - Encouraçado  : ocupa 2 casas (identificado pelo número 2)")
        print("   - Submarino    : ocupa 1 casa  (identificado pelo número 1)")
        print("\n4. REGRA ESPECIAL DO ENCOURAÇADO:")
        print("   O encouraçado é uma embarcação de blindagem pesada: exige que")
        print("   todas as suas posições sejam alvejadas para ser destruído.")
        print("\n5. SÍMBOLOS NA TELA:")
        print("   ~ = Água no tabuleiro de navios")
        print("   . = Posição ainda não alvejada no tabuleiro de tiros")
        print("   X = Tiro certeiro (atingiu parte de um navio)")
        print("   o = Tiro na água")
        print("   1, 2, 3, 4 = Partes das suas próprias embarcações")
        print("\n6. ENTRADA DE COORDENADAS:")
        print("   Digite apenas um número de 1 a 6 para a linha e para a coluna.")
        print("=" * 65)
        input("\nPressione Enter para retornar ao menu principal...")

    # -----------------------------------------------------------------
    # OPÇÃO 3: EXIBIÇÃO DO PLACAR GERAL
    # -----------------------------------------------------------------
    elif opcao_menu == "3":
        print("\n" + "=" * 65)
        print("                         PLACAR GERAL")
        print("=" * 65)
        print("Total de partidas disputadas :", total_partidas)
        print("Vitórias do Jogador 1        :", placar_jogador1)
        print("Vitórias do Jogador 2        :", placar_jogador2)
        print("=" * 65)
        input("\nPressione Enter para retornar ao menu principal...")

    # -----------------------------------------------------------------
    # OPÇÃO 1: INICIAR NOVA PARTIDA
    # -----------------------------------------------------------------
    elif opcao_menu == "1":

        # ===== REINICIALIZAÇÃO DAS MATRIZES COM FOR ANINHADO =====
        # Para permitir jogar novamente sem fechar o programa e mantendo o placar,
        # zeramos as 4 matrizes percorrendo linha por linha (i) e coluna por coluna (j).
        for i in range(6):
            for j in range(6):
                navios1[i][j] = 0
                navios2[i][j] = 0
                tiros1[i][j] = "."
                tiros2[i][j] = "."

        # Variáveis de controle de cada partida individual
        turno = 1
        total_partidas = total_partidas + 1

        print("\nIniciando a partida número", total_partidas, "...")
        print("Cada jogador deverá agora posicionar sua frota em segredo.")


        # =============================================================
        # BLOCO 3: POSICIONAMENTO DOS NAVIOS
        # =============================================================

        # ----- 3.1: SUBMARINO (1 casa) -----
        # O for jogador repete o procedimento para o Jogador 1 e depois Jogador 2.
        for jogador in range(1, 3):
            if jogador == 1:
                tabuleiro_atual = navios1
            else:
                tabuleiro_atual = navios2

            print("\nJogador", jogador, "- Posicione seu SUBMARINO (tamanho: 1 casa).")
            posicionado = False

            while posicionado == False:
                # for aninhado: desenha o tabuleiro com os navios atuais (~ = água)
                print("\n   1 2 3 4 5 6")
                for i in range(6):
                    print(i + 1, end="  ")
                    for j in range(6):
                        if tabuleiro_atual[i][j] == 0:
                            print("~", end=" ")
                        else:
                            print(tabuleiro_atual[i][j], end=" ")
                    print()

                # Validação da linha (1 a 6) sem try/except
                linha_valida = False
                while linha_valida == False:
                    entrada_linha = input("Digite a linha (1 a 6): ")
                    for numero in range(1, 7):
                        if entrada_linha == str(numero):
                            linha = numero - 1
                            linha_valida = True
                    if linha_valida == False:
                        print("Linha inválida! Digite um número de 1 a 6.")

                # Validação da coluna (1 a 6) sem try/except
                coluna_valida = False
                while coluna_valida == False:
                    entrada_coluna = input("Digite a coluna (1 a 6): ")
                    for numero in range(1, 7):
                        if entrada_coluna == str(numero):
                            coluna = numero - 1
                            coluna_valida = True
                    if coluna_valida == False:
                        print("Coluna inválida! Digite um número de 1 a 6.")

                # Verifica se a casa está livre
                if tabuleiro_atual[linha][coluna] == 0:
                    tabuleiro_atual[linha][coluna] = 1
                    posicionado = True
                    print("Submarino posicionado com sucesso!")

                    # for aninhado: confirma visualmente a posição do navio
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

            # Esconde a tela para manter sigilo tático entre os jogadores
            if jogador == 1:
                input("\nPasse a vez ao jogador 2 e pressione Enter.")
                print("\n" * 35)

        print("\nPosicionamento dos submarinos concluído!")


        # ----- 3.2: FRAGATA (3 casas) -----
        input("\nPasse a vez ao jogador 1 para posicionar a FRAGATA e pressione Enter.")
        print("\n" * 35)

        for jogador in range(1, 3):
            if jogador == 1:
                tabuleiro_atual = navios1
            else:
                tabuleiro_atual = navios2

            print("\nJogador", jogador, "- Posicione sua FRAGATA (tamanho: 3 casas).")
            posicionado = False

            while posicionado == False:
                # for aninhado: visualização do tabuleiro
                print("\n   1 2 3 4 5 6")
                for i in range(6):
                    print(i + 1, end="  ")
                    for j in range(6):
                        if tabuleiro_atual[i][j] == 0:
                            print("~", end=" ")
                        else:
                            print(tabuleiro_atual[i][j], end=" ")
                    print()

                # Leitura validada da linha inicial
                linha_valida = False
                while linha_valida == False:
                    entrada_linha = input("Linha inicial da fragata (1 a 6): ")
                    for numero in range(1, 7):
                        if entrada_linha == str(numero):
                            linha = numero - 1
                            linha_valida = True
                    if linha_valida == False:
                        print("Linha inválida! Digite um número de 1 a 6.")

                # Leitura validada da coluna inicial
                coluna_valida = False
                while coluna_valida == False:
                    entrada_coluna = input("Coluna inicial da fragata (1 a 6): ")
                    for numero in range(1, 7):
                        if entrada_coluna == str(numero):
                            coluna = numero - 1
                            coluna_valida = True
                    if coluna_valida == False:
                        print("Coluna inválida! Digite um número de 1 a 6.")

                # Leitura validada da direção (1 = horizontal, 2 = vertical)
                direcao_valida = False
                while direcao_valida == False:
                    direcao = input("Direção (1 = horizontal, 2 = vertical): ")
                    if direcao == "1" or direcao == "2":
                        direcao_valida = True
                    else:
                        print("Direção inválida! Digite 1 para horizontal ou 2 para vertical.")

                # Verificação de espaço livre e limites da matriz para as 3 casas
                espaco_livre = True
                for parte in range(3):
                    linha_parte = linha
                    coluna_parte = coluna
                    if direcao == "1":
                        coluna_parte = coluna + parte
                    else:
                        linha_parte = linha + parte

                    # Impede transbordamento da matriz ou colisão com outro navio
                    if linha_parte >= 6 or coluna_parte >= 6:
                        espaco_livre = False
                    elif tabuleiro_atual[linha_parte][coluna_parte] != 0:
                        espaco_livre = False

                if espaco_livre == True:
                    # Registra a fragata (valor 3) nas casas selecionadas
                    for parte in range(3):
                        if direcao == "1":
                            tabuleiro_atual[linha][coluna + parte] = 3
                        else:
                            tabuleiro_atual[linha + parte][coluna] = 3

                    posicionado = True
                    print("Fragata posicionada com sucesso!")

                    # for aninhado: visualização atualizada
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
                    print("A fragata não cabe nessa posição ou colide com outro navio. Tente novamente.")

            if jogador == 1:
                input("\nPasse a vez ao jogador 2 e pressione Enter.")
                print("\n" * 35)


        # ----- 3.3: ENCOURAÇADO (2 casas) E PORTA-AVIÕES (4 casas) -----
        # O range(2, 5, 2) percorre os valores 2 e 4:
        # Quando tipo_navio == 2 -> Encouraçado (2 casas)
        # Quando tipo_navio == 4 -> Porta-aviões (4 casas)
        for tipo_navio in range(2, 5, 2):
            if tipo_navio == 2:
                nome_navio = "ENCOURAÇADO"
            else:
                nome_navio = "PORTA-AVIÕES"

            input("\nPasse a vez ao jogador 1 para posicionar o " + nome_navio + " e pressione Enter.")
            print("\n" * 35)

            for jogador in range(1, 3):
                if jogador == 1:
                    tabuleiro_atual = navios1
                else:
                    tabuleiro_atual = navios2

                print("\nJogador", jogador, "- Posicione seu", nome_navio, "(tamanho:", tipo_navio, "casas).")
                posicionado = False

                while posicionado == False:
                    # for aninhado: visualização do tabuleiro
                    print("\n   1 2 3 4 5 6")
                    for i in range(6):
                        print(i + 1, end="  ")
                        for j in range(6):
                            if tabuleiro_atual[i][j] == 0:
                                print("~", end=" ")
                            else:
                                print(tabuleiro_atual[i][j], end=" ")
                        print()

                    # Validação da linha inicial
                    linha_valida = False
                    while linha_valida == False:
                        entrada_linha = input("Linha inicial (1 a 6): ")
                        for numero in range(1, 7):
                            if entrada_linha == str(numero):
                                linha = numero - 1
                                linha_valida = True
                        if linha_valida == False:
                            print("Linha inválida! Digite um número de 1 a 6.")

                    # Validação da coluna inicial
                    coluna_valida = False
                    while coluna_valida == False:
                        entrada_coluna = input("Coluna inicial (1 a 6): ")
                        for numero in range(1, 7):
                            if entrada_coluna == str(numero):
                                coluna = numero - 1
                                coluna_valida = True
                        if coluna_valida == False:
                            print("Coluna inválida! Digite um número de 1 a 6.")

                    # Validação da direção
                    direcao_valida = False
                    while direcao_valida == False:
                        direcao = input("Direção (1 = horizontal, 2 = vertical): ")
                        if direcao == "1" or direcao == "2":
                            direcao_valida = True
                        else:
                            print("Direção inválida! Digite 1 ou 2.")

                    # Verifica limites e ocupação para as tipo_navio casas
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
                        for parte in range(tipo_navio):
                            if direcao == "1":
                                tabuleiro_atual[linha][coluna + parte] = tipo_navio
                            else:
                                tabuleiro_atual[linha + parte][coluna] = tipo_navio

                        posicionado = True
                        print(nome_navio, "posicionado com sucesso!")

                        # for aninhado: visualização atualizada
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
                        print("Posição inválida ou com navio no caminho. Escolha outra.")

                if jogador == 1:
                    input("\nPasse a vez ao jogador 2 e pressione Enter.")
                    print("\n" * 35)

        input("\nTodos os navios foram posicionados! Passe a vez ao jogador 1 para iniciar a batalha e pressione Enter.")
        print("\n" * 35)


        # =============================================================
        # BLOCO 4: LAÇO PRINCIPAL DA PARTIDA E LEITURA DE DISPAROS
        # =============================================================

        fim_de_jogo = False

        while fim_de_jogo == False:

            # Seleção das referências da matriz com base no jogador da vez:
            # - tabuleiro_navios  : frota do jogador atual
            # - tabuleiro_tiros   : registro dos tiros que o jogador atual deu
            # - navios_adversario : frota do oponente (alvo do tiro)
            # - tiros_recebidos   : tiros que o adversário disparou contra a frota do jogador atual
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

            # for aninhado: Exibição da frota própria com danos recebidos
            print("\n" + "=" * 55)
            print("  JOGADOR", turno, "- SEU TABULEIRO DE NAVIOS (Danos sofridos)")
            print("=" * 55)
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

            # for aninhado: Exibição do radar de tiros do jogador da vez
            print("\n" + "=" * 55)
            print("  JOGADOR", turno, "- SEU TABULEIRO DE TIROS (Disparos efetuados)")
            print("=" * 55)
            print("   1 2 3 4 5 6")
            for i in range(6):
                print(i + 1, end="  ")
                for j in range(6):
                    print(tabuleiro_tiros[i][j], end=" ")
                print()

            # ----- LEITURA E VALIDAÇÃO DO TIRO -----
            atirou = False
            while atirou == False:

                # Validação da linha do tiro sem try/except
                linha_valida = False
                while linha_valida == False:
                    entrada_linha = input("\nLinha do disparo (1 a 6): ")
                    for numero in range(1, 7):
                        if entrada_linha == str(numero):
                            linha = numero - 1
                            linha_valida = True
                    if linha_valida == False:
                        print("Linha inválida! Digite um número de 1 a 6.")

                # Validação da coluna do tiro sem try/except
                coluna_valida = False
                while coluna_valida == False:
                    entrada_coluna = input("Coluna do disparo (1 a 6): ")
                    for numero in range(1, 7):
                        if entrada_coluna == str(numero):
                            coluna = numero - 1
                            coluna_valida = True
                    if coluna_valida == False:
                        print("Coluna inválida! Digite um número de 1 a 6.")

                # Impede repetição de tiro na mesma casa
                if tabuleiro_tiros[linha][coluna] != ".":
                    print("Você já atirou nessa posição! Escolha outra casa.")
                else:
                    # Verifica acerto ou água
                    if navios_adversario[linha][coluna] > 0:
                        tabuleiro_tiros[linha][coluna] = "X"
                        print("\n>>> FOGO! Você ACERTOU uma embarcação adversária! <<<")

                        # for aninhado: verifica se todas as partes deste navio foram afundadas
                        tipo_atingido = navios_adversario[linha][coluna]
                        partes_restantes = 0
                        for i in range(6):
                            for j in range(6):
                                if navios_adversario[i][j] == tipo_atingido and tabuleiro_tiros[i][j] != "X":
                                    partes_restantes = partes_restantes + 1

                        if partes_restantes == 0:
                            if tipo_atingido == 1:
                                print(">>> ALVO DESTRUÍDO: O submarino adversário foi AFUNDADO! <<<")
                            elif tipo_atingido == 2:
                                print(">>> ALVO DESTRUÍDO: O encouraçado adversário foi AFUNDADO! <<<")
                            elif tipo_atingido == 3:
                                print(">>> ALVO DESTRUÍDO: A fragata adversária foi AFUNDADA! <<<")
                            else:
                                print(">>> ALVO DESTRUÍDO: O porta-aviões adversário foi AFUNDADO! <<<")
                    else:
                        tabuleiro_tiros[linha][coluna] = "o"
                        print("\n>>> ÁGUA! Nenhum navio nessa posição. <<<")

                    atirou = True


            # =========================================================
            # BLOCO 5: VERIFICAÇÃO DE VITÓRIA E ATUALIZAÇÃO DO PLACAR
            # =========================================================

            # for aninhado: Conta quantas partes de navios do oponente ainda estão intactas
            partes_vivas = 0
            for i in range(6):
                for j in range(6):
                    # Se há navio na casa e o jogador ainda não acertou nela:
                    if navios_adversario[i][j] > 0 and tabuleiro_tiros[i][j] != "X":
                        partes_vivas = partes_vivas + 1

            # CASO DE VITÓRIA:
            # Se não restou nenhuma parte intacta, a frota adversária foi aniquilada.
            if partes_vivas == 0:
                print("\n" + "=" * 65)
                print("VITÓRIA! O JOGADOR", turno, "AFUNDOU TODA A FROTA ADVERSÁRIA!")
                print("=" * 65)
                if turno == 1:
                    placar_jogador1 = placar_jogador1 + 1
                else:
                    placar_jogador2 = placar_jogador2 + 1

                fim_de_jogo = True
                input("\nPressione Enter para retornar ao menu principal...")

            # CONTINUA A PARTIDA:
            else:
                input("\nAperte Enter e passe a vez ao outro jogador.")
                print("\n" * 35)
                # Alternância matemática de turno:
                # Se turno == 1 -> 3 - 1 = 2 (vez do Jogador 2)
                # Se turno == 2 -> 3 - 2 = 1 (vez do Jogador 1)
                turno = 3 - turno
