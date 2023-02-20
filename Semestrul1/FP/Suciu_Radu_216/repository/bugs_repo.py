from exceptions.exceptions import CorruptedFile, EmptyException
from domain.enitities import Bug


class BugsRepo_file:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Preia din fisier bugurile
        :return: lista de buguri
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            raise CorruptedFile()

        bugs = []
        lines = f.readlines()
        for line in lines:
            id, name, desc, priority = [token.strip() for token in line.split(',')]
            id = int(id)
            priority = int(priority)
            bug_to_add = Bug(id, name, desc, priority)
            bugs.append(bug_to_add)
        f.close()
        return bugs

    def __save_to_file(self, bugs):
        """
        Salveaza in fisier bugurile modificate
        :param bugs: noua lista de buguri
        """
        with open(self.__filename, 'w') as f:
            for bug in bugs:
                bugs_string = str(bug.getID()) + ',' + str(bug.getName()) + ',' + str(bug.getDesc()) + ',' + str(
                    bug.getPriority()) + '\n'
                f.write(bugs_string)

    def ordered(self, word):
        """
        Cauta dupa un cuvant si afiseaza
        :param word: Cuvantul cautat in descriere
        """
        all_bugs = self.__load_from_file()
        if all_bugs is None:
            raise EmptyException()

        filtered_bugs = []
        for bug in all_bugs:
            if word in bug.getDesc():
                filtered_bugs.append(bug)
        sorted_bugs = sorted(filtered_bugs, key=lambda Bug: Bug.getPriority(), reverse=True)
        return sorted_bugs

    def media(self):
        """
        Media prioritatilor in functie de nume grupate
        :raises: EmptyException
        """
        all_bugs = self.__load_from_file()
        if all_bugs is None:
            raise EmptyException()


    def show(self):
        """
        Afiseaza toate bugurile
        """
        all_bugs = self.__load_from_file()
        if all_bugs == []:
            raise EmptyException()

        for bug in all_bugs:
            print(bug)

    def size_bugs(self):
        return len(self.__load_from_file())

    def get_all(self):
        return self.__load_from_file()

    def delete_all(self):
        self.__save_to_file([])

