import unittest
from repository.event_repo import EventInMemoryRepository
from domain.validators import EventValidator
from service.event_service import EventService
from exceptions.exceptions import EventNotFoundException, ValidationException


class TestCaseEventService(unittest.TestCase):
    def setUp(self) -> None:
        repo = EventInMemoryRepository()
        val = EventValidator()

        self.__event_serv = EventService(repo, val)

    def test_modify_event(self):
        from datetime import date, time
        event1 = self.__event_serv.create_event(1, date(2020, 12, 21), time(12, 1, 1), 'Serbare')
        event2 = self.__event_serv.create_event(2, date(2001, 10, 22), time(12, 1, 1), 'Nunta')
        event3 = self.__event_serv.create_event(3, date(2020, 12, 21), time(12, 1, 1), 'Botez')
        all_events = self.__event_serv.get_all_events()
        self.assertEqual(all_events, [event1, event2, event3])

        p1 = self.__event_serv.modify_event(1, date(2022, 12, 21), time(12, 1, 1), 'Serbare')
        self.assertEqual(p1.getDate(), date(2022, 12, 21))
        self.assertEqual(p1.getTime(), time(12, 1, 1))
        self.assertRaises(EventNotFoundException, self.__event_serv.modify_event, 4, date(2010, 5, 7), time(10, 10, 10),
                          'Cununie')

    def test_get_all_events(self):
        from datetime import time, date
        test_repo = EventInMemoryRepository()
        test_val = EventValidator()

        test_srv = EventService(test_repo, test_val)
        event = test_srv.create_event(23, date(1996, 2, 9), time(10, 19, 29), 'Descriere')
        self.assertEqual(len(test_srv.get_all_events()), 1)
        self.assertEqual(test_srv.get_all_events(), [event])
        event2 = test_srv.create_event(24, date(2005, 10, 19), time(9, 20, 59), 'Descriere')
        self.assertEqual(test_srv.get_all_events(), [event, event2])

    def test_create_event(self):
        from datetime import date, time
        test_repo = EventInMemoryRepository()
        test_val = EventValidator()

        test_srv = EventService(test_repo, test_val)
        event = test_srv.create_event(1, date(2020, 12, 21), time(10, 20, 19), 'Serbare')
        self.assertEqual(event.getIDe(), 1)
        self.assertEqual(event.getDate(), date(2020, 12, 21))
        self.assertEqual(event.getTime(), time(10, 20, 19))
        self.assertEqual(event.getDescription(), 'Serbare')
        self.assertEqual(len(test_srv.get_all_events()), 1)
        self.assertRaises(ValidationException, test_srv.create_event, -1, date(2021, 11, 9), time(12, 9, 1), 'Festival')


if __name__ == '__main__':
    unittest.main()
