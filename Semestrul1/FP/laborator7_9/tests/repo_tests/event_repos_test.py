import unittest

from domain.entities import Event
from domain.validators import EventValidator
from exceptions.exceptions import ValidationException, EventNotFoundException
from repository.event_repo import EventInMemoryRepository, EventInMemoryRepository_file, EventInMemoryInheriatance


class TestCaseEventInMemoryRepo(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = EventInMemoryRepository_file('test_event_repo')

    def test_setup_repo(self):
        from domain.entities import Event
        from datetime import date, time
        test_rep = EventInMemoryRepository()
        e1 = Event(1, date(2020, 1, 5), time(19, 20, 0), 'Descriere')
        e2 = Event(2, date(2000, 9, 2), time(19, 20, 0), 'Descriere')
        e3 = Event(3, date(2001, 2, 24), time(19, 20, 0), 'Descriere')
        e4 = Event(4, date(2005, 6, 20), time(19, 20, 0), 'Descriere')
        e5 = Event(5, date(2020, 6, 15), time(19, 20, 0), 'Descriere')
        e6 = Event(6, date(2010, 8, 4), time(19, 20, 0), 'Descriere')
        e7 = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        e8 = Event(8, date(2019, 7, 30), time(19, 20, 0), 'Descriere')
        test_rep.add_event_list(e1)
        test_rep.add_event_list(e2)
        test_rep.add_event_list(e3)
        test_rep.add_event_list(e4)
        test_rep.add_event_list(e5)
        test_rep.add_event_list(e6)
        test_rep.add_event_list(e7)
        test_rep.add_event_list(e8)
        return test_rep

    def test_add_event_list(self):
        from service.event_service import Event
        from datetime import date, time
        rep = EventInMemoryRepository()

        event = Event(8, date(2019, 7, 30), time(19, 20, 0), 'Descriere')
        rep.add_event_list(event)

        self.assertEqual(rep.get_all_events(), [event])
        event1 = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        rep.add_event_list(event1)

        self.assertEqual(rep.get_all_events(), [event, event1])

    def test_get_all_events(self):
        from domain.entities import Event
        from datetime import date, time
        rep = EventInMemoryRepository()
        event = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        rep.add_event_list(event)

        self.assertEqual(rep.get_all_events(), [event])
        self.assertEqual(len(rep.get_all_events()), 1)
        event1 = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        rep.add_event_list(event1)
        self.assertEqual(len(rep.get_all_events()), 2)
        self.assertEqual(rep.get_all_events(), [event, event1])

    def test_size(self):
        repo = self.test_setup_repo()
        self.assertEqual(repo.size_events(), 8)

    def test_find_id(self):
        repo = self.test_setup_repo()
        t1 = repo.find_id(9)
        self.assertEqual(t1, -1)
        t2 = repo.find_id(8)
        self.assertEqual(t2, 7)

    def test_find_event(self):
        from datetime import date, time

        repo = self.test_setup_repo()

        t1 = repo.find_event(4)
        self.assertEqual(t1.getIDe(), 4)
        self.assertEqual(t1.getDate(), date(2005, 6, 20))
        self.assertEqual(t1.getTime(), time(19, 20, 0))
        self.assertEqual(t1.getDescription(), 'Descriere')
        t2 = repo.find_event(9)
        self.assertEqual(t2, None)

    def test_find_event_recursively(self):
        from datetime import date, time
        repo = self.test_setup_repo()
        e1 = Event(1, date(2020, 1, 5), time(19, 20, 0), 'Descriere')
        all_events = repo.get_all_events()
        long = repo.size_events()

        searched_event = repo.find_event_recursively(all_events, 1, long-1)
        self.assertEqual(searched_event, e1)

    def test_delete_all(self):
        repo = self.test_setup_repo()
        self.assertEqual(repo.size_events(), 8)
        repo.delete_all_events()
        self.assertEqual(repo.size_events(), 0)

        repo1 = EventInMemoryRepository()
        self.assertEqual(repo1.size_events(), 0)
        repo1.delete_all_events()
        self.assertEqual(repo1.size_events(), 0)

    def test_delete_event(self):
        from datetime import date, time
        repo = self.test_setup_repo()
        deleted_event = repo.delete_event(1)
        self.assertEqual(deleted_event.getIDe(), 1)
        self.assertEqual(deleted_event.getDate(), date(2020, 1, 5))
        self.assertEqual(deleted_event.getTime(), time(19, 20, 0))
        self.assertEqual(deleted_event.getDescription(), 'Descriere')

        self.assertRaises(EventNotFoundException, self._repo.delete_event, 9)

    def test_modify_event(self):
        from domain.entities import Event
        from datetime import date, time

        repo = self.test_setup_repo()
        e = Event(1, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        self.assertEqual(e, repo.modify_event(1, e))
        self.assertRaises(EventNotFoundException, repo.modify_event, 12, e)


class TestCaseEventInMemoryRepo_File(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = EventInMemoryInheriatance('test_event_repo')

    def test_setup_repo(self):
        from domain.entities import Event
        from datetime import date, time
        test_rep = self.__repo
        e1 = Event(1, date(2020, 1, 5), time(19, 20, 0), 'Descriere')
        e2 = Event(2, date(2000, 9, 2), time(19, 20, 0), 'Descriere')
        e3 = Event(3, date(2001, 2, 24), time(19, 20, 0), 'Descriere')
        e4 = Event(4, date(2005, 6, 20), time(19, 20, 0), 'Descriere')
        e5 = Event(5, date(2020, 6, 15), time(19, 20, 0), 'Descriere')
        e6 = Event(6, date(2010, 8, 4), time(19, 20, 0), 'Descriere')
        e7 = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        e8 = Event(8, date(2019, 7, 30), time(19, 20, 0), 'Descriere')
        test_rep.add_event_list(e1)
        test_rep.add_event_list(e2)
        test_rep.add_event_list(e3)
        test_rep.add_event_list(e4)
        test_rep.add_event_list(e5)
        test_rep.add_event_list(e6)
        test_rep.add_event_list(e7)
        test_rep.add_event_list(e8)
        return test_rep

    def test_add_event_list(self):
        from service.event_service import Event
        from datetime import date, time
        event = Event(8, date(2019, 7, 30), time(19, 20, 0), 'Descriere')
        self.__repo.add_event_list(event)

        self.assertEqual(self.__repo.get_all_events(), [event])
        event1 = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        self.__repo.add_event_list(event1)

        self.assertEqual(self.__repo.get_all_events(), [event, event1])

    def test_get_all_events(self):
        from domain.entities import Event
        from datetime import date, time
        event = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        repo = self.__repo
        repo.add_event_list(event)

        self.assertEqual(repo.get_all_events(), [event])
        self.assertEqual(len(repo.get_all_events()), 1)
        event1 = Event(7, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        repo.add_event_list(event1)
        self.assertEqual(len(repo.get_all_events()), 2)
        self.assertEqual(repo.get_all_events(), [event, event1])

    def test_size(self):
        repo = self.test_setup_repo()
        self.assertEqual(repo.size_events(), 8)

    def test_find_id(self):
        repo = self.test_setup_repo()
        t1 = repo.find_id(9)
        self.assertEqual(t1, -1)
        t2 = repo.find_id(8)
        self.assertEqual(t2, 7)

    def test_find_event(self):
        from datetime import date, time

        repo = self.test_setup_repo()

        t1 = repo.find_event(4)
        self.assertEqual(t1.getIDe(), 4)
        self.assertEqual(t1.getDate(), date(2005, 6, 20))
        self.assertEqual(t1.getTime(), time(19, 20, 0))
        self.assertEqual(t1.getDescription(), 'Descriere')
        t2 = repo.find_event(9)
        self.assertEqual(t2, None)

    def test_delete_all(self):
        repo = self.test_setup_repo()
        self.assertEqual(repo.size_events(), 8)
        repo.delete_all_events()
        self.assertEqual(repo.size_events(), 0)

        repo1 = EventInMemoryRepository()
        self.assertEqual(repo1.size_events(), 0)
        repo1.delete_all_events()
        self.assertEqual(repo1.size_events(), 0)

    def test_delete_event(self):
        from datetime import date, time
        repo = self.test_setup_repo()
        deleted_event = repo.delete_event(1)
        self.assertEqual(deleted_event.getIDe(), 1)
        self.assertEqual(deleted_event.getDate(), date(2020, 1, 5))
        self.assertEqual(deleted_event.getTime(), time(19, 20, 0))
        self.assertEqual(deleted_event.getDescription(), 'Descriere')
        self.assertRaises(EventNotFoundException, repo.delete_event,9)

    def test_modify_event(self):
        from domain.entities import Event
        from datetime import date, time

        repo = self.test_setup_repo()
        e = Event(1, date(2018, 12, 1), time(19, 20, 0), 'Descriere')
        self.assertEqual(e, repo.modify_event(1, e))

        self.assertRaises(EventNotFoundException, repo.modify_event,12, e)


    def tearDown(self) -> None:
        self.__repo.delete_all_events()


if __name__ == '__main__':
    unittest.main()
