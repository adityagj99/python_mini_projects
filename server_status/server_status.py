import socket

def isrunning(site):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False


while True:
    site = input("Please enter URL: ")
    if isrunning(f"{site}"):
        ip_address = socket.gethostbyname(site)
        print(f"\nIP adress of {site} is: {ip_address}")
        print(f"\n{site} is running!\n")
    else:
        print(f"\nThere is problem with {site}!\n")
    if str(input("Would you like to check another website? (y/n) ")) not in ("y","Y"):
        break