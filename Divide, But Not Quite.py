while (True):
    n, m = map(int, input().split(" "))
    a = []
    if (n < m or m <= 1 or n < 0):
        print("Boring!")
        continue
    while n % m == 0:
        a.append(n)
        n = n//m

    if n == 1:
        a.append(1)
        print(" ".join(map(str, a)))
    else:
        print("Boring!")
