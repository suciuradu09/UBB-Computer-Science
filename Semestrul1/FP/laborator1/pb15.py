#Cel mai mare nr prim mai mic decat n

def isPrime(n):
    if n <= 1 :
        return 0
    else:
        k = 0
        for d in range(2,n//2 + 1):
            if n % d == 0:
                k = k + 1
        if k:
            return 0
        else:
            return 1

def pb15():
    numar = int(input("N: "))
    ok = 1
    numar = numar - 1
    while numar > 1 and ok == 1:
        if isPrime(numar) == 1:
            ok = 0
    if ok == 0:
        print(numar)
    else:
        print("Numar inexistent!")
