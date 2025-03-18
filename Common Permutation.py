while True:
    try:
        n = input().strip().lower()
        m = input().strip().lower()
    except EOFError:
        break

    count = [0] * 26
    result = [0] * 26

    for i in n:
        if 'a' <= i <= 'z':
            count[ord(i) - ord("a")] += 1

    for j in m:
        if 'a' <= i <= 'z':
            idx = ord(j) - ord('a')
            if count[idx] > 0:
                count[idx] -= 1
                result[idx] += 1

    for i in range(26):
        print(chr(i + ord('a')) * result[i], end="")
    print()
