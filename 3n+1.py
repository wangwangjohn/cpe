while (True):
    n, m = map(int, input().split(" "))
    maxLength = 0
    oldn = n
    oldm = m
    if (n > m):
        temp = n
        n = m
        m = temp
    for i in range(n, m+1):
        x = i
        length = 0
        while (True):
            if x == 1:
                length += 1
                break
            if x % 2 != 0:
                x = 3*x+1
                length += 1
            else:
                x = x//2
                length += 1
        if (length > maxLength):
            maxLength = length
    print(f'{oldn} {oldm} {maxLength}')
