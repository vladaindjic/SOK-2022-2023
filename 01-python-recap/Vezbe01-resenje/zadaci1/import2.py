from zadaci1.funkcije import brojanje_reci, switch
from zadaci1.parametri import prikaz, prva, druga, treca

if __name__ == '__main__':
    rez = brojanje_reci(["Proba", "import"])
    print(rez)

    rez = switch(6)
    print(rez)

    d, s, v = prva(20, 30)
    prikaz(d, s, v)

    d, s, v = druga(40, 50, 60)
    prikaz(d, s, v)

    d, s, v = treca(duzina=70, visina=80)
    prikaz(d, s, v)