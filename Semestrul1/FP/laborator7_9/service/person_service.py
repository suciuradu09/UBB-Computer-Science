from domain.entities import Person, Event
from domain.validators import PersonValidator
from repository.person_repo import PersonInMemoryRepository
from repository.event_repo import EventInMemoryRepository


class PersonService:
    """
        GRASP Controller
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
    """

    def __init__(self, repo, validator):
        """
        Initializeaza sevice
        :param repo: ajuta la gestionarea listei de persoane
        :type repo: InMemoryRepository
        :param validator: validatorul care verifica persoanele
        :type validator: PersonValidator
        """
        self.__repo = repo
        self.__validator = validator

    def create_person(self, id, nume, adresa):
        """
        Adaugare persoana
        :param id: id-ul persoanei
        :type id: int(>0)
        :param nume: numele persoanei
        :type nume: str
        :param adresa: adresa persoanei
        :type adresa: str
        :return: persoana de adaugat in lista
        :rtype: Person
        :raises: Value Error daca persoana este invalida
        """
        person = Person(id, nume, adresa)
        self.__validator.validate(person)  # Validare persoana
        self.__repo.add_person_list(person)  # Adaugare persoana la lista
        return person

    def create_person_random(self):
        """
        Adaugare persoana
        :return: persoana de adaugat in lista
        :rtype: Person
        :raises: Value Error daca persoana este invalida
        """
        person = self.__repo.generate_random_person()
        self.__validator.validate(person)  # Validare persoana
        self.__repo.add_person_list(person)  # Adaugare persoana la lista
        return person

    def delete_person(self, id):
        """
        Sterge persoana dupa id
        :param id: id-ul persoanei
        :type id: int (>0)
        :return: Persoana stearsa
        :rtype: Person
        :raise: ValueError daca persoana nu exista
        """
        return self.__repo.delete_person(id)

    def modify_person(self, id, nume, adresa):
        """
        Modifica persoana cu id-ul cautat in persoana data
        :param id: id-ul persoanei cautate
        :type id: int
        :param nume: numele noii persoane
        :type nume: str
        :param adresa: adresa noii persoane
        :type adresa: str
        :return: persoana modificata
        :rtype: Person
        """
        person = Person(id, nume, adresa)
        self.__validator.validate(person)  # Validate person
        return self.__repo.modify_person(id, person)

    def find_person(self, id):
        """
        Cauta o persoana dupa id
        :param id: id-ul cautat
        :return: persona cautata
        """
        person = self.__repo.find_person(id)
        if person is None:
            raise ValueError("Id-ul persoanei cautate nu exita in lista.")
        return person

    def get_all_persons(self):
        """
        Returneaza toate persoanele de pe lista
        :rtype: list of Person objects
        """
        return self.__repo.get_all_persons()

    def merge(self, arr1, arr2, key):
        """
        Lipire arr1, arr2 in functie de key
        :param arr1: primul sir
        :param arr2: al doilea sir
        :param key: conditia aplicata
        :return: sirul rezultat
        """
        result = []

        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if key(arr1[i]) > key(arr2[j]):  # reversed
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        result.extend(arr1[i:])
        result.extend(arr2[j:])

        return result

    def merge_sort_with_key(self, my_list, key=lambda x: x):
        """
        MergeSort cu conditie
        :param my_list: lista care trebuie sortata
        :param key: conditia
        :return: lista sortata
        """
        list_length = len(my_list)

        if list_length <= 1:
            return my_list

        middle = list_length // 2

        left = my_list[:middle]
        right = my_list[middle:]

        sorted_left = self.merge_sort_with_key(left, key)
        sorted_right = self.merge_sort_with_key(right, key)

        return self.merge(sorted_left, sorted_right, key)

    def selection_sort_with_key(self, my_list, key=lambda x: x):
        """
        Sortare prin selectie
        :param my_list: lista care trebuie sortata
        :param key: conditia
        :return: lista sortata
        """
        list_length = len(my_list)

        if list_length <= 1:
            return my_list

        for i in range(0, list_length - 1):
            for j in range(i + 1, list_length - 1):
                if key(my_list[i]) > key(my_list[j]):
                    my_list[i], my_list[j] = my_list[j], my_list[i]

        return my_list

    def shake_sort(self, my_list):
        """
        Shake sort
        :param my_list: lista care trebuie sortata
        :return:lista sortata
        """
        for i in range(len(my_list) - 1, 0, -1):
            is_swapped = False

            for j in range(i, 0, -1):
                if my_list[j] < my_list[j - 1]:
                    my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                    is_swapped = True

            for j in range(i):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    is_swapped = True

            if not is_swapped:
                return my_list

    def ordered_events(self, id):
        """
        Cauta persoana dupa id si sorteaza dupa descrierea evenimentelor
        :param id: id persoana cautata
        :return: Evenimentele ordonate la care participa persoana
        """
        persoana_cautata = self.find_person(id)
        all_ev = persoana_cautata.getEvent()
        # all_ev = sorted(all_ev, key=lambda Event: Event.getDescription(), reverse=False)
        all_ev = self.selection_sort_with_key(all_ev, key=lambda x: x.getDescription())
        return all_ev

    def ordered_events1(self, id):
        """
        Cauta persoana dupa id si sorteaza dupa data evenimentelor
        :param id: id persoana cautata
        :return: Evenimentele ordonate la care participa persoana
        """
        persoana_cautata = self.find_person(id)
        all_ev = persoana_cautata.getEvent()
        # all_ev = sorted(all_ev, key=lambda Event: Event.getDate(), reverse=False)
        all_ev = self.selection_sort_with_key(all_ev, key=lambda x: x.getDate())
        return all_ev

    def get_most_popular(self):
        """
        Persoanele care participa la cele mai multe evenimente
        :return:
        """
        list_of_persons = self.__repo.get_all_persons()
        max_events = 0
        for el in list_of_persons:
            max_events = max(len(el.getEvent()), max_events)

        list = []
        for el in list_of_persons:
            if len(el.getEvent()) == max_events and max_events != 0:
                list.append(el)

        return list
