import unittest

from domain.validators import PersonValidator
from exceptions.exceptions import ValidationException, PersonNotFoundException
from repository.person_repo import PersonInMemoryRepository
from service.person_service import PersonService
from domain.entities import Event

class TestCasePersonService(unittest.TestCase):
    def setUp(self) -> None:
        repo = PersonInMemoryRepository()
        val = PersonValidator()
        self.__person_serv = PersonService(repo, val)

    def test_get_most_popular(self):
        from datetime import date, time
        test_repo = PersonInMemoryRepository()
        test_val = PersonValidator()

        test_srv = PersonService(test_repo, test_val)

        event1 = Event(1, date(2020, 12, 3), time(10, 20, 19), 'c')
        event2 = Event(2, date(2020, 12, 1), time(10, 20, 19), 'a')
        event3 = Event(3, date(2020, 12, 2), time(10, 20, 19), 'b')

        person1 = test_srv.create_person(1, 'Radu', 'Adresa1')
        person2 = test_srv.create_person(2, 'Adi', 'Adresa2')

        person1.addEvent(event1)
        person1.addEvent(event2)
        person1.addEvent(event3)

        person2.addEvent(event1)
        person2.addEvent(event2)
        person2.addEvent(event3)

        lista = test_srv.get_most_popular()

        i = 0
        for el in lista:
            if i == 0:
                self.assertEqual(el.getID(), 1)
            elif i == 1:
                self.assertEqual(el.getID(), 2)
            i += 1

    def test_create_person(self):
        test_repo = PersonInMemoryRepository()
        test_val = PersonValidator()

        test_srv = PersonService(test_repo, test_val)

        person = test_srv.create_person(1, 'Adrian', 'Marasti')
        self.assertEqual(person.getID(), 1)
        self.assertEqual(person.getNume(), 'Adrian')
        self.assertEqual(person.getAdress(), 'Marasti')
        self.assertEqual(len(test_srv.get_all_persons()), 1)
        self.assertRaises(ValueError, test_srv.create_person, 1, 'Daniel', 'Cutezantei')
        self.assertRaises(ValidationException, test_srv.create_person, -1, 'Ana', 'Pandurilor')


    def test_delete_person(self):
        test_repo = PersonInMemoryRepository()
        test_val = PersonValidator()

        test_srv = PersonService(test_repo, test_val)

        person1 = test_srv.create_person(1, 'Adrian', 'Marasti')
        person2 = test_srv.create_person(2, 'Marius', 'Unirii')

        all = test_srv.get_all_persons()

        self.assertEqual(all, [person1, person2])

        test_srv.delete_person(1)

        self.assertEqual(all, [person2])

        test_srv.delete_person(2)

        self.assertEqual(all, [])
        self.assertRaises(ValueError, test_srv.delete_person, 0)


    def test_modify_person(self):
        test_repo = PersonInMemoryRepository()
        test_val = PersonValidator()

        test_srv = PersonService(test_repo, test_val)

        person1 = test_srv.create_person(1, 'Adi', 'Unirii')
        person2 = test_srv.create_person(2, 'Radu', 'Aleea')
        person3 = test_srv.create_person(3, 'Marius', 'Floresti')
        all_persons = test_srv.get_all_persons()
        self.assertEqual(all_persons, [person1, person2, person3])

        p1 = test_srv.modify_person(1, 'Daniel', 'Reghin')
        self.assertEqual(p1.getNume(), 'Daniel')
        self.assertEqual(p1.getAdress(), 'Reghin')
        self.assertRaises(ValueError, test_srv.modify_person, 5, 'Andrei', 'Selimbar')

    def test_get_all_persons(self):
        test_repo = PersonInMemoryRepository()
        test_val = PersonValidator()

        test_srv = PersonService(test_repo, test_val)

        person = test_srv.create_person(1, 'Adi', 'Unirii')
        person2 = test_srv.create_person(2, 'Radu', 'Aleea')
        person3 = test_srv.create_person(3, 'Marius', 'Floresti')
        all = test_srv.get_all_persons()
        self.assertEqual(len(all), 3)
        self.assertEqual(all[0], person)
        self.assertEqual(all[1], person2)
        self.assertEqual(all[2], person3)

    def test_ordered_event(self):
        from datetime import date, time
        test_repo = PersonInMemoryRepository()
        test_val = PersonValidator()

        test_srv = PersonService(test_repo, test_val)

        event1 = Event(1, date(2020, 12, 3), time(10, 20, 19), 'c')
        event2 = Event(2, date(2020, 12, 1), time(10, 20, 19), 'a')
        event3 = Event(3, date(2020, 12, 2), time(10, 20, 19), 'b')

        person = test_srv.create_person(1, 'Radu', 'Adresa1')
        person.addEvent(event1)
        person.addEvent(event2)
        person.addEvent(event3)

        lista = test_srv.ordered_events(1)

        i = 0
        for el in lista:
            if i == 0:
                self.assertEqual(el.getIDe(), 2)
            elif i == 1:
                self.assertEqual(el.getIDe(), 3)
            elif i == 2:
                self.assertEqual(el.getIDe(), 1)
            i += 1

        test_srv.ordered_events1(1)

        i = 0
        for el in lista:
            if i == 0:
                self.assertEqual(el.getIDe(), 2)
            elif i == 1:
                self.assertEqual(el.getIDe(), 3)
            elif i == 2:
                self.assertEqual(el.getIDe(), 1)
            i += 1


if __name__ == '__main__':
    unittest.main()
