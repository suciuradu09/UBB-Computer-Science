import unittest
from domain.entities import Person, Event
from domain.validators import PersonValidator, EventValidator
from datetime import date, time

class TestCaseValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.__person_validator = PersonValidator()
        self.__event_validator = EventValidator()

    def person_validator_test(self):
        validator = PersonValidator()
        p1 = Person(1, 'Alin', 'Floresti')
        validator.validate(p1)
        p2 = Person(1, 'Darius', '')
        self.assertRaises(ValueError, validator.validate, p2)
        p3 = Person(10, 'Marian', '')
        self.assertRaises(ValueError, validator.validate, p3)

    def event_validator_test(self):
        validator = EventValidator()
        e1 = Event(-1, date(10, 10, 2021), time(10, 20, 00), 'Spectacol')

        self.assertRaises(ValueError, validator.validate_event, e1)
        e2 = Event(1, date(-1, -1, -1), time(10, 20, 00), 'Spectacol')

        self.assertRaises(ValueError, validator.validate_event, e2)
