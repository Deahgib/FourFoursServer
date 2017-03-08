import threading 
from TCPParser import TCPParser

class ThreadStack(object):
  def __init__(self, size, server_status):
    print("Starting up threads")
    self.threads = []
    for _ in range(size):
      t = TCPParser(server_status, self ) 
      self.threads.append( t )
      t.start()

    self.lock = threading.RLock()

  def pop(self):
    with self.lock:
      if len(self.threads) > 0:
        return self.threads.pop()
      else:
        return None

  def push(self, thread):
    with self.lock:
      self.threads.append(thread)


