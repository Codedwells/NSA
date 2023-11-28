import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8002)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening on {}:{}".format(*server_address))

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print("Connection from", client_address)

    # Receive and send data
    try:
        while True:
            data = client_socket.recv(1024)
            print("Received:", data.decode())

            # Send a response back to the client
            response = "{} received".format(data.decode())
            client_socket.sendall(response.encode())
    except KeyboardInterrupt:
        # Clean up the connection
        print("Closing connection")
        client_socket.sendall(b'Server closed the connection')
        client_socket.close()
