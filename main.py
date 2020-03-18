from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from Interface import interfaz

import sentencepiece as spm

class ExampleApp(QtWidgets.QMainWindow,interfaz.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btn1.clicked.connect(self.tokenize)
        
        self.btn2.clicked.connect(self.clean)
    def tokenize(self):
        sp_word = spm.SentencePieceProcessor()
        if self.rb1.isChecked():
           sp_word.load('Models/m_word.model')
        else:
            sp_word.load('Models/m_user.model')

        token= str(sp_word.encode_as_pieces(self.text1.toPlainText()))
        self.text2.setPlainText(token)
  
    def clean(self):
        self.text1.setPlainText("")
        self.text2.setPlainText("")



def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()