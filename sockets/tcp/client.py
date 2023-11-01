import socket

class TCPClient:
    def __init__(self):
        self.server_host = 'localhost'
        self.server_port = 7896
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_host, self.server_port))

    def start(self):
        message = 'Olá, servidor, meu nome é Kelvy!'
        self.client_socket.send(message.encode())
        data = self.client_socket.recv(1024)
        print('Resposta do servidor:', data.decode())
        self.client_socket.close()

if __name__ == "__main__":
    client = TCPClient()
    client.start()