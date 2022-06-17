import socket
import os

# Connect to battery server and request charge. Printing it at end
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.1.78', 8089))
clientsocket.send('get'.encode())
buf = clientsocket.recv(64)
charge = 0
if len(buf) > 0:
    charge = float(buf.decode().strip(" Percent"))

print(charge)
#if charge >= 100:
#    os.system("shutdown now")
