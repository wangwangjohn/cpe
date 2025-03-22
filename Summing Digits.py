def solve(n):
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    return n % 9


while (1):

    n = int(input())
    if (n == 0):
        break
    print(solve(n))
