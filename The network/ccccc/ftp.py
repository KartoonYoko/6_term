from ftplib import FTP

ftp = FTP()
HOST = 'localhost'
PORT = 9999
print(ftp.connect(HOST, PORT))
print(ftp.login())
# ftp = FTP('ftp.cse.buffalo.edu')
# print(ftp.welcome)
# print(ftp.login())
print(ftp.quit())
