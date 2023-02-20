def consistent(x):
    if len(x) == 1:
        return True
    else:
        #return not x[-1] == x[-2] == 1
        for i in range(len(x)-1):
            if x[i] == x[i+1] == 1:
                return False
    return True


def backtrack_rec(x, n):
    x.append(0)
    for i in range(2):
        x[-1] = i
        if consistent(x):
            if len(x) == n:
                print('[BACKTRACKING RECURSIV] Solutie:', x)
            else:
                backtrack_rec(x[:], n)
    x.pop()


def backtrack_iterativ(n):
    # solutie candidat
    x = [-1]
    while len(x) > 0:
        chosen = False
        print(x)
        while not chosen and x[-1] < 1:
            x[-1] = x[-1] + 1
            chosen = consistent(x)
        print(x)
        if chosen:
            if len(x) == n:
                print('[BACKTRACKING ITERATIV] Solutie:', x)
            else:
                x.append(-1)
        else:
            x = x[:-1]

n = int(input("N = "))
backtrack_rec([], n)
print()
backtrack_iterativ(n)
