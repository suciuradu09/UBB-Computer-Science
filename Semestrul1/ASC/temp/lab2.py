#CEL MAI MIC NUMAR PERFECT MAI MARE DECAT N DAT

n = int(input("Introdu n: "))
aux = n
ok = 1
while ok == 1:
    aux = aux + 1
    s=0
    for i in range(1,aux//2+1):
        if aux % i == 0:
            s = s + i
    if s == aux:
             ok = 0
    
else:
    print(aux)
