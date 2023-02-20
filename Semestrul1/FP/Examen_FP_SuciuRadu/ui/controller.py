from domain.entities import Spectacol
class Console:
    """
    Clasa specifica interfetei utlizatorului
    """
    def __init__(self, service):
        self._serv = service

    def _add_spectacol(self):
        """
        Adaugare spectacol in fisier cu date introduse de la tastatura
        :raises: ValueError daca nu e valid spectacolul introdus
        """
        try:
            titlu = input("Titlu: ")
            artist = input("Artist: ")
            gen = input("Gen: ")
            durata = int(input("Durata:"))
            spectacol = Spectacol(titlu, artist, gen, durata)

            self._serv.add_spectacol(spectacol)
            print("Spectacolul ", spectacol, " a fost adaugat cu succes!")
        except ValueError as ve:
            print(ve)

    def _modify_spectacol(self):
        """
        Modifica genul si durata unui spectacol specificat
        :raises: ValueError daca nu e valid spectacolul cautat
        """
        try:
            print("Introduceti datele spectacolul pe care vreti sa-l modificati:")
            titlu = input("Titlu: ")
            artist = input("Artist: ")
            gen = input("Gen: ")
            durata = int(input("Durata:"))
            spectacol_cautat = Spectacol(titlu, artist, gen, durata)

            print("Introduceti noile informatii pentru spectacol:")
            new_gen = input("Genul: ")
            new_durata = int(input("Durata: "))
            new_spectacol = Spectacol(titlu, artist, new_gen, new_durata)

            self._serv.modify_spectacol(spectacol_cautat, new_spectacol)
            print("Spectacolul a fost modificat cu succes!")
        except ValueError as ve:
            print(ve)

    def _generate_spectacole(self):
        """
        Genereaza spectacole in mod aleator si le tipareste in fisier
        """
        try:
            numarul_de_spectacole_generate = int(input("Numarul de generari: "))
            self._serv.generate_spectacole(numarul_de_spectacole_generate)
        except ValueError as ve:
            print(ve)

    def _export(self):
        """
        Exporta spectacolele sortate dupa autor si titlu
        :param nume_fisier: Numele fisierului in care se face export
        """
        try:
            nume_fisier = input("Introduceti numele fisierului: ")
            self._serv.export(nume_fisier)
        except IOError as io:
            print(io)

    def show_ui(self):
        ok = False
        while not ok:
            print("Comenzi disponibile: add, modify, generate, export_menu exit")
            cmd = input("Comanda >> ").lower()
            if cmd == 'add':
                self._add_spectacol()
            elif cmd == 'modify':
                self._modify_spectacol()
            elif cmd == 'generate':
                self._generate_spectacole()
            elif cmd == 'export_menu':
                x = input("Pentru a exporta fisiere introduceti comanda export: ")
                if x == 'export':
                    self._export()
                else:
                    print("Nu ai introdus export")
            elif cmd == 'exit':
                ok = True
            else:
                print("Comanda introdusa este invalida!")