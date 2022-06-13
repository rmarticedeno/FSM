import re
from tkinter.tix import Tree
from src import FSM
from utils import dns_resolver
import socket


def fake_info():
    return 43

def status_comparer(local_info, remote_info):
    return True

def on_change():
    pass

def peer_resolver():
    return dns_resolver('uh.cu')

def fake_resolver():
    return ['127.0.0.1']

def conn_validator(conn):
    ip = socket.getpeername(conn._channel.stream.sock)[0]
    return ip in peer_resolver()

def fake_conn_validator(conn):
    return True


if __name__ == "__main__":
    server = FSM(fake_info, status_comparer, on_change, fake_resolver, fake_conn_validator, sleep_time=10)
    server.start()