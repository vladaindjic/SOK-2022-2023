from .funkcije import brojanje_reci, switch
from .parametri import prva, druga, treca, prikaz


#if __name__ == '__main__':
'''Kod se mora nalaziti van ove provere, jer se ovaj modul ne moze koristiti za pokretanje aplikacije,
   posto je za realtivni import potrebno da __name__ atribut ima postavljenu vrednost putanje do trenutnog modula
'''

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