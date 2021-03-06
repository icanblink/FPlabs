#9. A number of n soldiers, numbered 1, ..., n, are considered. A matrix A(n,n) is given, with the
#meaning: A[i,j] is 1 if i is the superior of j and 0 otherwise. Determine all possible modalities to
#place the soldiers in a line such that no soldier has a superior before him.

def print_it(sol, n):
    for i in range(1, n + 1):
        print sol[i],
    return

def succesor(n, k, sol):
    if sol[k] < n:
        sol[k] = sol[k] + 1;
        return True
    return False

def is_valid(k, sol, a):
    for i in range(1, k):
        if sol[k] == sol[i] : return False

    for i in range(1, k):
        if a[sol[i]][sol[i + 1]] == 1 : return False
    return True

def is_solution(k, n):
    return (k == n + 1)

def bcktr(n, k, sol, a):
    if is_solution(k, n):
        print_it(sol, n)
        print '\n'
    else :
        sol[k] = 0
        while succesor(n, k, sol) :
            if is_valid(k, sol, a) : bcktr(n, k + 1, sol, a)

def main():
    sol = []
    n = input('n=')
    for i in range(n + 1): sol.append(i)
    a = [[0 for col in range(n + 1)] for row in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            a[i][j] = int(input(str("A[" + str(i) + "][" + str(j) + "]=")))
            if a[i][j] == 0 : a[j][i] = 1
    bcktr(n, 1, sol, a)

main()
