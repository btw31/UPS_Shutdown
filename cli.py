import socket

# Connect to battery server and request charge. Printing it at end
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.1.78', 8089))
clientsocket.send('get'.encode())
buf = clientsocket.recv(64)
if len(buf) > 0:
    print(buf)
