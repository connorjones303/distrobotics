# echo server
import socket

host = ''
port = 40001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    print('starting socket on', host, port)
    while True:
        print('awaiting client')
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                print('reveived', repr(data))
                conn.sendall(data)

    
