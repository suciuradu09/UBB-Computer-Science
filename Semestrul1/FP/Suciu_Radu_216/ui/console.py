from exceptions.exceptions import EmptyException

class Console:
    def __init__(self, bugs_service):
        self.__bserv = bugs_service

    def _ordered(self):
        """
        Lista ordonata de bugs in functie de descriere
        """
        try:
            words = input("Search for: ")
            list_of_bugs = self.__bserv.ordered(words)
            print("List of ordered bugs: ")
            for bug in list_of_bugs:
                print(bug)
        except EmptyException as ee:
            print(ee)

    def _media(self):
        """
        Media bugurilor grupate dupa nume, si afiseaza priority
        """
        try:
            print("Media bugurilor grupate dupa nume: ")
        except Exception as e:
            print(e)

    def _show(self):
        self.__bserv.show()

    def show_ui(self):
        finished = False
        while not finished:
            print("Comenzi disponibile: ordered, media, show bugs, exit")
            command = input("Insert command >> ")
            if command == 'ordered':
                self._ordered()
            elif command == 'media':
                self._media()
            elif command == 'show bugs':
                self._show()
            elif command == 'exit':
                return
            elif command == '':
                continue
            else:
                print("Comanda invalida!")