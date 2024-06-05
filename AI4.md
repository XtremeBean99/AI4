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
     messages = ["Mephistopheles", "my password is 1234 but don't tell anyone"]

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
     
     if __name__ == "__main__":
         recieveAndSend()
     ```

## Challenge Coversheet and Instructions

### Challenge Coversheet

#### Title: Capturing and Decrypting Encrypted Broadcast Messages

**Objective**: Participants are required to capture and decrypt encrypted messages being broadcasted by a virtual machine on a local network.

**Tools Needed**:
- A configured Virtual Machine (VM) with a Linux-based operating system.
- Network scanning tools (e.g., Nmap).
- Network packet capturing tools (e.g., Wireshark).
- Python 3 for scripting.
- Basic understanding of networking, packet analysis, and Python programming.

### Challenge Instructions

#### Overview:
You are provided with a virtual environment where a Linux-based VM is continuously broadcasting encrypted messages over the network. Your task is to capture these messages and decrypt them to reveal their contents.

#### Step 1: Discover the VM's IP Address

1. **Network Scanning**:
   - Use Nmap or any similar tool to scan your network and identify all active devices. You will need to determine which one is your target VM.
   - Example command to scan your network:
     ```bash
     nmap -sn 10.13.37.0/24
     ```

#### Step 2: Capture Network Traffic

1. **Setting Up Packet Capturing**:
   - Install and set up Wireshark on your host machine.
   - Begin capturing packets on the network interface that communicates with the VM. Focus on capturing UDP traffic, as the encrypted messages are being sent over this protocol.
   - Useful Wireshark filter:
     ```plaintext
     udp
     ```

#### Step 3: Analyze the Traffic

1. **Identify the Encrypted Messages**:
   - While monitoring the traffic, look for repeated UDP packets that might be the broadcasted encrypted messages.
   - Take note of any patterns such as packet size, frequency, or specific ports used (e.g., 8000).

#### Step 4: Write a Script to Decrypt the Messages

1. **Decryption Hints**:
   - The messages are encoded and broadcasted in a manner that might require base64 decoding and understanding of simple encryption techniques.
   - Suggested Python functions:
     - `socket` for creating network connections.
     - `base64.b64decode` for decoding the messages.
     - Look into Python's `socket` library to bind to the broadcasting port and listen for incoming messages.

#### Hints and Tips:

- **Python Scripting**:
  - Use Python’s `socket` library to create a listener on the network that intercepts broadcast messages.
  - Apply your knowledge of Python's `base64` module to attempt decryption of these messages.
  
- **Wireshark Use**:
  - Capture traffic over the correct network interface and use filters effectively to isolate relevant data.
  - Pay attention to the details in the packet's data portion which might give you clues for decryption.

- **Testing and Validation**:
  - Make sure your script is capable of running continuously to capture real-time data.
  - Validate the results by cross-checking with known information or debugging outputs.

**Goal**: Successfully decrypt the broadcast message and understand the content.
