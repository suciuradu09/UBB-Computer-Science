from domain.entities import Event
from domain.validators import EventValidator
from repository.event_repo import EventInMemoryRepository


class EventService:
    """
        GRASP Controller
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
    """

    def __init__(self, repo, validator):
        """
        Initializeaza sevice
        :param repo: ajuta la gestionarea listei de evenimente
        :type repo: InMemoryRepository
        :param validator: validatorul care verifica evenimentele
        :type validator: EventValidator
        """
        self.__repo = repo
        self.__validator = validator

    def create_event(self, id, data, timp, descriere):
        """
        Adaugare eveniment
        :param id: id-ul evenimentului
        :type id: int(>0)
        :param data: data evenimentului
        :type data: date
        :param timp: dutara evenimentului
        :type timp: time
        :param descriere: descrierea evenimentului
        :type descriere: str
        :return: evenimentul de adaugat in lista
        :rtype: Event
        :raises: Value Error daca evenimetul este invalid
        """
        event = Event(id, data, timp, descriere)
        self.__validator.validate_event(event)  # Validare eveniment
        self.__repo.add_event_list(event)  # Adaugare eveniment la lista
        return event

    def create_event_random(self):
        """
        Adaugare eveniment
        :return: evenimentul de adaugat in lista
        :rtype: Event
        :raises: Value Error daca evenimetul este invalid
        """
        event = self.__repo.generate_random_event()
        self.__validator.validate_event(event)  # Validare eveniment
        self.__repo.add_event_list(event)  # Adaugare eveniment la lista
        return event

    def delete_event(self, id):
        """
        Sterge eveniment dupa id
        :param id: id-ul eveniment
        :type id: int (>0)
        :return: Eveniment stears
        :rtype: Event
        :raise: ValueError daca evenimentul nu exista
        """
        return self.__repo.delete_event(id)

    def modify_event(self, id, data, timp, descriere):
        """
        Modifica eveniment cu id-ul cautat
        :param id: id-ul evenimentului cautat
        :type id: int
        :param data: data noului eveniment
        :type data: date
        :param timp: durata noului eveniment
        :type timp: time
        :return: eveniment modificat
        :rtype: Event
        """
        event = Event(id, data, timp, descriere)
        self.__validator.validate_event(event)  # Validate event
        return self.__repo.modify_event(id, event)

    def size_events(self):
        """
        Numarul de evenimente
        :return: Number of events
        """
        return self.__repo.size_events()

    def get_all_events(self):
        """
        Returneaza toate evenimentele de pe lista
        :rtype: list of Event objects
        """
        return self.__repo.get_all_events()

    def find_event(self, id):
        """
        Cauta eveniment dupa id
        :param id: id-ul cautat
        :return: eveniment cautat
        """
        event = self.__repo.find_event(id)
        if event is None:
            raise ValueError("Id-ul evenimentului cautat nu exita in lista.")
        return event

    def find_event_recursively(self, id):
        """
        Cauta un eveniment recursiv
        :param id: id-ul evenimentului cautat
        :return: evenimentul cautat
        :raises: EventNotFoundException
        """
        all_ev = self.__repo.get_all_events()
        long = self.size_events()-1
        return self.__repo.find_event_recursively(all_ev, id, long)

    def merge(self, arr1, arr2, key):
        """
        Lipire arr1, arr2 in functie de key
        :param arr1: primul sir
        :param arr2: al doilea sir
        :param key: conditia aplicata
        :return: sirul rezultat
        """
        result = []

        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if key(arr1[i]) > key(arr2[j]): #reversed
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        result.extend(arr1[i:])
        result.extend(arr2[j:])

        return result

    def merge_sort_with_key(self, my_list, key=lambda x: x):
        """
        MergeSort cu conditie
        :param my_list: lista care trebuie sortata
        :param key: conditia
        :return: lista sortata
        """
        list_length = len(my_list)

        if list_length <= 1:
            return my_list

        middle = list_length // 2

        left = my_list[:middle]
        right = my_list[middle:]

        sorted_left = self.merge_sort_with_key(left, key)
        sorted_right = self.merge_sort_with_key(right, key)

        return self.merge(sorted_left, sorted_right, key)

    def get_top_events(self):
        list_of_events = self.__repo.get_all_events()
        # sorted_list_of_events = sorted(list_of_events, key=lambda Event: len(Event.getPersoane()), reverse=True)
        sorted_list_of_events = self.merge_sort_with_key(list_of_events, key=lambda x: len(x.getPersoane()))
        number_of_events = abs(0.2 * len(sorted_list_of_events))
        list = []
        for el in sorted_list_of_events:
            if not number_of_events:
                break
            list.append(el)
            number_of_events -= 1
        return list


