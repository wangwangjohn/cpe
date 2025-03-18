def fib():
    L = [0]*50
    L[0] = 1
    L[1] = 1
    for i in range(2, len(L)):
        L[i] = L[i-1]+L[i-2]
    return L


def solve(n):
    temp = n
    a = ''
    for i in L[::-1]:
        if temp >= i:
            a += '1'
            temp -= i
        elif a:
            a += '0'
    return f'{n} = {a[:-1]} (fib)'


L = fib()
T = int(input())
for i in range(T):
    n = int(input())
    print(solve(n))
