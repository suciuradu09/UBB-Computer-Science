"""
1.Citirea unei liste care contine numere intregi.
2.Gasirea secventei de lungime maxima in care, oricare doua elemente consecutive au cel putin 2 cifre distincte comune
3.Gasirea secventei de lungime maxima in care, elementele contin cel mult trei valori distincte
4.Gaseste secventa de lungime maxima in care, oricare doua elemente consecutive sunt relativ prime intre ele.
5.Iesire din aplicatie
"""

def print_menu():
    print("1.Citeste lista de numere intregi.")
    print("2.Gaseste secventa de lungime maxima in care, oricare doua elemente consecutive au cel putin 2 cifre distincte comune.")
    print("3.Gaseste secventa de lungime maxima in care, elementele contin cel mult trei valori distincte.")
    print("4.Gaseste secventa de lungime maxima in care, oricare doua elemente consecutive sunt relativ prime intre ele.")
    print("5.Iesire din aplicatie.")

def read_list():
    """
    Citire lista de intregi de la tastatura
    :return: lista introdusa
    """
    list = []
    flist = []
    list = input("Introduceti elementele: ")
    list = list.split(" ")
    for i in list:
        flist.append(int(i))
    return flist

def print_list(message, this_list):
    """
    Afiseaza lista curenta
    :param message: Mesajul de dinaintea listei
    :param this_list: lista de intregi
    """
    print(message, this_list)

def cmmdc(a, b):
    """
    Functia returneaza cmmdc a 2 numere introduse ca parametrii
    :param nr1: parametru nr 1
    :param nr2: parametru nr 2
    :return: cel maimare divizor comun, false in caz contrar
    """
    if a < 0 or b < 0:
        return False
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def prime_intre_ele(a, b):
    """
    Functia verifica daca 2 numere sunt prime intre ele
    :return: True daca sunt prime, false in caz contrar
    """
    return cmmdc(a,b) == 1

def cerinta1(nr1, nr2):
    """
    Functia verifica daca doua numere consecutive au
    cel putin 2 cifre distincte comune
    """
    if nr1 <= 9 or nr2 <= 9:
        return False
    if nr1 < 0:
        nr1 = abs(nr1)
    if nr2 < 0:
        nr2 = abs(nr2)
    c = 0
    fv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while nr1 != 0:
        aux = nr1 % 10
        fv[aux] = 1
        nr1 = nr1 // 10

    while nr2 != 0:
        aux = nr2 % 10
        if fv[aux] == 1:
            c = c + 1
            fv[aux] = 0
        nr2 = nr2 // 10
    return c >= 2

def parcurgere(lista, func):
    """
     Functia parcurge lista si gaseste secventa maxima la care se aplica
    cerinta.
    :type lista : list
    :param lista: lista de intregi
    :return: secventa maxima
    :rtype: list
    """
    poz = -1
    k = 0
    max_len = 0
    for i in range(1, len(lista)):
        if func(lista[i - 1], lista[i]) == True:
            k = k + 1
        else:
            k = 0
        if k >= max_len:
            max_len = k + 1
            poz = i
    return lista[poz - max_len - 1:poz + 1]


def cerinta2(lista):
    """
     Gaseste secventa maxima de elemente cu cel mult 3 valori distincte
    :type lista: list
    :param lista: lista cu numere intregi
    :return: secventa maxima care indeplineste cerinta
    :rtype: list
    """
    a = lista[0]
    b = 0
    c = 0
    i = 1
    poz = 0
    local_max = 1
    max_len = 1
    while lista[i] == a and i < len(lista):
        i = i + 1
    b = lista[i]
    i = i + 1
    while (lista[i] == b or lista[i] == a) and i < len(lista):
        i = i + 1
    c = lista[i]
    i = i + 1
    local_max = i
    while i < len(lista):
        if lista[i] == a or lista[i] == b or lista[i] == c:
            local_max = local_max + 1
            i = i + 1
        else:
            local_max = 2
            a = b
            b = c
            c = lista[i]
        if local_max > max_len:
            max_len = local_max
            poz = i - 1

    return lista[poz - max_len + 1: poz + 1]

def test_cerinta1():
    assert cerinta1(10, 100) == True
    assert cerinta1(0, 0) == False
    assert cerinta1(345, 23135) == True
    assert cerinta1(756, 987) == False
    assert cerinta1(300, 0) == False

def test_prime():
    assert prime_intre_ele(7, 11) == True
    assert prime_intre_ele(23, 29) == True
    assert prime_intre_ele(51, 199) == True
    assert prime_intre_ele(-1, 127) == False
    assert prime_intre_ele(4, 6) == False

def start():
    lista = []

    while True:
        print_menu()
        print_list('Lista curenta este: ', lista)
        optiune = int(input("Optiunea dumneavoastra este: "))
        if optiune == 1:
            lista = read_list()
        elif optiune == 2:
            print('Secventa maxima este: ', parcurgere(lista, cerinta1))
        elif optiune == 3:
            print('Secventa maxima este: ', cerinta2(lista))
        elif optiune == 4:
            print('Secventa maxima este: ', parcurgere(lista, prime_intre_ele))
        elif optiune == 5:
            return
        test_cerinta1()
        test_prime()

start()
