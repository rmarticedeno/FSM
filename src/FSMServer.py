import rpyc

class FSMServer(rpyc.Service):

    def __init__(self, id, conn_validator, status_info):
        super().__init__()
        self.id = id
        self.conn_validator = conn_validator
        self.status_info = status_info

    def on_connect(self, conn):
        if not self.conn_validator(conn):
            conn.close()

    def exposed_info(self):
        return (self.id, self.status_info())