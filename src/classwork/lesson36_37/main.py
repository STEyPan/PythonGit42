import DataBaseInterface as DBI
import threading
import time


DBManager = DBI()
Thread1 = threading.Thread(target=DBI.DataBaseInterface.run, args=DBManager)

