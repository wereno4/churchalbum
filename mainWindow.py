# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1301, 902)
        self.add = QAction(MainWindow)
        self.add.setObjectName(u"add")
        self.addmenu = QAction(MainWindow)
        self.addmenu.setObjectName(u"addmenu")
        self.modify = QAction(MainWindow)
        self.modify.setObjectName(u"modify")
        self.strip = QAction(MainWindow)
        self.strip.setObjectName(u"strip")
        self.fileDelete = QAction(MainWindow)
        self.fileDelete.setObjectName(u"fileDelete")
        self.updateAction = QAction(MainWindow)
        self.updateAction.setObjectName(u"updateAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendertype = QComboBox(self.centralwidget)
        self.calendertype.setObjectName(u"calendertype")
        self.calendertype.setGeometry(QRect(10, 30, 321, 25))
        self.image = QLabel(self.centralwidget)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(350, 20, 941, 681))
        self.typelabel = QLabel(self.centralwidget)
        self.typelabel.setObjectName(u"typelabel")
        self.typelabel.setGeometry(QRect(10, 10, 67, 17))
        self.theme = QComboBox(self.centralwidget)
        self.theme.setObjectName(u"theme")
        self.theme.setGeometry(QRect(10, 80, 151, 25))
        self.themelabel = QLabel(self.centralwidget)
        self.themelabel.setObjectName(u"themelabel")
        self.themelabel.setGeometry(QRect(10, 60, 67, 17))
        self.yearlabel = QLabel(self.centralwidget)
        self.yearlabel.setObjectName(u"yearlabel")
        self.yearlabel.setGeometry(QRect(10, 110, 67, 17))
        self.monthlabel = QLabel(self.centralwidget)
        self.monthlabel.setObjectName(u"monthlabel")
        self.monthlabel.setGeometry(QRect(180, 110, 67, 17))
        self.year = QComboBox(self.centralwidget)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(10, 130, 151, 25))
        self.month = QComboBox(self.centralwidget)
        self.month.setObjectName(u"month")
        self.month.setGeometry(QRect(180, 130, 151, 25))
        self.church = QComboBox(self.centralwidget)
        self.church.setObjectName(u"church")
        self.church.setGeometry(QRect(10, 230, 321, 25))
        self.churchlabel = QLabel(self.centralwidget)
        self.churchlabel.setObjectName(u"churchlabel")
        self.churchlabel.setGeometry(QRect(10, 210, 67, 17))
        self.regionlabel = QLabel(self.centralwidget)
        self.regionlabel.setObjectName(u"regionlabel")
        self.regionlabel.setGeometry(QRect(180, 160, 67, 17))
        self.region = QComboBox(self.centralwidget)
        self.region.setObjectName(u"region")
        self.region.setGeometry(QRect(180, 180, 151, 25))
        self.countrylabel = QLabel(self.centralwidget)
        self.countrylabel.setObjectName(u"countrylabel")
        self.countrylabel.setGeometry(QRect(10, 157, 111, 20))
        self.country = QComboBox(self.centralwidget)
        self.country.setObjectName(u"country")
        self.country.setGeometry(QRect(10, 180, 151, 25))
        self.note = QTextBrowser(self.centralwidget)
        self.note.setObjectName(u"note")
        self.note.setGeometry(QRect(350, 710, 941, 131))
        self.imageList = QTableWidget(self.centralwidget)
        if (self.imageList.columnCount() < 3):
            self.imageList.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.imageList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.imageList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.imageList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.imageList.setObjectName(u"imageList")
        self.imageList.setGeometry(QRect(10, 270, 321, 531))
        self.imageList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.series = QComboBox(self.centralwidget)
        self.series.setObjectName(u"series")
        self.series.setGeometry(QRect(180, 80, 151, 25))
        self.serieslabel_2 = QLabel(self.centralwidget)
        self.serieslabel_2.setObjectName(u"serieslabel_2")
        self.serieslabel_2.setGeometry(QRect(180, 60, 67, 17))
        self.searchCombo = QComboBox(self.centralwidget)
        self.searchCombo.addItem("")
        self.searchCombo.addItem("")
        self.searchCombo.setObjectName(u"searchCombo")
        self.searchCombo.setGeometry(QRect(10, 820, 91, 25))
        self.search = QLineEdit(self.centralwidget)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(110, 820, 221, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1301, 27))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu2 = QMenu(self.menubar)
        self.menu2.setObjectName(u"menu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu2.menuAction())
        self.menu.addAction(self.addmenu)
        self.menu.addAction(self.modify)
        self.menu2.addAction(self.strip)
        self.menu2.addAction(self.fileDelete)
        self.menu2.addAction(self.updateAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc131\ub2f9 \uc0ac\uc9c4 \ubcf4\ub294 \ud504\ub85c\uadf8\ub7a8", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
#if QT_CONFIG(tooltip)
        self.add.setToolTip(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130\ub97c \ucd94\uac00\ud568", None))
#endif // QT_CONFIG(tooltip)
        self.addmenu.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
        self.modify.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815/\uc0ad\uc81c", None))
        self.strip.setText(QCoreApplication.translate("MainWindow", u"\uacf5\ubc31 \uc9c0\uc6b0\uae30", None))
        self.fileDelete.setText(QCoreApplication.translate("MainWindow", u"\uc789\uc5ec \ud30c\uc77c \uc9c0\uc6b0\uae30", None))
        self.updateAction.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uc5c5\ub370\uc774\ud2b8", None))
        self.image.setText("")
        self.typelabel.setText(QCoreApplication.translate("MainWindow", u"\ub2ec\ub825 \uc885\ub958", None))
        self.themelabel.setText(QCoreApplication.translate("MainWindow", u"\ud14c\ub9c8", None))
        self.yearlabel.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\ub3c4", None))
        self.monthlabel.setText(QCoreApplication.translate("MainWindow", u"\uc6d4", None))
        self.churchlabel.setText(QCoreApplication.translate("MainWindow", u"\uc7a5\uc18c", None))
        self.regionlabel.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc5ed", None))
        self.countrylabel.setText(QCoreApplication.translate("MainWindow", u"\uad6d\uac00", None))
        ___qtablewidgetitem = self.imageList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.imageList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc7a5\uc18c", None));
        ___qtablewidgetitem2 = self.imageList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uba85", None));
        self.serieslabel_2.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\ub9ac\uc988", None))
        self.searchCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc7a5\uc18c", None))
        self.searchCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uba85", None))

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130\ubca0\uc774\uc2a4", None))
        self.menu2.setTitle(QCoreApplication.translate("MainWindow", u"\ud3b8\uc758 \uae30\ub2a5", None))
    # retranslateUi

