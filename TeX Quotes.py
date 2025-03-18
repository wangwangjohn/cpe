count = 0
while (True):
    try:
        n = list(input())
        for i in range(len(n)):
            if n[i] == '"':
                if count % 2 == 0:
                    n[i] = "``"
                else:
                    n[i] = "''"
                count += 1
        print(''.join(n))
    except EOFError:
        break
