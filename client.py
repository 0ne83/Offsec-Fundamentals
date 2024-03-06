#/usr/bin/python3
#client.py

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000
res=b"Hello"
try:
    client.connect((host, port))
    print(client.recv(11).decode("ascii"))
    client.send(res)

except ConnectionRefusedError:
    print("The server is not accepting our connection request!")
    exit(1)

client.close()



# while True:
#     msg = client.recv(11)
#     print(msg.decode("utf-8", "ignore"))
#     break
#     if not msg:
#         break
#
#     res += msg
    # client.send(msg)
# resStr=res.decode("utf-8", errors="ignore")
# print(res)
# enc = chardet.detect(res)['encoding'] 
# print(enc)
# print(res.decode("utf-8","ignore"))
