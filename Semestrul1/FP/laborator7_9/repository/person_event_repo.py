from domain.entities import Invitatie, Person, Event
from exceptions.exceptions import CorruptedFileException, DuplicateIDException
from repository.person_repo import PersonInMemoryRepository_file
from repository.event_repo import EventInMemoryRepository_file
from datetime import date, time


class InvitationRepoMemory:
    def __init__(self):
        self._invitations = []

    def find(self, invitatie):
        for inv in self._invitations:
            if inv == invitatie:
                return inv
        return None

    def create_invite(self, invitatie):
        inv = self.find(invitatie)
        if inv is not None:
            self._invitations.append(invitatie)

    def get_all(self):
        return self._invitations


class InvitationRepoMemory_file:
    def __init__(self, filename):
        self._filename = filename
        self._person_repo = PersonInMemoryRepository_file('data/persons.txt')
        self._event_repo = EventInMemoryRepository_file('data/events.txt')

    def __load_from_file(self):
        try:
            f = open(self._filename, 'r')
        except IOError:
            raise CorruptedFileException()
        invites = []
        lines = f.readlines()
        if lines is not []:
            for line in lines:
                person_id, person_name, person_adr, event_id, event_date, event_time, event_desc = [token.strip() for
                                                                                                    token in
                                                                                                    line.split(',')]
                person_id = int(person_id)
                person = Person(person_id, person_name, person_adr)


                event_id = int(event_id)
                event_date = [el.strip() for el in event_date.split('-')]  # 2021-10-9
                event_d = date(int(event_date[0]), int(event_date[1]), int(event_date[2]))
                event_time = [el.strip() for el in event_time.split(':')]  # 10:10:00
                event_t = time(int(event_time[0]), int(event_time[1]), int(event_time[2]))
                event = Event(event_id, event_d, event_t, event_desc)
                invite = Invitatie(person, event)
                invites.append(invite)

        f.close()
        return invites

    def __save_to_file(self, invites):
        with open(self._filename, 'w') as f:
            for invite in invites:
                pers = invite.getPerson()
                ev = invite.getEvent()
                str_pers_id = str(pers.getID())
                str_pers_na = str(pers.getNume())
                str_pers_adr = str(pers.getAdress())

                str_ev_id = str(ev.getIDe())
                str_ev_date = str(ev.getDate())
                str_ev_time = str(ev.getTime())
                str_ev_desc = str(ev.getDescription())

                invites_string = str_pers_id + ',' + str_pers_na + ',' + str_pers_adr + ',' + \
                                 str_ev_id + ',' + str_ev_date + ',' + str_ev_time + ',' + str_ev_desc + '\n'
                f.write(invites_string)

    def create_invite(self, invite):
        all_invites = self.__load_from_file()

        all_invites.append(invite)
        self.__save_to_file(all_invites)

    def find(self, invitatie):
        all_invites = self.__load_from_file()
        for invite in all_invites:
            if invitatie == invite:
                return invitatie
        return None

    def get_all(self):
        return self.__load_from_file()
