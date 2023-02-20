import unittest
from domain.validator import EventValidator
from repository.event_repo import EventRepo_file
from datetime import date

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._validator = EventValidator()
        self._repo = EventRepo_file('tests/test_file.txt')

    def show_event(self):
        val = self._validator
        repo = self._repo
        day = date.today()
        repo.show_events(day)


if __name__ == '__main__':
    unittest.main()
