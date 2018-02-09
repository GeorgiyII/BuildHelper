import sqlite3
from math import sqrt, ceil


class BoltsNumber:
    """n - усилие действующее на болт
        rbs - Расчетное сопротивление срезу (см.таб. D4 лист 142)
        rbp - Расчетное сопротивление смятию (см. таб. D5 лист 143 с таб. G2 лист 131)
        rbt - Расчетное сопротивление растяжению (см. таб. D4 лист 142)
        ab - площадь поперечного сечения болта (см. таб. D8 лист 144)
        abn - площадь поперечного сечения нетто болта за резьбой (см. таб. D8 let.144)
        db - диаметр болта
        sumtmin - минимальная сумма соединяемых толщин
        ns - количество соединяемых элементов
        jb - коэф. условия роботы болтового соединения (см. таб. 16.4 лист 87)
        jc - коэф. условия работы (см. таб. 5.1)
        jn - коэф. условия работы"""

    def __init__(self, n, rbs, rbp, ab, db, sumtmin, ns, jb=0.9, jc=0.9, jn=0.95):

        self.n = float(n)
        self.rbs = int(rbs) * 10
        self.rbp = int(rbp) * 10
        self.ab = float(ab)
        self.db = (db) / 10
        self.sumtmin = float(sumtmin)
        self.ns = int(ns)
        self.jb = jb
        self.jc = jc
        self.jn = jn

    def formula(self):

        force = []

        # Расчет усилий

        shear = self.rbs * self.ab * self.ns * self.jb * self.jc * self.jn
        crushing = self.rbp * self.db * self.sumtmin * self.jb * self.jc * self.jn

        force.append(int(shear))
        force.append(int(crushing))

        return force

    def number(self):

        # Выбор меньшего значения усилия и округление его до целого значения

        nbt = int(ceil(min(self.formula())))

        # Округление результата в большую сторону

        number = ceil((self.n * self.jn)/nbt)

        return number


class BoltStrength:

    def __init__(self, rop, l, a, n):
        self.rop = float(rop)
        self.l = float(l)
        self.a = float(a)
        self.n = int(n)

    def strength(self):

        Nb = sqrt((self.rop / self.n) ** 2 + ((self.rop * self.l) / self.a) ** 2)

        return int(ceil(Nb))


class BoltBase:

    @staticmethod
    def res_mark():

        # Создание списка с Run и Марками стали

        database = sqlite3.connect('base/norms.db')
        c = database.cursor()

        mark = c.execute('SELECT res_mark.class, res_mark.Run FROM res_mark')

        list_run = []

        for row in mark:
            list_run.append(row)

        database.close()

        return list_run

    @staticmethod
    def res_crushing():

        # Создание списка с Run - class A и BC

        database = sqlite3.connect('base/norms.db')
        c = database.cursor()

        crushing = c.execute('SELECT  res_crushing.Run, res_crushing."class A", res_crushing."class BC" '
                             'FROM res_crushing')
        list_class1 = []

        for row in crushing:
            list_class1.append(row)

        database.close()

        return list_class1

    @staticmethod
    def res_shear():

        # Создание списка с классом болта, Rbs, Rbt

        database = sqlite3.connect('base/norms.db')
        c = database.cursor()

        shear = c.execute('SELECT res_shear_tension.class, res_shear_tension.Rbs, res_shear_tension.Rbt '
                          'FROM res_shear_tension')

        list_class2 = []

        for row in shear:
            list_class2.append(row)

        database.close()

        return list_class2

    @staticmethod
    def area():

        # Создание списка с площадями в заисимости от диаметра

        database = sqlite3.connect('base/norms.db')
        c = database.cursor()

        area = c.execute('SELECT  area.diameter, area.Ab, area.Abn FROM area')

        list_area = []

        for row in area:
            list_area.append(row)

        database.close()

        return list_area
