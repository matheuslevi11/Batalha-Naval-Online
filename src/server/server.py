import socket
from _thread import *

# Variáveis que serão utilizadas no jogo
x = '0'
y = '0'
number_of_connections = 0
turn = '1'
ready = 0
score = {'1': 0, '2': 0}
# ----------------------------------------

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = 'localhost'
    port = 8080
    server_adress = (server_host, port)

    try:
        server_socket.bind(server_adress) 

    except socket.error as error:
        print(str(error))

    server_socket.listen(2)
    print("Aguardando por jogadores")
    
    # Loop do socket aguardando conexões
    while True:
        conn, address = server_socket.accept()
        print("Um jogador com este endereço se conectou: ", address)
        global number_of_connections
        number_of_connections += 1
        # Inicia uma nova thread no servidor para cada nova conexão
        start_new_thread(client_connection, (conn,))

def client_connection(conn):
    global number_of_connections, turn, x, y, ready, score
    conn.send(str.encode('Início da conexão'))
    response = ' '

    while True:
        try:
            request = conn.recv(4096).decode('utf-8')
            request = request.split(' ')
            # code - operação enviada pelo usuario segundo o protocolo
            code = request[0]
            
            if code == "players":
                response = str(number_of_connections)
            elif code == "turn":
                response = str(turn)
            
            elif code == "play":
                player = request[1]
                result = request[2]
                x = request[3]
                y = request[4]
                print(f"Player {player} atirou em [{x}][{y}] e {result}")
                
                if result == 'acertou':
                    score[player] += 1
                
                # Trocando o turno após a jogada
                if turn == '1':
                    turn = '2'
                elif turn == '2': 
                    turn = '1'

            elif code == "score":
                print(f"{score['1']} {score['2']}")
                response = f"{score['1']} {score['2']}"
                # Checando condições de vitória
                if score['1'] == 10:
                    response = "winner 1"
                if score['2'] == 10:
                    response = "winner 2"

            conn.sendall(str.encode(response))
        except Exception as error:
            print('Erro no servidor!', error)
            break

    print("Jogador se desconectou")
    number_of_connections -= 1
    if number_of_connections == 0:
        # jogo se encerrou
        turn = '1'
        score = {'1': 0, '2': 0}
    conn.close()

main()