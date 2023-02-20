"""
Se cere dezvoltarea unei aplicatii pentru gestiunea unui cont bancar.
Fiecare tranzactie are ziua (date), suma (float) si tipul(intrare/iesire).

Aplicatia are interfata tip consola si permite urmatoarele functionalitati:

1. Adaugare tranzactie (zi, suma, tip)
2. Actualizeaza tranzactie (zi, suma, tip)

3. Sterge cheltuielile pentru o zi specificata (se da ziua)
4. Sterge cheltuielile pentru o perioada data (se da ziua de inceput si sfarsit)
5. Sterge tranzactiile de un anumit tip

6. Tipareste tranzactiile cu sume mai mari decat o suma data
7. Tipareste tranzactiile efectualte inainte de o zi si mai mari decat o suma (se da suma si ziua)
8. Tipareste tranzactiile de un anumit tip

9. Suma totala a tranzactiilor de un anumit tip
10. Soldul contului la o data specificata
11. Tipareste tranzactiile de un anumit tip ordonate dupa suma

12. Elimina toate tranzactiile de un anumit tip
13. Elimina toate tranzactiile mai mici de o suma data care are tipul specificat

14. Reface ultima operatie

Se adauga o optiune pentru printarea listei curente
"""

from termcolor import colored


# Functii care lucreaza cu entitatea tranzactie

def generate_transactions():
    return [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare'],
            [12, 10, 'Retragere'], [30, 5000.32, 'Depozitare'], [1, 123.80, 'Depozitare'],
            [27, 550, 'Retragere'], [23, 634.50, 'Depozitare'], [31, 405.50, 'Retragere']]

def get_previous_list(lista):
    return lista[-2]


def get_date(transaction):
    return transaction[0]


def get_suma(transaction):
    return transaction[1]


def get_type(transaction):
    return transaction[2]


def create_transaction(date, value, tip):
    """
    Functia verifica formatul introdus si adauga in
     lista parametrii, returneaza -1 in caz contrar
    :param date: ziua in care s-a produs tranzactia
    :param value: valoarea introdusa
    :param tip: tipul tranzactiei
    :return: lista cu parametrii
    """
    if date <= 31 and date >= 1 and (tip == 'Depozitare' or tip == 'Retragere'):
        return [date, value, tip]
    return 0


def add_to_transactions(lista, transaction):
    """
    Functia preia o tranzactie si o adauga in lista tranzactiilor
    daca este corecta
    :param transaction: Tranzactia curenta
    :param lista: Lista tranzactiilor curente
    """
    if transaction != 0 and type(transaction) == list:
        lista.append(transaction)
    else:
        print(colored("Nu s-a efectuat tranzactia!", 'red'))


def update_transaction(lista, transaction1, transaction2):
    """
    Functia cauta o tranzactie si o actualizeaza din lista cu tranzactii
    :param lista: lista cu tranzactii
    :param transaction1: tranzactia cautata
    :param transaction2: tranzactia modificata
    """
    ok = 0
    for x in lista:
        if x == transaction1:
            poz = lista.index(x)
            lista.remove(x)
            lista.insert(poz,transaction2)
            ok = 1
    return ok


def find_transaction(lista, transaction):
    """
    Functia cauta tranzactia specifica in tranzactiile curente.
    :param lista: lista de tranzactii
    :param transaction: tranzactia cautata
    :return: True daca tranzactia e gasita, False in caz contrar
    """
    for x in lista:
        if x == transaction:
            return True
    return False


def delete_transaction(lista, element1, element2, func):
    """
    Functia sterge tranzactii in functie de valorile parametrilor.
    Cand element2 = -1 functia modifica lista cu element1 eliminat,
    cand element2 > 0 functia sterge tranzactiile din perioada (element1,element2)
    :param lista: lista tranzactiilor
    :type lista: list
    :param element1: ziua care sa se stearga
    :type element1: int
    """
    if element2 >= 0:
        if element1 <= element2:
            i = 0
            while i < len(lista):
                el = func(lista[i])
                if el >= element1 and el <= element2:
                    lista.remove(lista[i])
                else:
                    i = i + 1
        else:
            print(colored("Date introduse incorect!", 'red'))
    else:
        i = 0
        while i < len(lista):
            el = func(lista[i])
            if el == element1:
                lista.remove(lista[i])
            else:
                i = i + 1


def filter_list(lista, tip):
    """
    Filtreaza tranzactiile in functie de tip
    :param lista: lista de tranzactii
    :param tip: tipul tranzactiei
    :return: o noua lista de tranzactii filtrata
    :rtype: list
    """
    return [transaction for transaction in lista if get_type(transaction) != tip]


def search_transaction_sum(lista, suma):
    """
    Functia creeaza o noua lista cu tranzactii a caror suma e mai mare
    decat suma introdusa
    :param lista: lista de tranzactii
    :type lista: list of lists
    :param suma: valoarea minima
    :type suma: int
    :return: o noua lista cu tranzactiile cautate
    """
    return [transaction for transaction in lista if get_suma(transaction) > suma]


def search_transaction_sum_day(lista, suma, ziua):
    """
    Functia creeaza o noua lista cu tranzactii a caror suma e mai mare
    decat suma introdusa si inainte de o zi
    :param lista: lista de tranzactii
    :type lista: list of lists
    :param suma: valoarea minima
    :type suma: int
    :return: o noua lista cu tranzactiile cautate
    """
    return [transaction for transaction in lista if get_suma(transaction) > suma and get_date(transaction) < ziua]


def search_transaction_type(lista, tip):
    """
    Functia creeaza o noua lista cu tranzactiile de un tip specificat
    :param lista: lista tranzactiilor
    :type lista: list
    :param tip: tipul tranzactiei cautat
    :type tip: string
    :return: o noua lista cu tranzactiile cautate
    """
    return [transaction for transaction in lista if get_type(transaction) == tip]


def sum_of_transactions_type(lista, tip):
    """
    Suma tranzactiilor de un anumit tip
    :param lista: lista tranzactiilor
    :param tip: tipul tranzactiilor cautate
    :return: suma tranzactiilor
    :rtype: int
    """
    sum = 0
    for transaction in lista:
        if get_type(transaction) == tip:
            sum += get_suma(transaction)
    return sum


def calculate_balance(lista, data):
    """
    Calculeaza soldul contului la o data specificata
    :param lista: lista tranzactiiolor
    :param data: data la care se calculeaza soldul
    :type lista: list of lists
    :type data: int
    :return: soldul contului la data specificata
    :rtype: int
    """
    if data >= 0 and data <= 31:
        balance = 0
        for transaction in lista:
            if get_date(transaction) <= data:
                if get_type(transaction) == 'Depozitare':
                    balance += get_suma(transaction)
                elif get_type(transaction) == 'Retragere':
                    balance -= get_suma(transaction)
    return balance


def ordered_by_sum_type(lista, tip):
    """
    Sorteaza si returneaza o lista noua cu tranzactiile
    de tipul introdus de utilizator
    :param lista: lista tranzactiilor
    :param tip: tipul tranzactiilor
    :return: o noua lista cu tranzactii ordonate dupa suma
    """
    ordered_list = []
    for transaction in lista:
        if get_type(transaction) == tip:
            ordered_list.append(transaction)

    ordered_list.sort(key=get_suma)

    return ordered_list


def delete_transaction_sum_type(lista, suma, tipul):
    """
    Sterge tranzactiile ale caror suma este mai mica decat cea
    introdus si care au tipul specificat.
    :param lista: lista tranzactiilor
    :param suma: suma introdusa de utilizator
    :param tipul: tipul tranzactiilor cautate
    """
    try:
        i = 0
        while i < len(lista):
            tip_tranzactie = get_type(lista[i])
            suma_tranzactie = get_suma(lista[i])
            if tip_tranzactie == tipul and suma_tranzactie == suma:
                lista.remove(lista[i])
            else:
                i = i + 1
    except:
        print(colored("Nu s-a efectuat stergerea!", 'red'))

def undo(lista, istoric):
    try:
        lista.clear()
        lista.copy(get_previous_list(istoric))
        istoric.pop(-1) # sterge ultima lista
    except:
        print(colored("Istoricul este gol, nu se mai poate face undo", 'red'))

# Functii UI

def print_current_list(list):
    """
    Functia afiseaza tranzactiile curente
    :param list: lista curenta
    :type list: list
    """
    if list == []:
        print(colored('Nicio tranzactie! - Pentru a adauga selectati 1', 'yellow'))
        return
    for i, transaction in enumerate(list):
        print(i, 'Ziua: ', colored(get_date(transaction), 'blue'),
              '- Suma:', colored(get_suma(transaction), 'blue'),
              '- Tip: ', colored(get_type(transaction), 'blue'))


def add_transaction_ui(list):
    """
    Functia adauga o noua tranzactie la tranzactiile curente
    :param list: lista de tranzactii curente
    :type list: list
    """
    tran = []
    try:
        t_date = int(input("Introduceti ziua: "))
        t_value = float(input("Introduceti suma: "))
        t_type = str(input("Tipul de tranzactie (Depozitare/Retragere): "))
        tran = create_transaction(t_date, t_value, t_type)
        add_to_transactions(list, tran)
    except:
        print(colored("Format incorect!", 'red'))


def update_transaction_ui(lista):
    """
    Functia actualizeaza o tranzactie
    :param lista: lista de tranzactii
    """
    tr1 = []
    tr2 = []
    try:
        t_date = int(input("Introduceti ziua: "))
        t_value = float(input("Introduceti suma: "))
        t_type = str(input("Tipul de tranzactie (Depozitare/Retragere): "))
        tr1 = create_transaction(t_date, t_value, t_type)  # tranzactia cautata

        print("Introduceti noile valori pentru tranzactie: ")
        t_date_new = int(input("Introduceti ziua: "))
        t_value_new = float(input("Introduceti suma: "))
        t_type_new = str(input("Tipul de tranzactie (Depozitare/Retragere): "))
        tr2 = create_transaction(t_date_new, t_value_new, t_type_new)  # tranzactia noua
    except:
        print(colored("Format incorect!", 'red'))
    if find_transaction(lista, tr1) == True:
        update_transaction(lista, tr1, tr2)
        print(colored("Actualizare reusita", 'green'))
    else:
        print(colored("Actualizare esuata!", 'red'))


def filter_transaction_ui(lista):
    """
    Filtreaza lista in functie de un tip dat de la tastatura
    :param lista: lista de tranzactii
    :type lista: list
    """
    type_t = str(input(("Introduceti tipul(Depozitare/Retragere): ")))
    filtered_list = filter_list(lista, type_t)
    print(colored("Lista filtrata:", 'yellow'))
    print_current_list(filtered_list)


def delete_transaction_type_ui(lista):
    """
       Functia sterge tranzactiile dintr-o data specificata
       :param lista: lista de tranzactii
       :type lista: list
       """
    try:
        tipul = str(input("Introduceti tipul tranzactiei: "))
        delete_transaction(lista, tipul, -1, get_type)
        print(colored("Stergere efectuata!", 'green'))
    except:
        print(colored("Stergere esuata!", 'red'))


def delete_transaction_day_ui(lista):
    """
    Functia sterge tranzactiile dintr-o data specificata
    :param lista: lista de tranzactii
    :type lista: list
    """
    try:
        day = int(input("Introduceti ziua: "))
        delete_transaction(lista, day, -1, get_date)
        print(colored("Stergere efectuata!", 'green'))
    except:
        print(colored("Stergere esuata!", 'red'))


def delete_transaction_period_ui(lista):
    """
    Functia sterge tranzactiile dintr-o perioada data
    :param lista: lista de tranzactii
    """
    try:
        p1 = int(input("Introduceti ziua de inceput: "))
        p2 = int(input("Introduceti ziua de sfarsit: "))
        delete_transaction(lista, p1, p2, get_date)
        print(colored("Stergere efectuata!", 'green'))
    except:
        print(colored("Stergere esuata!", 'red'))


def search_transaction_sum_ui(lista):
    """
    Cauta si afiseaza tranzactiile care au suma mai mare decat suma introdusa
    de utilizator
    :param lista: lista de tranzactii
    :type lista: list of lists
    """
    sum = int(input("Introduceti suma: "))
    try:
        print_current_list(search_transaction_sum(lista, sum))
    except:
        print(colored("Nu a fost efectuata cautarea!", 'red'))


def search_transaction_sum_day_ui(lista):
    """
    Tipareste tranzactiile efectualte inainte de o zi si mai mari decat o suma
    :param lista: lista tranzactiilor
    :type lista: list
    """
    ziua = int(input("Introduceti ziua: "))
    sum = int(input("Introduceti suma: "))
    try:
        print_current_list(search_transaction_sum_day(lista, sum, ziua))
    except:
        print(colored("Nu a fost efectuata cautarea!", 'red'))


def search_transaction_type_ui(lista):
    """
    Tipareste tranzactiile de un anumit tip
    :type lista: list
    """
    tipul = str(input("Introduceti tipul tranzactiei: "))
    try:
        print_current_list(search_transaction_type(lista, tipul))
    except:
        print(colored("Nu a fost efectuata cautarea!", 'red'))


def sum_of_transactions_type_ui(lista):
    """
    Suma tuturor tranzactiilor de un anumit tip
    :param lista: lista tranzactiilor
    :type lista: list of lists
    :return: suma tranzactiilor
    :rtype: int
    """
    tipul = str(input("Introduceti tipul: "))
    try:
        n = sum_of_transactions_type(lista, tipul)
        print("Suma tranzactiilor de tipul ", tipul, " este: ", n)
    except:
        print(colored("Nu s-a efectuat suma!", 'red'))


def calculate_balance_ui(lista):
    """
    Calculeaza soldul la o data specificata
    :param lista: lista tranzactiilor
    :type lista: list of lists
    """
    ziua = int(input("Afiseaza soldul la data: "))
    try:
        n = calculate_balance(lista, ziua)
        print("In data de", ziua, "soldul contului era: ", n)
    except:
        print(colored("Nu s-a putut calcula soldul!", 'red'))


def ordered_by_sum_type_ui(lista):
    """
    Afiseaza tranzactiile de un anumit tip ordonate dupa suma
    :param lista: lista tranzactiilor
    :type lista: list of lists
    """
    tipul = str(input("Introduceti tipul: "))
    try:
        print_current_list(ordered_by_sum_type(lista, tipul))
    except:
        print(colored("Nu s-a afisat lista ordonata.", 'red'))


def delete_transaction_sum_type_ui(lista):
    """
    Sterge tranzactiile cu o suma mai mica decat cea specificata de un anumit tip
    :param lista: lista tranzactiilor
    """
    sum = int(input("Suma: "))
    tip = str(input("Tipul tranzactiilor: "))
    try:
        delete_transaction_sum_type(lista, sum, tip)
    except:
        print(colored("Nu s-a efectuat stergerea!", 'red'))


def print_menu():
    print(colored("Adaugare de noi tranzactii", 'blue'))
    print("1. Adaugare tranzactie")
    print("2. Actualizeaza tranzactie (zi, suma, tip)")
    print(colored("Stergere", 'blue'))
    print("3. Sterge cheltuielile pentru o zi specificata (se da ziua)")
    print("4. Sterge cheltuielile pentru o perioada data (se da ziua de inceput si sfarsit)")
    print("5. Sterge tranzactiile de un anumit tip")
    print(colored("Cautari", 'blue'))
    print("6. Tipareste tranzactiile cu sume mai mari decat o suma data")
    print("7. Tipareste tranzactiile efectualte inainte de o zi si mai mari decat o suma (se da suma si ziua)")
    print("8. Tipareste tranzactiile de un anumit tip")
    print(colored("Rapoarte", 'blue'))
    print("9. Suma totala a tranzactiilor de un anumit tip")
    print("10.Soldul contului la o data specificata")
    print("11.Tipareste tranzactiile de un anumit tip ordonate dupa suma")
    print(colored("Filtrare", 'blue'))
    print("12.Elimina toate tranzactiile de un anumit tip")
    print("13.Elimina toate tranzactiile mai mici de o suma data care are tipul specificat")
    print(colored("Undo", 'blue'))
    print("14.Reface ultima operatie")
    print("S. Afiseaza lista tranzactiilor")
    print("E. Inchidere aplicatie")


def start():
    list_of_transactions = []
    current_list = []
    history_list = []
    history_list.append(list_of_transactions)
    finished = False
    while not finished:
        current_list = list_of_transactions.copy()
        print_menu()
        option = input("Optiunea este: ")
        if option == '1':
            try:
                add_transaction_ui(list_of_transactions)
                history_list.append(current_list)
            except:
                print(colored("Tranzactia nu s-a realizat!", 'red'))
        elif option == '2':
            try:
                update_transaction_ui(list_of_transactions)
                history_list.append(current_list)
            except:
                print(colored("Actualizare esuata!", 'red'))
        elif option == '3':
            try:
                delete_transaction_day_ui(list_of_transactions)
                history_list.append(list_of_transactions)
            except:
                print(colored("Stergere esuata!", 'red'))
        elif option == '4':
            try:
                delete_transaction_period_ui(list_of_transactions)
                history_list.append(current_list)
            except:
                print(colored("Stergere esuata!", 'red'))
        elif option == '5':
            try:
                delete_transaction_type_ui(list_of_transactions)
                history_list.append(current_list)
            except:
                print(colored("Stergere esuata!", 'red'))
        elif option == '6':
            try:
                search_transaction_sum_ui(list_of_transactions)
            except:
                print(colored("Cautare esuata!", 'red'))
        elif option == '7':
            try:
                search_transaction_sum_day_ui(list_of_transactions)
            except:
                print(colored("Cautare esuata!", 'red'))
        elif option == '8':
            try:
                search_transaction_type_ui(list_of_transactions)
            except:
                print(colored("Cautare esuata!", 'red'))
        elif option == '9':
            try:
                sum_of_transactions_type_ui(list_of_transactions)
            except:
                print(colored("Nu s-a putut efectua suma!", 'red'))
        elif option == '10':
            try:
                calculate_balance_ui(list_of_transactions)
            except:
                print(colored("A aparut o eroare in calcularea soldului!", 'red'))
        elif option == '11':
            try:
                ordered_by_sum_type_ui(list_of_transactions)
            except:
                print(colored("Nu s-au afisat tranzactiile!", 'red'))
        elif option == '12':
            try:
                filter_transaction_ui(list_of_transactions)
            except:
                print(colored("Filtrare esuata!", 'red'))
        elif option == '13':
            try:
                delete_transaction_sum_type_ui(list_of_transactions)
                history_list.append(current_list)
                print(colored("Tranzactii eliminate!", 'green'))
            except:
                print(colored("Filtrare esuata!", 'red'))
        elif option == '14':
            undo(list_of_transactions, history_list)
        elif option == 'S' or option == 's':
            print_current_list(list_of_transactions)
        elif option == 'E' or option == 'e':
            finished = True
        elif option == 'test':
            print(history_list)
        else:
            print(colored("Optiune invalida!", 'red'))

# Teste Functii

def run_tests():
    test_delete_transaction()
    test_add_to_transaction()
    test_update_transaction()
    test_filter_list()


def test_add_to_transaction():
    test_list = []
    tr1 = create_transaction(20, 100.50, 'Depozitare')
    add_to_transactions(test_list, tr1)
    assert (len(test_list) == 1)
    assert (get_date(test_list[0]) == 20)
    assert (get_suma(test_list[0]) == 100.50)
    assert (get_type(test_list[0]) == 'Depozitare')

    tr2 = create_transaction(10, 30.25, 'Depozitare')
    add_to_transactions(test_list, tr2)
    assert (len(test_list) == 2)
    assert (get_date(test_list[1]) == 10)
    assert (get_suma(test_list[1]) == 30.25)
    assert (get_type(test_list[1]) == 'Depozitare')


def test_update_transaction():
    test_list = generate_transactions()
    assert (update_transaction(test_list, [10, 25.00, 'Depozitare'], [10, 30, 'Retragere']) == True)
    assert (update_transaction(test_list, [200, 75.50, 'Depozitare'], [10, 30, 'Retragere']) == False)
    assert (update_transaction(test_list, [], [10, 30, 'Retragere']) == False)
    assert (update_transaction(test_list, [10, 25.00, 'Depozitare'], []) == True)
    assert (update_transaction(test_list, [], []) == False)


def test_delete_transaction():
    test_list = generate_transactions()

    initial_length = len(test_list)
    delete_transaction(test_list, 11, -1, get_date)
    assert (initial_length == len(test_list) + 2)

    test_list = generate_transactions()
    delete_transaction(test_list, 10, -1, get_date)
    assert (len(test_list) == initial_length - 1)

    test_list = generate_transactions()
    delete_transaction(test_list, 20, -1, get_date)
    assert (len(test_list) == initial_length)

    test_list = generate_transactions()
    auxiliary_list = test_list
    delete_transaction(test_list, -1, -1, get_date)
    assert (test_list == auxiliary_list)


def test_filter_list():
    test_list = generate_transactions()

    assert (filter_list(test_list, 'Retragere') == (
        [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']]))
    assert (filter_list(test_list, '') == [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'],
                                           [11, 100.00, 'Depozitare'],
                                           [12, 10, 'Retragere']])
    assert (len(filter_list(test_list, 'Depozitare')) == 1)


start()

# run_tests()
