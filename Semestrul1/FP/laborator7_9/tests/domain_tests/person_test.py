import unittest

from domain.entities import Person
from domain.validators import PersonValidator
from exceptions.exceptions import ValidationException


class TestCasePerson(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = PersonValidator()

    def test_create_person(self):
        p1 = Person(10, 'Alin', 'Muncii')
        self.assertEqual(p1.getID(), 10)
        self.assertEqual(p1.getNume(), 'Alin')
        self.assertEqual(p1.getAdress(), 'Muncii')

        p1.setID(10)
        self.assertEqual(p1.getID(), 10)
        p1.setNume('Marian')
        self.assertEqual(p1.getNume(), 'Marian')
        p1.setAdress('Bahnea')
        self.assertEqual(p1.getAdress(), 'Bahnea')

    def test_equal_id(self):
        p1 = Person(1, 'Darius', 'Rozelor')
        p2 = Person(1, 'Radu', 'Pandurilor')
        self.assertEqual(p1, p2)
        p3 = Person(6, 'Marius', 'Unirii')
        self.assertNotEqual(p1, p3)

    def test_validate_person(self):
        p = Person(1, 'Ana', 'Adress1')
        self.__validator.validate(p)
        p1 = Person(2, '', 'Adress2')
        self.assertRaises(ValidationException, self.__validator.validate, p1)
        p2 = Person(3, 'Andrei', '')
        self.assertRaises(ValidationException, self.__validator.validate, p2)

if __name__ == '__main__':
    unittest.main()
