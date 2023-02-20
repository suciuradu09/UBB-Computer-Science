"""
Se dă o listă de numere întregi a1,...an. Determinaţi toate posibilităţile de a insera
operatorul de + şi – între numere astfel încât rezultatul expresiei este pozitiv
"""


def suma(x, numbers):
    """
    Calculeaza suma elementelor dintr-o lista in functie de operatii
    :param x: lista de operatii
    :param numbers: lista cu numere
    :return: suma elementelor
    """
    summ = numbers[0]
    for i in range(len(x)):
        if x[i] == '-':
            summ -= numbers[i + 1]
        elif x[i] == '+':
            summ += numbers[i + 1]

    return summ


def solutie(x, numere):
    if suma(x, numere) > 0 and len(x) == len(numere) - 1:
        return True
    return False


def consistent(x, numbers):
    if len(x) >= len(numbers):
        return False

    elif suma(x, numbers) < 0:
        return False

    return True


def p12_rec(x, numere, operatii):
    x.append('-')
    for i in operatii:
        x[-1] = i
        if consistent(x, numere):
            if solutie(x, numere):
                print('[SOLUTIE RECURSIVA]: ', x, ' = ', suma(x, numere))
            else:
                p12_rec(x[:], numere, operatii)
    x.pop()


def p12_iterativ(x, numere, operatii):
    x.append(' ')
    while len(x) > 0:
        chosen = False
        while not chosen and operatii.index(x[-1]) < 2:
            x[-1] = operatii[operatii.index(x[-1]) + 1]
            chosen = consistent(x, numere)

        if chosen:
            if len(x) == len(numere) - 1 and suma(x, numere) > 0:
                print('[SOLUTIE ITERATIVA]:', x, ' = ', suma(x, numere))
            else:
                x.append(' ')
        else:
            x = x[:-1]


def run():
    list_of_numbers = []
    n = int(input("n >> "))
    print("Enter ", n, 'elements: ')
    for i in range(n):
        el = int(input())
        list_of_numbers.append(el)
    operatii = ['-', '+']
    p12_rec([], list_of_numbers, operatii)
    print()
    operatii = [' ', '-', '+']
    p12_iterativ([], list_of_numbers, operatii)


def test_sum():
    numbers = [1, 2, 3, 4]
    op = ['+', '-', '+']
    print(suma(op, numbers))


run()
