import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 9988))
sock.listen()
conn, addr = sock.accept()
print("Accept a connect from: %s" % str(addr))
ret = conn.recv(1024)
print(ret)
conn.send(b'hi')
conn.close()
sock.close()