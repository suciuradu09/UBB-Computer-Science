# laborator1

def sumaNr():
    s = 0
    x = int(input("N = "))
    for i in range(x):
        y = int(input())
        s = s + y
    print("Suma numerelor este: ", s)


def verifPrim():
    ok = 1
    x = int(input("N = "))
    if x < 2:
        ok = 0
    else:
        for i in range(2, x // 2):
            if x % i == 0:
                ok = 0
    if ok == 1:
        print("numarul e prim")
    elif ok == 0:
        print("numarul nu e prim")


def cmmdc():
    a = int(input("citeste a: "))
    b = int(input("citeste b: "))
    if a <= 0 or b <= 0:
        print("eroare")
    else:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        print("cel mai mare divizor comun: ", a)


sumaNr()
#verifPrim()
#cmmdc()