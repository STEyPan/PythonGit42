import psycopg2
import threading

class DataBaseInterface(threading.Thread):

    __connectDB = psycopg2.connect()
    __cursorDB = "cursor"
    __ThreadStop = False
    __resReady = False
    __results = str()

    def __init__(self):
        threading.Thread.__init__(self)
        self.__connectDB = psycopg2.connect(
            dbname = "postgres",
            user = "postgres",
            host = "localhost",
            password = "postgres",
            port = 5432
        )

        self.__cursorDB = self.__connectDB.cursor()

    def __del__(self):
        self.__connectDB.close()

    def run(self):
        while True:
            pass

        return 0

    def getResult(self):
        if not self.__resReady:
            return str()

        if not self.__results:
            return "not results"

        return self.__results