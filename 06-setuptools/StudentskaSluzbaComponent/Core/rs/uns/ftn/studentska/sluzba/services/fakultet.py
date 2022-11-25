from abc import ABC, abstractmethod


class ServiceBase(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass


class FakultetUcitatiBase(ServiceBase):

    @abstractmethod
    def ucitati_fakultete(self):
        pass


class FakultetPrikazBase(ServiceBase):

    @abstractmethod
    def prikazati_fakultete(self, lista_fakulteta):
        pass
