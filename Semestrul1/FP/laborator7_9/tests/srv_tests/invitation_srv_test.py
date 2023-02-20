import unittest
from domain.entities import Invitatie
from service.person_event_service import InvitationService
from repository.person_repo import PersonInMemoryRepository_file
from repository.event_repo import EventInMemoryRepository_file
from repository.person_event_repo import InvitationRepoMemory_file


class TestCaseInvitationService(unittest.TestCase):
    def setUp(self) -> None:
        i_repo = InvitationRepoMemory_file('test_invitation_srv')
        p_repo = PersonInMemoryRepository_file('test_person_srv')
        e_repo = EventInMemoryRepository_file('test_event_srv')
        self.__invitation_serv = InvitationService(i_repo, p_repo, e_repo)

    #TO DO:
    def test_add_invitation(self):
        pass

    def test_get_all(self):
        pass

    
if __name__ == '__main__':
    unittest.main()
