import socket
import os
import shutil
import zipfile

buff_size = 512

# откроем файл
f = open('zenitsu.jpg', 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST, PORT = "localhost", 9999
sock.connect((HOST, PORT))
# sock.send(b'Message')
data = ''

while data != b'':
    data = f.read(buff_size)
    sock.send(data)
sock.close()

f.close()



