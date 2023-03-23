#1. Creati o clasa la alegere cu 3-4 proprietati encapsulate.

from abc import ABC, abstractmethod


class AsRow(ABC):
    @abstractmethod
    def as_row(self) -> tuple:
        pass


class Elev(AsRow):
    def __init__(self, nume, prenume, punctaj_nota):
        self.nume = nume
        self.prenume = prenume
        self.punctaj_nota = punctaj_nota

    def as_row(self) -> tuple:
        return self.nume, self.prenume, self.punctaj_nota

#2. Adaugati inca o clasa, si faceti-o compatibila cu tabelul de 3 coloane de mai sus

class Produs(AsRow):

    def __init__(self, denumire, descriere, stock):
        self.denumire = denumire
        self.descriere = descriere
        self.stock = stock

    def as_row(self) -> tuple:
        return self.denumire, self.descriere, self.stock



def list_objects(objects):
    for obj in objects:
        print(f'|{obj.as_row()[0]:<25}|{obj.as_row()[1]:^25}|{obj.as_row()[2]:>25}|')


elev = [
    Elev('Voicu','Alexandra', 97),
    Elev('Stanescu','Gabriel', 57),
    Elev('Iuganu','Elena', 67),
    Elev('Blaj','Larisa', 100),
    Elev('Popescu','Florin', 38),
    Produs('Rochie', 'Pe stoc', True),
    Produs('Pantaloni', 'Pe stoc', True),
    Produs('Ghete', 'Lipsa stoc', False),
]
list_objects(elev)