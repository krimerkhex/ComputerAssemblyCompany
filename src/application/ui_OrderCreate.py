# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderCreate.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_CreateOrder(object):
    def setupUi(self, CreateOrder):
        if not CreateOrder.objectName():
            CreateOrder.setObjectName(u"CreateOrder")
        CreateOrder.resize(1021, 800)
        self.label = QLabel(CreateOrder)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 171, 20))
        self.Table = QTableWidget(CreateOrder)
        self.Table.setObjectName(u"Table")
        self.Table.setGeometry(QRect(0, 40, 1020, 760))
        self.Create = QPushButton(CreateOrder)
        self.Create.setObjectName(u"Create")
        self.Create.setGeometry(QRect(200, 10, 110, 29))

        self.retranslateUi(CreateOrder)

        QMetaObject.connectSlotsByName(CreateOrder)
    # setupUi

    def retranslateUi(self, CreateOrder):
        CreateOrder.setWindowTitle(QCoreApplication.translate("CreateOrder", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreateOrder", u"\u041e\u043a\u043d\u043e \u0421\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0417\u0430\u043a\u0430\u0437\u043e\u0432", None))
        self.Create.setText(QCoreApplication.translate("CreateOrder", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0417\u0430\u043a\u0430\u0437", None))
    # retranslateUi

