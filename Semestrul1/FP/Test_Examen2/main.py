from service.product_service import productService
from repository.product_repository import productRepo_file
from domain.validator import validator
from ui.controller import Console

repo = productRepo_file('data/produse.txt')
val = validator()

serv = productService(repo, val)

ui = Console(serv)
ui.show_ui()
