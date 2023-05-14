import sys
from pathlib import Path
import json
from collections import defaultdict
import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ihgui import Ui_MainWindow

book_index = defaultdict(list)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.writeindex)
        self.toolButton_2.clicked.connect(self.cleanslate)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        self.action_Open.triggered.connect(self.openformatted)
        self.action_Save.triggered.connect(self.writeindex)
        self.action_Format.triggered.connect(self.formattedvers)
        self.action_SaveChanges.triggered.connect(self.editindex)
        self.action_Update.triggered.connect(self.updateindex)
        self.action_Quit.triggered.connect(self.close)
        self.lineEdit_2.returnPressed.connect(self.createindex)
        self.lineEdit_2.returnPressed.connect(self.changetext)
        self.lineEdit_2.returnPressed.connect(self.lineEdit_2.clear)

    def changetext(self):
        val = self.lineEdit_2.text()
        self.textEdit.append(val)
        

    def cleanslate(self):
        self.textEdit.clear()
        self.lineEdit.clear()
    

    def createindex(self):
        page = self.lineEdit.text()
        term = self.lineEdit_2.text()
        book_index[term].append(page)

    def updateindex(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Update file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                old = json.load(f)
                for key, value in book_index.items():
                    if key in old: 
                        old[key].extend(value)
                    else:
                        old.update(book_index)

            with open(fname[0], 'w', encoding='utf-8') as json_file:
                json.dump(old, json_file, ensure_ascii=False, sort_keys=True)
                book_index.clear()
                old.clear()
                self.textEdit.clear()
                self.lineEdit.clear()

    def writeindex(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getSaveFileName(self, 'Save file', home_dir)

        if fname[0]:
            with open(fname[0], 'w', encoding='utf-8') as json_file:
                json.dump(book_index, json_file, ensure_ascii=False, sort_keys=True)
                book_index.clear()
                self.textEdit.clear()
                self.lineEdit.clear()

    def openformatted(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Format file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            
            with f:
                data = json.load(f)
                for key, value in data.items():
                    value.sort()
                    value = ", ".join(map(str, value))
                    self.textEdit.append('%s: %s\n' % (key, value))
           
    
    def editindex(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getSaveFileName(self, 'Save file', home_dir)

        if fname[0]:
            with open(fname[0], 'w', encoding='utf-8') as json_file:
                edited = self.textEdit.toPlainText()
                reedited = defaultdict(list)
                for k, v in re.findall(r'(?=\S|^)(.+?): ([\d+].*)', edited.rstrip()):
                    reedited[k].append(v)
                json.dump(reedited, json_file, ensure_ascii=False, sort_keys=True)
                self.textEdit.clear()

    def formattedvers(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = json.load(f)

                with open(fname[0], 'w') as f:
                    for key, value in data.items():
                        value.sort()
                        value = ", ".join(map(str, value))
                        f.write('%s: %s\n' % (key, value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

  