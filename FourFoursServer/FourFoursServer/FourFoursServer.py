# Echo server program
import socket
import threading 
from threading import Thread
import sqlite3
from TCPParser import TCPParser
from ServerStatus import ServerStatus
from ThreadStack import ThreadStack

if __name__ == '__main__':  
  
  connection = sqlite3.connect("game-results.db")
  cursor = connection.cursor()

  sql_command = """
  CREATE TABLE IF NOT EXISTS results ( 
  solution_id INTEGER PRIMARY KEY AUTOINCREMENT,
  game_mode VARCHAR(1), 
  target INTEGER, 
  solution VARCHAR(255)
  );"""
  cursor.execute(sql_command)
  cursor.close()
  connection.close()



  server_status = ServerStatus()
  thread_stack = ThreadStack(15, server_status)

  HOST = ''                 # Symbolic name meaning all available interfaces
  PORT = 50175              # Arbitrary non-privileged port
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Listening on port ", PORT)
    while server_status.is_server_active():
      print ("Waiting for connection ... \n")
      conn, addr = s.accept()
      t = thread_stack.pop()
      t.parse_tcp(conn, addr)
