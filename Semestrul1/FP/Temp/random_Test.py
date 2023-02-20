def crit(el):
    return el[1]


lista = [[1, 'a'], [2, 'c'], [3, 'd'], [4, 'b'], [5, 'e']]
lista.sort(reverse=True, key=crit)
print(lista)
