# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Current.ui'
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

class Ui_CurrentOrders(object):
    def setupUi(self, CurrentOrders):
        if not CurrentOrders.objectName():
            CurrentOrders.setObjectName(u"CurrentOrders")
        CurrentOrders.resize(1021, 800)
        self.label = QLabel(CurrentOrders)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 271, 20))
        self.Table = QTableWidget(CurrentOrders)
        self.Table.setObjectName(u"Table")
        self.Table.setGeometry(QRect(0, 40, 1020, 760))
        self.Delete = QPushButton(CurrentOrders)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setGeometry(QRect(280, 10, 83, 29))

        self.retranslateUi(CurrentOrders)

        QMetaObject.connectSlotsByName(CurrentOrders)
    # setupUi

    def retranslateUi(self, CurrentOrders):
        CurrentOrders.setWindowTitle(QCoreApplication.translate("CurrentOrders", u"Form", None))
        self.label.setText(QCoreApplication.translate("CurrentOrders", u"\u041e\u043a\u043d\u043e \u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0422\u0435\u043a\u0443\u0449\u0438\u0445 \u0417\u0430\u043a\u0430\u0437\u043e\u0432", None))
        self.Delete.setText(QCoreApplication.translate("CurrentOrders", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

