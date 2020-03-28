from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
import sys
import design
import getsubs
import resources_rc
import os
import time

class MyApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyApp,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SubFinder")
        self.setFixedSize(433,102)
        self.setWindowIcon(QtGui.QIcon(':images/gold-fish-icon.png'))

        self.start = None
        self.subNameList = self.subLinksList = []
        self.movieName = self.filepath = self.filename = None
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.btnSub.clicked.connect(self.get_sub)
        self.btnAlt.clicked.connect(self.get_sub)
        self.btnFold.clicked.connect(self.open_folder)
        #self.lineEdit.setPlaceholderText("Select the movie file")
        self.lineEdit.returnPressed.connect(self.get_sub)
        self.lineEdit.textChanged.connect(self.text_changed)

    def browse_folder(self):
        #self.lineEdit.clear()
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Pick a file..", os.getcwd(), "Videos *.avi *.mkv *.mp4 *.flv")
        if file_name:
            self.lineEdit.setText(file_name)
            self.subNameList = []
            self.subLinksList = []
            self.movieName = None
            self.stackedWidget.setCurrentIndex(0)

    def get_sub(self):
        if self.lineEdit.text():
            self.btnAlt.setText("Searching..")
            self.btnSub.setText("Searching..")
            self.btnAlt.setEnabled(False)
            self.btnSub.setEnabled(False)
            self.lineEdit.clearFocus()
            self.btnFold.clearFocus()
            self.filepath = os.path.dirname(str(self.lineEdit.text()))
            self.filename = os.path.splitext(os.path.basename(str(self.lineEdit.text())))[0]   #.replace(' ', '.')
            print 'QueryName:', self.filename
            self.start = time.clock()
            self.get_thread = getsubs.GetSubsThread(self.filepath, self.filename, self.subLinksList, self.subNameList,
                                                    self.movieName)
            self.connect(self.get_thread, SIGNAL("subtitle_params(PyQt_PyObject)"), self.ret_sub_params)
            self.get_thread.start()
        else:
            QtGui.QMessageBox.information(self, "Error", "Choose a file first!")

    def ret_sub_params(self, ret_tup):
        print time.clock() - self.start   #Time taken for fetching the subs to be printed.
        self.btnAlt.setText("Get Alternate Subtitles")
        self.btnSub.setText("Get Subtitles")
        self.btnAlt.setEnabled(True)
        self.btnSub.setEnabled(True)
        self.movieName, subnames, self.subLinksList, error = ret_tup
        if error is None:
            QtGui.QMessageBox.information(self, "Message", "Cheers, downloaded!")
            if subnames:
                self.subNameList = subnames + self.subNameList
                print self.subNameList
            self.stackedWidget.setCurrentIndex(1)
            self.btnAlt.setFocus()
        elif error is 1:
            QtGui.QMessageBox.information(self, "Error", "Check internet connection!")
        elif error is 2:
            QtGui.QMessageBox.information(self, "Error", "No matches for for the title. Spell check!")
        elif error is 3:
            QtGui.QMessageBox.information(self, "Error", "Could not find any(more)!")

    def text_changed(self):
        self.movieName = None
        self.subLinksList = []
        #self.subNameList = [] | Because we don't want copies of the files when they're just tweaking the linedit.
        self.stackedWidget.setCurrentIndex(0)

    def open_folder(self):
        self.filepath = os.path.dirname(str(self.lineEdit.text()))
        os.startfile(self.filepath)


def main():
    #sys.stderr = sys.stdout
    app = QtGui.QApplication(sys.argv)
    form = MyApp()
    form.show()
    return app.exec_()

if __name__ == '__main__':
    main()
