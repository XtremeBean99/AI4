 import socket
 
 def send_password():
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     server_address = ('10.13.37.161', 8000)  # Ensure this matches the IP and port your server is listening on
     password = "coolgamebro"
     messageBytes = password.encode("ascii")
     
     # Send the password
     print(f"Sending message: {messageBytes}")
     sock.sendto(messageBytes, server_address)
     
     # Listen for a response
     sock.settimeout(5)  # Set a timeout for the response
     try:
         data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
         print(f"Received response from {addr}: {data.decode('ascii')}")
     except socket.timeout:
         print("No response received within the timeout period.")
 
 if __name__ == "__main__":
     send_password()
