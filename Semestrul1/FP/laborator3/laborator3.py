"""
Scrieti o aplicatie care are interfata utilizator tip consolă cu un meniu:
1 Citirea unei liste de numere intregi
2,3 Gasirea secventelor de lungime maxima care respectă o proprietatea dată. Fiecare student primeste 2 proprietati din lista
de mai jos.
4 Iesire din aplicatie.

"""


def print_menu():
    print("1.Citeste de la tastatura o lista de numere rationale (float).")
    print("2.Afiseaza media aritmetica a numerelor din lista.")
    print("3.Afiseaza lista numerelor intregi.")
    print("4.Verifica daca suma partii fractionare a tuturor numerelor este > 1.")
    print("5.Iesire din aplicatie.")


def populate_list(the_list):
    the_list.append(2.45)
    the_list.append(5.23)
    the_list.append(9.23)
    the_list.append(1.01)


def print_list(message, lst):
    print(message, lst)


def read_list():
    # FORMAT: 3.21, 4.5, 10.09
    the_list_as_string = input("Dati lista in formatul cerut: ")
    print('Lista ca string', the_list_as_string, type(the_list_as_string))
    list_of_strings = the_list_as_string.split(",")
    number_list = []

    for elem in list_of_strings:
        elem_float = float(elem)
        number_list.append(elem)

    number_list = the_list_as_string.split(",")
    # print('Lista de numere',number_list,type(number_list),type(number_list[0]))
    return number_list


def compute_mean(the_list):
    """
    calculeaza media aritmetica a numerelor dintr--o lista data
    :param the_list: lista pentri care se doreste calcularea mediei aritmetie
    :type the_list: list
    :return: media aritmetica a numerelor din lista
    :rtype: float
    """
    suma = 0
    for elem in the_list:
        elem = float(elem)
        suma = suma + elem
    return suma/len(the_list)


def get_all_integers(the_list):
    """
    Gaseste toate numerele intregi din lista
    :type the_list: list
    :param the_list:  lista data cu numere
    :return: lista cu toate numerele intregi din lista
    :rtype: list
    """
    elems = []
    for el in the_list:
        # math.floor(el) == el
        if el == int(el):
            elems.append(el)
    return elems


def is_franc_greater_than(the_list, value):
    """
    Verifica daca suma partilor fractionare a elementelor din lista
    este mai mare ca o valoare data
    :type the_list : list
    :param the_list: lista cu numre rationale
    :param value: valoarea cu care se compara
    :return: Adevarat daca suma > valoarea, si Fals daca suma < valoarea data
    :rtype: bool
    """
    sum_frac = 0
    for el in the_list:
        el_frac = el - int(el)
        sum_frac = sum_frac + el_frac

    return sum_frac > value


def start():
    current_list = []
    populate_list(current_list)
    while True:
        print_menu()
        print_list('Lista curenta este: ', current_list)
        option = int(input("Optiunea dumneaoastra este: "))
        if option == 1:
            current_list = read_list()
        elif option == 2:
            print('Media aritmetica a numerelor este: ', compute_mean(current_list))
        elif option == 3:
            print_list('Lista cu numere intregi este: ', get_all_integers(current_list))
        elif option == 4:
            crt_value = 1
            if is_franc_greater_than(current_list, crt_value):
                print("Suma e mai mare ca 1")
            else:
                print("Suma nu e mai mare ca 1.")
        elif option == 5:
            return


start()
