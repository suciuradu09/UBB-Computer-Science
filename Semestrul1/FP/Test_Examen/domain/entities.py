
class Event:
    def __init__(self, data, ora, descriere):
        """
        Clasa specifica obiectului de tip eveniment
        :param data: data la care incepe evenimentul
        :param ora: ora la care incepe evenimentul
        :param descriere: descrierea evenimentului
        """
        self._data = data
        self._ora = ora
        self._desc = descriere

    def getData(self):
        return self._data

    def getOra(self):
        return self._ora

    def getDesc(self):
        return self._desc

    def __eq__(self, other):
        if self._data == other.getData() or self._ora == other.getOra():
            return True
        return False

    def __str__(self):
        return "Data: " + str(self._data) + " Ora: " + str(self._ora) + " Descriere: " + str(self._desc)