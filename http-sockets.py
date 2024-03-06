#!/usr/bin/python3
#http-sockets.py

import socket

remote_host = "192.168.45.201" 
remote_port = 8080

request = "GET http://192.168.234.68/index.html HTTP/1.1\r\nHost: 192.168.234.68\r\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((remote_host,remote_port))
client.send(request.encode())

response = client.recv(4096)
print(response.decode())
