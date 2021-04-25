import threading
import time


class FtpServerProtocol(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.value = 0

    def run(self):
        while True:
            print("here")
            time.sleep(2)


if __name__ == "__main__":
    f = FtpServerProtocol()
    f.start()
    while True:
        print("asdd")
        time.sleep(1)
