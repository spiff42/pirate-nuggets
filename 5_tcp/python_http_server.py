import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and bind to a port
server_socket.bind(("0.0.0.0", 8080))

# Enable the server to accept connections (5 is the number of unaccepted connections that the system will allow before refusing new connections)
server_socket.listen(5)

print("Listening on port 8080")

while True:
    # Establish a connection
    client_socket, address = server_socket.accept()
    print(f"Received request from {address}")

    # Receive the request from the client
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received HTTP request: {request}")

    # Create an HTTP response
    response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
    response_body = "<html><body><h1>Hello, World!</h1></body></html>"

    http_response = f"{response_headers}{response_body}"

    # Send HTTP response
    client_socket.sendall(http_response.encode('utf-8'))

    # Close the connection
    client_socket.close()

