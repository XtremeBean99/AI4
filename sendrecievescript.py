import socket
import base64


def recieveAndSend():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('10.13.37.161', 8000)  # Use broadcasting address and a specific port
    sock.bind(server_address)
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        stringData = ""
        try:
            stringData64 = base64.b64decode(data)
            stringData = stringData64.decode("ascii")
        except:
            stringData = data.decode("ascii")

        if stringData == "coolgamebro":
            sendSecret(addr)
        print(stringData)

def sendSecret(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (addr, 8000)  # Use broadcasting address and a specific port
    message = "cbr_CTF(assignment41357321080805508456)"
    sock.sendto(message.encode("ascii"), server_address)
recieveAndSend()
