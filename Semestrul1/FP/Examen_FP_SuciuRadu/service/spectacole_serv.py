
class spectacoleServ:
    def __init__(self, repository, validator):
        self._repo = repository
        self._val = validator

    def add_spectacol(self, spectacol):
        """
        Adauga un spectacol in lista de spectacole din fisier
        :param spectacol: spectacolul care este adaugat
        :return: None
        """
        self._val.validate(spectacol)
        return self._repo.add_spectacol(spectacol)

    def find_spectacol(self, spectacol):
        """
        Cauta un spectacol in lista de spectacole
        :param spectacol: spectacolul cautat
        :return: spectacolul cautat
        """
        return self._repo.find_spectacol(spectacol)

    def modify_spectacol(self, spectacol, new_spectacol):
        """
        Modifica genul si durata unui spectacol specificat
        :param spectacol: spectacolul cautat
        :param new_spectacol: spectacolul cu modificari
        :raises: ValueError daca nu e valid spectacolul cautat
        """
        self._val.validate(spectacol)
        self._val.validate(new_spectacol)
        return self._repo.modify_spectacol(spectacol, new_spectacol)

    def generate_spectacole(self, numarul_de_spectacol_generate):
        """
        Genereaza spectacole aleator si pe pune in fisier
        :param numarul_de_spectacol_generate: obvious
        :return: spectacolele generate
        """
        return self._repo.generate_spectacole(numarul_de_spectacol_generate)

    def export(self, nume_fisier):
        """
        Exporta spectacolele sortate dupa autor si titlu
        :param nume_fisier: Numele fisierului in care se face export
        :return:
        """
        return self._repo.export(nume_fisier)