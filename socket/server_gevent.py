# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()
# import socket
from gevent import socket
import gevent
import threading

HOST = '127.0.0.1'
PORT = 5678

def response(conn, addr):
    try:
        print(threading.current_thread().getName())
        while True:
            res = conn.recv(1024)
            print('client %s:%s msg: %s' % (addr[0], addr[1], res))
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()

def service():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(100)

    while True:
        conn, addr = server.accept()
        gevent.spawn(response, conn, addr)

if __name__ == '__main__':
    service()
