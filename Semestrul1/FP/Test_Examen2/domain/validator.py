
class validator:
    def validate(self, product):
        """
        Valideaza entitati de tip produs
        """
        errors = []
        if product.getID() < 0:
            errors.append("Id-ul trebuie sa fie pozitiv")
        if product.getID() == '':
            errors.append("Id-ul nu poate fi nul")

        if product.getDenumire() == '':
            errors.append("Denumirea produsului nu poate fi nula")

        if product.getPret() < 0:
            errors.append("Pretul produsului nu poate fi negativ")
        if product.getPret() == '':
            errors.append("Pretul produsului nu poate fi nul")

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)
