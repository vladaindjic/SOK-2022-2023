from zadaci1 import *

if __name__ == '__main__':
    rez = funkcije.brojanje_reci(["Proba", "import"])
    print(rez)

    rez = funkcije.switch(6)
    print(rez)

    d, s, v = parametri.prva(20, 30)
    parametri.prikaz(d, s, v)

    d, s, v = parametri.druga(40, 50, 60)
    parametri.prikaz(d, s, v)

    d, s, v = parametri.treca(duzina=70, visina=80)
    parametri.prikaz(d, s, v)
