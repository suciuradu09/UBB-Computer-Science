from domain.validators import PersonValidator, EventValidator
from repository.person_repo import PersonInMemoryRepository, PersonInMemoryRepository_file
from repository.event_repo import EventInMemoryRepository, EventInMemoryRepository_file
from repository.person_event_repo import InvitationRepoMemory_file
from service.person_service import PersonService
from service.event_service import EventService
from service.person_event_service import InvitationService
from ui.console import Console

p_val = PersonValidator()
#p_repo = PersonInMemoryRepository()
p_repo_file = PersonInMemoryRepository_file('data/persons.txt')
p_serv = PersonService(p_repo_file, p_val)

e_val = EventValidator()
#e_repo = EventInMemoryRepository()
e_repo_file = EventInMemoryRepository_file('data/events.txt')
e_serv = EventService(e_repo_file, e_val)


i_repo = InvitationRepoMemory_file('data/invites.txt')
i_serv = InvitationService(i_repo, p_repo_file, e_repo_file)

ui = Console(p_serv, e_serv, i_serv)
ui.show_ui1()
