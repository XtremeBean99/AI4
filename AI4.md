## Project Plan: Capturing and Decrypting Encrypted Messages from a Virtual Machine

### Introduction

This project will guide participants through the process of setting up a virtual machine that broadcasts an encrypted message in a loop. Participants will be required to use network analysis tools like Wireshark to capture these packets and then develop their own Python script to decrypt the message. An additional challenge is included, where participants must first discover the IP address of the virtual machine using network scanning tools like Nmap before they can log on and start capturing packets.

### Project Objectives

1. **Set Up a Virtual Machine (VM):** Create a VM that runs a Python script to broadcast an encrypted message continuously.
2. **Network Scanning:** Teach participants to use Nmap to find the IP address of the VM.
3. **Packet Sniffing:** Guide participants on using Wireshark to capture network packets containing the encrypted message.
4. **Decryption Challenge:** Instruct participants on writing a Python script to decrypt the captured message.

### Steps to Achieve the Objectives

#### 1. Setting Up the Virtual Machine

1. **Create a VM:**
   - Use a virtualisation platform such as VirtualBox, VMware, or a cloud service like AWS.
   - Install a Linux-based OS (e.g., Ubuntu) on the VM.

2. **Install Necessary Software:**
   - Python 3
   - Necessary Python libraries (e.g., `cryptography`, `socket`)

3. **Develop the Encryption Script:**
   - Write a Python script that encrypts a message and sends it over the network. Use a simple encryption method such as Caesar cipher, AES, etc.

   ```python
   from cryptography.fernet import Fernet
   import socket

   # Generate a key for encryption and decryption
   key = Fernet.generate_key()
   cipher_suite = Fernet(key)

   # Message to be encrypted
   message = b"Secret Message"

   # Encrypt the message
   encrypted_message = cipher_suite.encrypt(message)

   # Set up a socket to broadcast the message
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

   while True:
   	s.sendto(encrypted_message, ('<broadcast>', 12345))
   ```

4. **Run the Script:**
   - Ensure the script runs automatically on VM startup. This can be achieved by adding the script to the startup applications or using a cron job.

#### 2. Network Scanning with Nmap

1. **Hide the VM’s IP Address:**
   - Configure the VM’s network settings to use a bridged adapter or a host-only adapter to make the IP less predictable.

2. **Nmap Tutorial:**
   - Provide a tutorial on using Nmap to discover the IP address of devices on the network.

   ```bash
   nmap -sn 192.168.1.0/24
   ```

#### 3. Packet Sniffing with Wireshark

1. **Wireshark Installation:**
   - Guide participants to install Wireshark on their host machine.

2. **Capture Packets:**
   - Instruct participants to start a packet capture on the network interface connected to the VM.

3. **Filter Packets:**
   - Use Wireshark filters to isolate the packets containing the encrypted message.

   ```bash
   udp.port == 12345
   ```

#### 4. Decryption Challenge

1. **Packet Extraction:**
   - Teach participants how to export the captured packets from Wireshark for analysis.

2. **Write a Decryption Script:**
   - Guide participants to write a Python script to decrypt the captured messages. Provide the encryption key used in the VM script.

   ```python
   from cryptography.fernet import Fernet

   # The encryption key used in the VM
   key = b'your-encryption-key-here'
   cipher_suite = Fernet(key)

   # Encrypted message captured from Wireshark
   encrypted_message = b'encrypted-message-here'

   # Decrypt the message
   decrypted_message = cipher_suite.decrypt(encrypted_message)
   print(decrypted_message.decode('utf-8'))
   ```

### Evaluation and Outcomes

Participants will be evaluated based on their ability to:

1. Discover the IP address of the VM using Nmap.
2. Capture the encrypted messages using Wireshark.
3. Develop a Python script to decrypt the captured messages successfully.

By completing this project, participants will gain practical experience in network security, encryption/decryption, and network scanning techniques. This hands-on challenge will solidify their understanding of these crucial cybersecurity concepts.

Sure, here's a detailed plan for your new cybersecurity challenge, which includes setting up a virtual machine broadcasting an encrypted message and requiring participants to use Wireshark and Python for decryption, with the added step of using Nmap to find the machine's IP address.

## Virtual Machine Setup and Challenge Plan

### Objective

Participants will need to:
1. Use Nmap to discover the IP address of a virtual machine.
2. Use Wireshark to capture network traffic and identify the encrypted message.
3. Develop a Python script to decrypt the message.

### Challenge Overview

1. **Setup a Virtual Machine**:
   - Install a Linux-based VM (e.g., Ubuntu).
   - Configure the VM with a static IP initially but do not disclose it to the participants.
   - Ensure the VM is connected to the same network as the participants.

2. **Python Script for Message Broadcasting**:
   - Create a Python script that continuously sends an encrypted message over the network.
   - Use symmetric encryption (e.g., Caesar cipher or a more complex method like AES) to encrypt the message.

3. **Network Discovery with Nmap**:
   - Instruct participants to use Nmap to find the IP address of the VM.

4. **Packet Sniffing with Wireshark**:
   - Instruct participants to use Wireshark to capture the network traffic and identify the packets containing the encrypted message.

5. **Message Decryption**:
   - Instruct participants to develop a Python script to decrypt the captured message.

### Detailed Steps

#### 1. Virtual Machine Setup

1. **Install and Configure the VM**:
	- Install a VM using a platform like VirtualBox or VMware.
	- Install Ubuntu or any preferred Linux distribution.

2. **Network Configuration**:
	- Set the network adapter to Bridged mode (or another mode that allows direct network communication with the host network).
	- Assign a static IP address initially (do not disclose this IP to participants).

3. **Install Necessary Software**:
	- Install Python and necessary libraries (`sudo apt-get install python3 python3-pip`).
	- Install OpenSSH Server for remote access (`sudo apt-get install openssh-server`).

#### 2. Python Script for Message Broadcasting

Create a Python script named `broadcast_message.py`:

```python
import socket
import time
from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance (for AES encryption example)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the message
message = "Secret Message"
cipher_text = cipher_suite.encrypt(message.encode())

def broadcast_message():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ('<broadcast>', 10000)  # Use broadcasting address and a specific port

	while True:
    	try:
        	print(f"Broadcasting encrypted message: {cipher_text}")
        	sock.sendto(cipher_text, server_address)
        	time.sleep(5)
    	except Exception as e:
        	print(f"Error: {e}")
    	finally:
        	sock.close()

if __name__ == "__main__":
	broadcast_message()
```

#### 3. Network Discovery with Nmap

Participants need to use Nmap to discover the IP address of the VM.

```bash
nmap -sP <network-range>
```

Instruct participants to identify the IP address associated with the VM.

#### 4. Packet Sniffing with Wireshark

Participants will use Wireshark to capture the network traffic and filter for the specific port or protocol used in the broadcast script.

1. **Open Wireshark**.
2. **Start a capture on the network interface connected to the VM**.
3. **Filter by the specific port** (e.g., `udp.port == 10000`).

Participants should be able to identify and extract the encrypted message from the captured packets.

#### 5. Message Decryption

Provide instructions for participants to develop a Python script to decrypt the message. For example, if using Fernet (AES encryption):

```python
from cryptography.fernet import Fernet

# Use the same key used in the broadcast script
key = b'...'  # Replace with the actual key
cipher_suite = Fernet(key)

def decrypt_message(cipher_text):
	plain_text = cipher_suite.decrypt(cipher_text)
	return plain_text.decode()

if __name__ == "__main__":
	encrypted_message = b'...'  # Replace with captured encrypted message
	print("Decrypted message:", decrypt_message(encrypted_message))
```

### Conclusion

Participants will have successfully:
1. Discovered the VM's IP using Nmap.
2. Captured the encrypted message using Wireshark.
3. Decrypted the message using a Python script.

This challenge will test their skills in network scanning, packet analysis, and Python programming.
