from domain.entities import Invitatie, Event, Person
from domain.validators import EventValidator, PersonValidator
from exceptions.exceptions import EventNotFoundException, PersonNotFoundException
from repository.person_event_repo import InvitationRepoMemory
from repository.event_repo import EventInMemoryRepository
from repository.person_repo import PersonInMemoryRepository
from service.event_service import EventService
from service.person_service import PersonService


class InvitationService:
    def __init__(self, inv_repo, person_repo, event_repo):
        self._inv_repo = inv_repo
        self._person_repo = person_repo
        self._event_repo = event_repo

    def add_invite(self, person_id, event_id):
        person = self._person_repo.find_person(person_id)
        if person is None:
            raise PersonNotFoundException()

        event = self._event_repo.find_event(event_id)
        if event is None:
            raise EventNotFoundException()

        invite = Invitatie(person, event)
        self._inv_repo.create_invite(invite)

        self._person_repo.find_person(person_id).addEvent(event.getIDe())
        self._event_repo.find_event(event_id).addPersoane(person.getID())

        return invite

    def get_all(self):
        return self._inv_repo.get_all()



