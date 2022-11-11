import os

# Returns a dictionary of the current UPS info
def get_info():
    ups_info = os.popen("apcaccess").read().strip()

    ups_info = dict(item.split(": ") for item in ups_info.split("\n"))

    new_ups_info = {}
    for key,item in ups_info.items():
        new_ups_info[key.strip()] = item.strip()
    return new_ups_info

charge = get_info()["BCHARGE"]
charge = float(charge.split()[0])
if charge <= 20:
    os.system("shutdown now")    
