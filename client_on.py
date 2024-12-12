#!/usr/bin/env python3


# NET_CMD_SWITCH_DEVICE_SCREEN 1
import socket

HOST = '192.168.4.208'    # all available interfaces
PORT = 7610  # any port > 1023
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Client connected.')
while True:
    sdata = b'LEDTRL\x00\x00a\x03\x00\x00\x02\x00\x00\x00\x01}\xf9p\xbd\x81\xdb \x08\xf9v\x00g\xde\xecp\x06\x00\x00\x00\x80\xedv\x00\xef\x12\x0bq\xff\xff\xff\xff[}\xf9p\x9eZ\xf8p#[\xf8pF\xd8\x08qQ\x81\xdb \xd0\xedv\x00/\xe0\x08qA\x81\xdb \x08\xf9v\x00g\xde\xecp\x06\x00\x00\x00\xd0\xedv\x00L\xeev\x00\xa9\xf8\nq\xff\xff\xff\xff/\xe0\x08q+\xf7\x08qu\x81\xdb \x08\xf9v\x00\x08\xf9v\x00\x84\x04d\x00R\x00\x10\x00\xe0\xa5\xe5p4\xee\xe8p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x7f\xfc\xc6\xe8p\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x84\xc8\xe8p\xf8\xc8\xe8p\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xeev\x00T\xefv\x00\xd2;\x0cq\x00\x00\x00\x00x\xeev\x00\x12\xf3\x08q\x19\x00\x00\x00\x00\x00\x00\x00\x90\xeev\x00t\xeev\x00\x08\xf9v\x00R\x00\x10\x00\x9c\xeev\x00Q\xe9\x08q\x19\x00\x00\x00\x00\x00\x00\x00\x90\xeev\x00\x05\xe9\x08q\x84\x04d\x00 \x0b\x01\xad\x06\x00\x00\x00`\xefv\x00.\xf6\x08q \x0b\x01\xad\x84\x04d\x00m\x82\xdb 8\x01\x00\x00\x08\xf9v\x00\xc8T\xb0\x00R\x00\x10\x00\xb0\xc3\xe8p\x08[\xee\x00.\xf6\x08q \x0b\x01\xad\x84\x04d\x00\xff\xff\xff\x7f8\x01\x00\x00\x08\xf9v\x00\xc8T\xb0\x00R\x00\x10\x00\xb0\xc3\xe8p\x08[\xee\x00\x9e\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\xff\xff\xff\x7fgc\xbfv<\xefv\x00\x84\x04d\x00*\x03\xa5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x04\x00\x00\x00\x00\xf0v\x00\xdc\xefv\x00\x00\x00\x00\x00m\xbb\x86g\x01\x00\x00\x00\xc8T\xb0\x00\x98X\xb0\x00\x00\x00\x00\x00TL\x0ew0\x00\x00\x00*\x03\xa5\x00\xcd\xab\xba\xdc\x88\xefv\x00\xec\xefv\x00\xd2;\x0cq\x00\x00\x00\x00\x80\xefv\x00\x12\xf3\x08q8\x01\x00\x00 \x0b\x01\xad\x84\x04d\x00|\xefv\x00\x08\xf9v\x00R\x00\x10\x00\xf8\xefv\x00\xff\xd6\x08q8\x01\x00\x00\xf2\xf0\nqS\xd7\x08q%\x83\xdb 8\x01\x00\x00\x13\xac\x19\xeb\x10\xf0v\x00yK\x0ew8\x01\x00\x00R\x00\x10\x00\x93K\x0ew\x84\xb1G\x00\x00\x00\x00\x00\x00\x00\x00\x00R\x00\x10\x00\xf0\xefv\x00\xc8T\xb0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8T\xb0\x000\x90\xaf\x00\xd8\xac\x10q\xf4\xac\x10q\x94\xefv\x00T\xf0v\x00\xe80\x0bq,\xf0v\x000\xf0v\x006z\xf9p\xf4\xac\x10q\xf6\x03\x00\x00\x84\x04d\x00 \x81\x02\x01\x00\x00\x00\x00\\\xf0v\x00\x98x\xbfv`\\C\x01\x00\x00\x00\x00\x04m\xba-\x84\x04d\x00 \x81\x02\x01\x00\x00\x00\x00\x9eZ\xf8pH\xf0v\x00\xd5\xa8\xecp*\x03\xa5\x00\x1d\xf3\x01\x00\\\xf0v\x00\xd5\xce\x04q*\x03\xa5\x00\x84\x04d\x00 \x81\x02\x01\xf8\xf0v\x00H\x07\tq\xa9\x07\tq%\x9c\xdb \xf6\x03\x00\x00\x08\xf9v\x00\x00\x00\x00\x00*\x03\xa5\x00\xcd\xab\xba\xdcgY\xf8p8\x01\x00\x00*\x03\xa5\x00p\xf1v\x00\xca'
    s.sendall(sdata)  # encode needed to transform string to bytes
    data = s.recv(1024)
    if not data:
        break
    print("Data received from server: ", data)  # decode needed to convert data to string
