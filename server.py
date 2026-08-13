import socket

# gracefully instantiate a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_ipv4:
    
    # bind and ip and port for server
    socket_ipv4.bind(('0.0.0.0', 4000))

    # config max sockets
    socket_ipv4.listen(5)

    # main loop
    while True:

        # instantiate the socket info of client
        client_socket, client_address = socket_ipv4.accept()
        
        # gracefully manage client socket resource
        with client_socket:
            # config buffer size in bytes
            data = client_socket.recv(1024)

            # send message to client
            client_socket.sendall(b'handshake complete')
            client_socket.sendall(client_address)

            # immediately close connection
            socket_ipv4.sendall(b'socket closing')
            
            # client gracefully closes upon exiting with block
