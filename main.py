import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from mainWindow import Ui_MainWindow
import addWindow, modifyWindow, findWindow, stripWindow
import os, shutil


conn = sqlite3.connect("./church.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS church([image_id] INTEGER PRIMARY KEY, [type] TEXT, [theme] TEXT, [series] TEXT, [year] INTEGER, [month] INTEGER, [country] TEXT, [region] TEXT, [church] TEXT, [file_name] TEXT, [note] TEXT)")
conn.commit()

if not os.path.exists("./img"):
    os.makedirs("./img")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.combobox_generate()
        self.find_image()

        self.imageList.verticalHeader().hide()
        self.imageList.setColumnWidth(0, self.imageList.width()*1/10)
        self.imageList.setColumnWidth(1, self.imageList.width()*4/10)
        self.imageList.setColumnWidth(2, self.imageList.width()*3/10)
        

        self.calendertype.currentIndexChanged.connect(self.find_image)
        self.series.currentIndexChanged.connect(self.find_image)
        self.theme.currentIndexChanged.connect(self.series_listing)
        self.year.currentIndexChanged.connect(self.month_listing)
        self.month.currentIndexChanged.connect(self.find_image)
        self.country.currentIndexChanged.connect(self.for_country)
        self.region.currentIndexChanged.connect(self.church_listing)
        self.church.currentIndexChanged.connect(self.find_image)
        self.imageList.cellClicked.connect(self.show_image)
        self.addmenu.triggered.connect(self.addWindow)
        self.modify.triggered.connect(self.modifyWindow)
        self.search.textChanged.connect(self.search_list)
        self.strip.triggered.connect(self.strip_data)
        self.fileDelete.triggered.connect(self.file_delete)


        print(self.region.count())



    def combobox_generate(self):
        self.calendertype.clear()
        self.theme.clear()
        self.series.clear()
        self.year.clear()
        self.month.clear()
        self.country.clear()
        self.region.clear()
        self.church.clear()

        self.calendertype.addItem("-")
        cur.execute("SELECT type FROM church")
        types_list = cur.fetchall()
        types_list = [x[0] for x in types_list]
        types_list = list(set(types_list))
        for item in types_list:
            self.calendertype.addItem(item)
    
        self.theme.addItem("-")
        cur.execute("SELECT theme FROM church")
        theme_list = cur.fetchall()
        theme_list = [x[0] for x in theme_list]
        theme_list = list(set(theme_list))
        for item in theme_list:
            self.theme.addItem(item)

        self.year.addItem("-")
        cur.execute("SELECT year FROM church")
        year_list = cur.fetchall()
        year_list = [x[0] for x in year_list]
        year_list = list(set(year_list))
        for item in year_list:
            self.year.addItem(str(item))

        self.country.addItem("-")
        cur.execute("SELECT country FROM church")
        country_list = cur.fetchall()
        country_list = [x[0] for x in country_list]
        country_list = list(set(country_list))
        for item in country_list:
            self.country.addItem(item)

        self.calendertype.setItemText(0, "-")
        self.series.setItemText(0, "-")
        self.year.setItemText(0, "-")
        self.country.setItemText(0, "-")

        self.find_image()

    def find_image(self):
        self.imageList.clearContents()
        condition = "SELECT image_id, church, file_name FROM church"
        whereand = True
        if not (self.calendertype.currentText() == "-" or (self.calendertype.count() == 0 and self.calendertype.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE type = '{self.calendertype.currentText()}'"
            else:
                condition = condition + f" AND type = '{self.calendertype.currentText()}'"
            whereand = False
        if not (self.theme.currentText() == "-" or (self.theme.count() == 0 and self.theme.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE theme = '{self.theme.currentText()}'"
            else:
                condition = condition + f" AND theme = '{self.theme.currentText()}'"
            whereand = False
        if not (self.series.currentText() == "-" or (self.series.count() == 0 and self.series.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE series = '{self.series.currentText()}'"
            else:
                condition = condition + f" AND series = '{self.series.currentText()}'"
            whereand = False
        if not (self.year.currentText() == "-" or (self.series.count() == 0 and self.year.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE year = {self.year.currentText()}"
            else:
                condition = condition + f" AND year = {self.year.currentText()}"
            whereand = False
        if not (self.month.currentText() == "-" or (self.month.count() == 0 and self.month.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE month = {self.month.currentText()}"
            else:
                condition = condition + f" AND month = {self.month.currentText()}"
            whereand = False
        if not (self.country.currentText() == "-"  or (self.country.count() == 0 and self.country.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE country = '{self.country.currentText()}'"
            else:
                condition = condition + f" AND country = '{self.country.currentText()}'"
            whereand = False
        if not (self.region.currentText() == "-" or (self.region.count() == 0 and self.region.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE region = '{self.region.currentText()}'"
            else:
                condition = condition + f" AND region = '{self.region.currentText()}'"
            whereand = False
        if not (self.church.currentText() == "-" or (self.church.count() == 0 and self.church.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE church = '{self.church.currentText()}'"
            else:
                condition = condition + f" AND church = '{self.church.currentText()}'"
            whereand = False
        cur.execute(condition)
        image_list = cur.fetchall()
        self.imageList.setRowCount(len(image_list))
        
        y = 0
        for row in image_list:
            x = 0
            for item in row:
                tableItem = QTableWidgetItem(str(item))
                self.imageList.setItem(y, x, tableItem)
                x += 1
            y += 1


    def search_list(self):
        self.imageList.clearContents()
        condition = "SELECT image_id, church, file_name FROM church"
        whereand = True
        if not (self.calendertype.currentText() == "-" or (self.calendertype.count() == 0 and self.calendertype.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE type = '{self.calendertype.currentText()}'"
            else:
                condition = condition + f" AND type = '{self.calendertype.currentText()}'"
            whereand = False
        if not (self.theme.currentText() == "-" or (self.theme.count() == 0 and self.theme.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE theme = '{self.theme.currentText()}'"
            else:
                condition = condition + f" AND theme = '{self.theme.currentText()}'"
            whereand = False
        if not (self.series.currentText() == "-" or (self.series.count() == 0 and self.series.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE series = '{self.series.currentText()}'"
            else:
                condition = condition + f" AND series = '{self.series.currentText()}'"
            whereand = False
        if not (self.year.currentText() == "-" or (self.series.count() == 0 and self.year.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE year = {self.year.currentText()}"
            else:
                condition = condition + f" AND year = {self.year.currentText()}"
            whereand = False
        if not (self.month.currentText() == "-" or (self.month.count() == 0 and self.month.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE month = {self.month.currentText()}"
            else:
                condition = condition + f" AND month = {self.month.currentText()}"
            whereand = False
        if not (self.country.currentText() == "-"  or (self.country.count() == 0 and self.country.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE country = '{self.country.currentText()}'"
            else:
                condition = condition + f" AND country = '{self.country.currentText()}'"
            whereand = False
        if not (self.region.currentText() == "-" or (self.region.count() == 0 and self.region.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE region = '{self.region.currentText()}'"
            else:
                condition = condition + f" AND region = '{self.region.currentText()}'"
            whereand = False
        if not (self.church.currentText() == "-" or (self.church.count() == 0 and self.church.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE church = '{self.church.currentText()}'"
            else:
                condition = condition + f" AND church = '{self.church.currentText()}'"
            whereand = False
        if self.searchCombo.currentText() == "장소":
            if whereand:
                condition = condition + f" WHERE church LIKE '%{self.search.text()}%'"
            else:
                condition = condition + f" AND church LIKE '%{self.search.text()}%'"
            whereand = False
        elif self.searchCombo.currentText() == "파일명":
            if whereand:
                condition = condition + f" WHERE file_name LIKE '%{self.search.text()}%'"
            else:
                condition = condition + f" AND file_name LIKE '%{self.search.text()}%'"
            whereand = False

        cur.execute(condition)
        image_list = cur.fetchall()
        self.imageList.setRowCount(len(image_list))
        
        y = 0
        for row in image_list:
            x = 0
            for item in row:
                tableItem = QTableWidgetItem(str(item))
                self.imageList.setItem(y, x, tableItem)
                x += 1
            y += 1

        
    def month_listing(self):
        year = self.year.currentText()
        if year == "-" or (self.year.count() == 0 and year == ""):
            self.month.clear()
        else:
            self.month.clear()
            self.month.addItem("-")
            cur.execute(f"SELECT month FROM church WHERE year = {year}")
            month_list = cur.fetchall()
            month_list = [x[0] for x in month_list]
            month_list = list(set(month_list))
            for item in month_list:
                self.month.addItem(str(item))
            self.month.setItemText(0, "-")
        self.find_image()

    def series_listing(self):
        theme = self.theme.currentText()
        if theme == "-" or (self.theme.count() == 0 and theme == ""):
            self.series.clear()
        else:
            self.series.clear()
            self.series.addItem("-")
            cur.execute(f"SELECT series FROM church WHERE theme = '{theme}'")
            series_list = cur.fetchall()
            series_list = [x[0] for x in series_list]
            series_list = list(set(series_list))
            for item in series_list:
                self.series.addItem(str(item))
            self.series.setItemText(0, "-")
        self.find_image()


    def region_listing(self):
        country = self.country.currentText()
        if country == "-" or (self.country.count() == 0 and country == ""):
            self.region.clear()
        else:
            self.region.clear()
            self.region.addItem("-")
            cur.execute(f"SELECT region FROM church WHERE country = '{country}'")
            region_list = cur.fetchall()
            region_list = [x[0] for x in region_list]
            region_list = list(set(region_list))
            for item in region_list:
                self.region.addItem(str(item))
            self.region.setItemText(0, "-")
        self.find_image()

    def church_listing(self):
        country = self.country.currentText()
        region = self.region.currentText()
        if region == "-" or (self.country.count() == 0 and country == "") or (self.region.count() == 0 and region == "") or country == "-":
            self.church.clear()
        else:
            self.church.clear()
            self.church.addItem("-")
            cur.execute(f"SELECT church FROM church WHERE country = '{country}' and region = '{region}'")
            church_list = cur.fetchall()
            church_list = [x[0] for x in church_list]
            church_list = list(set(church_list))
            for item in church_list:
                self.church.addItem(str(item))
            self.church.setItemText(0, "-")
        self.find_image()

    def for_country(self):
        self.region_listing()
        self.church_listing()

    def show_image(self):
        pixmap = QPixmap(f"./img/{self.imageList.item(self.imageList.currentRow(), 2).text()}")
        if pixmap.size().width() >= pixmap.size().height():
            pixmap = pixmap.scaledToWidth(self.image.width())
        elif pixmap.size().width() <= pixmap.size().height():
            pixmap = pixmap.scaledToHeight(self.image.height())
        self.image.setPixmap(pixmap)
        cur.execute(f"SELECT note, image_id, type, theme, series, year, month, country, region, church FROM church WHERE image_id = '{self.imageList.item(self.imageList.currentRow(), 0).text()}'")
        note, id, *information = cur.fetchall()[0]
        information = [str(x) for x in information]
        note = note + "\n" if note != "" else note
        self.note.setPlainText(note+f"ID: {id}\n{'/'.join(information)}")

    def addWindow(self):
        dialog = addDialog()
        dialog.exec()
        self.combobox_generate()

    def modifyWindow(self):
        dialog = findDialog()
        dialog.exec()
        self.combobox_generate()
        self.image.clear()
        self.note.clear()

    def strip_data(self):
        dialog = stripDialog()
        dialog.exec()
        self.combobox_generate()
        self.image.clear()
        self.note.clear()
    
    def file_delete(self):
        dialog = fileDeleteDialog()
        dialog.exec()

class addDialog(QDialog, addWindow.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.acceptedButton)
        self.file_load.clicked.connect(self.file_browse)

    def file_browse(self):
        fname = QFileDialog.getOpenFileName(self, "", "", "Image File(*.jpg *.jpeg *.gif *.png *.webp *.tif *.tiff)")
        if fname[0]:
            self.file.setText(fname[0])

    def acceptedButton(self):
        if self.calendertype.text() == "" or self.series.text() == "" or self.month.text() == "" or self.year.text() == "" or self.country.text() == "" or self.region.text() == "" or self.church.text() == "" or self.file.text() == "" :
            QMessageBox.warning(self, '칸이 비어있음', '채워지지 않은 칸이 있습니다.')
            return
        if not self.year.text().isdigit():
            QMessageBox.warning(self, '연도가 유효하지 않음', '연도는 숫자여야 합니다.')
            return
        if not self.month.text().isdigit() or (self.month.text().isdigit() and (int(self.month.text()) < 1 or int(self.month.text()) > 12)):
            QMessageBox.warning(self, '월이 유효하지 않음', '월은 1~12 사이의 숫자여야 합니다.')
            return

        file_name = os.path.basename(self.file.text())
        cur.execute(f"SELECT EXISTS(SELECT file_name FROM church WHERE file_name = '{file_name}')")
        fileexists = cur.fetchall()
        fileexists = fileexists[0][0]
        if fileexists == 1:
            QMessageBox.warning(self, "중복되는 파일", "파일명이 같은 파일이 이미 있습니다.")
            return
        
        cur.execute("SELECT MAX(image_id) FROM church")
        max = cur.fetchall()
        max = max[0][0]
        key_to_add = 0 if max is None else max + 1

        shutil.copy(self.file.text(), './img/'+file_name)

        cur.execute(f"INSERT INTO church VALUES ({key_to_add}, '{self.calendertype.text()}', '{self.theme.text()}', '{self.series.text()}', {self.year.text()}, {self.month.text()}, '{self.country.text()}', '{self.region.text()}', '{self.church.text()}', '{file_name}', '{self.note.toPlainText()}')")
        conn.commit()
        self.accept()

class modifyDialog(QDialog, modifyWindow.Ui_Dialog):
    def __init__(self, ID, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.currentID = ID
        cur.execute(f"SELECT type, theme, series, year, month, country, region, church, file_name, note FROM church WHERE image_id = {self.currentID}")
        result = cur.fetchall()[0]
        self.calendertype.setText(result[0])
        self.theme.setText(result[1])
        self.series.setText(result[2])
        self.year.setText(str(result[3]))
        self.month.setText(str(result[4]))
        self.country.setText(result[5])
        self.region.setText(result[6])
        self.church.setText(result[7])
        self.file.setText(result[8])
        self.note.setPlainText(result[9])
        self.oldfilename = result[8]

        self.cancelButton.clicked.connect(self.reject)
        self.deleteButton.clicked.connect(self.delete_data)
        self.modifyButton.clicked.connect(self.modify_data)
        self.file_load.clicked.connect(self.file_browse)


    def file_browse(self):
        fname = QFileDialog.getOpenFileName(self, "", "", "Image File(*.jpg *.jpeg *.gif *.png *.webp *.tif *.tiff)")
        if fname[0]:
            self.file.setText(fname[0])

    def delete_data(self):
        buttonReply = QMessageBox.warning(self, "데이터가 지워집니다.",
                                          "해당 데이터를 지우겠습니까?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.No:
            return
        elif buttonReply == QMessageBox.Yes:
            cur.execute(f"DELETE FROM church WHERE image_id = {self.currentID}")
            conn.commit()
            self.accept()

    def modify_data(self):
        if self.calendertype.text() == "" or self.series.text() == "" or self.month.text() == "" or self.year.text() == "" or self.country.text() == "" or self.region.text() == "" or self.church.text() == "" or self.file.text() == "" :
            QMessageBox.warning(self, '칸이 비어있음', '채워지지 않은 칸이 있습니다.')
            return
        if not self.year.text().isdigit():
            QMessageBox.warning(self, '연도가 유효하지 않음', '연도는 숫자여야 합니다.')
            return
        if not self.month.text().isdigit() or (self.month.text().isdigit() and (int(self.month.text()) < 1 or int(self.month.text()) > 12)):
            QMessageBox.warning(self, '월이 유효하지 않음', '월은 1~12 사이의 숫자여야 합니다.')
            return
        buttonReply = QMessageBox.warning(self, "데이터가 수정됩니다.",
                                              "해당 데이터를 수정하시겠습니까?",
                                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.No:
            return
        elif buttonReply == QMessageBox.Yes:
            file_name = os.path.basename(self.file.text())
            file_changed = False
            if file_name != self.file.text():
                file_changed = True
            elif file_name == self.file.text():
                file_changed = False
            cur.execute(f"UPDATE church SET type='{self.calendertype.text()}', theme='{self.theme.text()}', series='{self.series.text()}', year={self.year.text()}, month={self.month.text()}, country='{self.country.text()}', region='{self.region.text()}', church='{self.church.text()}', file_name='{file_name}', note='{self.note.toPlainText()}' WHERE image_id = {self.currentID}")
            conn.commit()
            if file_changed:
                shutil.copy(self.file.text(), './img/'+file_name)
                
            self.accept()

class findDialog(QDialog, findWindow.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.combobox_generate()


        self.calendertype.currentIndexChanged.connect(self.find_image)
        self.series.currentIndexChanged.connect(self.find_image)
        self.theme.currentIndexChanged.connect(self.series_listing)
        self.year.currentIndexChanged.connect(self.month_listing)
        self.month.currentIndexChanged.connect(self.find_image)
        self.country.currentIndexChanged.connect(self.for_country)
        self.region.currentIndexChanged.connect(self.church_listing)
        self.church.currentIndexChanged.connect(self.find_image)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.tableWidget.cellDoubleClicked.connect(self.modify_window)



    def combobox_generate(self):
        self.calendertype.clear()
        self.theme.clear()
        self.series.clear()
        self.year.clear()
        self.month.clear()
        self.country.clear()
        self.region.clear()
        self.church.clear()

        self.calendertype.addItem("-")
        cur.execute("SELECT type FROM church")
        types_list = cur.fetchall()
        types_list = [x[0] for x in types_list]
        types_list = list(set(types_list))
        for item in types_list:
            self.calendertype.addItem(item)
    
        self.theme.addItem("-")
        cur.execute("SELECT theme FROM church")
        theme_list = cur.fetchall()
        theme_list = [x[0] for x in theme_list]
        theme_list = list(set(theme_list))
        for item in theme_list:
            self.theme.addItem(item)

        self.year.addItem("-")
        cur.execute("SELECT year FROM church")
        year_list = cur.fetchall()
        year_list = [x[0] for x in year_list]
        year_list = list(set(year_list))
        for item in year_list:
            self.year.addItem(str(item))

        self.country.addItem("-")
        cur.execute("SELECT country FROM church")
        country_list = cur.fetchall()
        country_list = [x[0] for x in country_list]
        country_list = list(set(country_list))
        for item in country_list:
            self.country.addItem(item)

        self.calendertype.setItemText(0, "-")
        self.series.setItemText(0, "-")
        self.year.setItemText(0, "-")
        self.country.setItemText(0, "-")

        self.find_image()

    def find_image(self):
        self.tableWidget.clearContents()
        condition = "SELECT image_id, type, theme, series, year, month, country, region, church, file_name, note FROM church"
        whereand = True
        if not (self.calendertype.currentText() == "-" or (self.calendertype.count() == 0 and self.calendertype.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE type = '{self.calendertype.currentText()}'"
            else:
                condition = condition + f" AND type = '{self.calendertype.currentText()}'"
            whereand = False
        if not (self.theme.currentText() == "-" or (self.theme.count() == 0 and self.theme.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE theme = '{self.theme.currentText()}'"
            else:
                condition = condition + f" AND theme = '{self.theme.currentText()}'"
            whereand = False
        if not (self.series.currentText() == "-" or (self.series.count() == 0 and self.series.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE series = '{self.series.currentText()}'"
            else:
                condition = condition + f" AND series = '{self.series.currentText()}'"
            whereand = False
        if not (self.year.currentText() == "-" or (self.series.count() == 0 and self.year.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE year = {self.year.currentText()}"
            else:
                condition = condition + f" AND year = {self.year.currentText()}"
            whereand = False
        if not (self.month.currentText() == "-" or (self.month.count() == 0 and self.month.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE month = {self.month.currentText()}"
            else:
                condition = condition + f" AND month = {self.month.currentText()}"
            whereand = False
        if not (self.country.currentText() == "-"  or (self.country.count() == 0 and self.country.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE country = '{self.country.currentText()}'"
            else:
                condition = condition + f" AND country = '{self.country.currentText()}'"
            whereand = False
        if not (self.region.currentText() == "-" or (self.region.count() == 0 and self.region.currentText()  == "")):
            if whereand:
                condition = condition + f" WHERE region = '{self.region.currentText()}'"
            else:
                condition = condition + f" AND region = '{self.region.currentText()}'"
            whereand = False
        if not (self.church.currentText() == "-" or (self.church.count() == 0 and self.church.currentText() == "")):
            if whereand:
                condition = condition + f" WHERE church = '{self.church.currentText()}'"
            else:
                condition = condition + f" AND church = '{self.church.currentText()}'"
            whereand = False
        cur.execute(condition)
        image_list = cur.fetchall()
        self.tableWidget.setRowCount(len(image_list))
        y = 0
        for row in image_list:
            x = 0
            for item in row:
                tableItem = QTableWidgetItem(str(item))
                self.tableWidget.setItem(y,x,tableItem)
                x += 1
            y += 1
            
    def month_listing(self):
        year = self.year.currentText()
        if year == "-" or (self.year.count() == 0 and year == ""):
            self.month.clear()
        else:
            self.month.clear()
            self.month.addItem("-")
            cur.execute(f"SELECT month FROM church WHERE year = {year}")
            month_list = cur.fetchall()
            month_list = [x[0] for x in month_list]
            month_list = list(set(month_list))
            for item in month_list:
                self.month.addItem(str(item))
            self.month.setItemText(0, "-")
        self.find_image()

    def series_listing(self):
        theme = self.theme.currentText()
        if theme == "-" or (self.theme.count() == 0 and theme == ""):
            self.series.clear()
        else:
            self.series.clear()
            self.series.addItem("-")
            cur.execute(f"SELECT series FROM church WHERE theme = '{theme}'")
            series_list = cur.fetchall()
            series_list = [x[0] for x in series_list]
            series_list = list(set(series_list))
            for item in series_list:
                self.series.addItem(str(item))
            self.series.setItemText(0, "-")
        self.find_image()


    def region_listing(self):
        country = self.country.currentText()
        if country == "-" or (self.country.count() == 0 and country == ""):
            self.region.clear()
        else:
            self.region.clear()
            self.region.addItem("-")
            cur.execute(f"SELECT region FROM church WHERE country = '{country}'")
            region_list = cur.fetchall()
            region_list = [x[0] for x in region_list]
            region_list = list(set(region_list))
            for item in region_list:
                self.region.addItem(str(item))
            self.region.setItemText(0, "-")
        self.find_image()

    def church_listing(self):
        country = self.country.currentText()
        region = self.region.currentText()
        if region == "-" or (self.country.count() == 0 and country == "") or (self.region.count() == 0 and region == "") or country == "-":
            self.church.clear()
        else:
            self.church.clear()
            self.church.addItem("-")
            cur.execute(f"SELECT church FROM church WHERE country = '{country}' and region = '{region}'")
            church_list = cur.fetchall()
            church_list = [x[0] for x in church_list]
            church_list = list(set(church_list))
            for item in church_list:
                self.church.addItem(str(item))
            self.church.setItemText(0, "-")
        self.find_image()

    def for_country(self):
        self.region_listing()
        self.church_listing()

    def for_country(self):
        self.region_listing()
        self.church_listing()

    def modify_window(self):
        dialog = modifyDialog(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        dialog.exec()
        self.combobox_generate()

class stripDialog(QDialog, stripWindow.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        cur.execute("SELECT image_id, type, theme, series, country, region, church FROM church")
        list = cur.fetchall()
        amount = len(list)
        self.progressBar.setMaximum(amount)
        progress = 0
        for item in list:
            cur.execute(f"UPDATE church SET type = '{item[1].strip()}' WHERE image_id={item[0]}")
            cur.execute(f"UPDATE church SET theme = '{item[2].strip()}' WHERE image_id={item[0]}")
            cur.execute(f"UPDATE church SET series = '{item[3].strip()}' WHERE image_id={item[0]}")
            cur.execute(f"UPDATE church SET country = '{item[4].strip()}' WHERE image_id={item[0]}")
            cur.execute(f"UPDATE church SET region = '{item[5].strip()}' WHERE image_id={item[0]}")
            cur.execute(f"UPDATE church SET church = '{item[6].strip()}' WHERE image_id={item[0]}")
            progress += 1
            self.label.setText(f"{progress}/{amount}")
            self.progressBar.setValue(progress)

        conn.commit()
        self.label.setText("창을 닫아주세요.")
        self.accept()

class fileDeleteDialog(QDialog, stripWindow.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        file_list = [file for file in os.listdir('./img') if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.gif') or file.endswith('.png') or file.endswith('.webp') or file.endswith('.tif') or file.endswith('.tiff')]
        amount = len(file_list)
        cur.execute('SELECT file_name FROM church')
        valid_file = [x[0] for x in cur.fetchall()]
        self.progressBar.setMaximum(amount)
        progress = 0
        for file in file_list:
            if file not in valid_file:
                os.remove('./img/'+file)
            progress += 1
            self.progressBar.setValue(progress)
            self.label.setText(f'{progress}/{amount}')
        self.label.setText("창을 닫아주세요.")

app = QApplication()
window = MainWindow()

window.show()

app.exec()
conn.close()

#FDSKFSDLKAFJSDALKJFWKALFNMSDKFAA
#FKLDSJAFKDLJSAFLKSDJF
#FfjAFKLDSAJLKFDSAJF