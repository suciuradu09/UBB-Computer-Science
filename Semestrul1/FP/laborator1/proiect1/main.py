
def perfect(nr):
    s = 0
    for d in range(1,nr//2 + 1):
        if nr % d == 0 :
            s = s + d
    if s == nr :
        return 1
    else : return 0

def perf():
    n = int(input("Introdu n: "))
    numar = n + 1
    while perfect(numar) == 0:
        numar = numar + 1
    else : print(numar)

perf()