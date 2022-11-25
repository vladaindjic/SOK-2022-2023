from rs.uns.ftn.studentska.sluzba.services.fakultet import FakultetPrikazBase


class FakultetPrikazObican(FakultetPrikazBase):
    def identifier(self):
        return "FakultetPrikazObican"

    def name(self):
        return "Prikaz samo naziva fakulteta"

    def prikazati_fakultete(self, lista_fakulteta):
        prikaz = "{}\n".format("Naziv")
        for f in lista_fakulteta:
            prikaz += "{}\n".format(f.naziv)
        return prikaz
