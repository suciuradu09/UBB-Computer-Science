from ui.controller import Console
from domain.validator import EventValidator
from repository.event_repo import EventRepo_file
from service.event_service import EventService


val = EventValidator()
repo = EventRepo_file('data/events.txt')

serv = EventService(repo, val)

ui = Console(serv)
ui.show_ui()



