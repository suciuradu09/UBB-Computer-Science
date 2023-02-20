class RepositoryException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def getMessage(self):
        return self._msg

    def __str__(self):
        return "RepositoryException: " + self._msg

class CorruptedFile(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Fisierul e corupt")

class EmptyException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Nu exista bugs.")
