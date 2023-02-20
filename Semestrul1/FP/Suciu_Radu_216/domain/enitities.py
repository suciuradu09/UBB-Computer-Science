class Bug:
    def __init__(self, id, name, desc, priority):
        self._id = id
        self._name = name
        self._desc = desc
        self._priority = priority

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getDesc(self):
        return self._desc

    def getPriority(self):
        return self._priority

    def setID(self, value):
        self._id = value

    def setName(self, value):
        self._name = value

    def setDesc(self, value):
        self._desc = value

    def setPriority(self, value):
        self._priority = value

    def __eq__(self, other):
        if self._id == other.getID():
            return True
        return False

    def __str__(self):
        return "ID: " + str(self._id) + " | Name: " + str(self._name) + " | Description: " + str(self._desc) + " | Priority: " + str(self._priority)

