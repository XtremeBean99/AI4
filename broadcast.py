import socket
import time
import base64

# Encrypt the message
messages = ["Patrick: What's the password","John: My password is coolgamebro dont tell anyone","Patrick:whats the ip and port","John:10.13.37.161:8000"]


def broadcast_message():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server_address = ('10.13.37.255', 8000)  # Use broadcasting address and a specific port
    while True:
        for message in messages:
            messageBytes = message.encode("ascii")
            cipher_text = base64.b64encode(messageBytes)
            print(f"Broadcasting encrypted message: {cipher_text}")
            sock.sendto(cipher_text, server_address)
            time.sleep(5)

if __name__ == "__main__":
    broadcast_message()

