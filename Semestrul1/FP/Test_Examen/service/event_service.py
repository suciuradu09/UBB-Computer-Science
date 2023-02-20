
class EventService:
    def __init__(self, repo, validator):
        self._repo = repo
        self._val = validator

    def show_events(self, day):
        """
        Afiseaza toate evenimentule din fisier din data de azi
        :param day: ziua de azi
        """
        return self._repo.show_events(day)

    def add_event(self, event):
        """
        Adaugare eveniment in fisier
        :param event: evenimentul care se adauga in fisier
        """
        return self._repo.add_event(event)

    def create(self, filename, sir):
        """
        Creeaza un fisier in care se gasesc toate evenimetele cu descrierea data
        :param filename: numele fisierului creat
        :type filename: strig
        :param sir: sirul cautat in descrieri
        :type sir: string
        """
        return self._repo.create(filename, sir)

