from abc import abstractmethod, ABC


class Identifikacija(object):
    def __init__(self, oznaka, opis, **kwargs):
        super().__init__(**kwargs)
        self.oznaka=oznaka
        self.opis=opis

    def __str__(self):
        return "{} {} {} {}".format("identifikacija", self.oznaka,self.opis, super().__str__())

class Dimenzije(object):
    def __init__(self, duzina, sirina, visina, **kwargs):
        super().__init__(**kwargs)
        self.duzina=duzina
        self.sirina=sirina
        self.visina=visina

    @property
    def duzina(self):
        return self.__duzina
    @duzina.setter
    def duzina(self, value):
        if value<=0:
            raise ValueError("Duzina mora biti veca od 0")
        self.__duzina=value

    @property
    def sirina(self):
        return self.__sirina

    @sirina.setter
    def sirina(self, value):
        if value <= 0:
            raise ValueError("Sirina mora biti veca od 0")
        self.__sirina = value

    @property
    def visina(self):
        return self.__visina

    @visina.setter
    def visina(self, value):
        if value <= 0:
            raise ValueError("Visina mora biti veca od 0")
        self.__visina = value

    def __str__(self):
        return "{} {} {} {}".format("deo", self.duzina,self.sirina,self.visina)

class Deo(Identifikacija,Dimenzije):
    def __init__(self, oznaka, opis, duzina, sirina, visina, **kwargs):
        super().__init__(oznaka=oznaka, opis=opis,
                         duzina=duzina, sirina=sirina,
                         visina=visina, **kwargs)
    def __str__(self):
        return "{}".format(super().__str__())

class MehanickiDeo(Deo):
    def __init__(self, oznaka, opis, duzina, sirina, visina, tezina, **kwargs):
        super().__init__(oznaka=oznaka, opis=opis,
                         duzina=duzina, sirina=sirina,
                         visina=visina, **kwargs)
        self.tezina=tezina

    def __str__(self):
        return "{} {}".format(super().__str__(),self.tezina)

class ElektricniDeo(Deo,ABC):
    def __init__(self, oznaka, opis, duzina, sirina, visina, **kwargs):
        super().__init__(oznaka=oznaka, opis=opis,
                         duzina=duzina, sirina=sirina,
                         visina=visina, **kwargs)
    @abstractmethod
    def elektricna_potrosnja(self):
        pass
    def __str__(self):
        return "{}".format(super().__str__())
class Okvir(MehanickiDeo):
    def __init__(self, oznaka, opis, duzina, sirina, visina, tezina, tip_materijala, **kwargs):
        super().__init__(oznaka=oznaka, opis=opis,
                         duzina=duzina, sirina=sirina,
                         visina=visina, tezina=tezina, **kwargs)
        self.tip_materijala=tip_materijala

    def __str__(self):
        return "{} {}".format(super().__str__(), self.tip_materijala)

class Motor(MehanickiDeo,ElektricniDeo):
    def __init__(self,oznaka, opis, duzina, sirina, visina, tezina,
                 vreme_rada, obrtaja_u_minuti, potrosnja_po_obtrtaju,
                 **kwargs):
        super().__init__(oznaka=oznaka, opis=opis,
                         duzina=duzina, sirina=sirina,
                         visina=visina, tezina=tezina,
                         **kwargs)
        self.vreme_rada=vreme_rada
        self.obrtaja_u_minuti=obrtaja_u_minuti
        self.potrosnja_po_obrtaju=potrosnja_po_obtrtaju
    def elektricna_potrosnja(self):
        return self.vreme_rada*self.obrtaja_u_minuti*self.potrosnja_po_obrtaju
    def __str__(self):
        return "{} {} {} {}".format(super().__str__(),self.vreme_rada,
                                    self.obrtaja_u_minuti,self.potrosnja_po_obrtaju)

class Senzor(ElektricniDeo):
    def __init__(self, oznaka, opis, duzina, sirina, visina,
                 tip, merna_jedinica, izmerena_vrednost,
                 potrosnja_po_merenju,broj_merenja,**kwargs):
        super().__init__(oznaka=oznaka, opis=opis,
                         duzina=duzina, sirina=sirina,
                         visina=visina,
                         **kwargs)
        self.tip=tip
        self.merna_jedinica=merna_jedinica
        self.izmerena_vrednost=izmerena_vrednost
        self.potrosnja_po_merenju=potrosnja_po_merenju
        self.broj_merenja=broj_merenja

    def elektricna_potrosnja(self):
        return self.potrosnja_po_merenju*self.broj_merenja
    def __str__(self):
        return "{} {} {} {} {} {}".format(super().__str__(),self.tip,self.merna_jedinica,
                                          self.izmerena_vrednost, self.potrosnja_po_merenju,
                                          self.broj_merenja)


