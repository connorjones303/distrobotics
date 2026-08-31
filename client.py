import socket

host = 'pi'
port = 40001
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print('connected to', host, port)
    while True:
        user_input = input('send message:' )
        bytes = user_input.encode('utf-8')
        s.sendall(bytes)
        data = s.recv(1024)
        print('received', repr(data))

