# Echo client program
import socket
import time

HOST = 'www.bennette.co.uk'    # The remote host
PORT = 50175              # The same port as used by the server

for _ in range(1):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		
		s.connect((HOST, PORT))
		s.sendall(bytes.fromhex('01 f2 83 e1 a3 44 da b7 af f4 d6 69 ca c9 01 00            63     00 00 00 0a      0b      28 34 2f 34 29 2b 28 34 2f 34 29'))
		time.sleep(1)
		
		
for _ in range(1):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		
		s.connect((HOST, PORT))
		s.sendall(bytes.fromhex('01 f2 83 e1 a3 44 da b7 af f4 d6 69 ca c9 01 00            63     00 00 00 03      0b      28 34 2f 34 29 2b 28 34 2f 34 29'))
		time.sleep(1)
		
		
for _ in range(1):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		
		s.connect((HOST, PORT))
		s.sendall(bytes.fromhex('01 f2 83 e1 a3 44 da b7 af f4 d6 69 ca c9 01 00            63     00 00 00 04      0b      28 34 2f 34 29 2b 28 34 2f 34 29'))
		time.sleep(1)
		
		
for _ in range(1):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		
		s.connect((HOST, PORT))
		s.sendall(bytes.fromhex('01 f2 83 e1 a3 44 da b7 af f4 d6 69 ca c9 01 00            63     00 00 00 06      0b      28 34 2f 34 29 2b 28 34 2f 34 29'))
		time.sleep(1)