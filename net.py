import socket

class Network:

    def __init__(self):
        self.PORT = 5050
        self.SERVER = "192.168.43.215"
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pos = self.connect()

    def get_pos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect((self.SERVER, self.PORT))
            return self.client.recv(1024).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(1024).decode()
        except socket.error as e:
            print(e)
