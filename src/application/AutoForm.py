from PySide6.QtWidgets import QWidget
from ui_Auto import Ui_Auto
from logger import Loger, logger
from PySide6.QtWidgets import QMessageBox
import psycopg2

DB_NAME = 'postgres'
USER_NAME = 'postgres'
PASSWORD = 'user'
HOST = '127.0.0.1'

class AutoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Auto()
        self.ui.setupUi(self)
        self.startbutt = self.ui.Start
        self.startbutt.clicked.connect(self.start)
        self.user = None
    @Loger
    def start(self):
        login = self.ui.Password.text()
        password = self.ui.Login.text()
        self.ui.Password.setText("")
        self.ui.Login.setText("")
        with psycopg2.connect(dbname=DB_NAME, user=USER_NAME, password=PASSWORD, host=HOST) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT login from Clients where password = '{password}';")
                response = cur.fetchone()
                if response is None:
                    cur.execute(f"INSERT INTO Clients (login, password) VALUES ('{login}','{password}');")
                    self.user = login
                else:
                    self.user = response[0]
                logger.info(f"Login: {self.user}")
        msg = QMessageBox(icon=QMessageBox.Information, text="Вы авторизованы")
        msg.exec()
        logger.info(self.user)


    def update(self):
        pass


