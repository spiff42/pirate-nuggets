import socket
import time

# Initialize the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP and port
server_socket.bind(('0.0.0.0', 1234))

# Listen for incoming connections
server_socket.listen(1)
print("Listening for connections on port 9999")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8').strip()
            if not data:
                break

            print(f"Received command: {data}")

            # Handle the command
            if data.upper() == 'HELLO':
                client_socket.sendall("Hello from server!\n".encode('utf-8'))
            elif data.upper() == 'TIME':
                current_time = time.ctime()
                client_socket.sendall(f"Current time: {current_time}\n".encode('utf-8'))
            elif data.upper() == 'EXIT':
                client_socket.sendall("Goodbye!\n".encode('utf-8'))
                break
            else:
                client_socket.sendall("Unknown command.\n".encode('utf-8'))

    finally:
        # Close the client socket
        client_socket.close()
        print(f"Closed connection from {client_address}")
