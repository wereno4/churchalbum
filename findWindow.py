# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QHeaderView, QLabel,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1143, 801)
        self.monthlabel = QLabel(Dialog)
        self.monthlabel.setObjectName(u"monthlabel")
        self.monthlabel.setGeometry(QRect(10, 750, 67, 17))
        self.region = QComboBox(Dialog)
        self.region.setObjectName(u"region")
        self.region.setGeometry(QRect(670, 720, 151, 25))
        self.church = QComboBox(Dialog)
        self.church.setObjectName(u"church")
        self.church.setGeometry(QRect(500, 770, 321, 25))
        self.typelabel = QLabel(Dialog)
        self.typelabel.setObjectName(u"typelabel")
        self.typelabel.setGeometry(QRect(170, 700, 67, 17))
        self.serieslabel = QLabel(Dialog)
        self.serieslabel.setObjectName(u"serieslabel")
        self.serieslabel.setGeometry(QRect(170, 750, 67, 17))
        self.yearlabel = QLabel(Dialog)
        self.yearlabel.setObjectName(u"yearlabel")
        self.yearlabel.setGeometry(QRect(10, 700, 67, 17))
        self.year = QComboBox(Dialog)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(10, 720, 151, 25))
        self.month = QComboBox(Dialog)
        self.month.setObjectName(u"month")
        self.month.setGeometry(QRect(10, 770, 151, 25))
        self.country = QComboBox(Dialog)
        self.country.setObjectName(u"country")
        self.country.setGeometry(QRect(500, 720, 151, 25))
        self.countrylabel = QLabel(Dialog)
        self.countrylabel.setObjectName(u"countrylabel")
        self.countrylabel.setGeometry(QRect(500, 697, 111, 20))
        self.regionlabel = QLabel(Dialog)
        self.regionlabel.setObjectName(u"regionlabel")
        self.regionlabel.setGeometry(QRect(670, 700, 67, 17))
        self.series = QComboBox(Dialog)
        self.series.setObjectName(u"series")
        self.series.setGeometry(QRect(170, 770, 321, 25))
        self.churchlabel = QLabel(Dialog)
        self.churchlabel.setObjectName(u"churchlabel")
        self.churchlabel.setGeometry(QRect(500, 750, 67, 17))
        self.calendertype = QComboBox(Dialog)
        self.calendertype.setObjectName(u"calendertype")
        self.calendertype.setGeometry(QRect(170, 720, 321, 25))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(830, 760, 311, 31))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 10, 1141, 681))
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\uc218\uc815\ud560 \ubaa9\ub85d \ucc3e\uae30", None))
        self.monthlabel.setText(QCoreApplication.translate("Dialog", u"\uc6d4", None))
        self.typelabel.setText(QCoreApplication.translate("Dialog", u"\ub2ec\ub825 \uc885\ub958", None))
        self.serieslabel.setText(QCoreApplication.translate("Dialog", u"\uc2dc\ub9ac\uc988", None))
        self.yearlabel.setText(QCoreApplication.translate("Dialog", u"\uc5f0\ub3c4", None))
        self.countrylabel.setText(QCoreApplication.translate("Dialog", u"\uad6d\uac00", None))
        self.regionlabel.setText(QCoreApplication.translate("Dialog", u"\uc9c0\uc5ed", None))
        self.churchlabel.setText(QCoreApplication.translate("Dialog", u"\uc7a5\uc18c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\ub2ec\ub825 \uc885\ub958", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\uc2dc\ub9ac\uc988", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\uc5f0\ub3c4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\uc6d4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\uad6d\uac00", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"\uc9c0\uc5ed", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"\uc7a5\uc18c", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"\ud30c\uc77c\uba85", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"\ube44\uace0", None));
    # retranslateUi

