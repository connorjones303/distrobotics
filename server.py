# echo server
import socket

host = '0.0.0.0'
port = 4000
# gracefully instantiate a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print('starting socket on', host, port)
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)

        
