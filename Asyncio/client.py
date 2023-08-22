import socket

server_address = ('127.0.0.1', 8000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)

try:
    while True:
        message = input("введите сообщение: ")
        if message.lower() == "exit":
            break

        client_socket.sendall(message.encode())

finally:
    client_socket.close()