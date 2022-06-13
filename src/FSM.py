import time
from .FSMServer import FSMServer
from rpyc.utils.server import ThreadedServer
import uuid
import rpyc

class FSM:
    
    def __init__(self, status_info, status_comparer, on_change, peer_resolver, conn_validator, id = None, port = 6000, sleep_time = 300):
        self.id = id if id is not None else str(uuid.uuid4())
        self.status_info = status_info
        self.on_change = on_change
        self.status_comparer = status_comparer
        self.sleep_time = sleep_time
        self.peer_resolver = peer_resolver
        self.port = port
        self.server = FSMServer(self.id, conn_validator, status_info)
    
    def _connect(self, host, port):
        conn = rpyc.connect(host, port)
        info = conn.root.info()
        local_info = self.status_info()
        if info[0] != self.id and self.status_comparer(local_info, info):
            self.on_change()

    def start(self):
        s = ThreadedServer(self.server, port=self.port)
        s._start_in_thread()
        while(True):
            try:
                for ip in self.peer_resolver():
                    self._connect(ip, self.port)
            finally:
                time.sleep(self.sleep_time)
            
            