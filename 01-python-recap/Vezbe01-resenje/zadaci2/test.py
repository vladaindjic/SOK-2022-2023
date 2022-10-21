from zadaci2.model import Okvir, Motor, Senzor, Deo, Identifikacija

if __name__ == '__main__':
    o = Okvir("O1", "Okvir 1", 20, 30, 15, 20, "aluminijum")
    print(o)

    m = Motor("M1", "Motor 1", 2, 3, 1, 10, 30, 40, 500)
    print(m)

    s = Senzor("S1", "Senzor 1", 1, 1, 1, "opticki", "lumens", 30, 300, 40)
    print(s)

    print(Deo.__mro__)
    print(Identifikacija.__mro__)

    d = Deo("oznaka", "opis", 1, 2, 3)
    print(d)
