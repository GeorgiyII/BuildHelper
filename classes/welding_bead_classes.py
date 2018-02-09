

class WeldingBead:

    # Расчет момента инерции и массы сварной двутавровой балки

    def __init__(self, hst, tst, bpol, tpol):
        self.hst = float(hst)
        self.tst = float(tst)
        self.bpol = float(bpol)
        self.tpol = float(tpol)

    def ix_calculate(self):

        ix = (self.tst * (self.hst ** 3)) / 12 + 2 * self.bpol * self.tpol * (((self.hst + self.tpol) / 2) ** 2)

        return int(ix)

    def m_calculate(self):

        m = (((self.hst / 100) * (self.tst / 100)) + ((self.bpol / 100) * (self.tpol / 100)) * 2) * 7850

        return round(m, 1)
