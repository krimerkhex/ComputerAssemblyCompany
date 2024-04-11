from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui_History import Ui_OrdersHistory
import psycopg2
from logger import Loger, logger


DB_NAME = 'postgres'
USER_NAME = 'postgres'
PASSWORD = 'user'
HOST = '127.0.0.1'

class HistoryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OrdersHistory()
        self.ui.setupUi(self)
        self.table = self.ui.Table
        self.table.setColumnCount(7)
        self.user = ""
        self.update()

    def update(self):
        self.table.setHorizontalHeaderLabels(["PRICE","CPU","GPU","RAM","HDD","POWER","FRAME"])
        self.table.setRowCount(100)
        with psycopg2.connect(dbname=DB_NAME, user=USER_NAME, password=PASSWORD, host=HOST) as conn:
            with conn.cursor() as cur:
                cur.execute(f"Select id from Clients where login = '{self.user}';")
                id = cur.fetchone()
                if id:
                    cur.execute(f"""Select a.price, a.cpu, a.gpu, a.ram, a.frame, a.power, a.hdd from History o
                    join assemblies a on o.assemblies_id = a.id
                    where o.client_id = {id[0]};""")
                    row = 0
                    for line in cur.fetchall():
                        self.table.setItem(row, 0, QTableWidgetItem(str(line[0])))
                        self.table.setItem(row, 1, QTableWidgetItem(line[1]))
                        self.table.setItem(row, 2, QTableWidgetItem(line[2]))
                        self.table.setItem(row, 3, QTableWidgetItem(line[3]))
                        self.table.setItem(row, 4, QTableWidgetItem(line[4]))
                        self.table.setItem(row, 5, QTableWidgetItem(line[5]))
                        self.table.setItem(row, 6, QTableWidgetItem(line[6]))
                        row += 1
