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

ups_info = get_info()
bat_perc = float(ups_info["BCHARGE"].replace(" Percent",""))

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send(str(bat_perc).encode())
