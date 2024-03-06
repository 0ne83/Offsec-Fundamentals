#/usr/bin/python3
#client.py

import socket
import telnetlib

def interact(socket):
    t = telnetlib.Telnet()
    t.sock = socket
    t.interact()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000
res=b""
try:
    client.connect((host, port))
    msg = client.recv(11)
    print(msg)
    interact(client)

except ConnectionRefusedError:
    print("The server is not accepting our connection request!")
    exit(1)

client.close()




