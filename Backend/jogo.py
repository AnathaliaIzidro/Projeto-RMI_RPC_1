class Jogo:
    def __init__(self):
        self.estado = "iniciado"
        self.tabuleiro = [
            [None, None, 1, 1, 1, None, None],
            [None, None, 1, 1, 1, None, None],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [None, None, 1, 1, 1, None, None],
            [None, None, 1, 1, 1, None, None]
        ]

    def start(self):
        while True:
            if self.estado == "iniciado":
                self.estado = "jogando"
                print("Jogo iniciado!")

            elif self.estado == "jogando":
                self.estado = "fim"
                print("Jogo terminado!")

    def processar_mensagem(self, mensagem):
        if mensagem.startswith('mover'):
            x, y, destino_x, destino_y = mensagem.split(' ')[1:]
            x, y, destino_x, destino_y = int(x), int(y), int(destino_x), int(destino_y)
            self.mover_peca(x, y, destino_x, destino_y)
        else:
            print(`Mensagem desconhecida: ${mensagem}`)

    def mover_peca(self, x, y, destino_x, destino_y):
        if self.tabuleiro[x][y] == 1:
            self.tabuleiro[x][y] = 0
            self.tabuleiro[destino_x][destino_y] = 1
            return True
        else:
            return False