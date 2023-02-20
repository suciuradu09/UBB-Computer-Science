from domain.entities import Product

class productRepo_file:
    def __init__(self, filename):
        self._filename = filename

    def load_from_file(self):
        """
        Citeste din fisier produsele
        """
        products = []
        with open(self._filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                id, denumire, pret = [token.strip() for token in line.split(';')]
                id_produs = int(id)
                denumire_produs = denumire
                pret_produs = int(pret)

                produs = Product(id_produs, denumire_produs, pret_produs)
                products.append(produs)
        return products

    def save_to_file(self, products):
        """
        Salveaza in fisier produsele introduse ca parametru
        """
        with open(self._filename, 'w') as file:
            for product in products:
                products_string = str(product.getID()) + ';' + \
                                  str(product.getDenumire()) + ';' + \
                                  str(product.getPret()) + '\n'
                file.write(products_string)

    def add_product(self, product):
        """
            Adauga in lista de produse un nou produs
        :param product: Produsul care va fi adaugat in list
        :return: produsul adaugat
        """
        all_products = self.load_from_file()
        all_products.append(product)
        self.save_to_file(all_products)
        return product

    def delete_product(self, cifra):
        """
          Sterge produse care contin o cifra introdusa de la tastatura
        in pretul lor
        :param cifra: cifra care sterge produsele
        :type cifra: int
        :return: numarul de produse sterse
        """
        contor = 0
        all_products = self.load_from_file()
        for product in all_products:
            print(product)
        for product in all_products:
            pret = product.getPret()
            ok = True
            #print("Produsul: ", product)
            #print("pret: ", pret)
            while pret > 0 and ok == True:
                #print(pret % 10)
                if pret % 10 == cifra:
                    contor += 1
                    pozitie_produs = all_products.index(product)
                    all_products.pop(pozitie_produs)
                    ok = False
                pret = pret // 10

        self.save_to_file(all_products)

        return contor

    def filter_products(self):
        """
        Filtreaza produsele in functie de pret si denumire
        """
        pass