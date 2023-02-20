from termcolor import colored


# validations

def validate_undo(istoric):
    errors = []
    if len(istoric) == 0:
        errors.append(colored("Nu s-a facut undo!", 'red'))
    if len(errors) > 0:
        error_string = '\n'.join(errors)
        raise Exception(error_string)


def validate_type(tip):
    errors = []
    if isinstance(tip, int) == True:
        errors.append(colored("Format incorect!", 'red'))
    elif tip != 'Depozitare' and tip != 'Retragere':
        errors.append(colored("Tip tranzactie incorect", 'red'))
    if len(errors) > 0:
        errors_string = '\n'.join(errors)
        raise Exception(errors_string)


def validate_date(date):
    if date < 1 or date > 31:
        raise Exception(colored("Data incorecta!", 'red'))


def validate_transaction(transaction):
    errors = []
    if isinstance(get_date(transaction), str) == True:
        errors.append(colored("Data trebuie sa fie de tip intreg!", 'red'))
    elif get_date(transaction) == '':
        errors.append(colored("Data introdusa este nula", 'red'))
    elif get_date(transaction) < 1 or get_date(transaction) > 31:
        errors.append(colored("Data introdusa este invalida!", 'red'))

    if isinstance(get_suma(transaction), str) == True:
        errors.append(colored("Suma trebuie sa fie de tip intreg!", 'red'))
    elif get_suma(transaction) == '':
        errors.append(colored("Suma introdusa este nula", 'red'))
    elif get_suma(transaction) < 0:
        errors.append(colored("Suma nu poate fi negativa", 'red'))

    if isinstance(get_type(transaction), float) == True:
        errors.append(colored("Tipul trebuie sa fie de tip caracter!", 'red'))
    elif get_type(transaction) == '':
        errors.append(colored("Tipul introdus nu poate fi nul", 'red'))
    elif get_type(transaction) != 'Depozitare' and get_type(transaction) != 'Retragere':
        errors.append(colored("Tipul tranzactiei este invalid!", 'red'))
    if len(errors) > 0:
        error_string = '\n'.join(errors)
        raise Exception(error_string)


# getters

def get_date(transaction):
    return transaction[0]


def get_suma(transaction):
    return transaction[1]


def get_type(transaction):
    return transaction[2]


def get_previous_list(lista):
    return lista[-1]


def create_transaction(date, value, tip):
    """
    Functia verifica formatul introdus si adauga in
     lista parametrii, returneaza -1 in caz contrar
    :param date: ziua in care s-a produs tranzactia
    :param value: valoarea introdusa
    :param tip: tipul tranzactiei
    :return: lista cu parametrii
    """
    return [date, value, tip]


# tests

def test_create_transaction():
    assert (create_transaction(12, 100.5, 'Depozitare') == [12, 100.5, 'Depozitare'])
    assert (create_transaction(10, 790, 'Depozitare') == [10, 790, 'Depozitare'])
    assert (create_transaction(100, 100.5, 'Depozitare') == 0)
    tranzactie = create_transaction(4, 50, 'Retragere')
    assert (type(tranzactie) == list)
    assert (get_date(tranzactie) == 4)
    assert (get_suma(tranzactie) == 50)
    assert (get_type(tranzactie) == 'Retragere')


def test_validate_transaction():
    t1 = [12, 45.5, 20]
    try:
        validate_transaction(t1)
    except Exception as ve:
        assert (str(ve) == "Tipul trebuie sa fie de tip caracter!")
    t2 = ['test', 45.5, 20]
    try:
        validate_transaction(t2)
    except Exception as ve:
        assert (str(ve) == "Data trebuie sa fie de tip intreg!")

    t3 = [12, 'test', 20]
    try:
        validate_transaction(t3)
    except Exception as ve:
        assert (str(ve) == "Suma trebuie sa fie de tip intreg!")
    t4 = [12, 45.5, 'Ceva']
    try:
        validate_transaction(t4)
    except Exception as ve:
        assert (str(ve) == "Tipul tranzactiei este invalid!")
