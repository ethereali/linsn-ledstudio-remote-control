#!/usr/bin/env python3

# NET_CMD_PAUSE
import socket

HOST = '192.168.4.208'  # all available interfaces
PORT = 7610  # any port > 1023
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Client connected.')
while True:
    sdata = b"LEDTRL\x00\x00a\x03\x00\x00\x11\x00\x00\x00\x05\x00\x00\x00\x90nt\x00\x00\x00\x00\x00\x84:s\x00 9s\x00\xc8U/w\x00\x00\x00\x00\x18\x10/w<\r\x01'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x90nt\x00\x98\xef=\x00\x05\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00dfltdflt\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x9cU/w<\r\x01'\x90nt\x00\x00\x00\x00\x00\xff\xff\xff\xffdflt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80vGf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x7f\x8cZn\x008\xfb=\x00X\x8eDf\x00\x00\x00\x00\x03\x00\x00\x00\xa5#\xf4\xa5\x90\xf0=\x00\xc1\xb73w<\r\x01'\xdc5s\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc47s\x00 9s\x00\r\x00\x00\x00\xf89s\x00\x00\x00\x00\x00\x84:s\x00\x00\x00\x00\x00\xb84s\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84:s\x00\x00\x00\x00\x00\xec\xf0=\x00z\xb53w<\r\x01'\xdc5s\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc47s\x0008s\x00\r\x00\x00\x00 9s\x00\r\x00\x00\x00\xf89s\x00\x00\x00\x00\x00\x84:s\x00\xb84s\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00b\x00\x00\x00 9s\x00\x00\x00\x00\x00\xc0ts\x00\x88\xf2=\x00\x86\xb33w\x01\x00\x00\x00\x00\x00\x00\x00<\r\x01'b\x00\x00\x00\x99\xb33w\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\r\x01'b\x00\x00\x00<\r'\xff\xff\xff\xff\xff\xa0(\x00\x00\x01'\x01\x04\x00\x0bm\x00\x00\x00\x00\x00\\\xf1=\x00\xd8\xc02w\r\x00\x00\x00\x00\xf4=\x00\x01\x00\x00\x00x\xf1=\x00\xf8AGw<\r\x01'\x800\x16\x01\r\x00\x00\x00\x00\xf4=\x00NAI\x00\xa8\xf3=\x00c}\xb8v<\r\x01'\x800\x16\x01\r\x00\x00\x00\x00\xf4=\x000/\x16\x01\x16\x00\x00\x00\x8c}\xb8v<\r\x01'\x800\x16\x01\x00\x06sfx\x8dr\x00\x00\x06sfh\xcaq\x00\x1c\x06sfU\x00S\x00E\x00\x00\x00\xdc\xf1=\x00\xf0\x9fZf\xe4\xf1=\x00\xf0\x9fZf\x1c\x06sfx\xaar\x008\xfb=\x00\x00\x00\x00\x00x\xaar\x00\x10\xf2=\x00x\xcbq\x00z\x07\x02\x00\x00\x00\x00\x00<\xf2=\x00\x98x\xb2v0/\x16\x01\x00\x00\x00\x00\x8d\xab9Xx\xcbq\x00z\x07\x02\x00\x00\x00\x00\x00EvYf\x00\x00\x00\x00\xc8skf<\xf2=\x00\x9bAKf\xb6\x07\x07\x00\x1d\xf3\x01\x00\xab\xebffx\xcbq\x00z\x07\x02\x00\xe8\xf2=\x00\xdf\xa6kfG\xa7kf\xa7\xb6\x14?\x02\x04\x00\x008\xfb=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x800\x16\x01\t\x00\x80\x01\x00\x00Kv<\r\x01'<\r\x01'\xa4\xf2=\x00\xf9>\xf4\xa5\xc8\xf2=\x00#\x0c:w\r\x00\x00\x008"
    s.sendall(sdata)  # encode needed to transform string to bytes
    data = s.recv(1024)
    if not data:
        break
    print("Data received from server: ", data)  # decode needed to convert data to string

