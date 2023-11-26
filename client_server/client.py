import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 8002)
client_socket.connect(server_address)
print("Connected to {}:{}".format(*server_address))

try:
    # Send data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())
    print("Sent:", message)

    # Receive the response from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())
finally:
    # Clean up the connection
    print("Closing connection")
    client_socket.close()
