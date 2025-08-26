import socket
import threading

SERVER = "127.0.0.1"
PORT = 54045

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

username = input("Введите ваше имя: ")
client.sendall(username.encode())

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Ошибка связи с сервером")
            client.close()
            break

def send_messages():
    while True:
        user_input = input()
        if user_input.lower() == 'quit':
            client.sendall(b'quit')  # Сообщение серверу о выходе
            client.close()
            break
        client.sendall(user_input.encode())

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()