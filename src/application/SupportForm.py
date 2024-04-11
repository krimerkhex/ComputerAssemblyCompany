from PySide6.QtWidgets import QWidget
from ui_Support import Ui_Support
import psycopg2
from logger import Loger, logger

DB_NAME = 'postgres'
USER_NAME = 'postgres'
PASSWORD = 'user'
HOST = '127.0.0.1'

class SupportForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Support()
        self.ui.setupUi(self)
        self.user = ""
        self.cause = self.ui.Cause
        self.order = self.ui.UUID
        self.update()

    def request(self):
        pass

    def update(self):
        self.cause.addItem("1. Компьютер не работает")
        self.cause.addItem("2. Комплектующие не соответсвуют заказанным")
        self.cause.addItem("3. Нужна помощь")
        self.req = self.ui.Start
        self.req.clicked.connect(self.request)
        with psycopg2.connect(dbname=DB_NAME, user=USER_NAME, password=PASSWORD, host=HOST) as conn:
            with conn.cursor() as cur:
                cur.execute(f"Select id from Clients where login = '{self.user}';")
                id = cur.fetchone()
                if id:
                    cur.execute(f"select id from History where client_id = {id[0]};")
                    for i in cur.fetchall():
                        self.order.addItem(f"{i[0]}")
