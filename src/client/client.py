import socket

class Socket:
    
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 8080
        self.address = (self.host, self.port)
        self.id = self.connect_to_server()
    
    def connect_to_server(self):
        self.client.connect(self.address)
        return self.client.recv(4096).decode()

    def send_to_server(self, data):
        """Função principal do socket que envia dados para o servidor e retorna a resposta"""
        try:
            self.client.send(data.encode('utf-8'))
            response = self.client.recv(4096).decode()
            return response
        except socket.error as error:
            return str(error)

def connect_player(cliente):
    player = 2
    while True:
        request = "players"
        response = cliente.send_to_server(request)
        while response == '1':
            response = cliente.send_to_server(request)
            player = 1
        break
    
    return player

def get_turn(cliente):
    request = "turn"
    response = cliente.send_to_server(request)
    
    return int(response)

def get_score(cliente):
    request = "score"
    response = cliente.send_to_server(request)
    response = response.split(' ')
   
    return (response[0], response[1])