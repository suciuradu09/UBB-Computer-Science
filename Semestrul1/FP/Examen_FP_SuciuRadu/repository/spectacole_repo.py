from domain.entities import Spectacol
from random import randint

class spectacoleRepo_file:
    def __init__(self, filename):
        self._filename = filename

    def load_from_file(self):
        """
        Citeste spectacolele din fisier
        :return: lista de spectacole
        """
        spectacole = []
        with open(self._filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                titlu, artist, gen, durata = [token.strip() for token in line.split(';')]
                titlu_spectacol = titlu
                artist_spectacol = artist
                gen_spectacol = gen
                durata_spectacol = int(durata)
                spectacol = Spectacol(titlu_spectacol, artist_spectacol, gen_spectacol, durata_spectacol)
                spectacole.append(spectacol)

        return spectacole

    def save_to_file(self, spectacole):
        """
        Scrie o lista de spectacole in fisier
        :param spectacole: spectacolele care se adauga
        :return: None
        """
        with open(self._filename, 'w') as f:
            for spectacol in spectacole:
                spectacole_string = str(spectacol.getTitlu()) + ';' \
                                    + str(spectacol.getArtist()) + ';' \
                                    + str(spectacol.getGen()) + ';' \
                                    + str(spectacol.getDurata()) + '\n'
                f.write(spectacole_string)

    def add_spectacol(self, spectacol):
        """
        Adauga un spectacol in lista de spectacole din fisier
        :param spectacol: spectacolul care este adaugat
        :return: None
        """
        all_spectacole = self.load_from_file()
        all_spectacole.append(spectacol)
        self.save_to_file(all_spectacole)
        return spectacol

    def find_spectacol(self, spectacol):
        """
        Cauta un spectacol in lista de spectacole
        :param spectacol: spectacolul cautat
        :return: pozitia spectacolului cautat, sau -1 in cazul in care nu este gasit
        """
        all_spectacole = self.load_from_file()
        for i in all_spectacole:
            if i == spectacol:
                poz = all_spectacole.index(i)
                return poz
        return -1

    def modify_spectacol(self, spectacol, new_spectacol):
        """
        Modifica genul si durata unui spectacol specificat
        :param spectacol: spectacolul cautat
        :param new_spectacol: spectacolul cu noile modificari
        :raises: ValueError daca nu e valid spectacolul cautat
        """
        all_spectacole = self.load_from_file()
        x = self.find_spectacol(spectacol)
        if x != -1:
            all_spectacole[x] = new_spectacol
            self.save_to_file(all_spectacole)
        else:
            raise ValueError("Spectacolul cautat este inexistent!")

    def generate_spectacole(self, numarul_de_spectacol_generate):
        """
        Genereaza spectacole aleator si pe pune in fisier
        :param numarul_de_spectacol_generate: obvious
        :return: spectacolele generate
        """
        all_spectacole = self.load_from_file()
        genuri = ["Comedie", "Concert", "Balet", "Altele"]
        print("Cele ", numarul_de_spectacol_generate, " spectacole generate random")
        for i in range(numarul_de_spectacol_generate):
            titlu = self.generate_nume()
            artist = self.generate_nume()
            indice_genuri = randint(0, 3)
            gen = genuri[indice_genuri]
            durata = randint(1, 10000)
            spectacol_random = Spectacol(titlu, artist, gen, durata)
            print(spectacol_random)
            all_spectacole.append(spectacol_random)
            self.save_to_file(all_spectacole)

        return all_spectacole

    def export(self, nume_fisier):
        """
        Export intr-ul fisier nou a spectacolelor sortate dupa autor si titlu
        :param nume_fisier: numele fisierului
        """
        all_spectacole = self.load_from_file()
        all_spectacole_sortate = sorted(all_spectacole, key=lambda x: (x.getTitlu(), x.getArtist()))
        with open(nume_fisier, 'x') as f:
            for spectacol in all_spectacole_sortate:
                spectacole_string = str(spectacol.getTitlu()) + ';' \
                                    + str(spectacol.getArtist()) + ';' \
                                    + str(spectacol.getGen()) + ';' \
                                    + str(spectacol.getDurata()) + '\n'
                f.write(spectacole_string)

        return all_spectacole_sortate

    def generate_nume(self):
        """
        Genereaza nume spectacolelor
        :return: numele generate
        """
        alphabet = ['a', 'b', 'c', 'd', 'e',
                    'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
        vocale = ['a', 'e', 'i', 'o', 'u']

        indice_space_random = randint(2, 9)
        ok = False
        while not ok:
            cuvant = ""
            while len(cuvant) < 12:
                indice = randint(0, len(alphabet) - 1)
                litera = alphabet[indice]
                if len(cuvant) == indice_space_random:
                    cuvant = cuvant + ' '

                if litera not in vocale and len(cuvant) < 11:
                    random_indice_vocala = randint(0, 4)
                    cuvant = cuvant + vocale[random_indice_vocala]

                cuvant = cuvant + litera

            for i in range(len(cuvant)):
                if cuvant[i] == " ":
                    return cuvant
        return None
