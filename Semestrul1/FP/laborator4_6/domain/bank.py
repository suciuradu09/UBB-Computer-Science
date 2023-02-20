from termcolor import colored
from domain.transaction import get_date, get_suma, get_type, get_previous_list, validate_date
from utils.operations import list_copy


def generate_transactions():
    return [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare'],
            [12, 10, 'Retragere'], [30, 5000.32, 'Depozitare'], [1, 123.80, 'Depozitare'],
            [27, 550, 'Retragere'], [23, 634.50, 'Depozitare'], [31, 405.50, 'Retragere']]


def add_to_transactions(lista, transaction):
    """
    Functia preia o tranzactie si o adauga in lista tranzactiilor
    daca este corecta
                                                                :param transaction: Tranzactia curenta
                                                                :param lista: Lista tranzactiilor curente
    """
    if type(transaction) == list:
        lista.append(transaction)


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
            lista.insert(poz, transaction2)
            ok = 1
    return ok


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
    try:
        validate_date(data)
        balance = 0
        for transaction in lista:
            if get_date(transaction) <= data:
                if get_type(transaction) == 'Depozitare':
                    balance += get_suma(transaction)
                elif get_type(transaction) == 'Retragere':
                    balance -= get_suma(transaction)
        return balance
    except Exception as e:
        print(e)


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
    """
    Functia reface operatia efectuata anterior
                                                                :param lista: lista de tranzactii
                                                                :param istoric: lista istoricului
                                                                :return: lista cu operatia efectuata
    """
    if istoric != []:
        lista.clear()
        return list_copy(get_previous_list(istoric))
    elif istoric == [[]]:
        print(colored("Istoricul este gol, nu se mai poate face undo", 'red'))


# tests
def test_add_to_transactions():
    test_list = []
    add_to_transactions(test_list, [1, 1, 'Depozitare'])
    assert (test_list == [[1, 1, 'Depozitare']])
    assert (len(test_list) == 1)
    add_to_transactions(test_list, [2, 1.2, 'Depozitare'])
    add_to_transactions(test_list, [3, 1.4, 'Depozitare'])
    add_to_transactions(test_list, [4, 1.6, 'Retragere'])
    assert (test_list == [[1, 1, 'Depozitare'], [2, 1.2, 'Depozitare'], [3, 1.4, 'Depozitare'], [4, 1.6, 'Retragere']])
    assert (len(test_list) == 4)
    assert (type(test_list) == list)


def test_update_transaction():
    test_list = [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']]
    assert (test_list == [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']])
    update_transaction(test_list, [10, 25.00, 'Depozitare'], [17, 100, 'Retragere'])
    assert (test_list == [[17, 100, 'Retragere'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']])
    update_transaction(test_list, [11, 45.50, 'Depozitare'], [])
    assert (test_list == [[17, 100, 'Retragere'], [], [11, 100.00, 'Depozitare']])


def test_delete_transaction():
    test_list = [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']]
    delete_transaction(test_list, 11, -1, get_date)
    assert (test_list == [[10, 25.00, 'Depozitare']])
    delete_transaction(test_list, 10, -1, get_date)
    assert (test_list == [])


def test_calculate_balance():
    test_list = [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']]
    assert (calculate_balance(test_list, 10) == 25.00)
    assert (calculate_balance(test_list, 11) == 170.50)


def test_sum_of_transaction_type():
    test_list = [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare'],
                 [12, 50, 'Retragere']]
    assert (sum_of_transactions_type(test_list, 'Depozitare') == 170.5)
    assert (sum_of_transactions_type(test_list, 'Retragere') == 50)


def test_ordered_by_sum_type():
    test_list = [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare'],
                 [12, 50, 'Retragere']]
    assert (ordered_by_sum_type(test_list, 'Depozitare') == [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'],
                                                             [11, 100.00, 'Depozitare']])
    assert (len(ordered_by_sum_type(test_list, 'Depozitare')) == 3)
    assert (ordered_by_sum_type(test_list, 'Retragere') == [[12, 50, 'Retragere']])
    assert (len(ordered_by_sum_type(test_list, 'Retragere')) == 1)
    assert (ordered_by_sum_type(test_list, '') == [])
    assert (len(ordered_by_sum_type(test_list, '')) == 0)


def test_find_transaction():
    test_list = [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']]
    assert (find_transaction(test_list, [10, 25.00, 'Depozitare']) == True)
    assert (find_transaction(test_list, [11, 45.50, 'Depozitare']) == True)
    assert (find_transaction(test_list, [11, 100.00, 'Depozitare']) == True)


def test_sum_of_transactions_type():
    test_list = [[10, 25.00, 'Depozitare'], [11, 45.50, 'Depozitare'], [11, 100.00, 'Depozitare']]
    assert (sum_of_transactions_type(test_list, 'Depozitare') == 170.5)
    assert (sum_of_transactions_type(test_list, 'Retragere') == 0)
    assert (isinstance(sum_of_transactions_type(test_list, 'Depozitare'), float) == True)
    assert (isinstance(sum_of_transactions_type(test_list, 'Retragere'), str) == False)
