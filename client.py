from socket import socket, AF_INET, SOCK_STREAM 

try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("127.0.1.1", 65432))

    message = input("Message: ")

    client_socket.sendall(bytes(message, "utf-8"))

    received_message = client_socket.recv(1024)
    print(type(received_message))
    received_message = repr(received_message)
    print(type(received_message))
    print(received_message[2:-1])
    # print(f"You received this message: \n {received_message}")


    client_socket.close()

except KeyboardInterrupt:
    print("Exiting \n")
    exit(0)