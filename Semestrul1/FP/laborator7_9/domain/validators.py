from domain.entities import Person, Event
from exceptions.exceptions import ValidationException


class PersonValidator:
    """
    clasa pentru incapsularea algoritmului de validare
    """

    def validate(self, person):
        errors = []
        if person.getID() == '':
            errors.append("ID-ul persoanei nu a fost introdus!")
        elif person.getID() < 0:
            errors.append("ID-ul persoanei nu poate fi un numar negativ!")

        if isinstance(person.getNume(), (int, float)):
            errors.append("Numele trebuie sa fie compus doar din litere!")
        elif person.getNume() == '':
            errors.append("Numele nu a fost introdus!")

        if isinstance(person.getAdress(), (int, float)):
            errors.append("Adresa trebuie sa fie compusa doar din litere!")
        elif person.getAdress() == '':
            errors.append("Adresa persoanei nu poate fi vida!")

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)


class EventValidator:
    def __init__(self):
        pass

    def validate_event(self, event):
        errors = []
        if event.getIDe() == '':
            errors.append("ID-ul nu poate fi nul!")
        elif event.getIDe() < 0:
            errors.append("ID-ul evenimentului nu poate fi negativ!")

        if event.getDate() == '':
            errors.append("Data nu poate fi nula!")

        if event.getTime() == '':
            errors.append("Durata nu poate fi nula!")

        if event.getDescription() == '':
            errors.append("Descrierea nu poate fi nula!")

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)
