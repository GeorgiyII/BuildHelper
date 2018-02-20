import sys
from classes import bolts_number_classes, welding_classes, welding_bead_classes, sweep_pipes_classes
from ui.bolts_number import *
from ui.welding1 import *
from ui.welding2 import *
from ui.welding3 import *
from ui.welding4 import *
from ui.welding5 import *
from ui.welding6 import *
from ui.main_ui import *
from ui.section import *
from ui.scan import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Main_menu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.boltsNumber.clicked.connect(self.pushBolts)
        self.ui.welding_fas1.clicked.connect(self.pushFas1)
        self.ui.welding_fas2.clicked.connect(self.pushFas2)
        self.ui.welding_fas3.clicked.connect(self.pushFas3)
        self.ui.welding_table1.clicked.connect(self.pushTable1)
        self.ui.welding_table2.clicked.connect(self.pushTable2)
        self.ui.welding_frame.clicked.connect(self.pushFrame)
        self.ui.section.clicked.connect(self.pushSection)
        self.ui.scan.clicked.connect(self.pushScan)

    def pushBolts(self):
        second = BoltsNumber(self)

    def pushFas1(self):
        second = WeldingFas1(self)

    def pushFas2(self):
        second = WeldingFas2(self)

    def pushFas3(self):
        second = WeldingFas3(self)

    def pushTable1(self):
        second = WeldingTable1(self)

    def pushTable2(self):
        second = WeldingTable2(self)

    def pushFrame(self):
        second = WeldingFrame(self)

    def pushSection(self):
        second = Section(self)

    def pushScan(self):
        second = Scan(self)


class BoltsNumber(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_boltsNumber()
        self.ui.setupUi(self)
        self.rbs = 0
        self.rbp = 0
        self.ab = 0
        self.db = 0
        self.run = 0
        self.base = bolts_number_classes.BoltBase
        self.bolts_number = 0
        self.number = 2

        # Заполнение полей в меню

        list1 = self.base.res_mark()
        for i in list1:
            self.ui.mark.addItem(str(i[0]))

        list2 = ['BC', 'A']
        for i in list2:
            self.ui.accuracy.addItem(str(i))

        list3 = self.base.res_shear()
        for i in list3:
            self.ui.strength.addItem(str(i[0]))

        list4 = self.base.area()
        for i in list4:
            self.ui.diameter.addItem(str(i[0]))

        list5 = [1, 2, 3, 4]
        for i in list5:
            self.ui.number.addItem(str(i))

        # Действие при нажатии кнопки

        self.ui.pushResult.clicked.connect(self.take_result)
        self.ui.pushResult_2.clicked.connect(self.strength)
        self.ui.kgs.setChecked(True)
        self.ui.radioButton.setChecked(True)

        self.show()

    def take_result(self):

        # Сортировка по выбраным пользователем параметрам

        list1 = self.base.res_mark()

        for i in list1:
            if self.ui.mark.currentText() == i[0]:
                self.run = i[1]

        list6 = self.base.res_crushing()
        list2 = ['A', 'BC']

        for i in list6:
            if self.ui.accuracy.currentText() == list2[0]:
                if i[0] == self.run:
                    self.rbp = i[1]
            else:
                if i[0] == self.run:
                    self.rbp = i[2]

        list3 = self.base.res_shear()

        for i in list3:
            if i[0] == self.ui.strength.currentText():
                self.rbs = i[1]

        list4 = self.base.area()

        for i in list4:
            if int(i[0]) == int(self.ui.diameter.currentText()):
                self.ab = i[1]
                self.db = i[0]

        # Вывод результата подсчета с проверкой на пустые поля

        if self.ui.force.text() == '' or self.ui.tmin.text() == '':
            self.ui.result.setText('Error')
        else:
            if self.ui.kH.isChecked():
                self.bolts_number = bolts_number_classes.BoltsNumber(((float(self.ui.force.text().replace(',', '.'))*1000) / 9.81),
                                                                     self.rbs, self.rbp, self.ab, self.db,
                                                                     self.ui.tmin.text().replace(',', '.'),
                                                                     self.ui.number.currentText())
                self.ui.nbt.setText(str(self.bolts_number.formula()[0]) + '' + ',' + ''
                                    + str(self.bolts_number.formula()[1]))
                self.ui.result.setText(str(self.bolts_number.number()))

            elif self.ui.kgs.isChecked():
                self.bolts_number = bolts_number_classes.BoltsNumber(float(self.ui.force.text().replace(',', '.')), self.rbs,
                                                                     self.rbp, self.ab, self.db,
                                                                     self.ui.tmin.text().replace(',', '.'),
                                                                     self.ui.number.currentText())
                self.ui.nbt.setText(str(self.bolts_number.formula()[0]) + ',' + ''
                                    + str(self.bolts_number.formula()[1]))
                self.ui.result.setText(str(self.bolts_number.number()))

    def strength(self):

        # Проверка на нажатие флага

        if self.ui.radioButton.isChecked():
            self.number = 2
        elif self.ui.radioButton_2.isChecked():
            self.number = 3

        # Проверка на пустые поля и вывод результата расчета

        if self.ui.distance_l.text() == '' or self.ui.distance_a.text() == '':
            self.ui.textResult.setText('Error')

        else:
            if self.ui.kH.isChecked():

                self.strength = bolts_number_classes.BoltStrength(((float(self.ui.force.text().replace(',', '.'))*1000) / 9.81),
                                                                  self.ui.distance_l.text().replace(',', '.'),
                                                                  self.ui.distance_a.text().replace(',', '.'),
                                                                  self.number)

                self.ui.nb.setText(str(self.strength.strength()))
                self.ui.textResult.setText('')

            elif self.ui.kgs.isChecked():

                self.strength = bolts_number_classes.BoltStrength(float(self.ui.force.text().replace(',', '.')),
                                                                  self.ui.distance_l.text().replace(',', '.'),
                                                                  self.ui.distance_a.text().replace(',', '.'),
                                                                  self.number)

                self.ui.nb.setText(str(self.strength.strength()))
                self.ui.textResult.setText('')


class WeldingFas1(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_weldingFas1()
        self.ui.setupUi(self)

        self.twofas = 1
        self.ryw = 0
        self.ui.pushResult.clicked.connect(self.welding)
        self.ui.montage.setChecked(True)
        self.ui.kgs.setChecked(True)

        self.show()

    def welding(self):

        # Проверка чекбокса на наличие ответной планки

        if self.ui.double.isChecked():
            self.twofas = 2
        elif not self.ui.double.isChecked():
            self.twofas = 1

        # Определение Ryсв в зависимости от монтажного или заводского шва

        if self.ui.montage.isChecked():
            self.ryw = 1660

        elif self.ui.prefab.isChecked():
            self.ryw = 1980

        # Определение единиц измерения кгс или кН и вывод результата и проверка на незаполненые поля

        if self.ui.rop.text() == '' or self.ui.force_l.text() == '' or self.ui.weld_l.text() == '' or self.ui.weld_k.text() == '':
            self.ui.result.setText('Error')

        else:
            if self.ui.kn.isChecked():
                Tw = welding_classes.WeldingFas((float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81), self.ui.force_l.text().replace(',', '.'),
                                                self.ui.weld_l.text().replace(',', '.'),
                                                self.ui.weld_k.text().replace(',', '.'), self.twofas)
                self.ui.result.setText(str(Tw.welding_fas1()))
                self.ui.ry_resist.setText(str(self.ryw))

            elif self.ui.kgs.isChecked():
                Tw = welding_classes.WeldingFas(self.ui.rop.text().replace(',', '.'), self.ui.force_l.text().replace(',', '.'),
                                                self.ui.weld_l.text().replace(',', '.'),
                                                self.ui.weld_k.text().replace(',', '.'), self.twofas)
                self.ui.result.setText(str(Tw.welding_fas1()))
                self.ui.ry_resist.setText(str(self.ryw))


class WeldingFas2(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_weldingFas2()
        self.ui.setupUi(self)

        self.twofas = 1
        self.ryw = 0
        self.ui.pushResult.clicked.connect(self.welding)
        self.ui.montage.setChecked(True)
        self.ui.kgs.setChecked(True)

        self.show()

    def welding(self):

        # Проверка чекбокса на наличие ответной планки

        if self.ui.double.isChecked():
            self.twofas = 2
        elif not self.ui.double.isChecked():
            self.twofas = 1

        # Определение Ryсв в зависимости от монтажного или заводского шва

        if self.ui.montage.isChecked():
            self.ryw = 1660

        elif self.ui.prefab.isChecked():
            self.ryw = 1980

        # Определение единиц измерения кгс или кН и вывод результата и проверка на заполненые поля

        if self.ui.rop.text() == '' or self.ui.force_l.text() == '' or self.ui.weld_l.text() == '' or self.ui.weld_k.text() == '':
            self.ui.result.setText('Error')
        else:
            if self.ui.kn.isChecked():
                Tw = welding_classes.WeldingFas((float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81),
                                                self.ui.force_l.text().replace(',', '.'),
                                                self.ui.weld_l.text().replace(',', '.'),
                                                self.ui.weld_k.text().replace(',', '.'), self.twofas)
                self.ui.result.setText(str(Tw.welding_fas1()))
                self.ui.ry_resist.setText(str(self.ryw))

            elif self.ui.kgs.isChecked():
                Tw = welding_classes.WeldingFas(self.ui.rop.text().replace(',', '.'),
                                                self.ui.force_l.text().replace(',', '.'),
                                                self.ui.weld_l.text().replace(',', '.'),
                                                self.ui.weld_k.text().replace(',', '.'), self.twofas)
                self.ui.result.setText(str(Tw.welding_fas1()))
                self.ui.ry_resist.setText(str(self.ryw))


class WeldingFas3(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_weldingFas3()
        self.ui.setupUi(self)

        self.twofas = 1
        self.ryw = 0
        self.ui.pushResult.clicked.connect(self.welding)
        self.ui.montage.setChecked(True)
        self.ui.kgs.setChecked(True)

        self.show()

    def welding(self):

        # Проверка чекбокса на наличие ответной планки

        if self.ui.double.isChecked():
            self.twofas = 2
        elif not self.ui.double.isChecked():
            self.twofas = 1

        # Определение Ryсв в зависимости от монтажного или заводского шва

        if self.ui.montage.isChecked():
            self.ryw = 1660

        elif self.ui.prefab.isChecked():
            self.ryw = 1980

        # Определение единиц измерения кгс или кН и вывод результата и проверка на заполненые поля

        if self.ui.rop.text() == '' or self.ui.force_l.text() == '' or self.ui.weld_l.text() == '' or self.ui.weld_k.text() == '' or self.ui.nop == '':
            self.ui.result.setText('Error')
        else:
            if self.ui.kn.isChecked():
                Tw = welding_classes.WeldingFas((float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81),
                                                self.ui.force_l.text().replace(',', '.'),
                                                self.ui.weld_l.text().replace(',', '.'),
                                                self.ui.weld_k.text().replace(',', '.'), self.twofas,
                                                (float(self.ui.nop.text().replace(',', '.')) * 1000 / 9.81))
                self.ui.result.setText(str(Tw.welding_fas1()))
                self.ui.ry_resist.setText(str(self.ryw))

            elif self.ui.kgs.isChecked():
                Tw = welding_classes.WeldingFas(self.ui.rop.text().replace(',', '.'),
                                                self.ui.force_l.text().replace(',', '.'),
                                                self.ui.weld_l.text().replace(',', '.'),
                                                self.ui.weld_k.text().replace(',', '.'),
                                                self.twofas, self.ui.nop.text().replace(',', '.'))
                self.ui.result.setText(str(Tw.welding_fas1()))
                self.ui.ry_resist.setText(str(self.ryw))


class WeldingTable1(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_weldingTable1()
        self.ui.setupUi(self)

        self.ui.pushResult.clicked.connect(self.welding_l)
        self.ui.pushResult2.clicked.connect(self.welding_h)
        self.ui.kgs.setChecked(True)

        self.show()

    def welding_l(self):

        # Определение единиц измерения кгс или кН и вывод результата и отлов пустых строк

        if self.ui.rop.text() == '' or self.ui.weld_k.text() == '':
            self.ui.result.setText('Error')

        else:
            if self.ui.kn.isChecked():
                table = welding_classes.WeldingTable((float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81),
                                                     self.ui.weld_k.text().replace(',', '.'), 1)
                self.ui.result.setText(str(table.welding_l2()))

            elif self.ui.kgs.isChecked():
                table = welding_classes.WeldingTable(float(self.ui.rop.text().replace(',', '.')),
                                                     self.ui.weld_k.text().replace(',', '.'), 1)
                self.ui.result.setText(str(table.welding_l2()))

    def welding_h(self):

        # Определение единиц измерения кгс или кН и вывод результата и отлов пустых строк

        if self.ui.rop.text() == '' or self.ui.length.text() == '':
            self.ui.result2.setText('Error')

        else:
            if self.ui.kn.isChecked():
                table = welding_classes.WeldingTable((float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81),
                                                     1, self.ui.length.text().replace(',', '.'))
                self.ui.result2.setText(str(table.welding_h1()))

            elif self.ui.kgs.isChecked():
                table = welding_classes.WeldingTable(float(self.ui.rop.text().replace(',', '.')), 1,
                                                     self.ui.length.text().replace(',', '.'))
                self.ui.result2.setText(str(table.welding_h1()))


class WeldingTable2(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_weldingTable2()
        self.ui.setupUi(self)

        self.ui.pushResult.clicked.connect(self.welding_l)
        self.ui.pushResult2.clicked.connect(self.welding_h)
        self.ui.kgs.setChecked(True)

        self.show()

    def welding_l(self):

        # Определение единиц измерения кгс или кН и вывод результата и отлов пустых строк

        if self.ui.rop.text() == '' or self.ui.weld_k.text() == '':
            self.ui.result.setText('Error')

        else:
            if self.ui.kn.isChecked():
                table = welding_classes.WeldingTable((float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81),
                                                     self.ui.weld_k.text().replace(',', '.'), 1)
                self.ui.result.setText(str(table.welding_l2()))

            elif self.ui.kgs.isChecked():
                table = welding_classes.WeldingTable(float(self.ui.rop.text().replace(',', '.')),
                                                     self.ui.weld_k.text().replace(',', '.'), 1)
                self.ui.result.setText(str(table.welding_l2()))

    def welding_h(self):

        # Определение единиц измерения кгс или кН и вывод результата и отлов пустых строк

        if self.ui.rop.text() == '' or self.ui.length.text() == '':
            self.ui.result2.setText('Error')

        else:
            if self.ui.kn.isChecked():
                table = welding_classes.WeldingTable((float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81),
                                                     1, self.ui.length.text().replace(',', '.'))
                self.ui.result2.setText(str(table.welding_h1()))

            elif self.ui.kgs.isChecked():
                table = welding_classes.WeldingTable(float(self.ui.rop.text().replace(',', '.')), 1,
                                                     self.ui.length.text().replace(',', '.'))
                self.ui.result2.setText(str(table.welding_h1()))


class WeldingFrame(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_weldingFrame()
        self.ui.setupUi(self)

        self.ryw = 1660
        self.ui.pushResult.clicked.connect(self.welding)
        self.ui.kgs.setChecked(True)

        self.show()

    def welding(self):

        # Определение единиц измерения кгс или кН и вывод результата и проверка пустых полей

        if self.ui.mom.text() == '' or self.ui.rop.text() == '' or self.ui.height.text() == '' or self.ui.force_l_2.text() == '' or self.ui.weld_k.text() == '':
            self.ui.result_2.setText('Error')
            self.ui.result.setText('Error')
        else:
            if self.ui.kn.isChecked():
                frame = welding_classes.WeldingFrame((float(self.ui.mom.text().replace(',', '.')) * 1000 / 9.81),
                                                     (float(self.ui.rop.text().replace(',', '.')) * 1000 / 9.81),
                                                     self.ui.height.text().replace(',', '.'),
                                                     self.ui.force_l_2.text().replace(',', '.'),
                                                     self.ui.weld_k.text().replace(',', '.'), self.ryw)
                self.ui.result_2.setText(str(frame.welding_b()))
                self.ui.result.setText(str(frame.welding_l()))

            elif self.ui.kgs.isChecked():
                frame = welding_classes.WeldingFrame(self.ui.mom.text().replace(',', '.'),
                                                     float(self.ui.rop.text().replace(',', '.')),
                                                     self.ui.height.text().replace(',', '.'),
                                                     self.ui.force_l_2.text().replace(',', '.'),
                                                     self.ui.weld_k.text().replace(',', '.'), self.ryw)
                self.ui.result_2.setText(str(frame.welding_b()))
                self.ui.result.setText(str(frame.welding_l()))


class Section(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_section()
        self.ui.setupUi(self)

        self.ui.pushResult.clicked.connect(self.calculation)

        self.show()

    def calculation(self):

        # Проверка заполнения полей и вывод результата

        if self.ui.hst.text() == '' or self.ui.tst.text() == '' or self.ui.bpol.text() == '' or self.ui.tpol.text() == '':
            self.ui.result.setText('Error')
            self.ui.result_2.setText('Error')
        else:
            ix_result = welding_bead_classes.WeldingBead(self.ui.hst.text().replace(',', '.'),
                                                         self.ui.tst.text().replace(',', '.'),
                                                         self.ui.bpol.text().replace(',', '.'),
                                                         self.ui.tpol.text().replace(',', '.'))

            self.ui.result.setText(str(ix_result.ix_calculate()))
            self.ui.result_2.setText(str(ix_result.m_calculate()))


class Scan(QtWidgets.QMainWindow):
    def __init__(self, parent=Main_menu):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_scan()
        self.ui.setupUi(self)

        self.ui.pushCylinder.clicked.connect(self.calculation_cylinder)
        self.ui.pushPipe90.clicked.connect(self.calculation_pipe90)
        self.ui.pushPipe.clicked.connect(self.calculation_pipe)


        self.show()

    def calculation_cylinder(self):

        # Очищение списка

        self.ui.listWidget.clear()

        # Получение списка с индексом и значением координаты

        if self.ui.d_cylinder.text() == '' or self.ui.t_cylinder.text() == '' or self.ui.h_cylinder.text() == '':
            self.ui.listWidget.addItem('Нет данных')

        else:
            tab_res = sweep_pipes_classes.SweepCylinder(self.ui.d_cylinder.text().replace(',', '.'),
                                                        self.ui.t_cylinder.text().replace(',', '.'),
                                                        self.ui.h_cylinder.text().replace(',', '.'))

            # Заполнение полей виджета

            for i in tab_res.cylinder():
                self.ui.listWidget.addItem('{} - {}'.format(i[0], i[1]))

    def calculation_pipe90(self):

        # Очищение списка

        self.ui.listWidget.clear()

        # Получение списка с индексом и значением координаты

        if self.ui.d_pipe90.text() == '' or self.ui.t_pipe90.text() == '' or self.ui.diam_pipe90.text() == '':
            self.ui.listWidget.addItem('Нет данных')

        else:
            if float(self.ui.d_pipe90.text().replace(',', '.')) <= float(self.ui.diam_pipe90.text().replace(',', '.')):

                tab_res = sweep_pipes_classes.SweepPipes(self.ui.d_pipe90.text().replace(',', '.'),
                                                         self.ui.t_pipe90.text().replace(',', '.'),
                                                         self.ui.diam_pipe90.text().replace(',', '.'), 0)

            # Заполнение полей виджета

                for i in tab_res.pipe_90():
                    self.ui.listWidget.addItem('{} - {}'.format(i[0], i[1]))
            else:
                self.ui.listWidget.addItem('Error')

    def calculation_pipe(self):

        # Очищение списка

        self.ui.listWidget.clear()

        # Получение списка с индексом и значением координаты

        if self.ui.d_pipe.text() == '' or self.ui.t_pipe.text() == '' or self.ui.diam_pipe.text() == '' or self.ui.beta_pipe.text() == '':
            self.ui.listWidget.addItem('Нет данных')

        else:
            if float(self.ui.d_pipe.text().replace(',', '.')) <= float(self.ui.diam_pipe.text().replace(',', '.')):
                tab_res = sweep_pipes_classes.SweepPipes(self.ui.d_pipe.text().replace(',', '.'),
                                                         self.ui.t_pipe.text().replace(',', '.'),
                                                         self.ui.diam_pipe.text().replace(',', '.'),
                                                         self.ui.beta_pipe.text().replace(',', '.'))

        # Заполнение полей виджета

                for i in tab_res.pipe_beta():
                    self.ui.listWidget.addItem('{} - {}'.format(i[0], i[1]))

            else:
                self.ui.listWidget.addItem('Error')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Main_menu()
    myapp.show()
    sys.exit(app.exec_())
