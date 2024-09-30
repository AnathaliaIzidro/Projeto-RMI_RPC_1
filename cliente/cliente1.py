import xmlrpc.client

#servidor RPC
servidor = xmlrpc.client.ServerProxy('http://localhost:12345')


def mover(x, y, destino_x, destino_y):
    return servidor.mover(x, y, destino_x, destino_y)


def get_tabuleiro():
    return servidor.get_tabuleiro()

#cliente RPC
print("Cliente1 RPC iniciado...")
while True:
    print("Opções:")
    print("1. Mover peça")
    print("2. Ver tabuleiro")
    print("3. Sair")
    opcao = input("Digite a opção: ")
    if opcao == "1":
        x = int(input("Digite a linha da peça: "))
        y = int(input("Digite a coluna da peça: "))
        destino_x = int(input("Digite a linha de destino: "))
        destino_y = int(input("Digite a coluna de destino: "))
        if mover(x, y, destino_x, destino_y):
            print("Peça movida com sucesso!")
        else:
            print("Erro ao mover peça!")
    elif opcao == "2":
        print("Tabuleiro:")
        print(get_tabuleiro())
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")