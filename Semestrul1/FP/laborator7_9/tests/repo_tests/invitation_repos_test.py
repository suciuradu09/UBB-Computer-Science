import unittest
from domain.entities import Invitatie
from domain.validators import PersonValidator, EventValidator
from exceptions.exceptions import ValidationException
from repository.person_event_repo import InvitationRepoMemory, InvitationRepoMemory_file
from repository.person_repo import PersonInMemoryRepository
from repository.event_repo import EventInMemoryRepository
from service.person_service import PersonService
from service.event_service import EventService
from service.person_event_service import InvitationService

class TestCaseInviationRepoMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InvitationRepoMemory()

    def test_get_all(self):
        from datetime import date, time
        test_repo_i = InvitationRepoMemory()
        test_repo_p = PersonInMemoryRepository()
        test_val_p = PersonValidator()
        test_serv_p = PersonService(test_repo_p, test_val_p)
        test_repo_e = EventInMemoryRepository()
        test_val_e = EventValidator()
        test_serv_e = EventService(test_repo_e, test_val_e)

        service = InvitationService(test_repo_i, test_repo_p, test_repo_e)

        p1 = test_serv_p.create_person(1, 'Adi', 'Adresa1')
        p2 = test_serv_p.create_person(2, 'Marius', 'Adresa2')

        e1 = test_serv_e.create_event(1, date(2021, 9, 2), time(2, 2, 1), 'Spectacol1')
        e2 = test_serv_e.create_event(2, date(2021, 9, 2), time(2, 2, 1), 'Spectacol2')
        service.add_invite(1, 1)
        service.add_invite(2, 1)

        service.add_invite(1, 2)

        i = 0
        for el in service.get_all():
            if i == 0:
                assert (el.getIDi == 1)
            elif i == 1:
                assert (el.getIDi == 2)

class TestCaseInviationRepoMemory_file(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InvitationRepoMemory_file('test_invitation_repo')

    def test_get_all(self):
        from datetime import date, time
        test_repo_i = InvitationRepoMemory()
        test_repo_p = PersonInMemoryRepository()
        test_val_p = PersonValidator()
        test_serv_p = PersonService(test_repo_p, test_val_p)
        test_repo_e = EventInMemoryRepository()
        test_val_e = EventValidator()
        test_serv_e = EventService(test_repo_e, test_val_e)
        service = InvitationService(test_repo_i, test_repo_p, test_repo_e)

        p1 = test_serv_p.create_person(1, 'Adi', 'Adresa1')
        p2 = test_serv_p.create_person(2, 'Marius', 'Adresa2')

        e1 = test_serv_e.create_event(1, date(2021, 9, 2), time(2, 2, 1), 'Spectacol1')
        e2 = test_serv_e.create_event(2, date(2021, 9, 2), time(2, 2, 1), 'Spectacol2')
        service.add_invite(1, 1)
        service.add_invite(2, 1)

        service.add_invite(1, 2)

        i = 0
        for el in service.get_all():
            if i == 0:
                assert (el.getIDi == 1)
            elif i == 1:
                assert (el.getIDi == 2)


if __name__ == '__main__':
    unittest.main()
