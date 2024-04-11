# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Auto.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Auto(object):
    def setupUi(self, Auto):
        if not Auto.objectName():
            Auto.setObjectName(u"Auto")
        Auto.resize(1021, 800)
        self.label = QLabel(Auto)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 20))
        self.label_2 = QLabel(Auto)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 63, 20))
        self.label_3 = QLabel(Auto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 63, 20))
        self.Login = QLineEdit(Auto)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(120, 70, 281, 28))
        self.Password = QLineEdit(Auto)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(120, 140, 281, 28))
        self.Start = QPushButton(Auto)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(190, 230, 83, 29))

        self.retranslateUi(Auto)

        QMetaObject.connectSlotsByName(Auto)
    # setupUi

    def retranslateUi(self, Auto):
        Auto.setWindowTitle(QCoreApplication.translate("Auto", u"Form", None))
        self.label.setText(QCoreApplication.translate("Auto", u"\u041e\u043a\u043d\u043e \u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Auto", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("Auto", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.Start.setText(QCoreApplication.translate("Auto", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

