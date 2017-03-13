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
      str = self.getName() + " working"
      print(str)
      with self.tcp_connection:
          print('Connected by', self.port_address)
          data = self.tcp_connection.recv(1024)

          if not data: return

          print(data)
          self.parse_packet(data)

      self.threads.push(self)
      self.waiting = True
      str = self.getName() + " finnished"
      print(str)



  def parse_packet(self, data):
    # Evaluate greeting
    greeting = bytes.fromhex('01 f2 83 e1 a3 44 da b7 af f4 d6 69 ca c9 01 00')
    index = 0
    for i in range(len(greeting)):
      if(greeting[i] != data[i]):
        return False
    print ("Greeting accepted")

    ## Read player ID (int)
    #index = len(greeting)
    #playerID = data[index: index+4]
    #playerID = int.from_bytes(playerID, byteorder='big', signed = False)
    ##print(playerID)
    ## Read name length (char)
    #index += 4
    #playerNameLength = int.from_bytes(data[index:index+1], byteorder='big', signed = False)

    ## Read name (str)
    #index += 1
    #playerNameBytes = data[index:index+playerNameLength]
    #playerName = playerNameBytes.decode("utf-8")
    ##print (playerName)

    # Get game mode (char)
    index += len(greeting)
    gameMode = data[index:index+1].decode("utf-8")
    index += 1
    #print (gameMode)

    # Solution for int (int)
    target = data[index: index+4]
    target = int.from_bytes(target, byteorder='big', signed = False)
    index += 4
    #print(target)

    # Read solution length (char)
    solutionLength = int.from_bytes(data[index:index+1], byteorder='big', signed = False)
    index += 1
    #print (solutionLength)

    # Read solution (str)
    solutionBytes = data[index:index+solutionLength]
    solution = solutionBytes.decode("utf-8")
    #print (solution)

    self.insert_data(gameMode, target, solution)


  def insert_data(self, gameMode, target, solution):
    connection = sqlite3.connect("game-results.db")
    cursor = connection.cursor()
    sql_command = """

        INSERT INTO results (game_mode, target, solution) 
        SELECT '{0}', {1}, '{2}'
        WHERE NOT EXISTS
          ( SELECT 1 FROM results WHERE
          target = {1} 
          AND solution = '{2}')

    """.format(gameMode, target, solution)
    cursor.execute(sql_command)
    connection.commit()
    cursor.close()
    connection.close()
