# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 612)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        self.font = QtGui.QFont()
        MainWindow.setFont(self.font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(75)
        item.setFont(self.font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(75)
        item.setFont(self.font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.Slider = QtWidgets.QSlider(self.centralwidget)
        self.Slider.setMaximum(100)
        self.Slider.setSliderPosition(50)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider.setTickInterval(10)
        self.Slider.setObjectName("Slider")
        self.gridLayout.addWidget(self.Slider, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openSong1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openSong1.sizePolicy().hasHeightForWidth())
        self.openSong1.setSizePolicy(sizePolicy)
        self.openSong1.setMaximumSize(QtCore.QSize(16777215, 70))
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setWeight(75)
        self.openSong1.setFont(self.font)
        self.openSong1.setObjectName("openSong1")
        self.horizontalLayout.addWidget(self.openSong1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setWeight(75)
        self.label.setFont(self.font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.openSong2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openSong2.sizePolicy().hasHeightForWidth())
        self.openSong2.setSizePolicy(sizePolicy)
        self.openSong2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setWeight(75)
        self.openSong2.setFont(self.font)
        self.openSong2.setObjectName("openSong2")
        self.horizontalLayout.addWidget(self.openSong2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.Mix = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mix.sizePolicy().hasHeightForWidth())
        self.Mix.setSizePolicy(sizePolicy)
        self.Mix.setMaximumSize(QtCore.QSize(16777215, 70))
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setWeight(75)
        self.Mix.setFont(self.font)
        self.Mix.setChecked(False)
        self.Mix.setObjectName("Mix")
        self.gridLayout.addWidget(self.Mix, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.Slider.setEnabled(False)
        self.Mix.setEnabled(False)
        self.label.hide()
        for col in range(2):
            self.tableWidget.horizontalHeader().setSectionResizeMode(
                col, QtWidgets.QHeaderView.Stretch)
            # self.tableWidget.horizontalHeaderItem(
            #     col).setBackground(QtGui.QColor(57, 65, 67))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Song Recognizer"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Song Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Similarity"))
        self.openSong1.setText(_translate("MainWindow", "Song 1"))
        self.label.setText(_translate("MainWindow", "50:50"))
        self.openSong2.setText(_translate("MainWindow", "Song 2"))
        self.Mix.setText(_translate("MainWindow", "Mix"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
