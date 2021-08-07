from socket import socket, AF_INET, SOCK_STREAM 

try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 65432))

    message = input("Message: ")

    client_socket.sendall(bytes(message, "utf-8"))

    received_message = client_socket.recv(1024)

    print(f"You received this message: \n {repr(received_message)}")

except KeyboardInterrupt:
    print("Exiting \n")
    exit(0)