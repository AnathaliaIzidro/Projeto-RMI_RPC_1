# Jogo de Resta Um

Este é um jogo de estratégia para dois jogadores. O objetivo é ser o último jogador com peças no tabuleiro.

## Como jogar

1. Execute o servidor com o comando `python servidor.py`.
2. Execute o cliente com o comando `python cliente1.py`e `python cliente2.py`.
3. Conecte-se ao servidor com o endereço IP e a porta (por exemplo, `localhost:12345`).
4. Jogue o jogo digitando comandos no terminal.

## Comandos disponíveis

* `mover x y destino_x destino_y`: move uma peça da posição (x, y) para a posição (destino_x, destino_y).
* `sair`: sai do jogo.

## Tecnologias utilizadas

* Python 3.x
* Biblioteca `random` para gerar números aleatórios.
