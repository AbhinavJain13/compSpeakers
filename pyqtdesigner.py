# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtdesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(624, 534)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.serverIp = QtGui.QLabel(self.centralwidget)
        self.serverIp.setGeometry(QtCore.QRect(140, 60, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.serverIp.setFont(font)
        self.serverIp.setLineWidth(1)
        self.serverIp.setTextFormat(QtCore.Qt.RichText)
        self.serverIp.setScaledContents(False)
        self.serverIp.setObjectName(_fromUtf8("serverIp"))
        self.serverPort = QtGui.QLabel(self.centralwidget)
        self.serverPort.setGeometry(QtCore.QRect(330, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.serverPort.setFont(font)
        self.serverPort.setTextFormat(QtCore.Qt.RichText)
        self.serverPort.setScaledContents(False)
        self.serverPort.setObjectName(_fromUtf8("serverPort"))
        self.portText = QtGui.QTextEdit(self.centralwidget)
        self.portText.setGeometry(QtCore.QRect(330, 110, 121, 31))
        self.portText.setObjectName(_fromUtf8("portText"))
        self.IPtext = QtGui.QPlainTextEdit(self.centralwidget)
        self.IPtext.setGeometry(QtCore.QRect(120, 110, 121, 31))
        self.IPtext.setObjectName(_fromUtf8("IPtext"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(220, 280, 151, 41))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.StartANDResume = QtGui.QComboBox(self.centralwidget)
        self.StartANDResume.setGeometry(QtCore.QRect(220, 180, 151, 22))
        self.StartANDResume.setObjectName(_fromUtf8("StartANDResume"))
        self.StartANDResume.addItem(_fromUtf8(""))
        self.StartANDResume.addItem(_fromUtf8(""))
        self.StopANDPause = QtGui.QComboBox(self.centralwidget)
        self.StopANDPause.setGeometry(QtCore.QRect(220, 220, 151, 22))
        self.StopANDPause.setObjectName(_fromUtf8("StopANDPause"))
        self.StopANDPause.addItem(_fromUtf8(""))
        self.StopANDPause.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.serverIp.setText(_translate("MainWindow", "SERVER IP", None))
        self.serverPort.setText(_translate("MainWindow", "SERVER PORT", None))
        self.StartANDResume.setItemText(0, _translate("MainWindow", "START", None))
        self.StartANDResume.setItemText(1, _translate("MainWindow", "RESUME", None))
        self.StopANDPause.setItemText(0, _translate("MainWindow", "STOP", None))
        self.StopANDPause.setItemText(1, _translate("MainWindow", "PAUSE", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

