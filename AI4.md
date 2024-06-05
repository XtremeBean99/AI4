# Detailed Setup Summary and Solutions for VM Challenge

## Detailed Setup Summary

### Step-by-Step Setup of the Challenge in the VM

1. **Virtual Machine Setup**:
   - Installed Ubuntu on a virtual machine using VirtualBox.
   - Configured the VM with a bridged network adapter to ensure it could communicate with other devices on the same network.

2. **Installing Necessary Software**:
   - Installed Python 3 on the VM using the command: `sudo apt-get install python3`.

3. **Creating the Broadcast Script**:
   - Initially attempted to copy-paste the script directly into the VM using the terminal, but the paste function was not working.
   - Overcame this challenge by using SSH to connect to the VM from my host machine. This allowed me to easily transfer the script.
   - Used the following command to SSH into the VM: `ssh username@10.13.37.161`.
   - Created the broadcast script using the nano editor:
     ```sh
     nano broadcast_message.py
     ```
   - Pasted the following broadcast script into `broadcast_message.py`:

     ```python
     import socket
     import time
     import base64

     # Encrypt the message
     messages = ["Secret Message", "password is coolgamebro dont tell anyone"]

     def broadcast_message():
         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
     ```

4. **Setting Up the Script to Run on Startup**:
   - Created a cron job to ensure the script runs on startup:
     ```sh
     crontab -e
     ```
   - Added the following line to the crontab file:
     ```sh
     @reboot /usr/bin/python3 /home/username/broadcast_message.py
     ```

### Completed Steps Summary

- Set up the VM and installed necessary software.
- Created and transferred the broadcast script using SSH due to initial difficulties with direct copy-paste.
- Configured the VM to run the broadcast script on startup using cron jobs.

## Solutions to the Challenge

### Solution 1: Using Wireshark and a Decryption Script

1. **Capturing Packets with Wireshark**:
   - Installed Wireshark on the host machine.
   - Started a packet capture on the network interface connected to the VM.
   - Applied the filter to isolate packets sent to port 8000:
     ```plaintext
     udp.port == 8000
     ```
   - Identified and exported the captured encrypted message.

2. **Decryption Script**:
   - Created a Python script to decrypt the captured messages:
     ```python
     import base64

     def decrypt_message(cipher_text):
         decoded_bytes = base64.b64decode(cipher_text)
         decrypted_message = decoded_bytes.decode("ascii")
         return decrypted_message

     if __name__ == "__main__":
         # Replace 'your-captured-encrypted-message-here' with the actual captured message from Wireshark
         encrypted_message = b'your-captured-encrypted-message-here'
         print("Decrypted message:", decrypt_message(encrypted_message))
     ```

### Solution 2: Using a Packet Capturing and Decryption Script

1. **Capturing and Decrypting Packets**:
   - Created a Python script to capture and decrypt packets directly:
     ```python
     import socket
     import base64

     def recieveAndSend():
         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         server_address = ('0.0.0.0', 8000)  # Bind to all interfaces on port 8000
         sock.bind(server_address)
         while True:
             data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
             stringData = ""
             try:
                 stringData64 = base64.b64decode(data)
                 stringData = stringData64.decode("ascii")
             except:
                 stringData = data.decode("ascii")

             print(f"Received encrypted message: {data}")
             print(f"Decrypted message: {stringData}")

             if stringData == "Secret Message":
                 sendSecret(addr)

     def sendSecret(client_address):
         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         server_address = client_address  # Use the address of the client that sent "Secret Message"
         message = "secret info you win"
         sock.sendto(message.encode("ascii"), server_address)

     if __name__ == "__main__":
         recieveAndSend()
     ```

## Coversheet and Instructions for the Challenge

### Challenge Coversheet

#### Title: Capturing and Decrypting Encrypted Messages from a Virtual Machine

**Objective**: Participants will use network analysis tools and Python scripting to capture and decrypt encrypted messages broadcasted by a virtual machine.

**Tools Needed**:
- Virtual Machine (VM) with a Linux-based OS
- Nmap
- Wireshark
- Python 3
- Basic knowledge of networking and Python programming

### Instructions for Attempting the Challenge

#### Step 1: Discover the VM's IP Address

1. Use Nmap to scan the network and discover the VM's IP address.
   ```bash
   nmap -sn 10.13.37.0/24
   ```

#### Step 2: Capture Packets Using Wireshark

1. Install Wireshark on your host machine.
2. Start a packet capture on the network interface connected to the VM.
3. Apply the filter to capture UDP packets on port 8000:
   ```plaintext
   udp.port == 8000
   ```
4. Identify the packets containing the encrypted message and export them for analysis.

#### Step 3: Decrypt the Captured Messages

1. Use the provided decryption script to decrypt the captured messages.

   ```python
   import base64

   def decrypt_message(cipher_text):
       decoded_bytes = base64.b64decode(cipher_text)
       decrypted_message = decoded_bytes.decode("ascii")
       return decrypted_message

   if __name__ == "__main__":
       # Replace 'your-captured-encrypted-message-here' with the actual captured message from Wireshark
       encrypted_message = b'your-captured-encrypted-message-here'
       print("Decrypted message:", decrypt_message(encrypted_message))
   ```

#### Step 4: Use the Packet Capturing and Decryption Script (Alternative Solution)

1. Run the following Python script to capture and decrypt messages directly from the network.

   ```python
   import socket
   import base64

   def recieveAndSend():
       sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       server_address = ('0.0.0.0', 8000)  # Bind to all interfaces on port 8000
       sock.bind(server_address)
       while True:
           data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
           stringData = ""
           try:
               stringData64 = base64.b64decode(data)
               stringData = stringData64.decode("ascii")
           except:
               stringData = data.decode("ascii")

           print(f"Received encrypted message: {data}")
           print(f"Decrypted message: {stringData}")

           if stringData == "Secret Message":
               sendSecret(addr)

   def sendSecret(client_address):
       sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       server_address = client_address  # Use the address of the client that sent "Secret Message"
       message = "secret info you win"
       sock.sendto(message.encode("ascii"), server_address)

   if __name__ == "__main__":
       recieveAndSend()
   ```

**Good luck with the challenge!**
