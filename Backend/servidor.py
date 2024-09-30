import xmlrpc.server

class JogoRPC:
    def __init__(self):
        self.tabuleiro = [
            [None, None, 1, 1, 1, None, None],
            [None, None, 1, 1, 1, None, None],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [None, None, 1, 1, 1, None, None],
            [None, None, 1, 1, 1, None, None]
        ]

    def mover(self, x, y, destino_x, destino_y):
        if self.tabuleiro[x][y] == 1:
            self.tabuleiro[x][y] = 0
            self.tabuleiro[destino_x][destino_y] = 1
            return True
        else:
            return False

    def get_tabuleiro(self):
        return self.tabuleiro

# CriarRPC
servidor = xmlrpc.server.SimpleXMLRPCServer(('localhost', 12345))

#JogoRPC no servidor
servidor.register_instance(JogoRPC())

# Iniciar o servidor
print("Servidor RPC iniciado...")
servidor.serve_forever()