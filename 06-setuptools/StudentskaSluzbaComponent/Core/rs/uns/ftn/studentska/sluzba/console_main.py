import pkg_resources


def console_menu(*args, **kwargs):
    svi_plugini = []
    napravi_opcije(svi_plugini=svi_plugini, *args, **kwargs)
    if len(svi_plugini) == 0:
        print("Nije prepoznati nijedan plugin!")
        return
    greska = False
    poruka = None
    while True:
        print("-----------------------------------")
        if greska:
            print("Uneli ste pogresnu vrednost za opciju")
            greska = False
        if poruka:
            print(poruka)
        print("Izaberite broj opcije:")
        for i, opcija in enumerate(svi_plugini):
            print("{} {} {}".format(i, opcija.identifier(), opcija.name()))
        print("{} za izlaz".format(len(svi_plugini)))
        try:
            izbor = int(input("Unesite redni broj opcije:"))
        except:
            greska = True
            continue
        if izbor == len(svi_plugini):
            return
        elif 0 <= izbor < len(svi_plugini):
            poruka = izabrana_opcija(opcija=svi_plugini[izbor], *args, **kwargs)
        else:
            greska = True


def izabrana_opcija(*args, **kwargs):
    try:
        opcija = kwargs['opcija']
        try:
            fakulteti = kwargs['fakulteti']
            pomocna_lista = opcija.ucitati_fakultete()
            del fakulteti[:]
            fakulteti.extend(pomocna_lista)
            return "Ucitani fakulteti"
        except AttributeError as ea:
            pass
        except Exception as e:
            print("Error: {}".format(e))

        try:
            fakulteti = kwargs['fakulteti']
            return opcija.prikazati_fakultete(fakulteti)
        except AttributeError as ea:
            pass
        except Exception as e:
            print("Error: {}".format(e))

    except:
        pass


def napravi_opcije(*args, **kwargs):
    try:
        svi_plugini = kwargs['svi_plugini']
        try:
            svi_plugini.extend(kwargs['fakultet_ucitavanje'])
        except Exception as e:
            pass
        try:
            svi_plugini.extend(kwargs['fakultet_prikaz'])
        except Exception as e:
            pass
    except:
        pass


def load_plugins(oznaka):
    """
    Dinamicko prepoznavanje plagina na osnovu pripadajuce grupe.
    """
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        # Ucitavanje plagina.
        p = ep.load()
        print("{} {}".format(ep.name, p))
        # instanciranje odgovarajuce klase
        plugin = p()
        plugins.append(plugin)
    return plugins


def main():
    try:
        fakultet_ucitavanje = load_plugins("fakultet.ucitavanje")
        fakultet_prikaz = load_plugins("fakultet.prikaz")

    except Exception as e:
        print("Error: {}".format(e))
        return

    try:
        fakulteti = []
        console_menu(fakultet_ucitavanje=fakultet_ucitavanje,
                     fakultet_prikaz=fakultet_prikaz,
                     fakulteti=fakulteti)

    except Exception as e:
        print("Error: {}".format(e))
        return


if __name__ == '__main__':
    main()
