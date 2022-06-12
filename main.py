import rpyc

class FSM(rpyc.Service):

    def on_connect(self, conn):
        if not validate_conn(conn):
            conn.close()

    def exposed_test(self):
        return 42


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(FSM, port=6000)
    t.start()