# -*- coding: utf-8 -*-

import threading
import socket

HOST = '127.0.0.1'
PORT = 5678

def response(conn, addr):
    try:
        print(threading.current_thread().getName())
        while True:
            res = conn.recv(1024)
            if not res:
                break;
            print('recvfrom %s:%s msg: %s' % (addr[0], addr[1], res))
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()

def server(serverip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((serverip, port))
    server.listen()

    t_l = []
    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=response, args=(conn, addr))
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

if __name__ == '__main__':
    server(HOST, PORT)