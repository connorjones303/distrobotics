import socket

host = 'pi'
port = '4000'
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'hello')
    data = s.recv(1024)
print('received', repr(data))

