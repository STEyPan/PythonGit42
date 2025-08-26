import errno
import threading
import socket
from ClientConnection import ClientConnection

class Server:
    __ThreadStop = False
    __socketAddr = str()
    __socketServer = socket.socket()
    __mutexLocker = threading.Lock()

    __clientDict = dict()

    def StopThread(self):
        self.__ThreadStop = True

    def __init__(self, address : str, port: int):
        self.__socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socketServer.bind((address, port))
        self.__socketAddr = address + str(port)

    def SendMessageAll(self, nameClient : str, message : str):

        if nameClient in self.__clientDict:

            for key in self.__clientDict:
                if key == nameClient:
                    continue
                self.__clientDict[key].addMessageForSending(message)
        else:
            for key in self.__clientDict:
                if key == "tempNameClient":
                    self.__clientDict[nameClient] = self.__clientDict["tempNameClient"]
                    self.__clientDict.pop("tempNameClient")
                    continue
                else:
                    pass

    def Leon(self, nameClient: int):
        self.__mutexLocker.locked()

        for key in self.__clientDict:
            if key != nameClient:
                continue
            self.__clientDict[nameClient].StopThread()
            

    def job(self):
        self.__socketServer.listen(10)

        while True:
            try:
                client, addr = self.__socketServer.accept()
                self.__clientDict["tempNameClient"] = ClientConnection(client, SendMessageAll, Leon)
            except errno.ETIMEDOUT:
                continue
            except Exception as error:
                print(error)
                break

        if len(self.__clientDict):
            for client in self.__clientDict:
                client.StopThread()

            self.__clientDict.clear()

        if self.__socketServer:
            self.__socketServer.close()

server_1 = Server("127.0.0.1", 54045)
server_1.job()