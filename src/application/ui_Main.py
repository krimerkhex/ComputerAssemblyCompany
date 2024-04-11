# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1185, 820)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(160, 0, 10, 1000))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.UserLine = QLineEdit(self.centralwidget)
        self.UserLine.setObjectName(u"UserLine")
        self.UserLine.setGeometry(QRect(20, 500, 131, 28))
        self.UserLine.setReadOnly(True)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 129, 461))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.AutoBut = QPushButton(self.widget)
        self.AutoBut.setObjectName(u"AutoBut")

        self.verticalLayout.addWidget(self.AutoBut)

        self.CreaBut = QPushButton(self.widget)
        self.CreaBut.setObjectName(u"CreaBut")

        self.verticalLayout.addWidget(self.CreaBut)

        self.CurrBut = QPushButton(self.widget)
        self.CurrBut.setObjectName(u"CurrBut")

        self.verticalLayout.addWidget(self.CurrBut)

        self.HistBut = QPushButton(self.widget)
        self.HistBut.setObjectName(u"HistBut")

        self.verticalLayout.addWidget(self.HistBut)

        self.SuppBut = QPushButton(self.widget)
        self.SuppBut.setObjectName(u"SuppBut")

        self.verticalLayout.addWidget(self.SuppBut)

        self.ExitBut = QPushButton(self.widget)
        self.ExitBut.setObjectName(u"ExitBut")

        self.verticalLayout.addWidget(self.ExitBut)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1185, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.UserLine.setText(QCoreApplication.translate("MainWindow", u"No user", None))
        self.AutoBut.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.CreaBut.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0417\u0430\u043a\u0430\u0437", None))
        self.CurrBut.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.HistBut.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0417\u0430\u043a\u0430\u0437\u043e\u0432", None))
        self.SuppBut.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0445. \u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.ExitBut.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

