# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Support.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Support(object):
    def setupUi(self, Support):
        if not Support.objectName():
            Support.setObjectName(u"Support")
        Support.resize(1021, 800)
        self.label = QLabel(Support)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 221, 20))
        self.label_2 = QLabel(Support)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 160, 30))
        self.UUID = QComboBox(Support)
        self.UUID.setObjectName(u"UUID")
        self.UUID.setGeometry(QRect(190, 70, 351, 30))
        self.label_3 = QLabel(Support)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 130, 150, 30))
        self.Cause = QComboBox(Support)
        self.Cause.setObjectName(u"Cause")
        self.Cause.setGeometry(QRect(190, 130, 350, 30))
        self.label_4 = QLabel(Support)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 190, 150, 20))
        self.Start = QPushButton(Support)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(20, 610, 530, 29))
        self.Description = QTextEdit(Support)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(190, 190, 351, 391))

        self.retranslateUi(Support)

        QMetaObject.connectSlotsByName(Support)
    # setupUi

    def retranslateUi(self, Support):
        Support.setWindowTitle(QCoreApplication.translate("Support", u"Form", None))
        self.label.setText(QCoreApplication.translate("Support", u"\u041e\u043a\u043d\u043e \u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Support", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0430\u0448 \u0437\u0430\u043a\u0430\u0437:", None))
        self.label_3.setText(QCoreApplication.translate("Support", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u0438\u0447\u0438\u043d\u0443:", None))
        self.label_4.setText(QCoreApplication.translate("Support", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.Start.setText(QCoreApplication.translate("Support", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

