# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welding6.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_weldingFas3(object):
    def setupUi(self, weldingFas3):
        weldingFas3.setObjectName("weldingFas3")
        weldingFas3.resize(600, 400)
        weldingFas3.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(weldingFas3)
        self.centralwidget.setObjectName("centralwidget")
        self.fas3img = QtWidgets.QPushButton(self.centralwidget)
        self.fas3img.setGeometry(QtCore.QRect(20, 20, 280, 260))
        self.fas3img.setText("")
        self.fas3img.setIcon(QtGui.QIcon('image/fas3/fas3img.png'))
        self.fas3img.setIconSize(QtCore.QSize(260, 260))
        self.fas3img.setObjectName("fas3img")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(320, 30, 101, 61))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 1, 1, 1)
        self.rop = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.rop.setObjectName("rop")
        self.gridLayout_5.addWidget(self.rop, 1, 1, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(320, 170, 101, 61))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 1, 1, 1)
        self.weld_l = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.weld_l.setObjectName("weld_l")
        self.gridLayout_6.addWidget(self.weld_l, 1, 1, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(460, 100, 111, 61))
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
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(460, 170, 111, 61))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 1, 1, 1)
        self.force_l = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.force_l.setObjectName("force_l")
        self.gridLayout_8.addWidget(self.force_l, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 290, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(80, 280, 81, 61))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.result = QtWidgets.QLabel(self.gridLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.gridLayout_9.addWidget(self.result, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(170, 290, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(200, 280, 81, 61))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ry_resist = QtWidgets.QLabel(self.gridLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ry_resist.setFont(font)
        self.ry_resist.setText("")
        self.ry_resist.setAlignment(QtCore.Qt.AlignCenter)
        self.ry_resist.setObjectName("ry_resist")
        self.gridLayout_10.addWidget(self.ry_resist, 0, 0, 1, 1)
        self.pushResult = QtWidgets.QPushButton(self.centralwidget)
        self.pushResult.setGeometry(QtCore.QRect(460, 240, 113, 51))
        self.pushResult.setObjectName("pushResult")
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(320, 100, 101, 61))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 0, 1, 1, 1)
        self.nop = QtWidgets.QLineEdit(self.gridLayoutWidget_11)
        self.nop.setObjectName("nop")
        self.gridLayout_11.addWidget(self.nop, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(440, 40, 141, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.kgs = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.kgs.setObjectName("kgs")
        self.gridLayout_2.addWidget(self.kgs, 0, 0, 1, 1)
        self.kn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.kn.setObjectName("kn")
        self.gridLayout_2.addWidget(self.kn, 0, 1, 1, 1)
        self.double = QtWidgets.QCheckBox(self.centralwidget)
        self.double.setGeometry(QtCore.QRect(310, 310, 141, 20))
        self.double.setObjectName("double")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(310, 230, 141, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.montage = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.montage.setObjectName("montage")
        self.gridLayout_3.addWidget(self.montage, 0, 0, 1, 1)
        self.prefab = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.prefab.setObjectName("prefab")
        self.gridLayout_3.addWidget(self.prefab, 1, 0, 1, 1)
        weldingFas3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(weldingFas3)
        self.statusbar.setObjectName("statusbar")
        weldingFas3.setStatusBar(self.statusbar)

        self.retranslateUi(weldingFas3)
        QtCore.QMetaObject.connectSlotsByName(weldingFas3)

    def retranslateUi(self, weldingFas3):
        _translate = QtCore.QCoreApplication.translate
        weldingFas3.setWindowTitle(_translate("weldingFas3", "Проверка длины сварного шва"))
        self.label_7.setText(_translate("weldingFas3", "Реакция (R)"))
        self.label_8.setText(_translate("weldingFas3", "Длина (Lш, см)"))
        self.label_9.setText(_translate("weldingFas3", "Катет (hш, см)"))
        self.label_10.setText(_translate("weldingFas3", "Плече (L, см)"))
        self.label_11.setText(_translate("weldingFas3", "Tш="))
        self.label_13.setText(_translate("weldingFas3", "<="))
        self.pushResult.setText(_translate("weldingFas3", "Расчитать"))
        self.label_12.setText(_translate("weldingFas3", "Реакция (N)"))
        self.kgs.setText(_translate("weldingFas3", "кгс"))
        self.kn.setText(_translate("weldingFas3", "кН"))
        self.montage.setText(_translate("weldingFas3", "Монтажный шев"))
        self.prefab.setText(_translate("weldingFas3", "Заводской шев"))
        self.double.setText(_translate("weldingFas3", "Ответная планка"))
        self.rop.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.nop.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.weld_l.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.weld_k.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.force_l.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.pushResult.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.fas3img.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)

