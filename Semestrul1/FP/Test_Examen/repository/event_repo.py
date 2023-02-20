import token
from datetime import date, time
from domain.entities import Event

class EventRepo_file:
    def __init__(self, filename):
        self._filename = filename

    def load_from_file(self):
        """
        Citeste din fisier toate evenimentele
        """
        events = []
        with open(self._filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data, ora, descriere = [token.strip() for token in line.split(';')]
                data_str = data.split('-')
                data_final = date(int(data_str[0]), int(data_str[1]), int(data_str[2]))
                ora_str = ora.split(':')
                ora_final = time(int(ora_str[0]), int(ora_str[1]), int(ora_str[2]))
                descriere_final = descriere
                event = Event(data_final, ora_final, descriere_final)
                events.append(event)
        return events
    def save_to_file(self, events):
        with open(self._filename, 'w') as f:
            for event in events:
                events_string = str(event.getData()) + ';' + \
                                str(event.getOra()) + ';' + \
                                str(event.getDesc()) + '\n'
                f.write(events_string)

    def add_event(self, event):
        """
        Adauga eveniment in fisier
        :param event: Evenimentul care se adauga
        """
        all_events = self.load_from_file()
        all_events.append(event)
        self.save_to_file(all_events)

    def create(self, filename, sir):
        """
        Creeaza un fisier in care se gasesc toate evenimetele cu descrierea data
        :param filename: numele fisierului creat
        :type filename: strig
        :param sir: sirul cautat in descrieri
        :type sir: string
        """
        try:
            fisier_creat = open(str(filename), 'w')
            fisier_existent = open(self._filename, 'r')
        except:
            raise IOError
        events = []
        lines = fisier_existent.readlines()
        for line in lines:
            data, ora, descriere = [token.strip() for token in line.split(';')]
            data_str = data.split('-')
            data_final = date(int(data_str[0]), int(data_str[1]), int(data_str[2]))
            ora_str = ora.split(':')
            ora_final = time(int(ora_str[0]), int(ora_str[1]), int(ora_str[2]))
            descriere_final = descriere
            event = Event(data_final, ora_final, descriere_final)
            if sir == str(descriere):
                events.append(event)
        sorted_events = sorted(events, key=lambda x: (x.getData(), x.getOra()))
        for event in sorted_events:
            event_string = str(event.getData()) + ';' + str(event.getOra()) + ';' + str(event.getDesc()) + '\n'
            fisier_creat.write(event_string)

    def show_events(self, day):
        """
        Afiseaza toate evenimentule din fisier din data de azi
        :param day: ziua de azi
        """
        all_events = self.load_from_file()
        if len(all_events) == 0:
            raise ValueError("Nu exista evenimente")
        print("Evenimentele din ziua", day, ":")
        all_events_sorted_by_hour = sorted(all_events, key=lambda x: x.getOra())
        for event in all_events_sorted_by_hour:
            if event.getData() == day:
                print(event)
        print('\n')

