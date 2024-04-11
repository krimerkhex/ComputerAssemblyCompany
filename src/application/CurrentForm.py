from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui_Current import Ui_CurrentOrders
import psycopg2
from logger import Loger, logger

DB_NAME = 'postgres'
USER_NAME = 'postgres'
PASSWORD = 'user'
HOST = '127.0.0.1'

class CurrentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CurrentOrders()
        self.ui.setupUi(self)
        self.delbut = self.ui.Delete
        self.delbut.clicked.connect(self.delete)
        self.table = self.ui.Table
        self.user = ""
        self.update()

    def update(self):
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["STATUS","PRICE","CPU","GPU","RAM","HDD","POWER","FRAME"])
        self.table.setRowCount(100)
        with psycopg2.connect(dbname=DB_NAME, user=USER_NAME, password=PASSWORD, host=HOST) as conn:
            with conn.cursor() as cur:
                cur.execute(f"Select id from Clients where login = '{self.user}';")
                id = cur.fetchone()
                if id:
                    cur.execute(f"""Select o.ready, o.price, a.cpu, a.gpu, a.ram, a.frame, a.power, a.hdd from Orders o
                    join assemblies a on o.assemblies_id = a.id
                    where o.client_id = {id[0]};""")
                    row = 0
                    data = cur.fetchall()
                    for line in data:
                        print(line[0])
                        self.table.setItem(row, 0, QTableWidgetItem("True" if line[0] else "False"))
                        self.table.setItem(row, 1, QTableWidgetItem(line[1]))
                        self.table.setItem(row, 2, QTableWidgetItem(line[2]))
                        self.table.setItem(row, 3, QTableWidgetItem(line[3]))
                        self.table.setItem(row, 4, QTableWidgetItem(line[4]))
                        self.table.setItem(row, 5, QTableWidgetItem(line[5]))
                        self.table.setItem(row, 6, QTableWidgetItem(line[6]))
                        self.table.setItem(row, 7, QTableWidgetItem(line[7]))
                        row += 1

    def delete(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)
        logger.info(self.user)
