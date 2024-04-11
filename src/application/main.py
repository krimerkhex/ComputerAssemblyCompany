# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from ui_Main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
from HistoryForm import HistoryForm
from CreateForm import CreatingForm
from SupportForm import SupportForm
from CurrentForm import CurrentForm
from AutoForm import AutoForm

GLOB_X = 170
GLOB_Y = 10

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.createForm = CreatingForm()
        self.supportForm = SupportForm()
        self.currentForm = CurrentForm()
        self.historyForm = HistoryForm()
        self.autoForm = AutoForm()
        self.userline = self.ui.UserLine
        self.showingWindow = self.autoForm
        self.change_window(self.autoForm)
        self.autobut = self.ui.AutoBut
        self.autobut.clicked.connect(self.show_auto)
        self.creabut = self.ui.CreaBut
        self.creabut.clicked.connect(self.show_create)
        self.currbut = self.ui.CurrBut
        self.currbut.clicked.connect(self.show_current)
        self.exitbut = self.ui.ExitBut
        self.exitbut.clicked.connect(self.exit)
        self.histbut = self.ui.HistBut
        self.histbut.clicked.connect(self.show_history)
        self.suppbut = self.ui.SuppBut
        self.suppbut.clicked.connect(self.show_support)

    def show_auto(self):
        self.change_window(self.autoForm)


    def show_create(self):
        self.change_window(self.createForm)


    def show_current(self):
        self.change_window(self.currentForm)


    def show_history(self):
        self.change_window(self.historyForm)


    def show_support(self):
        self.change_window(self.supportForm)

    def exit(self):
        exit(1)

    def change_window(self, new_window):
        self.showingWindow.hide()
        self.showingWindow = new_window
        self.showingWindow.move(170, 10)
        self.showingWindow.show()
        self.userline.setText(self.autoForm.user)
        self.showingWindow.user = self.autoForm.user
        self.showingWindow.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainForm()
    main.show()
    sys.exit(app.exec())
