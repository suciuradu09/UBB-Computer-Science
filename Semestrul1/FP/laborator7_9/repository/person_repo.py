from domain.entities import Person
from exceptions.exceptions import CorruptedFileException, DuplicateIDException, PersonNotFoundException
from random import *
import random


class PersonInMemoryRepository:
    """
    Clasa responsabila de gestionarea persoanelor
    """
    def __init__(self):
        # persons - persoanele pe care le gestionam
        # am ales sa stochez datele in lista
        # lista: [persona1, persoana2, persoana3]

        self.__persons = []

    def generate_random_id(self):
        """
        Random id generator
        :return: random id between 1000 and 9999
        """
        num = randint(1000, 9999)
        while self.find_person(num):
            num = randint(1000, 9999)
        return num

    def generate_random_person(self):
        """
        generates random person
        :return: random person
        """
        name = ('Andrei', 'Alex', 'Andreea', 'Darius', 'Erich', 'Ioana', 'Vlad', 'Sergiu')
        adresses = ('Unirii', 'Calea Floresti', 'Piezisa', 'Centru', 'Feleac', 'Observator')

        rand_name = random.choice(name)
        rand_adress = random.choice(adresses)
        random_person = Person(self.generate_random_id(), rand_name, rand_adress)
        return random_person

    def find_person(self, id):
        """
        Cauta o persoana cu id-ul dat in lista
        :param id: id-ul dat
        :type id: int
        :return: persoana cautata, None in caz contrar
        :rtype: Person
        """
        for person in self.__persons:
            if person.getID() == id:
                return person
        return None

    def add_person_list(self, person):
        """
        Adauga persoane in lista de persoane
        :param person: persoana adaugata
        :type person: Person
        :return: lista de persoane modificata
        """
        p = self.find_person(person.getID())
        if p is not None:
            raise ValueError('Pesoana cu id-ul cerut exista deja.')
        self.__persons.append(person)

    def get_all_persons(self):
        """
        :return: Returneaza o lista cu persoanele de pe lista
        :rtype: lista personelor
        """
        if self.__persons is None:
            raise ValueError('Nu exista persoane in lista.')
        return self.__persons

    def size_persons(self):
        """
        Returneaza lungimea curenta a listei de persoane
        :return: numarul de persoane din lista
        :rtype: int
        """
        return len(self.__persons)

    def find_id(self, id):
        """
        Returneaza indexul persoanei cautate
        :param id: id-ul cautat
        :type id: int
        :return: indexul persoanei
        :rtype: int (>0)
        """
        index = -1
        for i in range(self.size_persons()):
            if self.__persons[i].getID() == id:
                index = i
        return index

    def find_id_recursively(self, all_persons, id, i):
        """
        Gaseste persoana cu id-ul introdus ca parametru
        :param all_persons: toate persoanele
        :param id: id-ul persoanei cautate
        :param i: index
        :return: Persoana cautata
        """
        if i < 0:
            raise PersonNotFoundException()
        elif all_persons[i].getID() == id:
            return all_persons[i]
        else:
            return self.find_id_recursively(all_persons, id, i-1)

    def delete_person(self, id):
        """
        Sterge persoana dupa id
        :param id: id-ul cautat
        :return: persoana stearsa
        """
        pers_cautata = self.find_person(id)
        if pers_cautata is None:
            raise ValueError('Nu exista persoana cu id-ul cautat.')

        self.__persons.remove(pers_cautata)
        return pers_cautata

    def modify_person(self, id, persoana):
        """
        Modifica o persoana din lista
        :param id: id-ul persoanei cautate
        :type id: int
        :param persoana: persoana cu care se modifica
        :type persoana: Person
        :return: persoana modificata
        """
        p = self.find_person(id)
        if p is None:
            raise ValueError('Persoana cautata nu exista.')
        p.setNume(persoana.getNume())
        p.setAdress(persoana.getAdress())
        return p

    def delete_all_persons(self):
        """
        Sterge toate persoanele din lista
        """
        self.__persons.clear()


class PersonInMemoryRepository_file:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except IOError:
            raise CorruptedFileException()
        persons = []
        lines = f.readlines()
        for line in lines:
            person_id, person_name, person_adress = [token.strip() for token in line.split(';')]
            person_id = int(person_id)
            person = Person(person_id, person_name, person_adress)
            persons.append(person)

        f.close()
        return persons

    def __save_to_file(self, persons_list):
        with open(self.__filename, 'w') as f:
            for person in persons_list:
                persons_string = str(person.getID()) + ';' + \
                                 str(person.getNume()) + ';' + \
                                 str(person.getAdress()) + '\n'
                f.write(persons_string)

    def find_person(self, id):
        all_persons = self.__load_from_file()

        for person in all_persons:
            if person.getID() == id:
                return person
        return None


    def find_id(self, all_persons, id):
        index = -1
        for i in range(0, len(all_persons)):
            if all_persons[i].getID() == id:
                index = i
        return index



    def add_person_list(self, person):
        """
        Adauga persoana in lista
        :param person: persoana care trebuie adaugata
        :type person: Person
        :return: lista de persoane modificata
        :raises: DuplicateIDException
        """
        all_persons = self.__load_from_file()
        if person in all_persons:
            raise DuplicateIDException()

        all_persons.append(person)
        self.__save_to_file(all_persons)

    def modify_person(self, id, persoana):
        """
        Modifica o persoana cautata dupa id
        :param id: id-ul persoanei de modificat
        :param persoana: noua persoana
        :return: lista modificata
        :raises: PersonNotFoundException
        """

        all_persons = self.__load_from_file()
        index = self.find_id(all_persons, id)
        if index == -1:
            raise PersonNotFoundException()

        all_persons[index] = persoana
        self.__save_to_file(all_persons)
        return persoana

    def generate_random_id(self):
        """
        Random id generator
        :return: random id between 1000 and 9999
        """
        num = randint(10000, 99999)
        while self.find_person(num):
            num = randint(10000, 99999)
        return num

    def generate_random_person(self):
        """
        generates random person
        :return: random person
        """
        name = ('Andrei', 'Alex', 'Andreea', 'Darius', 'Erich', 'Ioana', 'Vlad', 'Sergiu')
        adresses = ('Unirii', 'Calea Floresti', 'Piezisa', 'Centru', 'Feleac', 'Observator')

        rand_name = random.choice(name)
        rand_adress = random.choice(adresses)
        random_person = Person(self.generate_random_id(), rand_name, rand_adress)
        return random_person

    def delete_person(self, id):
        """
        Stergem persoana dupa id
        :param id: id-ul persoanei cautate
        :return: lista modificata dupa stergere
        :raises: PersonNotFoundException
        """
        all_persons = self.__load_from_file()
        index = self.find_id(all_persons, id)
        if index == -1:
            raise PersonNotFoundException()

        deleted_person = all_persons.pop(index)
        self.__save_to_file(all_persons)
        return deleted_person

    def size_persons(self):
        all_persons = self.__load_from_file()
        return len(all_persons)

    def delete_all_persons(self):
        self.__save_to_file([])

    def get_all_persons(self):
        return self.__load_from_file()

class PersonInMemoryInheriatance(PersonInMemoryRepository):
    def __init__(self, filename):
        PersonInMemoryRepository.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _load_from_file(self):
        try:
            f = open(self._filename, 'r')
        except IOError:
            raise DuplicateIDException()

        lines = f.readlines()
        for line in lines:
            person_id, person_name, person_adress = [token.strip() for token in line.split(';')]
            person = Person(person_id, person_name, person_adress)

            PersonInMemoryRepository.add_person_list(self, person)
        f.close()

    def _save_to_file(self):
        person_list = PersonInMemoryRepository.get_all_persons(self)
        with open(self._filename, 'w') as f:
            for person in person_list:
                person_string = str(person.getID()) + ';' + \
                                str(person.getNume()) + ';' + \
                                str(person.getAdress()) + '\n'
                f.write(person_string)

    def add_person_list(self, person):
        PersonInMemoryRepository.add_person_list(self, person)
        self._save_to_file()

    def modify_person(self, id, persoana):
        persoana_modif = PersonInMemoryRepository.modify_person(self, id, persoana)
        self._save_to_file()
        return persoana_modif

    def delete_person(self, id):
        deleted_person = PersonInMemoryRepository.delete_person(self, id)
        self._save_to_file()
        return deleted_person

    def find_person(self, id):
        return PersonInMemoryRepository.find_person(self, id)

    def size(self):
        return PersonInMemoryRepository.size_persons(self)

    def delete_all_persons(self):
        PersonInMemoryRepository.delete_all_persons()
        self._save_to_file()

