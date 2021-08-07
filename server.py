import socket                       

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # print(type(server_socket))

    port_number = 65432

    server_socket.bind(("127.0.1.1", port_number))

    server_socket.listen()

    print(f"Listening for incoming connection on port {port_number}")

    connection, address = server_socket.accept()

    print(f"Connected by {address}.")

    while True:

            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data.upper())

    server_socket.close()
except KeyboardInterrupt:
    print("Exiting \n")
    exit(0)

