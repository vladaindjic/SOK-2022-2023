def brojanje_reci(lista_reci):
    lista_duzina = []
    for rec in lista_reci:
        lista_duzina.append(len(rec))
    return lista_duzina


def switch(x):
    opcije = {10: "deset",
              9: "devet",
              8: "osam",
              7: "sedam",
              6: "sest"}
    return opcije.get(x, "nije polozeno")


if __name__ == '__main__':
    lista = brojanje_reci(["Dobar", "dan"])
    print(lista)

    ocena = switch(4)
    print(ocena)

    ocena = switch(7)
    print(ocena)
