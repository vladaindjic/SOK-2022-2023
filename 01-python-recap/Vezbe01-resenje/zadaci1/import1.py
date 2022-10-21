import zadaci1.funkcije as f
import zadaci1.parametri as p

if __name__ == '__main__':
    rez=f.brojanje_reci(["Proba","import"])
    print(rez)

    rez=f.switch(6)
    print(rez)

    d, s, v=p.prva(20,30)
    p.prikaz(d, s, v)

    d, s, v=p.druga(40, 50 , 60)
    p.prikaz(d, s, v)

    d, s, v=p.treca(duzina=70, visina=80)
    p.prikaz(d, s, v)

