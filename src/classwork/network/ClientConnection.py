import time
import threading
import socket
import errno

class ClientConnection(threading.Thread):
    __clientSocket = socket.socket()
    __mutexLocker = threading.Lock()

    __ThreadStop = False
    __poolMessageForSending = list()

    __clientName = str()

    def StopThread(self):
        self.__ThreadStop = True

    def __init__(self, client: socket.socket, broadcastFunc, killMePlease):
        threading.Thread.__init__(self)
        self.__clientSocket = client
        self.__clientSocket.settimeout(10)
        self.__funcSendAll = broadcastFunc
        self.__killMePlease = killMePlease

    def addMessageForSending(self, message):
        self.__mutexLocker.locked()
        self.__poolMessageForSending.append(message)
        self.__mutexLocker.release()

    def run(self):
        while True:
            # Проверить наличие сообщений для этого клиента
            self.__mutexLocker.locked()
            if len(self.__poolMessageForSending) > 0:
                for message in self.__poolMessageForSending:
                    self.__clientSocket.send(message.encode())

                self.__poolMessageForSending.clear()
            self.__mutexLocker.release()
            # Отправить все сообщения

            if self.__ThreadStop:
                break
            try:
                dataBinary = self.__clientSocket.recv(1024)
                if not dataBinary:
                    # Отправить сообщение о том что клиент отключился
                    self.__funcSendAll(self.__clientName,f"{self.__clientName} покинул чат")
                    break
                message = dataBinary.decode()
                # Отправить сообщение всем остальным
                if len(self.__clientName):
                    self.__funcSendAll(f"{self.__clientName}: {message}")
                else:
                    self.__clientName = message
                    self.__funcSendAll(f"{self.__clientName} вошел в чат")

            except errno.ETIMEDOUT:
                continue

            except Exception as error:
                print(error)
                break

        if self.__clientSocket:
            self.__clientSocket.close()
