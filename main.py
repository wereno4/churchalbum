import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from mainWindow import Ui_MainWindow
import addWindow, modifyWindow, findWindow
import os, shutil


conn = sqlite3.connect("./church.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS church([image_id] INTEGER PRIMARY KEY, [type] TEXT, [series] TEXT, [year] INTEGER, [month] INTEGER, [country] TEXT, [region] TEXT, [church] TEXT, [file_name] TEXT, [note] TEXT)")
conn.commit()

if not os.path.exists("./img"):
    os.makedirs("./img")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.combobox_generate()
        self.find_image()

        self.calendertype.currentIndexChanged.connect(self.find_image)
        self.series.currentIndexChanged.connect(self.find_image)
        self.year.currentIndexChanged.connect(self.month_listing)
        self.month.currentIndexChanged.connect(self.find_image)
        self.country.currentIndexChanged.connect(self.for_country)
        self.region.currentIndexChanged.connect(self.church_listing)
        self.church.currentIndexChanged.connect(self.find_image)
        self.imageList.cellClicked.connect(self.show_image)
        self.addmenu.triggered.connect(self.addWindow)
        self.modify.triggered.connect(self.modifyWindow)



    def combobox_generate(self):
        self.calendertype.clear()
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
    
        self.series.addItem("-")
        cur.execute("SELECT series FROM church")
        series_list = cur.fetchall()
        series_list = [x[0] for x in series_list]
        series_list = list(set(series_list))
        for item in series_list:
            self.series.addItem(item)

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
        condition = "SELECT church, file_name FROM church"
        whereand = True
        if self.calendertype.currentText() != "-" and self.calendertype.currentText() != "":
            if whereand:
                condition = condition + f" WHERE type = '{self.calendertype.currentText()}'"
            else:
                condition = condition + f" AND type = '{self.calendertype.currentText()}'"
            whereand = False
        if self.series.currentText() != "-" and self.series.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE series = '{self.series.currentText()}'"
            else:
                condition = condition + f" AND series = '{self.series.currentText()}'"
            whereand = False
        if self.year.currentText() != "-" and self.year.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE year = {self.year.currentText()}"
            else:
                condition = condition + f" AND year = {self.year.currentText()}"
            whereand = False
        if self.month.currentText() != "-" and self.month.currentText() != "":
            if whereand:
                condition = condition + f" WHERE month = {self.month.currentText()}"
            else:
                condition = condition + f" AND month = {self.month.currentText()}"
            whereand = False
        if self.country.currentText() != "-" and self.country.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE country = '{self.country.currentText()}'"
            else:
                condition = condition + f" AND country = '{self.country.currentText()}'"
            whereand = False
        if self.region.currentText() != "-" and self.region.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE region = '{self.region.currentText()}'"
            else:
                condition = condition + f" AND region = '{self.region.currentText()}'"
            whereand = False
        if self.church.currentText() != "-" and self.church.currentText() != "":
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
                tableItem = QTableWidgetItem(item)
                self.imageList.setItem(y, x, tableItem)
                x += 1
            y += 1

        
    def month_listing(self):
        year = self.year.currentText()
        if year == "-" or year == "":
            self.month.clear()
        else:
            self.month.addItem("-")
            cur.execute(f"SELECT month FROM church WHERE year = {year}")
            month_list = cur.fetchall()
            month_list = [x[0] for x in month_list]
            month_list = list(set(month_list))
            for item in month_list:
                self.month.addItem(str(item))
            self.month.setItemText(0, "-")
        self.find_image()

    def region_listing(self):
        country = self.country.currentText()
        if country == "-" or country == "":
            self.region.clear()
        else:
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
        if region == "-" or country == "-" or region == "" or country == "":
            self.church.clear()
        else:
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
        pixmap = QPixmap(f"./img/{self.imageList.item(self.imageList.currentRow(), 1).text()}")
        if pixmap.size().width() >= pixmap.size().height():
            pixmap = pixmap.scaledToWidth(self.image.width())
        elif pixmap.size().width() <= pixmap.size().height():
            pixmap = pixmap.scaledToHeight(self.image.height())
        self.image.setPixmap(pixmap)
        cur.execute(f"SELECT note, image_id, type, series, year, month, country, region, church FROM church WHERE file_name = '{self.imageList.item(self.imageList.currentRow(), 1).text()}'")
        note, id, *information = cur.fetchall()[0]
        note = note + "\n" if note != "" else note
        self.note.setPlainText(note+f"ID: {id}\n{information}")

    def addWindow(self):
        dialog = addDialog()
        dialog.exec()
        self.combobox_generate()

    def modifyWindow(self):
        dialog = findDialog()
        dialog.exec()
        self.combobox_generate()

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

        cur.execute(f"INSERT INTO church VALUES ({key_to_add}, '{self.calendertype.text()}', '{self.series.text()}', {self.year.text()}, {self.month.text()}, '{self.country.text()}', '{self.region.text()}', '{self.church.text()}', '{file_name}', '{self.note.toPlainText()}')")
        conn.commit()

    
        self.accept()

class modifyDialog(QDialog, modifyWindow.Ui_Dialog):
    def __init__(self, ID, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.currentID = ID
        cur.execute(f"SELECT type, series, year, month, country, region, church, file_name, note FROM church WHERE image_id = {self.currentID}")
        result = cur.fetchall()[0]
        self.calendertype.setText(result[0])
        self.series.setText(result[1])
        self.year.setText(str(result[2]))
        self.month.setText(str(result[3]))
        self.country.setText(result[4])
        self.region.setText(result[5])
        self.church.setText(result[6])
        self.file.setText(result[7])
        self.note.setPlainText(result[8])
        self.oldfilename = result[7]

        self.cancelButton.clicked.connect(self.reject)
        self.deleteButton.clicked.connect(self.delete_data)
        self.modifyButton.clicked.connect(self.modify_data)


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
            cur.execute(f"UPDATE church SET type='{self.calendertype.text()}', series='{self.series.text()}', year={self.year.text()}, month={self.month.text()}, country='{self.country.text()}', region='{self.region.text()}', church='{self.church.text()}', file_name='{file_name}', note='{self.note.toPlainText()}' WHERE image_id = {self.currentID}")
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
    
        self.series.addItem("-")
        cur.execute("SELECT series FROM church")
        series_list = cur.fetchall()
        series_list = [x[0] for x in series_list]
        series_list = list(set(series_list))
        for item in series_list:
            self.series.addItem(item)

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
        condition = "SELECT image_id, type, series, year, month, country, region, church, file_name, note FROM church"
        whereand = True
        if self.calendertype.currentText() != "-" and self.calendertype.currentText() != "":
            if whereand:
                condition = condition + f" WHERE type = '{self.calendertype.currentText()}'"
            else:
                condition = condition + f" AND type = '{self.calendertype.currentText()}'"
            whereand = False
        if self.series.currentText() != "-" and self.series.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE series = '{self.series.currentText()}'"
            else:
                condition = condition + f" AND series = '{self.series.currentText()}'"
            whereand = False
        if self.year.currentText() != "-" and self.year.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE year = {self.year.currentText()}"
            else:
                condition = condition + f" AND year = {self.year.currentText()}"
            whereand = False
        if self.month.currentText() != "-" and self.month.currentText() != "":
            if whereand:
                condition = condition + f" WHERE month = {self.month.currentText()}"
            else:
                condition = condition + f" AND month = {self.month.currentText()}"
            whereand = False
        if self.country.currentText() != "-" and self.country.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE country = '{self.country.currentText()}'"
            else:
                condition = condition + f" AND country = '{self.country.currentText()}'"
            whereand = False
        if self.region.currentText() != "-" and self.region.currentText()  != "":
            if whereand:
                condition = condition + f" WHERE region = '{self.region.currentText()}'"
            else:
                condition = condition + f" AND region = '{self.region.currentText()}'"
            whereand = False
        if self.church.currentText() != "-" and self.church.currentText() != "":
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
        if year == "-" or year == "":
            self.month.clear()
        else:
            self.month.addItem("-")
            cur.execute(f"SELECT month FROM church WHERE year = {year}")
            month_list = cur.fetchall()
            month_list = [x[0] for x in month_list]
            month_list = list(set(month_list))
            for item in month_list:
                self.month.addItem(str(item))
            self.month.setItemText(0, "-")
        self.find_image()

    def region_listing(self):
        country = self.country.currentText()
        if country == "-" or country == "":
            self.region.clear()
        else:
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
        if region == "-" or country == "-" or region == "" or country == "":
            self.church.clear()
        else:
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

    def modify_window(self):
        dialog = modifyDialog(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        dialog.exec()
        self.combobox_generate()



app = QApplication()
window = MainWindow()

window.show()

app.exec()
conn.close()