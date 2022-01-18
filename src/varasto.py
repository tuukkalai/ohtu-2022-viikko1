class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def f10():
        """Cyclomatic complexity over 3"""

        # line too long
        too_long_row = 'This is too long row for pylint. Maximum allowed length for a row is 110 characters, but this exceeds it by 29 characters.'

        # over 20 statements
        print('1')
        print('2')
        print('3')
        print('4')
        print('5')
        print('6')
        print('7')
        print('8')
        print('9')
        print('10')
        print('11')
        print('12')
        print('13')
        print('14')
        print('15')
        print('16')
        print('17')
        print('18')
        print('19')
        print('20')
        print('21')

        # too many nested blocks
        if len(too_long_row) > 10:
            if len(too_long_row) > 30:
                if len(too_long_row) > 90:
                    print('Too long, and too many')

        myint = 2
        if myint == 5:
            return myint
        elif myint == 6:
            return myint
        elif myint == 7:
            return myint
        elif myint == 8:
            return myint
        elif myint == 9:
            return myint
        elif myint == 10:
            if myint == 8:
                while True:
                    return True
            elif myint == 8:
                with myint:
                    return 8
        else:
            if myint == 2:
                return myint
            return myint
        return myint

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
