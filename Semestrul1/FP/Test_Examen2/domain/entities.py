
class Product:
    """
    Clasa specifica entitatii de tip Product
    """
    def __init__(self, id, denumire, pret):
        self._id = id
        self._denumire = denumire
        self._pret = pret

    def getID(self):
        return self._id

    def getDenumire(self):
        return self._denumire

    def getPret(self):
        return self._pret

    def setID(self, value):
        self._id = value

    def setDenumire(self, value):
        self._denumire = value

    def setPret(self, value):
        self._pret = value

    def __eq__(self, other):
        if self._id == other.getID():
            return True
        return False

    def __str__(self):
        return "Id: " + str(self._id) + " Denumire: " + str(self._denumire) + " Pret: " + str(self._pret)
