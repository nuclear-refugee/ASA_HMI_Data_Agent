# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/hmi_save_diolog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HmiSaveDialog(object):
    def setupUi(self, HmiSaveDialog):
        HmiSaveDialog.setObjectName("HmiSaveDialog")
        HmiSaveDialog.resize(625, 349)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        HmiSaveDialog.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(HmiSaveDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(HmiSaveDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mat = QtWidgets.QWidget()
        self.tab_mat.setObjectName("tab_mat")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_mat)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_matSave = QtWidgets.QPushButton(self.tab_mat)
        self.pushButton_matSave.setObjectName("pushButton_matSave")
        self.gridLayout_3.addWidget(self.pushButton_matSave, 1, 1, 1, 1)
        self.tableWidget_mat = QtWidgets.QTableWidget(self.tab_mat)
        self.tableWidget_mat.setObjectName("tableWidget_mat")
        self.tableWidget_mat.setColumnCount(5)
        self.tableWidget_mat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mat.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_mat.setHorizontalHeaderItem(4, item)
        self.gridLayout_3.addWidget(self.tableWidget_mat, 1, 0, 5, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 1, 1, 1)
        self.pushButton_matClose = QtWidgets.QPushButton(self.tab_mat)
        self.pushButton_matClose.setObjectName("pushButton_matClose")
        self.gridLayout_3.addWidget(self.pushButton_matClose, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_mat)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_mat, "")
        self.tab_csv = QtWidgets.QWidget()
        self.tab_csv.setObjectName("tab_csv")
        self.label = QtWidgets.QLabel(self.tab_csv)
        self.label.setGeometry(QtCore.QRect(9, 9, 591, 301))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_csv, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(HmiSaveDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(HmiSaveDialog)

    def retranslateUi(self, HmiSaveDialog):
        _translate = QtCore.QCoreApplication.translate
        HmiSaveDialog.setWindowTitle(_translate("HmiSaveDialog", "Dialog"))
        self.pushButton_matSave.setText(_translate("HmiSaveDialog", "以陣列儲存"))
        item = self.tableWidget_mat.horizontalHeaderItem(0)
        item.setText(_translate("HmiSaveDialog", "name"))
        item = self.tableWidget_mat.horizontalHeaderItem(1)
        item.setText(_translate("HmiSaveDialog", "type"))
        item = self.tableWidget_mat.horizontalHeaderItem(2)
        item.setText(_translate("HmiSaveDialog", "nums"))
        item = self.tableWidget_mat.horizontalHeaderItem(3)
        item.setText(_translate("HmiSaveDialog", "bytes"))
        item = self.tableWidget_mat.horizontalHeaderItem(4)
        item.setText(_translate("HmiSaveDialog", "data"))
        self.pushButton_matClose.setText(_translate("HmiSaveDialog", "關閉"))
        self.pushButton.setText(_translate("HmiSaveDialog", "以結構儲存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mat), _translate("HmiSaveDialog", "mat file"))
        self.label.setText(_translate("HmiSaveDialog", "WIP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_csv), _translate("HmiSaveDialog", "csv file"))

