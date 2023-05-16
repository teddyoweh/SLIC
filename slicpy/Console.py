import socket
import ast
import pickle
class Console:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        if self.conn:
            self.conn.close()
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.host, self.port))

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def send(self, data: dict):
        self.connect()
        self.conn.send(str(data).encode("utf-8"))

    def receive(self, buffer_size: int = 1024):
        response = self.conn.recv(buffer_size).decode("utf-8")
        return ast.literal_eval(response)

    def get_server_variable(self, variable_name: str):
        data = {
            "access": ":get_server_variable",
            "payload": {"variable_name": variable_name},
            "type": "regular",
        }
        self.send(data)
        response = self.receive()
        if response["status"] == 200:
            return response["payload"]
        else:
            raise Exception(response["message"])

    def __del__(self):
        self.disconnect()


console = Console("localhost", 9951)
while True:
    var = input("> ")
 

    res = console.get_server_variable(var)
    print(res)
     

    #print(network_traffic)
