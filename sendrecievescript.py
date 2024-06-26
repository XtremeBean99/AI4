 import socket
 import base64
 
 def receiveAndSend():
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
     server_address = ('10.13.37.161', 8000)  # Use a specific port to listen
     sock.bind(server_address)
     while True:
         data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
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
     ip_address, port = addr  # Unpack the address tuple
     server_address = (ip_address, port)  # Use the IP address and port from addr
     message = "cbr_CTF(assignment41357321080805508456)"
     sock.sendto(message.encode("ascii"), server_address)
 
 receiveAndSend()
