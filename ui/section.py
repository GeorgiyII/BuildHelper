# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'section.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_section(object):
    def setupUi(self, section):
        section.setObjectName("section")
        section.resize(460, 400)
        section.setMinimumSize(QtCore.QSize(460, 400))
        self.centralwidget = QtWidgets.QWidget(section)
        self.centralwidget.setObjectName("centralwidget")
        self.weld_beadimg = QtWidgets.QPushButton(self.centralwidget)
        self.weld_beadimg.setGeometry(QtCore.QRect(20, 20, 221, 231))
        self.weld_beadimg.setText("")
        self.weld_beadimg.setIcon(QtGui.QIcon('image/section/weld_beadimg.png'))
        self.weld_beadimg.setIconSize(QtCore.QSize(220, 220))
        self.weld_beadimg.setObjectName("weld_beadimg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 153, 20))
        self.label.setObjectName("label")
        self.hst = QtWidgets.QLineEdit(self.centralwidget)
        self.hst.setGeometry(QtCore.QRect(290, 40, 111, 21))
        self.hst.setAlignment(QtCore.Qt.AlignCenter)
        self.hst.setObjectName("hst")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 80, 164, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 140, 164, 20))
        self.label_3.setObjectName("label_3")
        self.tst = QtWidgets.QLineEdit(self.centralwidget)
        self.tst.setGeometry(QtCore.QRect(290, 100, 111, 21))
        self.tst.setAlignment(QtCore.Qt.AlignCenter)
        self.tst.setObjectName("tst")
        self.bpol = QtWidgets.QLineEdit(self.centralwidget)
        self.bpol.setGeometry(QtCore.QRect(290, 160, 111, 21))
        self.bpol.setAlignment(QtCore.Qt.AlignCenter)
        self.bpol.setObjectName("bpol")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 200, 164, 20))
        self.label_4.setObjectName("label_4")
        self.tpol = QtWidgets.QLineEdit(self.centralwidget)
        self.tpol.setGeometry(QtCore.QRect(290, 220, 111, 21))
        self.tpol.setAlignment(QtCore.Qt.AlignCenter)
        self.tpol.setObjectName("tpol")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(35, 260, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(105, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(215, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.result_2 = QtWidgets.QLabel(self.centralwidget)
        self.result_2.setGeometry(QtCore.QRect(105, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.result_2.setFont(font)
        self.result_2.setText("")
        self.result_2.setAlignment(QtCore.Qt.AlignCenter)
        self.result_2.setObjectName("result_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(215, 320, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(35, 320, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushResult = QtWidgets.QPushButton(self.centralwidget)
        self.pushResult.setGeometry(QtCore.QRect(280, 280, 131, 51))
        self.pushResult.setObjectName("pushResult")
        section.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(section)
        self.statusbar.setObjectName("statusbar")
        section.setStatusBar(self.statusbar)

        self.retranslateUi(section)
        QtCore.QMetaObject.connectSlotsByName(section)

    def retranslateUi(self, section):
        _translate = QtCore.QCoreApplication.translate
        section.setWindowTitle(_translate("section", "Подбор сварного двутавра"))
        self.label.setText(_translate("section", "Высота стенки (hст, см)"))
        self.label_2.setText(_translate("section", "Толщина стенки (tст, см)"))
        self.label_3.setText(_translate("section", "Ширина полки (bп, см)"))
        self.label_4.setText(_translate("section", "Толщина полки (tп, см)"))
        self.label_5.setText(_translate("section", "Ix"))
        self.label_6.setText(_translate("section", "см4"))
        self.label_7.setText(_translate("section", "кг/м"))
        self.label_8.setText(_translate("section", "m"))
        self.pushResult.setText(_translate("section", "Расчитать"))
        self.pushResult.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.weld_beadimg.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.tst.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.hst.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.tpol.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.bpol.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))

