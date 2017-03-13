# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Tue Mar 07 16:49:28 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(467, 108)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.EditFrame = QtGui.QFrame(self.centralwidget)
        self.EditFrame.setObjectName(_fromUtf8("EditFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.EditFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.EditFrame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btnBrowse = QtGui.QPushButton(self.EditFrame)
        self.btnBrowse.setMinimumSize(QtCore.QSize(0, 23))
        self.btnBrowse.setAutoDefault(True)
        self.btnBrowse.setDefault(False)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout.addWidget(self.EditFrame)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnSub = QtGui.QPushButton(self.page)
        self.btnSub.setMinimumSize(QtCore.QSize(0, 25))
        self.btnSub.setAutoDefault(True)
        self.btnSub.setDefault(False)
        self.btnSub.setFlat(False)
        self.btnSub.setObjectName(_fromUtf8("btnSub"))
        self.horizontalLayout_3.addWidget(self.btnSub)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setEnabled(True)
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAlt = QtGui.QPushButton(self.page_2)
        self.btnAlt.setMinimumSize(QtCore.QSize(0, 25))
        self.btnAlt.setAutoDefault(True)
        self.btnAlt.setDefault(False)
        self.btnAlt.setFlat(False)
        self.btnAlt.setObjectName(_fromUtf8("btnAlt"))
        self.horizontalLayout_2.addWidget(self.btnAlt)
        self.btnFold = QtGui.QPushButton(self.page_2)
        self.btnFold.setMinimumSize(QtCore.QSize(0, 25))
        self.btnFold.setAutoDefault(True)
        self.btnFold.setDefault(False)
        self.btnFold.setObjectName(_fromUtf8("btnFold"))
        self.horizontalLayout_2.addWidget(self.btnFold)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnBrowse.setText(_translate("MainWindow", "Browse", None))
        self.btnSub.setText(_translate("MainWindow", "Get Subtitles", None))
        self.btnAlt.setText(_translate("MainWindow", "Get Alternate Subtitles", None))
        self.btnFold.setText(_translate("MainWindow", "Open Containing Folder", None))

