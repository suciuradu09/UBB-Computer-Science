from ui.console import Console
from repository.bugs_repo import BugsRepo_file
from service.bugs_serv import BugServ
from domain.validator import BugValidator

b_val = BugValidator()
b_repo = BugsRepo_file('data/bugs')
b_serv = BugServ(b_repo, b_val)

ui = Console(b_serv)
ui.show_ui()
