from random import *
import random
from domain.entities import Event
from exceptions.exceptions import CorruptedFileException, DuplicateIDException, EventNotFoundException
from datetime import date, time


class EventInMemoryRepository:
    """
    Clasa responsabila de gestionarea evenimentelor
    """

    def __init__(self):
        # events - evenimentele pe care le gestionam
        # am ales sa stochez datele in lista
        # lista: [eveniment1, eveniment2, eveniment3]

        self.__events = []

    def generate_random_id(self):
        """
        Random id generator
        :return: random id between 1000 and 9999
        """
        num = randint(1000, 9999)
        while self.find_event(num):
            num = randint(1000, 9999)
        return num

    def generate_random_event(self):
        """
        generates random person
        :return: random person
        """
        descriptions = (
        'Spectacol', 'Concert', 'Nunta', 'Festival', 'Botez', 'Festivitate', 'Lansare de carte', 'Seminar')

        rand_date = date(randint(1900, 2022), randint(1, 12), randint(0, 30))
        rand_time = time(randint(0, 23), randint(0, 59), randint(0, 59))
        rand_desc = random.choice(descriptions)

        random_event = Event(self.generate_random_id(), rand_date, rand_time, rand_desc)
        return random_event

    def add_event_list(self, event):
        """
        Adauga evenimente in lista de evenimente
        :param event: evenimentul adaugat
        :type event: Event
        :return: lista de evenimente modificata
        """
        self.__events.append(event)

    def get_all_events(self):
        """
        :return: Returneaza o lista cu toate evenimentele
        :rtype: lista evenimentelor
        """
        return self.__events

    def size_events(self):
        """
        Returneaza lungimea curenta a listei de evenimente
        :return: numarul de evenimente din lista
        :rtype: int
        """
        return len(self.__events)

    def find_id(self, id):
        """
        Returneaza indexul evenimentului cautat
        :param id: id-ul cautat
        :type id: int
        :return: indexul evenimentului
        :rtype: int (>0)
        """
        index = -1
        for i in range(self.size_events()):
            if self.__events[i].getIDe() == id:
                index = i
        return index

    def find_event(self, id):
        for event in self.__events:
            if event.getIDe() == id:
                return event
        return None

    def find_event_recursively(self, all_events, id, i):
        """
        Gaseste evenimentul in functie de id
        :param all_events: toate evenimentele
        :param id: id-ul cautat
        :param i: indice
        :return: evenimentul cautat
        :raises: EventNotFoundException
        """
        if i < 0:
            raise EventNotFoundException()
        elif all_events[i].getIDe() == id:
            return all_events[i]
        else:
            return self.find_event_recursively(all_events, id, i - 1)

    def modify_event(self, id, event):
        """
        Modifica eveniment cu id-ul cautat
        :param id: id-ul evenimentului cautat
        :type id: int
        :type event: Event
        :return: eveniment modificat
        :rtype: Event
        """
        e = self.find_event(id)
        if e is None:
            raise EventNotFoundException()
        e.setDate(event.getDate())
        e.setTime(event.getTime())
        e.setDescription(event.getDescription())
        return e

    def delete_event(self, id):
        """
        Sterge eveniment dupa id
        :param id: id-ul cautat
        :return: eveniment stears
        """
        eveniment = self.find_event(id)
        if eveniment is None:
            raise EventNotFoundException()

        self.__events.remove(eveniment)
        return eveniment

    def delete_all_events(self):
        """
        Sterge toate evenimentele din lista
        """
        self.__events.clear()


class EventInMemoryRepository_file:
    def __init__(self, filename):
        self._filename = filename

    def _load_from_file(self):
        try:
            f = open(self._filename, 'r')

        except IOError:
            raise CorruptedFileException()

        events = []
        lines = f.readlines()
        for line in lines:
            event_id, event_date, event_time, event_description = [token.strip() for token in line.split(';')]
            event_id = int(event_id)
            e = Event(event_id, event_date, event_time, event_description)
            events.append(e)
        f.close()
        return events

    def _save_to_file(self, events):
        with open(self._filename, 'w') as f:
            for event in events:
                event_string = str(event.getIDe()) + ';' + \
                               str(event.getDate()) + ';' + \
                               str(event.getTime()) + ';' + \
                               str(event.getDescription()) + '\n'
                f.write(event_string)

    def add_event_list(self, event):
        all_events = self._load_from_file()
        if event in all_events:
            raise DuplicateIDException()

        all_events.append(event)
        self._save_to_file(all_events)

    def find_event(self, id):
        all_events = self._load_from_file()
        for ev in all_events:
            if ev.getIDe() == id:
                return ev
        return None

    def generate_random_id(self):
        """
        Random id generator
        :return: random id between 1000 and 9999
        """
        num = randint(1000, 9999)
        while self.find_event(num):
            num = randint(1000, 9999)
        return num

    def generate_random_event(self):
        """
        generates random person
        :return: random person
        """
        descriptions = (
        'Spectacol', 'Concert', 'Nunta', 'Festival', 'Botez', 'Festivitate', 'Lansare de carte', 'Seminar')

        rand_date = date(randint(1990, 2022), randint(1, 12), randint(1, 31))
        rand_time = time(randint(0, 23), randint(0, 59), randint(0, 59))
        rand_desc = random.choice(descriptions)

        random_event = Event(self.generate_random_id(), rand_date, rand_time, rand_desc)
        return random_event

    def find_event_recursively(self, all_events, id, i):
        """
        Gaseste evenimentul in functie de id
        :param all_events: toate evenimentele
        :param id: id-ul cautat
        :param i: indice
        :return: evenimentul cautat
        :raises: EventNotFoundException
        """
        if i < 0:
            raise EventNotFoundException()
        elif all_events[i].getIDe() == id:
            return all_events[i]
        else:
            return self.find_event_recursively(all_events, id, i - 1)

    def find_id(self, id):
        all_events = self._load_from_file()
        index = -1
        for i in range(0, len(all_events)):
            if id == all_events[i].getIDe():
                index = i
        return index

    def delete_event(self, id):
        all_events = self._load_from_file()
        index = self.find_id(id)
        if index == -1:
            raise EventNotFoundException()

        deleted_event = all_events.pop(index)
        self._save_to_file(all_events)
        return deleted_event

    def modify_event(self, id, event):
        all_events = self._load_from_file()
        index = self.find_id(id)
        if index == -1:
            raise EventNotFoundException()

        all_events[index] = event
        self._save_to_file(all_events)
        return event

    def size_events(self):
        all_events = self._load_from_file()
        return len(all_events)

    def get_all_events(self):
        return self._load_from_file()

    def delete_all_events(self):
        self._save_to_file([])


class EventInMemoryInheriatance(EventInMemoryRepository):
    def __init__(self, filename):
        EventInMemoryRepository.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _load_from_file(self):
        try:
            f = open(self._filename, 'r')
        except IOError:
            raise DuplicateIDException()

        lines = f.readlines()
        for line in lines:
            event_id, event_date, event_time, event_description = [token.strip() for token in line.split(';')]
            event = Event(event_id, event_date, event_time, event_description)
            EventInMemoryRepository.add_event_list(self, event)
        f.close()

    def _save_to_file(self):
        event_list = EventInMemoryRepository.get_all_events(self)
        with open(self._filename, 'w') as f:
            for event in event_list:
                person_string = str(event.getIDe()) + ';' + \
                                str(event.getDate()) + ';' + \
                                str(event.getTime()) + ';' + \
                                str(event.getDescription()) + '\n'
                f.write(person_string)

    def add_person_list(self, event):
        EventInMemoryRepository.add_event_list(self, event)
        self._save_to_file()

    def modify_person(self, id, event):
        event_modif = EventInMemoryRepository.modify_event(self, id, event)
        self._save_to_file()
        return event_modif

    def delete_event(self, id):
        deleted_event = EventInMemoryRepository.delete_event(self, id)
        self._save_to_file()
        return deleted_event

    def find_event(self, id):
        return EventInMemoryRepository.find_event(self, id)

    def size(self):
        return EventInMemoryRepository.size_events(self)

    def delete_all_events(self):
        EventInMemoryRepository.delete_all_events(self)
        self._save_to_file()
