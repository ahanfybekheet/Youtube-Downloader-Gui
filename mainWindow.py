# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 991, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.video_btn = QtWidgets.QRadioButton(self.frame)
        self.video_btn.setObjectName("video_btn")
        self.horizontalLayout.addWidget(self.video_btn)
        self.audio_btn = QtWidgets.QRadioButton(self.frame)
        self.audio_btn.setObjectName("audio_btn")
        self.horizontalLayout.addWidget(self.audio_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.qualitybox = QtWidgets.QComboBox(self.frame)
        self.qualitybox.setObjectName("qualitybox")
        self.qualitybox.addItem("")
        self.qualitybox.addItem("")
        self.qualitybox.addItem("")
        self.horizontalLayout_2.addWidget(self.qualitybox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.search_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_3.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.search_input.returnPressed.connect(self.search_btn.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.video_btn.setText(_translate("MainWindow", "Video (mp4)"))
        self.audio_btn.setText(_translate("MainWindow", "Audio (mp3)"))
        self.label.setText(_translate("MainWindow", "Quality"))
        self.qualitybox.setItemText(0, _translate("MainWindow", "144p"))
        self.qualitybox.setItemText(1, _translate("MainWindow", "360p"))
        self.qualitybox.setItemText(2, _translate("MainWindow", "720p"))
        self.label_2.setText(_translate("MainWindow", "Search: "))
        self.search_btn.setText(_translate("MainWindow", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
