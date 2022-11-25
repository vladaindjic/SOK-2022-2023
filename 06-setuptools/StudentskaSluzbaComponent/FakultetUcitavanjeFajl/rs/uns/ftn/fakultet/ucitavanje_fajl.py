import os

from rs.uns.ftn.studentska.sluzba.model import Fakultet
from rs.uns.ftn.studentska.sluzba.services.fakultet import FakultetUcitatiBase


def apsolutnaPutanja(fajl):
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "fajlovi", fajl)


fakultetiTxt = apsolutnaPutanja("fakulteti.txt")


def ucitatiFakultete(fajl):
    fakulteti = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            f = Fakultet()
            f.oznaka = atributi[0]
            f.naziv = atributi[1]
            f.adresa = atributi[2]
            fakulteti.append(f)
    return fakulteti


class FakultetUcitavanjeFajl(FakultetUcitatiBase):
    def identifier(self):
        return "FakultetUcitatiFajl"

    def name(self):
        return "Ucitavanje fakulteta iz fajla"

    def ucitati_fakultete(self):
        return ucitatiFakultete(fakultetiTxt)
