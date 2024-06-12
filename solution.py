import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.13.37.161', 8000)
password = "coolgamebro"
messageBytes = password.encode("ascii")
print(f"Broadcasting encrypted message: {messageBytes}")
sock.sendto(messageBytes, server_address)