import os
import socket

# Returns a dictionary of the current UPS info
def get_info():
    ups_info = os.popen("apcaccess").read().strip()

    ups_info = dict(item.split(": ") for item in ups_info.split("\n"))

    new_ups_info = {}
    for key,item in ups_info.items():
        new_ups_info[key.strip()] = item.strip()
    return new_ups_info

# Create socket that will listen for requets
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.1.78', 8089)) 
serversocket.listen(5) # maximum 5 connections 

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64) 
    # If client sent a "get", respond with battery charge
    if len(buf) > 0 and buf == "get".encode():
        print("Received charge request")
        connection.send(get_info()["BCHARGE"].encode())
