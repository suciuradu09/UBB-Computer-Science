from domain.entities import Product

class Console:
    def __init__(self, service):
        self._serv = service

    def add_product(self):
        """
        Se intruduc datele produsului care se va adauga in lista
        """
        #try:
        id = int(input("Id: "))
        denumire = input("Denumire: ")
        pret = int(input("Pret: "))
        produs = Product(id, denumire, pret)
        produs_adaugat = self._serv.add_product(produs)
        print("Produsul ", produs_adaugat, " a fost adaugat cu succes")
       # except ValueError:
            #print("Produsul nu a fost adaugat in lista")

    def delete_product(self):
        """
        Sterge produse care contin o cifra introdusa de la tastatura
        in pretul lor
        """
        cifra = int(input("Introduceti cifra: "))
        nr_produse_sterse = self._serv.delete_product(cifra)
        print("Au fost sterse ", nr_produse_sterse, " produse")

    def show_ui(self):
        ok = False
        while not ok:
            print("Comenzi disponibile: add, filter, exit")
            cmd = input("Command >> ").lower()
            if cmd == 'exit':
                ok = True
            elif cmd == 'add':
                self.add_product()
            elif cmd == 'delete':
                self.delete_product()
            else:
                print("Comanda invalida!")