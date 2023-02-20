
class Spectacol:
    """
    Clasa specifica entitatii de tip spectacol
    """
    def __init__(self, titlu, artist, gen, durata):
        self._titlu = titlu
        self._artist = artist
        self._gen = gen
        self._durata = durata

    def getTitlu(self):
        return self._titlu

    def getArtist(self):
        return self._artist

    def getGen(self):
        return self._gen

    def getDurata(self):
        return self._durata

    def setTitlu(self, value):
        self._titlu = value.getTitlu()

    def setArtist(self, value):
        self._artist = value.getArtist()

    def setGen(self, value):
        self._gen = value.getGen()

    def setDurata(self, value):
        self._durata = value.getDurata()

    def __eq__(self, other):
        if self._titlu == other.getTitlu() and self._artist == other.getArtist() and self._gen == other.getGen() and self._durata == other.getDurata():
            return True
        return False


    def __str__(self):
        return "Titlu: " + str(self._titlu) + " Artist: " + str(self._artist) + " Gen: " + str(self._gen) + " Durata: " + str(self._durata)
