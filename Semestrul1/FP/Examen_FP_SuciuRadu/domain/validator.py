
class validator:
    def validate(self, spectacol):
        """
        Validator pentru obiecte de tip Spectacol
        :param spectacol: obiectul de tip spectacol
        :return: in cazul in care exista returneaza erori
        """
        errors = []
        if spectacol.getTitlu() == '':
            errors.append("Titlul spectacolului nu poate fi vid.")
        if spectacol.getArtist() == '':
            errors.append("Artistul nu poate fi vid.")
        if spectacol.getDurata() < 0:
            errors.append("Durata nu poate fi negativa")
        elif isinstance(spectacol.getDurata(), int) == False:
            errors.append("Durata spectacolului trebuie sa fie un numar intreg")

        if spectacol.getGen() not in ["Comedie", "Concert", "Balet", "Altele"]:
            errors.append("Genul spectacolului trebuie sa fie: Comedie, Concert, Balet sau Altele")

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)
