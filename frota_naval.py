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
print ("======================= Bem-vindo ao batalha dos navais! ======================")
print ("Aqui vai as regras do nosso jogo, você terá que adivinhar onde estão os navios do seu adversário, cada jogador tem 4 navios, sendo eles: 1 porta-aviões, 1 encouraçado, 1 submarino e 1 fragata.")
print ("O tamanho de cada navio é o seguinte: porta-aviões = 4, fragata = 3, encouraçado = 2 e submarino = 1.")
print ("Tem um regra especial, o navio encouraçado é blindado, ou seja, pra ele afundar, você precisa acertar ele 2 vezes.")
print ("O tamanho do tabuleiro é de 6x6, sendo que cada jogador terá um tabuleiro para colocar seus navios e outro para tentar acertar os navios do adversário.")
print ("Na tela vai aparecer o tabuleiro dos seus navios e, no tabuleiro da esquerda, os tiros que você deu no adversário.")
print ("Símbolos: . = casa ainda não atirada | X = acertou um navio | o = água | ~ = água no seu tabuleiro | 1, 2, 3, 4 = partes dos seus navios (1 = submarino, 2 = encouraçado, 3 = fragata, 4 = porta-aviões).")
print ("Como atirar: o jogo vai pedir primeiro a LINHA e depois a COLUNA, uma de cada vez.")
print ("Digite apenas um número de 1 a 6 e aperte Enter. Não use vírgula, ponto nem espaço.")