# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setMinimumSize(QtCore.QSize(500, 450))
        MainWindow.setMouseTracking(False)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boltsNumber = QtWidgets.QPushButton(self.centralwidget)
        self.boltsNumber.setGeometry(QtCore.QRect(40, 40, 131, 111))
        self.boltsNumber.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../2501917-2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boltsNumber.setIcon(QtGui.QIcon('image/main/1.png'))
        self.boltsNumber.setIconSize(QtCore.QSize(130, 130))
        self.boltsNumber.setObjectName("boltsNumber")
        self.welding_fas1 = QtWidgets.QPushButton(self.centralwidget)
        self.welding_fas1.setGeometry(QtCore.QRect(180, 40, 131, 111))
        self.welding_fas1.setText("")
        self.welding_fas1.setIcon(QtGui.QIcon('image/main/2.png'))
        self.welding_fas1.setIconSize(QtCore.QSize(130, 130))
        self.welding_fas1.setObjectName("welding_fas1")
        self.welding_fas2 = QtWidgets.QPushButton(self.centralwidget)
        self.welding_fas2.setGeometry(QtCore.QRect(320, 40, 131, 111))
        self.welding_fas2.setText("")
        self.welding_fas2.setIcon(QtGui.QIcon('image/main/3.png'))
        self.welding_fas2.setIconSize(QtCore.QSize(130, 130))
        self.welding_fas2.setObjectName("welding_fas2")
        self.welding_table1 = QtWidgets.QPushButton(self.centralwidget)
        self.welding_table1.setGeometry(QtCore.QRect(40, 160, 131, 111))
        self.welding_table1.setText("")
        self.welding_table1.setIcon(QtGui.QIcon('image/main/4.png'))
        self.welding_table1.setIconSize(QtCore.QSize(125, 125))
        self.welding_table1.setObjectName("welding_table1")
        self.welding_fas3 = QtWidgets.QPushButton(self.centralwidget)
        self.welding_fas3.setGeometry(QtCore.QRect(180, 160, 131, 111))
        self.welding_fas3.setText("")
        self.welding_fas3.setIcon(QtGui.QIcon('image/main/5.png'))
        self.welding_fas3.setIconSize(QtCore.QSize(130, 130))
        self.welding_fas3.setObjectName("welding_fas3")
        self.welding_frame = QtWidgets.QPushButton(self.centralwidget)
        self.welding_frame.setGeometry(QtCore.QRect(320, 160, 131, 111))
        self.welding_frame.setText("")
        self.welding_frame.setIcon(QtGui.QIcon('image/main/6.png'))
        self.welding_frame.setIconSize(QtCore.QSize(140, 140))
        self.welding_frame.setObjectName("welding_frame")
        self.welding_table2 = QtWidgets.QPushButton(self.centralwidget)
        self.welding_table2.setGeometry(QtCore.QRect(40, 280, 131, 111))
        self.welding_table2.setText("")
        self.welding_table2.setIcon(QtGui.QIcon('image/main/7.png'))
        self.welding_table2.setIconSize(QtCore.QSize(120, 120))
        self.welding_table2.setObjectName("welding_table2")
        self.section = QtWidgets.QPushButton(self.centralwidget)
        self.section.setGeometry(QtCore.QRect(180, 280, 131, 111))
        self.section.setText("")
        self.section.setIcon(QtGui.QIcon('image/main/8.png'))
        self.section.setIconSize(QtCore.QSize(130, 130))
        self.section.setObjectName("section")
        self.scan = QtWidgets.QPushButton(self.centralwidget)
        self.scan.setGeometry(QtCore.QRect(320, 280, 131, 111))
        self.scan.setText("")
        self.scan.setIcon(QtGui.QIcon('image/main/9.png'))
        self.scan.setIconSize(QtCore.QSize(130, 130))
        self.scan.setObjectName("scan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Помошник строителя"))
        self.boltsNumber.setStyleSheet("""
                    QPushButton:hover { background-color: rgb(228, 228, 228) }
                    QPushButton:!hover { background-color: white }

                    QPushButton:pressed { background-color: rgb(191, 241, 255); }
                """)
        self.boltsNumber.setToolTip("Расчет болтового соединения")
        self.welding_fas1.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.welding_fas1.setToolTip("Расчет сварного соединения через фасонки с балкой")
        self.welding_fas2.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.welding_fas2.setToolTip("Расчет сварного соединения через фасонки с колонной")
        self.welding_fas3.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.welding_fas3.setToolTip("Расчет сварного соединения через фасонки при действии продольной силы")
        self.welding_table1.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.welding_table1.setToolTip("Расчет сварных швов для соединения балок через опорный столик")
        self.welding_table2.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.welding_table2.setToolTip("Расчет сварных швов для соединения балки и колонны через опорный столик")
        self.welding_frame.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.welding_frame.setToolTip("Расчет сварных швов и размеров накладок рамного узла")
        self.section.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.section.setToolTip("Расчет момента инерции и веса сварных двутавровых балок")
        self.scan.setStyleSheet("""
                            QPushButton:hover { background-color: rgb(228, 228, 228) }
                            QPushButton:!hover { background-color: white }

                            QPushButton:pressed { background-color: rgb(191, 241, 255); }
                        """)
        self.scan.setToolTip("Расчет разверток круглых труб")
