class Zwierze(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def poruszaj_sie(self, x, y):
        self.move_x = x + 1
        self.move_y = y + 1
        return self.move_x, self.move_y

    def wyswietl(self):
        print("Poruszam sie: x: " + str(self.move_x) + " oraz y: " + str(self.move_y))


class Ssak(Zwierze):
    def poruszaj_sie(self, x, y):
        self.idz = Zwierze.poruszaj_sie(self, x, y)
        self.idz_x, self.idz_y = self.idz

    def wyswietl(self):
        print("Idę: x: " + str(self.idz_x) + " oraz y: " + str(self.idz_y))


class Ryba(Zwierze):
    def poruszaj_sie(self, x, y):
        self.plyn = Zwierze.poruszaj_sie(self, x, y)
        self.plyn_x, self.plyn_y = self.plyn

    def wyswietl(self):
        print("Płynę: x: " + str(self.plyn_x) + " oraz y: " + str(self.plyn_y))


class Ptak(Zwierze):
    def poruszaj_sie(self, x, y):
        self.lec = Zwierze.poruszaj_sie(self, x, y)
        self.lec_x, self.lec_y = self.lec

    def wyswietl(self):
        print("Lecę: x: " + str(self.lec_x) + " oraz y: " + str(self.lec_y))


def main():
    zwierzeta = [Zwierze(), Ssak(), Ryba(), Ptak()]
    x = 3
    y = 4
    print("x = " + str(x), " y = " + str(y))
    for zwierze in zwierzeta:
        zwierze.poruszaj_sie(x, y)
        zwierze.wyswietl()
        x = x ** 2
        y = y ** 2


main()
