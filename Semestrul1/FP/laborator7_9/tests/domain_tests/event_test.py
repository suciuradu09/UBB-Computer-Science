import unittest

from domain.entities import Event
from domain.validators import EventValidator
from exceptions.exceptions import ValidationException
from datetime import date, time

class TestCaseEvent(unittest.TestCase):
    def setUp(self) -> None:
        self._validator = EventValidator()

    def test_create_event(self):
        from datetime import date, time

        e1 = Event(1, date(2020, 9, 15), time(12, 10, 59), 'Nunta')
        assert (e1.getIDe() == 1)
        assert (e1.getDate() == date(2020, 9, 15))
        assert (e1.getTime() == time(12, 10, 59))
        assert (e1.getDescription() == 'Nunta')

        e1.setIDe(10)
        assert (e1.getIDe() == 10)
        e1.setDate(date(2010, 5, 21))
        assert (e1.getDate() == date(2010, 5, 21))
        e1.setTime(5)
        assert (e1.getTime() == 5)
        e1.setDescription('Spectacol')
        assert (e1.getDescription() == 'Spectacol')

    def test_validate_event(self):
        e = Event(1, date(2020, 9, 15), time(12, 10, 59), 'Nunta')
        self._validator.validate_event(e)
        e1 = Event(2, date(2020, 9, 15), time(12, 10, 59), '')
        self.assertRaises(ValidationException, self._validator.validate_event, e1)
        e2 = Event('', date(2020, 9, 15), time(12, 10, 59), 'Nunta')
        self.assertRaises(ValidationException, self._validator.validate_event, e2)

if __name__ == '__main__':
    unittest.main()
