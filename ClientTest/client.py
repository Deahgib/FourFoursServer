# Echo client program
import socket
import time

HOST = 'localhost'    # The remote host
PORT = 50175              # The same port as used by the server

for _ in range(10):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		
		s.connect((HOST, PORT))
		s.sendall(b'Hello, world')
		time.sleep(1)