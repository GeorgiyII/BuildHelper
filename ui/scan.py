# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scan(object):
    def setupUi(self, scan):
        scan.setObjectName("scan")
        scan.resize(740, 500)
        scan.setMinimumSize(QtCore.QSize(740, 500))
        self.centralwidget = QtWidgets.QWidget(scan)
        self.centralwidget.setObjectName("centralwidget")
        self.img1 = QtWidgets.QPushButton(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(20, 30, 130, 130))
        self.img1.setText("")
        self.img1.setIcon(QtGui.QIcon('image/scan/img1.png'))
        self.img1.setIconSize(QtCore.QSize(120, 120))
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QPushButton(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(20, 170, 130, 130))
        self.img2.setText("")
        self.img2.setIcon(QtGui.QIcon('image/scan/img2.png'))
        self.img2.setIconSize(QtCore.QSize(130, 130))
        self.img2.setObjectName("img2")
        self.img3 = QtWidgets.QPushButton(self.centralwidget)
        self.img3.setGeometry(QtCore.QRect(20, 310, 130, 130))
        self.img3.setText("")
        self.img3.setIcon(QtGui.QIcon('image/scan/img3.png'))
        self.img3.setIconSize(QtCore.QSize(130, 130))
        self.img3.setObjectName("img3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 6, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 35, 41, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.d_cylinder = QtWidgets.QLineEdit(self.centralwidget)
        self.d_cylinder.setGeometry(QtCore.QRect(190, 35, 60, 20))
        self.d_cylinder.setObjectName("d_cylinder")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 152, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 297, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 65, 41, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.t_cylinder = QtWidgets.QLineEdit(self.centralwidget)
        self.t_cylinder.setGeometry(QtCore.QRect(190, 65, 60, 20))
        self.t_cylinder.setObjectName("t_cylinder")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 95, 41, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.h_cylinder = QtWidgets.QLineEdit(self.centralwidget)
        self.h_cylinder.setGeometry(QtCore.QRect(190, 95, 61, 21))
        self.h_cylinder.setObjectName("h_cylinder")
        self.pushCylinder = QtWidgets.QPushButton(self.centralwidget)
        self.pushCylinder.setGeometry(QtCore.QRect(155, 120, 130, 30))
        self.pushCylinder.setObjectName("pushCylinder")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(255, 35, 21, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.img1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.img1_1.setGeometry(QtCore.QRect(290, 30, 300, 120))
        self.img1_1.setText("")
        self.img1_1.setIcon(QtGui.QIcon('image/scan/img1_1.png'))
        self.img1_1.setIconSize(QtCore.QSize(300, 300))
        self.img1_1.setObjectName("img1_1")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(255, 65, 21, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(255, 95, 31, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(255, 240, 21, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 240, 41, 16))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pushPipe90 = QtWidgets.QPushButton(self.centralwidget)
        self.pushPipe90.setGeometry(QtCore.QRect(155, 265, 130, 30))
        self.pushPipe90.setObjectName("pushPipe90")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(255, 210, 21, 16))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(150, 180, 41, 16))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(255, 180, 21, 16))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.diam_pipe90 = QtWidgets.QLineEdit(self.centralwidget)
        self.diam_pipe90.setGeometry(QtCore.QRect(190, 240, 61, 21))
        self.diam_pipe90.setObjectName("diam_pipe90")
        self.d_pipe90 = QtWidgets.QLineEdit(self.centralwidget)
        self.d_pipe90.setGeometry(QtCore.QRect(190, 180, 60, 20))
        self.d_pipe90.setObjectName("d_pipe90")
        self.t_pipe90 = QtWidgets.QLineEdit(self.centralwidget)
        self.t_pipe90.setGeometry(QtCore.QRect(190, 210, 60, 20))
        self.t_pipe90.setObjectName("t_pipe90")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(150, 210, 41, 16))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.img2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.img2_2.setGeometry(QtCore.QRect(290, 175, 300, 120))
        self.img2_2.setText("")
        self.img2_2.setIcon(QtGui.QIcon('image/scan/img2_2.png'))
        self.img2_2.setIconSize(QtCore.QSize(300, 300))
        self.img2_2.setObjectName("img2_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(150, 380, 41, 16))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(255, 380, 21, 16))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(255, 320, 21, 16))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.t_pipe = QtWidgets.QLineEdit(self.centralwidget)
        self.t_pipe.setGeometry(QtCore.QRect(190, 350, 60, 20))
        self.t_pipe.setObjectName("t_pipe")
        self.pushPipe = QtWidgets.QPushButton(self.centralwidget)
        self.pushPipe.setGeometry(QtCore.QRect(155, 440, 130, 30))
        self.pushPipe.setObjectName("pushPipe")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(255, 350, 21, 16))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.d_pipe = QtWidgets.QLineEdit(self.centralwidget)
        self.d_pipe.setGeometry(QtCore.QRect(190, 320, 60, 20))
        self.d_pipe.setObjectName("d_pipe")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(150, 350, 41, 16))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(150, 320, 41, 16))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.diam_pipe = QtWidgets.QLineEdit(self.centralwidget)
        self.diam_pipe.setGeometry(QtCore.QRect(190, 380, 61, 21))
        self.diam_pipe.setObjectName("diam_pipe")
        self.beta_pipe = QtWidgets.QLineEdit(self.centralwidget)
        self.beta_pipe.setGeometry(QtCore.QRect(190, 410, 61, 21))
        self.beta_pipe.setObjectName("beta_pipe")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(150, 410, 41, 16))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(255, 410, 31, 16))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.img2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.img2_3.setGeometry(QtCore.QRect(290, 320, 300, 120))
        self.img2_3.setText("")
        self.img2_3.setIcon(QtGui.QIcon('image/scan/img3_3.png'))
        self.img2_3.setIconSize(QtCore.QSize(300, 300))
        self.img2_3.setObjectName("img2_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(600, 35, 110, 400))
        self.listWidget.setObjectName("listWidget")
        scan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(scan)
        self.statusbar.setObjectName("statusbar")
        scan.setStatusBar(self.statusbar)

        self.retranslateUi(scan)
        QtCore.QMetaObject.connectSlotsByName(scan)

    def retranslateUi(self, scan):
        _translate = QtCore.QCoreApplication.translate
        scan.setWindowTitle(_translate("scan", "Расчет координат развертки труб"))
        self.label.setText(_translate("scan", "Под углом к плоскости"))
        self.label_4.setText(_translate("scan", "d ="))
        self.label_5.setText(_translate("scan", "Стык с трубой"))
        self.label_6.setText(_translate("scan", "Под углом к трубе"))
        self.label_7.setText(_translate("scan", "t ="))
        self.label_8.setText(_translate("scan", "B ="))
        self.pushCylinder.setText(_translate("scan", "Расчитать"))
        self.label_9.setText(_translate("scan", "мм"))
        self.label_10.setText(_translate("scan", "мм"))
        self.label_11.setText(_translate("scan", "град"))
        self.label_12.setText(_translate("scan", "мм"))
        self.label_13.setText(_translate("scan", "D ="))
        self.pushPipe90.setText(_translate("scan", "Расчитать"))
        self.label_14.setText(_translate("scan", "мм"))
        self.label_15.setText(_translate("scan", "d ="))
        self.label_16.setText(_translate("scan", "мм"))
        self.label_17.setText(_translate("scan", "t ="))
        self.label_18.setText(_translate("scan", "D ="))
        self.label_19.setText(_translate("scan", "мм"))
        self.label_20.setText(_translate("scan", "мм"))
        self.pushPipe.setText(_translate("scan", "Расчитать"))
        self.label_21.setText(_translate("scan", "мм"))
        self.label_22.setText(_translate("scan", "t ="))
        self.label_23.setText(_translate("scan", "d ="))
        self.label_24.setText(_translate("scan", "B ="))
        self.label_25.setText(_translate("scan", "град."))
        self.label_2.setText(_translate("scan", "Результат"))
        self.pushCylinder.setStyleSheet("""
                                    QPushButton:hover { background-color: rgb(228, 228, 228) }
                                    QPushButton:!hover { background-color: white }

                                    QPushButton:pressed { background-color: rgb(191, 241, 255); }
                                """)
        self.pushPipe90.setStyleSheet("""
                                    QPushButton:hover { background-color: rgb(228, 228, 228) }
                                    QPushButton:!hover { background-color: white }

                                    QPushButton:pressed { background-color: rgb(191, 241, 255); }
                                """)
        self.pushPipe.setStyleSheet("""
                                    QPushButton:hover { background-color: rgb(228, 228, 228) }
                                    QPushButton:!hover { background-color: white }

                                    QPushButton:pressed { background-color: rgb(191, 241, 255); }
                                """)
        self.img1.setStyleSheet("""
                                            QPushButton:hover { background-color: white }
                                            QPushButton:!hover { background-color: white }

                                            QPushButton:pressed { background-color: white; }
                                        """)
        self.img1_1.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.img2.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.img2_2.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.img3.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.img2_3.setStyleSheet("""
                                                    QPushButton:hover { background-color: white }
                                                    QPushButton:!hover { background-color: white }

                                                    QPushButton:pressed { background-color: white; }
                                                """)
        self.d_cylinder.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.t_cylinder.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.h_cylinder.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.d_pipe90.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.diam_pipe90.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.t_pipe90.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.d_pipe.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.diam_pipe.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.t_pipe.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))
        self.beta_pipe.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 3))

