import socket
import threading
import io

class TCPServer:
    def __init__(self):
        self.server_host = 'localhost'
        self.server_port = 7896
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_host, self.server_port))
        self.server_socket.listen()

    def start(self):
        print("Servidor iniciado")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Conexão estabelecida com {client_address}")
            connection = Connection(client_socket)
            connection.start()

class Connection(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
    
    def run(self):
        data = self.client_socket.recv(1024).decode()
        print(data)
        self.client_socket.send(data.upper().encode())
        # linha abaixo deve ser descomentada para a Q2 item F, comentar as linhas acima
        # self.client_socket.send("kelvyaaaaa\n123\n19".encode())

if __name__ == "__main__":
    server = TCPServer()
    server.start()