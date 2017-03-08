from threading import Thread
import threading
import sqlite3

class TCPParser(Thread):

  def parse_tcp(self, conn, addr):
    self.tcp_connection = conn
    self.port_address = addr
    self.waiting = False



  def __init__(self, server_status, thread_stack):
    super().__init__()
    self.daemon = True
    self.waiting = True
    self.server_status = server_status
    self.threads = thread_stack

  def run(self):
    while self.server_status.is_server_active():
      while self.waiting: 
        continue
      print(self.getName(), " working")
      with self.tcp_connection:
          print('Connected by', self.port_address)
          data = self.tcp_connection.recv(1024)
      
          if not data: return

      
          connection = sqlite3.connect("company.db")
          cursor = connection.cursor()
          sql_command = """INSERT INTO employeeTest (staff_number, fname, lname, gender, birth_date)
        VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");"""
          cursor.execute(sql_command)
          cursor.close()
          connection.close()

      self.threads.push(self)
      self.waiting = True
      print(self.getName(), " finnished")