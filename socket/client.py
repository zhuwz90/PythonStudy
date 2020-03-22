import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9988))
sock.send(b'hello!')
ret = sock.recv(1024)
print(ret)
sock.close()