from service.spectacole_serv import spectacoleServ
from repository.spectacole_repo import spectacoleRepo_file
from domain.validator import validator
from ui.controller import Console

val = validator()
repo = spectacoleRepo_file('data/spectacole.txt')

serv = spectacoleServ(repo, val)

ui = Console(serv)
ui.show_ui()
