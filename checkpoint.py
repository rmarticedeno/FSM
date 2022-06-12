from dns_resolver import get_members
from socket import socket



def filtered_open(func):

    def apply(self, conn):

        ip = socket.getpeername(conn._channel.stream.sock)

        print(ip)

        return func(args, **kwargs)

    return apply

def validate_conn(conn):
    ip = socket.getpeername(conn._channel.stream.sock)
    print(ip)

    return True