import threading

class ServerStatus(object):
    """description of class"""
    def __init__(self):
      self.server_active = True
      self.lock = threading.RLock()

    def shutdown_server(self):
      with self.lock:
        self.server_active  = False

    def is_server_active(self):
      return self.server_active



