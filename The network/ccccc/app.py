import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):
    buff_size = 0
    # порт управляющего соединения - 21
    # активный режим, порт - 20
    # пассивный режим, порт > 1024

    def setup(self):
        """

        """
        self.buff_size = 1024

    def send_file(self, file_name: str):
        """
            ОТпрвит файл с именем file
        """
        f = open(file_name, 'rb')
        data = ''
        while data != b'':
            data = f.read(self.buff_size)
            self.request.sendall(data)
        f.close()

    def get_file(self, file_name: str):
        """
            Получить файл с именем file
        """
        op = open(file_name, 'wb')
        while True:
            data = self.request.recv(self.buff_size).strip()
            if not data:
                break

            op.write(data)
            print('Data: {}', format(data))
        op.close()

    def handle(self):

        data = self.request.recv(1024).strip()
        self.request.sendall("200 Welcome to the coolest Server ever".encode())
        print(data)


if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 9999
    with ThreadingTCPServer((HOST, PORT), EchoTCPHandler) as server:
        server.serve_forever()

