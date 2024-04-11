# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'History.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_OrdersHistory(object):
    def setupUi(self, OrdersHistory):
        if not OrdersHistory.objectName():
            OrdersHistory.setObjectName(u"OrdersHistory")
        OrdersHistory.resize(1021, 800)
        self.label = QLabel(OrdersHistory)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 271, 20))
        self.Table = QTableWidget(OrdersHistory)
        self.Table.setObjectName(u"Table")
        self.Table.setGeometry(QRect(0, 30, 1020, 760))

        self.retranslateUi(OrdersHistory)

        QMetaObject.connectSlotsByName(OrdersHistory)
    # setupUi

    def retranslateUi(self, OrdersHistory):
        OrdersHistory.setWindowTitle(QCoreApplication.translate("OrdersHistory", u"Form", None))
        self.label.setText(QCoreApplication.translate("OrdersHistory", u"\u041e\u043a\u043d\u043e \u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0418\u0441\u0442\u043e\u0440\u0438\u0438 \u0417\u0430\u043a\u0430\u0437\u043e\u0432", None))
    # retranslateUi

