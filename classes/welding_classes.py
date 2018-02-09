from math import sqrt, ceil


class WeldingFas:

    # Проверка несущей способности сварных швов для крепления через фасонку

    def __init__(self, rop, l, lw, hw, double, nforce = 0):
        self.rop = float(rop)
        self.l = float(l)
        self.lw = float(lw)
        self.hw = float(hw)
        self.nforce = float(nforce)
        self.double = int(double)

    def welding_fas1(self):

        tw = sqrt((self.rop / (0.7 * self.double * self.hw * self.lw)) ** 2 + ((6 * self.rop * self.l)/(0.7 *
                        self.double * self.hw * (self.lw) ** 2) + (self.nforce / (0.7 * self.hw * self.lw))) ** 2)

        return int(ceil(tw))


class WeldingTable:

    # Расчет сварных швов и размеров опорных столиков

    def __init__(self, rop, h2, l1, ryw=1980):
        self.rop = float(rop)
        self.l1 = float(l1)
        self.ryw = ryw
        self.h2 = float(h2)

    def welding_h1(self):

        h1 = self.rop / (2 * 0.7 * self.l1 * self.ryw)

        return round(h1, 1)

    def welding_l2(self):

        l2 = self.rop / (2 * 0.7 * 0.65 * self.h2 * self.ryw)

        return round(l2, 2)


class WeldingFrame:

    # Расчет сварных швов и размеров накладки рамного узла

    def __init__(self, mop, rop, h, t, hw, ryw):
        self.mop = float(mop)
        self.rop = float(rop)
        self.h = float(h)
        self.t = float(t)
        self.hw = float(hw)
        self.ryw = int(ryw)

    def welding_b(self):

        b = self.mop / (self.h * self.rop * self.t)

        return round(b, 2)

    def welding_l(self):

        l = self.mop / (2 * 0.7 * self.h * self.hw * self.ryw)

        return round(l, 2)
