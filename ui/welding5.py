# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welding5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_weldingTable2(object):
    def setupUi(self, weldingTable2):
        weldingTable2.setObjectName("weldingTable2")
        weldingTable2.resize(630, 500)
        weldingTable2.setMinimumSize(QtCore.QSize(630, 500))
        self.centralwidget = QtWidgets.QWidget(weldingTable2)
        self.centralwidget.setObjectName("centralwidget")
        self.table2img = QtWidgets.QPushButton(self.centralwidget)
        self.table2img.setGeometry(QtCore.QRect(40, 20, 250, 200))
        self.table2img.setText("")
        self.table2img.setIcon(QtGui.QIcon('image/table2/table2img2.png'))
        self.table2img.setIconSize(QtCore.QSize(250, 200))
        self.table2img.setObjectName("table2img")
        self.table2img2 = QtWidgets.QPushButton(self.centralwidget)
        self.table2img2.setGeometry(QtCore.QRect(335, 20, 250, 200))
        self.table2img2.setText("")
        self.table2img2.setIcon(QtGui.QIcon('image/table2/table2img.png'))
        self.table2img2.setIconSize(QtCore.QSize(250, 200))
        self.table2img2.setObjectName("table2img2")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(230, 220, 101, 61))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 1, 1, 1)
        self.rop = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.rop.setObjectName("rop")
        self.gridLayout_5.addWidget(self.rop, 1, 1, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(80, 290, 101, 61))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 1, 1, 1)
        self.weld_k = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.weld_k.setObjectName("weld_k")
        self.gridLayout_7.addWidget(self.weld_k, 1, 1, 1, 1)
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(420, 290, 101, 61))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 1, 1, 1)
        self.length = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.length.setObjectName("length")
        self.gridLayout_8.addWidget(self.length, 1, 1, 1, 1)
        self.pushResult = QtWidgets.QPushButton(self.centralwidget)
        self.pushResult.setGeometry(QtCore.QRect(40, 360, 201, 31))
        self.pushResult.setObjectName("pushResult")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 390, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(120, 400, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 410, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(360, 220, 101, 61))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushResult2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushResult2.setGeometry(QtCore.QRect(370, 360, 201, 31))
        self.pushResult2.setObjectName("pushResult2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 410, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.result2 = QtWidgets.QLabel(self.centralwidget)
        self.result2.setGeometry(QtCore.QRect(440, 400, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.result2.setFont(font)
        self.result2.setText("")
        self.result2.setAlignment(QtCore.Qt.AlignCenter)
        self.result2.setObjectName("result2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 390, 115, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(350, 220, 71, 61))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.kgs = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.kgs.setObjectName("kgs")
        self.gridLayout_3.addWidget(self.kgs, 0, 0, 1, 1)
        self.kn = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.kn.setObjectName("kn")
        self.gridLayout_3.addWidget(self.kn, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(480, 220, 61, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        weldingTable2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(weldingTable2)
        self.statusbar.setObjectName("statusbar")
        weldingTable2.setStatusBar(self.statusbar)
        self.retranslateUi(weldingTable2)
        QtCore.QMetaObject.connectSlotsByName(weldingTable2)

    def retranslateUi(self, weldingTable2):
        _translate = QtCore.QCoreApplication.translate
        weldingTable2.setWindowTitle(_translate("weldingTable2", "Проверка длины сварного шва"))
        self.label_7.setText(_translate("weldingTable2", "Реакция (R)"))
        self.label_9.setText(_translate("weldingTable2", "Катет (h2, см)"))
        self.label_10.setText(_translate("weldingTable2", "Длина (L1, см)"))
        self.pushResult.setText(_translate("weldingTable2", "Расчитать длину"))
        self.label.setText(_translate("weldingTable2", "Длина шва:"))
        self.label_5.setText(_translate("weldingTable2", "см"))
        self.pushResult2.setText(_translate("weldingTable2", "Расчитать катет шва"))
        self.label_6.setText(_translate("weldingTable2", "см"))
        self.label_2.setText(_translate("weldingTable2", "Катет шва:"))
        self.kgs.setText(_translate("weldingTable2", "кгс"))
        self.kn.setText(_translate("weldingTable2", "кН"))
        self.rop.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.length.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.weld_k.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.pushResult.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.pushResult2.setStyleSheet("""
                                   QPushButton:hover { background-color: rgb(228, 228, 228) }
                                   QPushButton:!hover { background-color: white }

                                   QPushButton:pressed { background-color: rgb(191, 241, 255); }
                               """)
        self.table2img.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.table2img2.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
