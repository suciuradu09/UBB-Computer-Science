"""
Generați cel mai mic număr perfect mai mare decât un număr dat. Un număr este perfect daca
este egal cu suma divizorilor proprii. Ex. 6 este un număr perfect (6=1+2+3)
"""

def perfect(nr):
    s = 0
    for d in range(1, nr//2 + 1):
        if nr % d == 0:
            s = s + d
    if s == nr:
        return 1
    else:
        return 0

def perf():
    n = int(input("N: "))
    numar = n + 1
    while perfect(numar) == 0:
        numar = numar + 1
    else:
        print(numar)

perf()
