import unittest
from domain.entities import Person
from domain.validators import PersonValidator
from exceptions.exceptions import ValidationException, PersonNotFoundException
from repository.person_repo import PersonInMemoryRepository, PersonInMemoryInheriatance, PersonInMemoryRepository_file

class TestCasePersonInMemoryRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = PersonInMemoryRepository()
        self.__repo_f = PersonInMemoryRepository_file('test_person_repo')

    def setup_test_repo(self):
        test_rep = PersonInMemoryRepository()
        p1 = Person(1, 'Adi', 'Adresa1')
        p2 = Person(2, 'Ana', 'Adresa2')
        p3 = Person(3, 'Marius', 'Adresa3')
        p4 = Person(4, 'Darius', 'Adresa4')
        p5 = Person(5, 'Cristian', 'Adresa5')
        p6 = Person(6, 'Damian', 'Adresa6')
        p7 = Person(7, 'Alex', 'Adresa7')
        p8 = Person(8, 'Alexia', 'Adresa8')
        test_rep.add_person_list(p1)
        test_rep.add_person_list(p2)
        test_rep.add_person_list(p3)
        test_rep.add_person_list(p4)
        test_rep.add_person_list(p5)
        test_rep.add_person_list(p6)
        test_rep.add_person_list(p7)
        test_rep.add_person_list(p8)
        return test_rep

    def test_add_person_list(self):
        rep = PersonInMemoryRepository()
        person = Person(1, 'Adi', 'Adresa1')
        rep.add_person_list(person)

        self.assertEqual(rep.get_all_persons(), [person])
        person1 = Person(2, 'Ana', 'Adresa2')
        rep.add_person_list(person1)

        self.assertEqual(rep.get_all_persons(), [person, person1])

    def test_get_all_persons(self):
        person = Person(1, 'Adi', 'Adresa1')
        self.__repo.add_person_list(person)

        self.assertEqual(self.__repo.get_all_persons(), [person])
        self.assertEqual(len(self.__repo.get_all_persons()), 1)
        person1 = Person(2, 'Ana', 'Adresa2')
        self.__repo.add_person_list(person1)
        self.assertEqual(len(self.__repo.get_all_persons()), 2)
        self.assertEqual(self.__repo.get_all_persons(), [person, person1])

    def test_size(self):
        self.__repo = self.setup_test_repo()
        self.assertEqual(self.__repo.size_persons(), 8)

    def test_find_id(self):
        t1 = self.__repo.find_id(9)
        self.assertEqual(t1, -1)
        t2 = self.__repo.find_id(8)
        self.assertEqual(t2, -1)

    def test_find_id_recursively(self):
        p1 = Person(1, 'Adi', 'Adresa1')
        p2 = Person(2, 'Ana', 'Adresa2')
        p3 = Person(3, 'Marius', 'Adresa3')
        p4 = Person(4, 'Darius', 'Adresa4')
        self.__repo.add_person_list(p1)
        self.__repo.add_person_list(p2)
        self.__repo.add_person_list(p3)
        self.__repo.add_person_list(p4)

        all = self.__repo.get_all_persons()
        long = self.__repo.size_persons()

        self.assertEqual(self.__repo.find_id_recursively(all, 2, long-1), p2)
        self.assertEqual(self.__repo.find_id_recursively(all, 1, long-1), p1)
        self.assertRaises(PersonNotFoundException, self.__repo.find_id_recursively, all, 5, long-1)
        self.assertRaises(PersonNotFoundException, self.__repo.find_id_recursively, all, -1, long-1)

    def test_find_person(self):
        self.__repo = self.setup_test_repo()
        t1 = self.__repo.find_person(4)
        self.assertEqual(t1.getID(), 4)
        self.assertEqual(t1.getNume(), 'Darius')
        self.assertEqual(t1.getAdress(), 'Adresa4')
        t2 = self.__repo.find_person(9)
        self.assertEqual(t2, None)

    def test_delete_all(self):
        self.assertEqual(self.__repo.size_persons(), 0)
        self.__repo.delete_all_persons()
        self.assertEqual(self.__repo.size_persons(), 0)

        self.assertEqual(self.__repo.size_persons(), 0)
        self.__repo.delete_all_persons()
        self.assertEqual(self.__repo.size_persons(), 0)

    def test_delete_person(self):
        self.__repo = self.setup_test_repo()
        deleted_person = self.__repo.delete_person(1)
        self.assertEqual(deleted_person.getID(), 1)
        self.assertEqual(deleted_person.getNume(), 'Adi')
        self.assertEqual(deleted_person.getAdress(), 'Adresa1')

        self.assertRaises(ValueError, self.__repo.delete_person, 9)

    def test_modify_person(self):
        p1 = Person(1, 'Andrei', 'Adresa10')
        self.assertRaises(ValueError, self.__repo.modify_person, 12, p1)


