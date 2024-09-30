class Jogador:
    def __init__(self, conexao, id):
        self.conexao = conexao
        self.id = id

    def enviar_mensagem(self, mensagem):
        self.conexao.sendall(mensagem.encode())

    def receber_mensagem(self):
        mensagem = self.conexao.recv(1024)
        if mensagem:
            return mensagem.decode()
        else:
            return None

    def processar_mensagem(self, mensagem):
        if mensagem.startswith('mover'):
            x, y, destino_x, destino_y = mensagem.split(' ')[1:]
            x, y, destino_x, destino_y = int(x), int(y), int(destino_x), int(destino_y)
            self.mover_peca(x, y, destino_x, destino_y)
        else:
            print(`Mensagem desconhecida: ${mensagem}`)

    def mover_peca(self, x, y, destino_x, destino_y):
        if self.conexao.tabuleiro[x][y] == 1:
            self.conexao.tabuleiro[x][y] = 0
            self.conexao.tabuleiro[destino_x][destino_y] = 1
            return True
        else:
            return False