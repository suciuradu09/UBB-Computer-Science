from repository.bugs_repo import BugsRepo_file

class BugServ:
    def __init__(self, repo, val):
        self._repo = repo
        self._val = val

    def ordered(self, word):
        """
        :param word: cuvantul cautat in descriere
        :type word: str
        :return: lista de buguri
        :raises:
        """
        return self._repo.ordered(word)

    def media(self):
        """
        Pentru fiecare componentă afectată, afișați media priorităților bugurilor aferente
        """
        return self._repo.media()

    def show(self):
        self._repo.show()

    def get_all(self):
        self._repo.get_all()
