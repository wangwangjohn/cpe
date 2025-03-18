while (True):
    try:
        n, m = map(int, input().split(" "))
        a = []

    except EOFError:
        break
    if (n < m or n <= 0 or m <= 1):
        print('Boring!')
        continue
    while n % m == 0:
        a.append(n)
        n = n//m

    if n == 1:
        a.append(1)
        print(" ".join(map(str, a)))
    else:
        print('Boring!')
