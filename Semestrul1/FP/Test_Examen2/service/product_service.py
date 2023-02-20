
class productService:
    def __init__(self, repository, validator):
        self._repo = repository
        self._val = validator

    def add_product(self, product):
        """
        Adauga produsul in lista de produse din fisier
        :param product: produsul care trebuie adaugat
        :type product: Product
        """
        self._val.validate(product)
        return self._repo.add_product(product)

    def delete_product(self, cifra):
        """
          Sterge produse care contin o cifra introdusa de la tastatura
        in pretul lor
        :param cifra: cifra care va sterge produsele ce o contin
        :type cifra: int
        """
        return self._repo.delete_product(cifra)
