#!/usr/bin/python3
#scanner.py
import math
import socket
import time 

startTime = time.time()
pronic = [4032, 4160, 4290, 4422, 4556, 4692, 4830, 4970]

target = input("Please enter the host that you want to scan: ")
# targetIP = socket.gethostbyname(target)
print("Initiating Scan for host: ", target)

for i in pronic:
    print(i)
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = scanner.connect_ex((target, i))
    print(conn)
    if (conn==0):
        print("Port %d: OPEN" %(i))
    scanner.close()

endTime = time.time()
totalTime = endTime - startTime
print('Total Time: %s' %(totalTime))


