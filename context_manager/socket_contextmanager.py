import socket
from contextlib import contextmanager


@contextmanager
def socketcontext(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    
    yield server
    
    server.close()
    

        

with socketcontext('localhost', 9999) as server:
    client, address = server.accept()