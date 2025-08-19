# Конечные точки (endpooint) - это место приема сетевого трафика (интерфейс, ссылка и т.д.)
# на непосредственно той машине, которая будет осуществлять обработку запроса

# Сокет - это абстрактное представление сетевой конечной точкки выраженный
# в конкретном ip адресе и порту

import socket

ipAdress = "127.0.0.1" #"localhost", но лучше конкретный IP
port = 48084 # до 1024 порта запрещенно использовать без режима привелегий

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((ipAdress, port))
soc.listen()
connective, addr = soc.accept()

while True:

    print(f"Установлено новое соединение: {addr}")
    data = ""
    dataBinary = connective.recv(1024)
    if not dataBinary:
        break

    data += dataBinary.decode()
    print(f"Пришли следующие данные: {data}")
    message = input()

    if message == "quit":
        connective.close()
        break

    connective.send(message.encode())

    if not soc:
        break

