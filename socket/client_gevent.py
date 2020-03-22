from gevent import monkey
monkey.patch_all()
from socket import *
import threading
import gevent
import time

HOST = '127.0.0.1'
PORT = 5678

def client(addr):
    c = socket(AF_INET, SOCK_STREAM)
    c.connect(addr)

    count = 0
    while count < 5:
        c.send(('%s say hello %s' % (
            threading.current_thread().getName(), count)).encode('utf-8'))
        msg = c.recv(1024)
        print(msg.decode('utf-8'))
        count += 1
        time.sleep(1)

    c.close()

if __name__ == '__main__':
    g_l = [gevent.spawn(client, (HOST, PORT)) for i in range(10)]
    gevent.joinall(g_l)