# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welding1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_weldingFas1(object):
    def setupUi(self, weldingFas1):
        weldingFas1.setObjectName("weldingFas1")
        weldingFas1.resize(600, 600)
        weldingFas1.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(weldingFas1)
        self.centralwidget.setObjectName("centralwidget")
        self.fas1img = QtWidgets.QPushButton(self.centralwidget)
        self.fas1img.setGeometry(QtCore.QRect(50, 65, 200, 130))
        self.fas1img.setText("")
        self.fas1img.setIcon(QtGui.QIcon('image/fas1/fas1img.png'))
        self.fas1img.setIconSize(QtCore.QSize(130, 130))
        self.fas1img.setObjectName("fas1img")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.fas2img = QtWidgets.QPushButton(self.centralwidget)
        self.fas2img.setGeometry(QtCore.QRect(50, 225, 200, 130))
        self.fas2img.setText("")
        self.fas2img.setIcon(QtGui.QIcon('image/fas1/fas2img.png'))
        self.fas2img.setIconSize(QtCore.QSize(135, 135))
        self.fas2img.setObjectName("fas2img")
        self.fas3img = QtWidgets.QPushButton(self.centralwidget)
        self.fas3img.setGeometry(QtCore.QRect(320, 65, 200, 130))
        self.fas3img.setText("")
        self.fas3img.setIcon(QtGui.QIcon('image/fas1/fas3img.png'))
        self.fas3img.setIconSize(QtCore.QSize(130, 130))
        self.fas3img.setObjectName("fas3img")
        self.fas4img = QtWidgets.QPushButton(self.centralwidget)
        self.fas4img.setGeometry(QtCore.QRect(320, 225, 200, 130))
        self.fas4img.setText("")
        self.fas4img.setIcon(QtGui.QIcon('image/fas1/fas4img.png'))
        self.fas4img.setIconSize(QtCore.QSize(135, 135))
        self.fas4img.setObjectName("fas4img")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 370, 430, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(30, 400, 101, 61))
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
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(200, 400, 101, 61))
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
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(330, 400, 101, 61))
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
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(460, 400, 111, 61))
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
        self.label_11.setGeometry(QtCore.QRect(320, 490, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(370, 480, 81, 61))
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
        self.label_13.setGeometry(QtCore.QRect(460, 490, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(490, 480, 81, 61))
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
        self.pushResult.setGeometry(QtCore.QRect(190, 518, 110, 20))
        self.pushResult.setObjectName("pushResult")
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(140, 400, 71, 61))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.kgs = QtWidgets.QRadioButton(self.gridLayoutWidget_12)
        self.kgs.setObjectName("kgs")
        self.gridLayout_12.addWidget(self.kgs, 0, 0, 1, 1)
        self.kn = QtWidgets.QRadioButton(self.gridLayoutWidget_12)
        self.kn.setObjectName("kn")
        self.gridLayout_12.addWidget(self.kn, 1, 0, 1, 1)
        self.double = QtWidgets.QCheckBox(self.centralwidget)
        self.double.setGeometry(QtCore.QRect(180, 485, 160, 20))
        self.double.setObjectName("double")
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(30, 470, 150, 80))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.montage = QtWidgets.QRadioButton(self.gridLayoutWidget_13)
        self.montage.setObjectName("montage")
        self.gridLayout_13.addWidget(self.montage, 0, 0, 1, 1)
        self.prefab = QtWidgets.QRadioButton(self.gridLayoutWidget_13)
        self.prefab.setObjectName("prefab")
        self.gridLayout_13.addWidget(self.prefab, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 45, 60, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 205, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 45, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 205, 60, 16))
        self.label_5.setObjectName("label_5")
        weldingFas1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(weldingFas1)
        self.statusbar.setObjectName("statusbar")
        weldingFas1.setStatusBar(self.statusbar)

        self.retranslateUi(weldingFas1)
        QtCore.QMetaObject.connectSlotsByName(weldingFas1)

    def retranslateUi(self, weldingFas1):
        _translate = QtCore.QCoreApplication.translate
        weldingFas1.setWindowTitle(_translate("weldingFas1", "Проверка длины сварного шва"))
        self.label_2.setText(_translate("weldingFas1", "Варианты сварного соединения"))
        self.label_6.setText(_translate("weldingFas1", "Проверка несущей способности сварного шва"))
        self.label_7.setText(_translate("weldingFas1", "Реакция (R)"))
        self.label_8.setText(_translate("weldingFas1", "Длина (Lш, см)"))
        self.label_9.setText(_translate("weldingFas1", "Катет шва (см)"))
        self.label_10.setText(_translate("weldingFas1", "Плече (L, см)"))
        self.label_11.setText(_translate("weldingFas1", "Tш="))
        self.label_13.setText(_translate("weldingFas1", "<="))
        self.pushResult.setText(_translate("weldingFas1", "Расчитать"))
        self.kgs.setText(_translate("weldingFas1", "кгс"))
        self.kn.setText(_translate("weldingFas1", "кН"))
        self.montage.setText(_translate("weldingFas1", "Монтажный шев"))
        self.prefab.setText(_translate("weldingFas1", "Заводской шев"))
        self.double.setText(_translate("weldingFas1", "Ответная планка"))
        self.label.setText(_translate("weldingFas1", "R<=3т"))
        self.label_3.setText(_translate("weldingFas1", "R<=5т"))
        self.label_4.setText(_translate("weldingFas1", "R>5т"))
        self.label_5.setText(_translate("weldingFas1", "R<=5т"))
        self.rop.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.weld_l.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.weld_k.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.force_l.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.pushResult.setStyleSheet("""
                    QPushButton:hover { background-color: rgb(228, 228, 228) }
                    QPushButton:!hover { background-color: white }

                    QPushButton:pressed { background-color: rgb(191, 241, 255); }
                """)
        self.fas2img.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.fas1img.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.fas3img.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.fas4img.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
