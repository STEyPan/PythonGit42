import socket

ipServer = "192.168.3.2"
port = 48084
sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockClient.connect((ipServer, port))

while True:
    message = input("Клиент: ")

    if message == "quit":
        sockClient.close()
        break

    sockClient.send(message.encode())
    data = ""
    dataBinary = sockClient.recv(1024)
    data += dataBinary.decode()
    print(f"Сервер: {data}")

# sockClient.send("Hello Server!!!".encode())
# data = sockClient.recv(1024)

# print(f"Ответ: {data.decode()}")
