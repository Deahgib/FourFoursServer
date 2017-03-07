# Echo server program
import socket
import threading 
from threading import Thread
import sqlite3

def parse_tcp_input(conn, addr):
  print("Doing the good stuff")
  with conn:
      print('Connected by', addr)
      data = conn.recv(1024)
      
      if not data: return

      conn.sendall(b'Server answer is very generic')

if __name__ == '__main__':

  HOST = ''                 # Symbolic name meaning all available interfaces
  PORT = 50175              # Arbitrary non-privileged port
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    s.listen(1)
    print("Listening on port ", PORT)
    while True:
      conn, addr = s.accept()
      t = threading.Thread(target=parse_tcp_input, args=(conn, addr, ))
      t.start()

    

