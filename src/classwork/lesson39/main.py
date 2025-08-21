import socket

ipAdress = "127.0.0.1"
port = 48084

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((ipAdress, port))
soc.listen(10)
connective, addr = soc.accept()

while True:

    print(f"Установлено новое соединение: {addr}")
    data = ""
    dataBinary = connective.recv(1024)
    if not dataBinary:
        break

    data += dataBinary.decode()
    print(f"Ответ: {data}")
    message = input("Сервер: ")

    if message == "quit":
        connective.close()
        break

    connective.send(message.encode())

    if not soc:
        break

