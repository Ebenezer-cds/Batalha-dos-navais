# ⚓ Batalha Naval no Terminal (6x6)

> **Projeto Prático da 2ª Avaliação (AV2)**  
> **Instituição:** Centro Universitário Maurício de Nassau (UNINASSAU – Teresina-PI)  
> **Curso:** Bacharelado em Ciência da Computação  
> **Disciplina:** Coding  
> **Professor:** M.Sc. Tiago Martins Ribeiro  
> **Equipe de Desenvolvimento:**  
> - Héber Ebenézer  
> - Valderso Leandro  
> - Carlos Felix  

---

## 📌 Sobre o Projeto

O **Batalha dos Navais** é um jogo de estratégia em combate naval por turnos, desenvolvido em linguagem **Python** para execução diretamente no terminal/console. Projetado para **dois jogadores locais**, cada participante posiciona estrategicamente sua frota naval em segredo e, em seguida, alternam disparos de artilharia até que um dos jogadores aniquile por completo todos os navios do oponente.

---

## 🎯 Regras do Jogo e Embarcações

* **Dimensão dos Tabuleiros:** Matrizes bidimensionais de ordem **6x6** (linhas de 1 a 6 e colunas de 1 a 6).
* **Frotas:** Cada jogador comanda 4 embarcações (totalizando 10 posições ocupadas):
  * **Porta-aviões:** ocupa 4 casas (identificado na matriz pelo número `4`);
  * **Fragata:** ocupa 3 casas (identificado na matriz pelo número `3`);
  * **Encouraçado:** ocupa 2 casas (identificado na matriz pelo número `2`, blindagem pesada);
  * **Submarino:** ocupa 1 casa (identificado na matriz pelo número `1`).
* **Simbologia Visual no Terminal:**
  * `~` : Água no tabuleiro próprio de posicionamento;
  * `.` : Coordenada ainda não alvejada no tabuleiro de tiros;
  * `X` : Tiro certeiro (atingiu parte de um navio inimigo);
  * `o` : Tiro na água (alvo errado).
* **Condição de Vitória:** O jogo não possui empate; a batalha prossegue turno a turno até que um dos jogadores destrua integralmente todas as 10 partes da frota adversária.

---

## ⚙️ Restrições e Diretrizes Pedagógicas Atendidas

Para atender rigorosamente aos critérios de avaliação da disciplina, o código foi construído utilizando **exclusivamente a lógica e sintaxe fundamentais da linguagem**:

1. **Sem Funções:** Nenhuma função ou procedimento foi definido (`sem def` e `sem return`). Todo o fluxo é estruturado em blocos sequenciais e laços.
2. **Sem Bibliotecas:** Nenhum módulo externo ou biblioteca embutida foi importado (`sem nenhum import`).
3. **Sem Tratamento de Exceções:** Não utiliza `try / except`. As entradas do usuário são tratadas e validadas comparando as strings fornecidas com caracteres válidos (`str(numero)`) em laços `while`.
4. **Sem Métodos de Coleção/Texto:** Não foram utilizados métodos prontos como `.isdigit()`, `.append()`, dicionários, nem listas auxiliares fora das matrizes do tabuleiro.
5. **Sem Comandos de Quebra Forçada:** Não utiliza `break`. O controle de execução é feito exclusivamente por meio de variáveis lógicas/booleanas.
6. **Matrizes e Laços Aninhados:** As matrizes 6x6 foram declaradas por extenso e toda renderização, verificação de vitória e reinício é realizada através de laços `for` aninhados.

---

## 🎮 Funcionalidades do Sistema

* **Menu Principal Interativo:**
  * `1` - Iniciar nova partida
  * `2` - Ver regras do jogo e símbolos
  * `3` - Exibir placar geral
  * `0` - Sair do programa
* **Validação Robusta:** O sistema é blindado contra entradas vazias, letras, símbolos e números fora da escala permitida (1 a 6).
* **Sistema de Placar Contínuo:** Acumula as vitórias do Jogador 1 e Jogador 2 enquanto o programa permanecer aberto.
* **Reinicialização Completa:** Permite disputar múltiplas partidas seguidas sem fechar o terminal, limpando as matrizes via `for` aninhado e mantendo o placar atualizado.
* **Sigilo Tático:** Utiliza espaçamento visual de tela para que um jogador não visualize a frota nem os tiros do outro durante as passagens de vez.

---

## 🚀 Como Executar o Jogo

### Pré-requisitos:
* **Python 3.8** ou superior instalado no sistema operacional.

### Passo a passo:
1. Clone o repositório ou baixe os arquivos do projeto:
   ```bash
   git clone https://github.com/Ebenezer-cds/Batalha-dos-navais.git
   cd Batalha-dos-navais
   ```

2. Execute o arquivo principal pelo terminal:
   ```bash
   python frota_naval.py
   ```

---

## 📂 Organização do Código (`frota_naval.py`)

| Bloco | Responsabilidade no Sistema | Estruturas Utilizadas |
| :--- | :--- | :--- |
| **Bloco 1** | Declaração das matrizes 6x6 e variáveis do placar e de controle | Listas de listas, inteiros e booleanas |
| **Bloco 2** | Menu principal com opções (jogar, regras, placar e sair) | `while`, `input()`, `if/elif/else` |
| **Bloco 3** | Posicionamento validado da frota de cada jogador (Submarino, Fragata, Encouraçado e Porta-aviões) | `for` aninhado, `while`, `if/else` |
| **Bloco 4** | Laço da partida: exibição dos tabuleiros e leitura/validação dos disparos | `while`, `for` aninhado, `if/else` |
| **Bloco 5** | Verificação de vitória com contagem de partes restantes e atualização do placar | `for` aninhado, operadores lógicos, alternância de turnos |

---

## 👥 Autores
* **Héber Ebenézer**
* **Valderso Leandro**
* **Carlos Felix**

*UNINASSAU – Ciência da Computação (2026)*
