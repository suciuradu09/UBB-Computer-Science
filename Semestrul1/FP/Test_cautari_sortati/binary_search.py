"""
Sa se implementeze un algoritm de cautare binara pe un vector sortat in functie de o cheie data
"""

v1 = [1, 2, 3, 4, 6, 7, 8, 9, 10, 15, 23, 35, 45, 78, 100]
v2 = [2, 3, 5, 7, 11, 21, 45, 65, 79, 101]
v3 = [9, 20, 10, 4, 6, 2, 11, 31, 42, 100]
v4 = [-5, -4, 2, 6, -10, 22, 102, 98, 3]

def binary_search(v, x):
    """
    Functia returneaza pozitia in care se afla numarul cautat
    :param v: vectorul in care cautam rezultatul
    :type v: list
    :param x: numarul cautat
    :type x: int
    """
    st = 1
    dr = len(v)
    middle = (st + dr) // 2
    while st <= dr:
        if v[middle] < x:
            st = middle + 1
        elif x < v[middle]:
            dr = middle - 1
        elif x == v[middle]:
            return middle
        middle = (st + dr) // 2
    return False


def merge(x, y):
    """
    Functia concateneaza doua siruri de numere crescatoare
    :param x: primul sir de numere
    :param y: al doilea sir de numere
    """
    i = 0
    j = 0
    rez = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            rez.append(x[i])
            i = i + 1
        elif x[i] > y[j]:
            rez.append(y[j])
            j = j + 1
        elif x[i] == y[j]:
            rez.append(x[i])
            rez.append(y[j])
            i = i + 1
            j = j + 1

    rez.extend(x[i:])
    rez.extend(y[j:])

    return rez


def merge_sort(list):
    """
    Algoritmul de sortare Merge-sort
    :param list: lista de sortat
    :type list: list
    """
    list_length = len(list)

    if list_length <= 1:
        return list

    middle = list_length // 2

    left = list[:middle]
    right = list[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def quick(v, st, dr):
    i = st
    j = dr
    val = v[(st+dr)//2]
    while i <= j:
        while v[i] < val:
            i = i + 1
        while val < v[j]:
            j = j - 1
        if i <= j:
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
            i = i + 1
            j = j - 1
    if st < j:
        quick(v, st, j)
    if i < dr:
        quick(v, i, dr)

def insertion_sort(v):
    for i in range(len(v)):
        poz = i - 1
        a = v[i]
        while a < v[poz] and poz >= 0:
            v[poz + 1] = v[poz]
            poz = poz - 1
        v[poz + 1] = a

def bubble_sort(v):
    for i in range(len(v)):
        for j in range(0, i - 1):
            if v[i] < v[j]:
                v[i], v[j] = v[j], v[i]

def divide_et_impera(v):
    """
    Cauta elementul minim din vector
    """
    mij = len(v) // 2
    if len(v) <= 1:
        return v[0]
    else:
        return min(divide_et_impera(v[:mij]), divide_et_impera(v[mij:]))

def run():
    a = binary_search(v1, 8)
    b = merge(v1, v2)
    c = merge_sort(v3)
    # quick(v3, 0, len(v3)-1)
    # insertion_sort(v4)
    # bubble_sort(v3)
    x = divide_et_impera(v4)
    print(x)
run()
