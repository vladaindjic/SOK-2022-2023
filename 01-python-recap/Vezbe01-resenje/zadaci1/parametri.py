def prva(duzina=1, sirina=1, visina=1):
    if duzina <= 0:
        duzina = 1
    if sirina <= 0:
        sirina = 1
    if visina <= 0:
        visina = 1
    return duzina, sirina, visina


def druga(*args):
    try:
        duzina = args[0]
    except:
        duzina = 1
    try:
        sirina = args[1]
    except:
        sirina = 1
    try:
        visina = args[2]
    except:
        visina = 1
    return prva(duzina, sirina, visina)


def treca(**kwargs):
    duzina = kwargs.get("duzina", 1)
    sirina = kwargs.get("sirina", 1)
    visina = kwargs.get("visina", 1)
    return prva(duzina, sirina, visina)


def prikaz(duzina, sirina, visina):
    print("D:{0} S:{1} V:{2}".format(duzina, sirina, visina))


if __name__ == '__main__':
    print("Prva")
    duzina, sirina, visina = prva(10)
    prikaz(duzina, sirina, visina)
    duzina, sirina, visina = prva(20, 30)
    prikaz(duzina, sirina, visina)
    duzina, sirina, visina = prva(40, 50, 60)
    prikaz(duzina, sirina, visina)

    print("Druga")
    duzina, sirina, visina = druga(10)
    prikaz(duzina, sirina, visina)
    duzina, sirina, visina = druga(20, 30)
    prikaz(duzina, sirina, visina)
    duzina, sirina, visina = druga(40, 50, 60)
    prikaz(duzina, sirina, visina)

    print("Treca")
    duzina, sirina, visina = treca(duzina=10)
    prikaz(duzina, sirina, visina)
    duzina, sirina, visina = prva(duzina=20, sirina=30)
    prikaz(duzina, sirina, visina)
    duzina, sirina, visina = prva(duzina=40,
                                  sirina=50,
                                  visina=60)
    prikaz(duzina, sirina, visina)
