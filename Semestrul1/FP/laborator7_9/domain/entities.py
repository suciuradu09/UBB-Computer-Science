class Person:
    def __init__(self, id, nume, adresa):
        """
        Initializeaza un obiect de tip persoana cu valorile date
        :param id: id-ul persoanei
        :type id: int (>0)
        :param nume: numele persoanei
        :type nume: str
        :param adresa: adresa persoanei
        :type adresa: str
        """
        self.__id = id
        self.__nume = nume
        self.__adress = adresa
        self.__evenimente = []

    def getID(self):
        return self.__id

    def getNume(self):
        return self.__nume

    def getAdress(self):
        return self.__adress

    def getEvent(self):
        return self.__evenimente

    def setID(self, value):
        self.__id = value

    def setNume(self, value):
        self.__nume = value

    def setAdress(self, value):
        self.__adress = value

    def addEvent(self, value):
        self.__evenimente.append(value)

    def __eq__(self, other):
        """
        Verifica egalitatea
        :param other: persoana cu care se compara persoana curenta
        :type other: Person
        :return: True daca persoanele au id identic, False in caz contrar
        :rtype: bool
        """
        if self.__id == other.getID():
            return True
        return False

    def __str__(self):
        return "Id: " + str(self.__id) + " | Nume: " + str(self.__nume) + " | adresa: " + str(self.__adress)


class Event:
    def __init__(self, id_eveniment, data, timp, descriere):
        """
        Initializare obiect de tip eveniment
        :param id_eveniment: id-ul evenimentului (>0)
        :type id_eveniment: int
        :param data: data evenimentului
        :type data: date
        :param timp: durata evenimentului
        :type timp: time
        :param descriere: descrierea evenimentului
        :type descriere: str
        """
        self.__id_eveniment = id_eveniment
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere
        self.__persoane = []

    def getIDe(self):
        return self.__id_eveniment

    def getDate(self):
        return self.__data

    def getTime(self):
        return self.__timp

    def getDescription(self):
        return self.__descriere

    def getPersoane(self):
        return self.__persoane

    def setIDe(self, value):
        self.__id_eveniment = value

    def setDate(self, value):
        self.__data = value

    def setTime(self, value):
        self.__timp = value

    def setDescription(self, value):
        self.__descriere = value

    def addPersoane(self, value):
        self.__persoane.append(value)

    def __eq__(self, other):
        """
        Verifica egalitatea
        :param other: Evenimentul cu care se compara evenimentul curent
        :type other: Event
        :return: True daca id-ul evenimentelor este lafel, False in caz contrar
        :rtype: Bool
        """
        if self.__id_eveniment == other.getIDe() and self.__data == other.getDate():
            return True
        return False

    def __str__(self):
        return "Id eveniment: " + str(self.__id_eveniment) + " | data: " + str(self.__data) + " | ora: " + str(
            self.__timp) + " | descriere: " + str(self.__descriere)


class Invitatie:
    def __init__(self, person, event):
        self.__id = person.getID()
        self.__person = person
        self.__event = event

    def getIDi(self):
        return self.__id

    def getPerson(self):
        return self.__person

    def getEvent(self):
        return self.__event

    def setPerson(self, value):
        self.__person = value

    def setEvent(self, value):
        self.__event = value

    def __eq__(self, other):
        if self.__person.getID() == other.__person.getID() and self.__event.getIDe() == other.__event.getIDe():
            return True
        return False

    def __str__(self):
        return 'Persoana: [' + str(self.__person.getNume()) + ' ; ' + str(
            self.__person.getAdress()) + '] Eveniment: [' + \
               str((self.__event.getDate())) + ' ; ' + str((self.__event.getTime())) + ' ; ' + \
               str((self.__event.getDescription())) + ']'