from termcolor import colored
from datetime import date, time
from exceptions.exceptions import ValidationException, PersonNotFoundException, \
    EventNotFoundException, DuplicateIDException



class Console:
    def __init__(self, person_srv, event_srv, person_event_srv):
        self.__person_srv = person_srv
        self.__event_srv = event_srv
        self.__person_event_srv = person_event_srv

    def _print_menu(self):
        print("Alegeti optiunea dorita: ")
        print(colored("Comenzi care lucreaza cu persoane si evenimente", attrs=['bold']))
        print(colored("add person", 'blue'), " - Adaugare persoana")
        print(colored("add event", 'blue'), " - Adaugare eveniment")
        print(colored("delete person", 'blue'), " - Stergere persoana")
        print(colored("delete event", 'blue'), " - Stergere eveniment")
        print(colored("modify person", 'blue'), " - Modifica persoana")
        print(colored("modify event", 'blue'), " - Modifica eveniment")
        print(colored("find person", 'blue'), " - Gaseste persoana dupa ID")
        print(colored("find event", 'blue'), " - Gaseste eveniment dupa ID")
        print(colored("show persons", 'blue'), " - Afiseaza persoanele de pe lista")
        print(colored("show events", 'blue'), " - Afiseaza lista de evenimente")
        print(colored("Comenzi care lucreaza cu persoane inscrise in evenimente", attrs=['bold']))
        print(colored("invite", 'blue'), " - Incriere persoana la eveniment")
        print(colored("ordered event list", 'blue'), " - Evenimentele la care participa persoana, ordonate alfabetic")
        print(colored("most popular", 'blue'), " - Persoanele care participa la cele mai multe evenimente")
        print(colored("top events", 'blue'), " - Primele 20% evenimente cu cei mai multi participanti")
        print(colored("exit", 'blue'), " - Iesire din aplicatie")

    def __show_all_persons(self):
        """
        Afiseaza toate persoanele
        """
        persons = self.__person_srv.get_all_persons()
        if len(persons) == 0:
            print(colored("Nu exista persoane invitate pe lista", 'yellow'))
        else:
            print("Lista de persoane: ")
            for person in persons:
                print('ID: ', colored(person.getID(), 'green'),
                      ' - Nume: ', colored(person.getNume(), 'green'),
                      ' - Adresa: ', colored(person.getAdress(), 'green'))

    def __show_all_events(self):
        events = self.__event_srv.get_all_events()
        if len(events) == 0:
            print(colored("Nu exista evenimente!", 'yellow'))
        else:
            print("Lista de evenimente: ")
            for event in events:
                print('ID: ', colored(event.getIDe(), 'green'),
                      ' - Data: ', colored(event.getDate(), 'green'),
                      ' - Ora: ', colored(event.getTime(), 'green'),
                      ' - Descriere', colored(event.getDescription(), 'green'))

    def __add_person(self):
        """
        adauga o persoana pe lista
        """
        try:
            id = int(input("Id-ul persoanei: ")) # id introddus de utilizator
            nume = input("Numele persoanei: ")
            adresa = input("Adresa persoanei: ")
        except ValueError:
            print(colored("Id-ul trebuie sa fie un numar natural!", 'red'))
            return

        try:
            added_person = self.__person_srv.create_person(id, nume, adresa)
            print(colored('Persona ', 'green'), added_person, colored(' a fost adaugata cu succes', 'green'))
        except DuplicateIDException as ve:
            print(colored(str(ve), 'red'))

    def __add_person_random(self):
        """
        Adauga o persoana random
        """
        try:
            added_person = self.__person_srv.create_person_random()
            print(colored('Persona ', 'green'), added_person, colored(' a fost adaugata cu succes', 'green'))
        except DuplicateIDException as ve:
            print(colored(str(ve), 'red'))


    def __delete_person(self):
        """
        Sterge o persoana din lista
        """
        try:
            id = int(input("Introduceti id-ul persoanei cautate: "))
        except:
            print(colored('Id-ul trebuie sa fie numar intreg.', 'red'))

        try:
            index = self.__person_srv.delete_person(id)  # id-ul persoanei cautate
            print(colored("Persoana cu id-ul: ", 'green'), index, colored(" a fost stearsa", 'green'))
        except PersonNotFoundException as ve:
            print(colored(str(ve), 'red'))

    def __modify_person(self):
        """
        Modifica o persoana din lista
        :return: persoana modificata
        """
        try:
            id_modificat = int(input("Introduceti id-ul persoanei cautate: "))
            nume_modificat = str(input("Introduceti numele noii persoane: "))
            adresa_modificat = str(input("Introduceti adresa noii persoane: "))
            person = self.__person_srv.modify_person(id_modificat,  nume_modificat, adresa_modificat)
            print(colored("Persoana: ", 'green'), person, colored(" a fost modificata", 'green'))
        except PersonNotFoundException as ve:
            print(colored(str(ve), 'red'))

    def __find_person(self):
        """
        Cauta persoana in lista dupa id
        """
        try:
            id = int(input("Introduceti id-ul persoanei cautate: "))
        except:
            print(colored("Id-ul trebuie sa fie numar", 'red'))

        try:
            person = self.__person_srv.find_person(id)
            print(colored("Persoana cautata: ", 'green'), person, colored(" a fost gasita", 'green'))
        except PersonNotFoundException as ve:
            print(colored(str(ve), 'red'))

    def __add_event(self):
        try:
            id = int(input("Id-ul evenimentului: "))
            data = input("Data: ")
            data_string = data.split('-')
            data_int = [int(i) for i in data_string]
            data = date(data_int[0], data_int[1], data_int[2])
            ora = input("Ora: ")
            ora_string = ora.split(':')
            ora_int = [int(i) for i in ora_string]
            timp = time(ora_int[0], ora_int[1], ora_int[2])
            descriere = input("Descriere: ")
        except ValueError as ve:
            print(colored(str(ve), 'red'))
            return

        try:
            added_event = self.__event_srv.create_event(id, data, timp, descriere)
            print(colored('Evenimentul ', 'green'), added_event, colored(' a fost adaugata cu succes', 'green'))
        except DuplicateIDException as ve:
            print(colored(str(ve), 'red'))

    def __add_event_random(self):
        """
        Adauga un eveniment random
        """
        try:
            added_event = self.__event_srv.create_event_random()
            print(colored('Evenimentul', 'green'), added_event, colored(' a fost adaugat cu succes', 'green'))
        except DuplicateIDException as ve:
            print(colored(str(ve), 'red'))

    def __delete_event(self):
        try:
            id = int(input("Id-ul evenimentului: "))
        except ValueError as ve:
            print(colored(str(ve), 'red'))
            return

        try:
            index = self.__event_srv.delete_event(id)  # id-ul evenimentului cautat
            print(colored("Evenimentul cu id-ul: ", 'green'), index, colored(" a fost sters", 'green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))
            return

    def __modify_event(self):
        try:
            id = int(input("Introduceti id-ul evenimentului cautat: "))
            an = int(input("Introduceti anul: "))
            luna = int(input("Introduceti luna: "))
            zi = int(input("Introduceti ziua: "))
            data = date(an, luna, zi) # format YYYY-MM-DD
            ora = int(input("Ora: "))
            minut = int(input("Minut: "))
            secunda = int(input("Secunda: "))
            timp = time(ora, minut, secunda)
            description = input("Introduceti descrierea: ")
            event = self.__event_srv.modify_event(id, data, timp, description)
            print(colored("Evenimentul : ", 'green'), event, colored(" a fost modificat", 'green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __find_event(self):
        """
        Cauta event in lista dupa id
        """
        try:
            id = int(input("Introduceti id-ul evenimentului cautat: "))
        except:
            print(colored("Id-ul trebuie sa fie numar", 'red'))

        try:
            # event = self.__event_srv.find_event(id) # non recursive
            event = self.__event_srv.find_event_recursively(id)
            print(colored("Eveniment cautat: ", 'green'), event, colored(" a fost gasit", 'green'))
        except EventNotFoundException as enfe:
            print(colored(str(enfe), 'red'))


    def __invite(self):
        """
        Inscrie persoane la eveniment
        """
        person_id = int(input("Id persoana: "))
        event_id = int(input("Id eveniment: "))
        try:
            self.__person_event_srv.add_invite(person_id, event_id)
            print('Persoana este inscrisa la eveniment')
        except ValidationException as ve:
            print(colored(str(ve), 'red'))
        except PersonNotFoundException as e:
            print(colored(str(e), 'red'))
        except EventNotFoundException as e:
            print(colored(str(e), 'red'))

    def __ordered_event_list(self):
        """
        Lista de evenimente la care participă o
        persoană ordonat alfabetic după descriere
        """
        try:
            person_id = int(input("Id persoana: "))
            all_desc = self.__person_srv.ordered_events(person_id)
            all_date = self.__person_srv.ordered_events1(person_id)
            print("List ordered by description: ")
            for elem in all_desc:
                print(elem)

            print("List ordered by date: ")
            for elem in all_date:
                print(elem)

        except ValueError as ve:
            print(colored(ve, 'red'))


    def __most_popular(self):
        """ Persoane participante la cele mai multe evenimente """
        try:
            list_of_persons = self.__person_srv.get_most_popular()
            for el in list_of_persons:
                print(el)
        except PersonNotFoundException as pnfe:
            print(str(pnfe), 'red')

    def __top_events(self):
        """
        Primele 20% evenimente cu numar cel mai mare de participanti
        """
        try:
            list_of_events = self.__event_srv.get_top_events()
            for i in list_of_events:
                print("Descrierea evenimentului: ", i.getDescription(), " | Numar participanti: ", len(i.getPersoane()))
        except EventNotFoundException as enfe:
            print(str(enfe), 'red')

    def _show_lista(self):
        all = self.__event_srv.get_all_events()
        for pers in all:
            print(pers.getPersoane())

    def show_ui(self):
        finished = False
        while not finished:
            self._print_menu()
            option = input('Optiunea este: ')
            option = option.lower()
            if option == 'add person':
                self.__add_person()
            elif option == 'add event':
                self.__add_event()
            elif option == 'delete person':
                self.__delete_person()
            elif option == 'modify person':
                self.__modify_person()
            elif option == 'delete event':
                self.__delete_event()
            elif option == 'modify event':
                self.__modify_event()
            elif option == 'find person':
                self.__find_person()
            elif option == 'find event':
                self.__find_event()
            elif option == 'show persons':
                self.__show_all_persons()
            elif option == 'show events':
                self.__show_all_events()
            elif option == 'invite':
                self.__invite()
            elif option == 'ordered event list':
                self.__ordered_event_list()
            elif option == 'most popular':
                self.__most_popular()
            elif option == 'top events':
                self.__top_events()
            elif option == 'exit':
                return
            elif option == '':
                continue
            else:
                print(colored("Optiunea introdusa e invalida!", 'red'))

    def _print_choose(self):
        print(colored("Work with entities: add, delete, modify, find, show + <person/event>", 'blue'))
        print(colored("Work with reports: reports", 'blue'))

    def show_ui1(self):
        finished = False
        while not finished:
            self._print_choose()
            print(colored("exit - close application.", 'red'))
            option = input('Insert command >> ').lower().strip()
            command = option
            if command == 'add':
                cmd = input("person / event >> ").lower()
                if cmd == 'person':
                    self.__add_person()
                elif cmd == 'event':
                    self.__add_event()
                elif cmd == 'person random':
                    self.__add_person_random()
                elif cmd == 'event random':
                    self.__add_event_random()
            elif command == 'delete':
                cmd = input("person / event >> ").lower()
                if cmd == 'person':
                    self.__delete_person()
                elif cmd == 'event':
                    self.__delete_event()
            elif command == 'modify':
                cmd = input("person / event >> ").lower()
                if cmd == 'person':
                    self.__modify_person()
                elif cmd == 'event':
                    self.__modify_event()
            elif command == 'find':
                cmd = input("person / event >> ").lower()
                if cmd == 'person':
                    self.__find_person()
                elif cmd == 'event':
                    self.__find_event()
            elif command == 'show':
                cmd = input("person / event >> ").lower()
                if cmd == 'person':
                    self.__show_all_persons()
                elif cmd == 'event':
                    self.__show_all_events()
            elif command == 'reports':
                print(colored("Available commands: invite, ordered event list, most popular, top events", 'blue'))
                cmd = input("Insert command >> ")
                if cmd == 'invite':
                    self.__invite()
                elif cmd == 'ordered event list':
                    self.__ordered_event_list()
                elif cmd == 'most popular':
                    self.__most_popular()
                elif cmd == 'top events':
                    self.__top_events()
            elif command == 'exit':
                return
            elif command == '':
                continue
            else:
                print(colored("Optiunea introdusa e invalida!", 'red'))
