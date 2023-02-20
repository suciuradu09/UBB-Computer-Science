class ValidationException(Exception):
    def __init__(self, messages):
        self.__err_messages = messages

    def getMessages(self):
        return self.__err_messages

    def __str__(self):
        return 'Validation Exception: ' + str(self.__err_messages)


class RepositoryException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def getMessage(self):
        return self.__msg

    def __str__(self):
        return 'Repository Exception: ' + str(self.__msg)


class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "ID duplicat.")


class PersonNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Persoana nu a fost gasita. ")


class EventNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Evenimentul nu a fost gasit. ")


class InvitationNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Aceasta invitatie nu a fost gasita. ")


class CorruptedFileException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Fisierul este corupt.")
