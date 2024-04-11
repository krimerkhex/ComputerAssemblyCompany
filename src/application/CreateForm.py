from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui_OrderCreate import Ui_CreateOrder
import psycopg2
from logger import Loger, logger


DB_NAME = 'postgres'
USER_NAME = 'postgres'
PASSWORD = 'user'
HOST = '127.0.0.1'

class CreatingForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateOrder()
        self.ui.setupUi(self)
        self.startbutt = self.ui.Create
        self.table = self.ui.Table
        self.user = ""
        self.startbutt.clicked.connect(self.create)
        self.update()


    def update(self):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["PRICE","CPU","GPU","RAM","HDD","POWER","FRAME"])
        self.table.setRowCount(100)
        with psycopg2.connect(dbname=DB_NAME, user=USER_NAME, password=PASSWORD, host=HOST) as conn:
            with conn.cursor() as cur:
                cur.execute("Select * from Assemblies;")
                row = 0
                for line in cur.fetchall():
                    self.table.setItem(row, 0, QTableWidgetItem(str(line[7])))
                    self.table.setItem(row, 1, QTableWidgetItem(line[1]))
                    self.table.setItem(row, 2, QTableWidgetItem(line[2]))
                    self.table.setItem(row, 3, QTableWidgetItem(line[3]))
                    self.table.setItem(row, 4, QTableWidgetItem(line[4]))
                    self.table.setItem(row, 5, QTableWidgetItem(line[5]))
                    self.table.setItem(row, 6, QTableWidgetItem(line[6]))
                    row += 1

    def create(self):
        row = self.table.currentRow()
        if row >= 0:
            with psycopg2.connect(dbname=DB_NAME, user=USER_NAME, password=PASSWORD, host=HOST) as conn:
                with conn.cursor() as cur:
                    cur.execute(f"Select id from Clients where login = '{self.user}';")
                    id = cur.fetchone()
                    if id:
                        request = f"INSERT INTO Orders (Client_ID, Assemblies_ID, Price, Ready) values ({id[0]}, {row+1}, '{self.table.itemAt(row, 0).text()}', false);"
                        print(request)
                        cur.execute(request)
            logger.info(self.user)
