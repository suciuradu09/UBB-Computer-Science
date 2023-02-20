from service.event_service import EventService
from datetime import date, time
from domain.entities import Event
import termcolor

class Console:
    def __init__(self, serv):
        self._serv = serv

    def show_events(self, day):
        try:
            self._serv.show_events(day)
        except ValueError as ve:
            print(ve)

    def add_event(self):
        """
        Adaugare eveniment in fisierul cu evenimente
        """
        try:
            year = int(input("Anul: "))
            month = int(input("Luna: "))
            day = int(input("Ziua: "))
            data = date(year, month, day)
            hour = int(input("Ora: "))
            minute = int(input("Minut: "))
            second = 0
            ora = time(hour, minute, second)
            descriere = input("Descriere: ")
            event = Event(data, ora, descriere)
            self._serv.add_event(event)
            print("Evenimentul ", event, " a fost adaugat.")
        except:
            print("Evenimentul nu s-a adaugat, date invalide!")

    def modify_date(self):
        """
        Modifica data la care se afiseaza evenimentele
        """
        year = int(input("Anul: "))
        month = int(input("Luna: "))
        day = int(input("Ziua: "))
        data = date(year, month, day)
        return data

    def create_file(self):
        """
        Creeaza un fisier cu nume introdus de utilizator in care sa se afiseze toate
        evenimentele care contin un sir introdus la tastatura
        """
        filename = input("Numele fisierului: ")
        sir = input("Sir de caractere: ")
        try:
            self._serv.create(filename, sir)
            print("Fisierul ", filename, " a fost creat cu succes")
        except IOError:
            print("Fisierul este corupt")
    def show_ui(self):
        day = date.today() #  afiseaza evenimentele din ziua de azi DONE
        ok = False
        while not ok:
            self.show_events(day)
            print("Command: Add, Modify_date, exit")
            cmd = input("Command >> ")
            if cmd == "Add":
                self.add_event()
            elif cmd == "Modify_date":
                try:
                    day = self.modify_date()
                except:
                    print("Data la care se afiseaza evenimentele nu a fost modificata.")
            elif cmd == "create":
                self.create_file()
            elif cmd == "exit":
                ok = True
            else:
                print("Comanda invalida")
