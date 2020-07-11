#Python port scanner

import socket

address = input("IP Address to scan: ")
startPort = input("Starting port: ")
startPort = int(startPort)
endPort = input("Ending port: ")
endPort = int(endPort)

for i in range(startPort, endPort):
    s = socket.socket()
    s.settimeout(2.0)
    status = s.connect_ex((address, i))
    if status == 0:
        print("Port " + str(i) + ":      Open")

