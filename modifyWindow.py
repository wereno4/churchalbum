# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(346, 582)
        self.churchlabel = QLabel(Dialog)
        self.churchlabel.setObjectName(u"churchlabel")
        self.churchlabel.setGeometry(QRect(10, 260, 67, 17))
        self.calendertype = QLineEdit(Dialog)
        self.calendertype.setObjectName(u"calendertype")
        self.calendertype.setGeometry(QRect(10, 80, 321, 25))
        self.monthlabel = QLabel(Dialog)
        self.monthlabel.setObjectName(u"monthlabel")
        self.monthlabel.setGeometry(QRect(180, 160, 67, 17))
        self.serieslabel = QLabel(Dialog)
        self.serieslabel.setObjectName(u"serieslabel")
        self.serieslabel.setGeometry(QRect(10, 110, 67, 17))
        self.regionlabel = QLabel(Dialog)
        self.regionlabel.setObjectName(u"regionlabel")
        self.regionlabel.setGeometry(QRect(180, 210, 67, 17))
        self.notelabel = QLabel(Dialog)
        self.notelabel.setObjectName(u"notelabel")
        self.notelabel.setGeometry(QRect(10, 390, 67, 17))
        self.typelabel = QLabel(Dialog)
        self.typelabel.setObjectName(u"typelabel")
        self.typelabel.setGeometry(QRect(10, 60, 67, 17))
        self.file = QLineEdit(Dialog)
        self.file.setObjectName(u"file")
        self.file.setEnabled(False)
        self.file.setGeometry(QRect(10, 330, 321, 25))
        self.note = QPlainTextEdit(Dialog)
        self.note.setObjectName(u"note")
        self.note.setGeometry(QRect(10, 410, 321, 111))
        self.filelabel = QLabel(Dialog)
        self.filelabel.setObjectName(u"filelabel")
        self.filelabel.setGeometry(QRect(10, 310, 67, 17))
        self.country = QLineEdit(Dialog)
        self.country.setObjectName(u"country")
        self.country.setGeometry(QRect(10, 230, 151, 25))
        self.yearlabel = QLabel(Dialog)
        self.yearlabel.setObjectName(u"yearlabel")
        self.yearlabel.setGeometry(QRect(10, 160, 67, 17))
        self.year = QLineEdit(Dialog)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(10, 180, 151, 25))
        self.church = QLineEdit(Dialog)
        self.church.setObjectName(u"church")
        self.church.setGeometry(QRect(10, 280, 321, 25))
        self.countrylabel = QLabel(Dialog)
        self.countrylabel.setObjectName(u"countrylabel")
        self.countrylabel.setGeometry(QRect(10, 207, 111, 20))
        self.series = QLineEdit(Dialog)
        self.series.setObjectName(u"series")
        self.series.setGeometry(QRect(10, 130, 321, 25))
        self.file_load = QPushButton(Dialog)
        self.file_load.setObjectName(u"file_load")
        self.file_load.setGeometry(QRect(10, 360, 321, 25))
        self.month = QLineEdit(Dialog)
        self.month.setObjectName(u"month")
        self.month.setGeometry(QRect(180, 180, 151, 25))
        self.region = QLineEdit(Dialog)
        self.region.setObjectName(u"region")
        self.region.setGeometry(QRect(180, 230, 151, 25))
        self.IDlabel = QLabel(Dialog)
        self.IDlabel.setObjectName(u"IDlabel")
        self.IDlabel.setGeometry(QRect(10, 10, 67, 17))
        self.ID = QLineEdit(Dialog)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(10, 30, 151, 25))
        self.checkID = QPushButton(Dialog)
        self.checkID.setObjectName(u"checkID")
        self.checkID.setGeometry(QRect(180, 30, 151, 25))
        self.deleteButton = QPushButton(Dialog)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(20, 530, 89, 25))
        self.modifyButton = QPushButton(Dialog)
        self.modifyButton.setObjectName(u"modifyButton")
        self.modifyButton.setGeometry(QRect(130, 530, 89, 25))
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(240, 530, 89, 25))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\uc218\uc815/\uc0ad\uc81c", None))
        self.churchlabel.setText(QCoreApplication.translate("Dialog", u"\uc7a5\uc18c", None))
        self.monthlabel.setText(QCoreApplication.translate("Dialog", u"\uc6d4", None))
        self.serieslabel.setText(QCoreApplication.translate("Dialog", u"\uc2dc\ub9ac\uc988", None))
        self.regionlabel.setText(QCoreApplication.translate("Dialog", u"\uc9c0\uc5ed", None))
        self.notelabel.setText(QCoreApplication.translate("Dialog", u"\ube44\uace0", None))
        self.typelabel.setText(QCoreApplication.translate("Dialog", u"\ub2ec\ub825 \uc885\ub958", None))
        self.filelabel.setText(QCoreApplication.translate("Dialog", u"\ud30c\uc77c", None))
        self.yearlabel.setText(QCoreApplication.translate("Dialog", u"\uc5f0\ub3c4", None))
        self.countrylabel.setText(QCoreApplication.translate("Dialog", u"\uad6d\uac00", None))
        self.file_load.setText(QCoreApplication.translate("Dialog", u"\ubd88\ub7ec\uc624\uae30", None))
        self.IDlabel.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.checkID.setText(QCoreApplication.translate("Dialog", u"\uc815\ubcf4 \ud655\uc778", None))
        self.deleteButton.setText(QCoreApplication.translate("Dialog", u"\uc0ad\uc81c", None))
        self.modifyButton.setText(QCoreApplication.translate("Dialog", u"\uc218\uc815", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\ucde8\uc18c", None))
    # retranslateUi

