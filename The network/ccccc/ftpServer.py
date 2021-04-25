import socket
from pyftpdlib.servers import FTPServer
HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 9999        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    s.settimeout(None)

    try:
        conn, addr = s.accept()
        conn.sendall("200 Welcome to the coolest Server ever".encode())
    except socket.error:
        print('No connections')
    else:
        print('Connected by', addr)
    #     data = conn.recv(1024).decode('utf-8')
        # if data == "QUIT":
        #     conn.sendall("221 adios stranger!".encode())
        # data = ''
        # while data != "QUIT":
        #     data = conn.recv(1024).decode('utf-8')
        #     print(data)
