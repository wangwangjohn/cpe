def solve(n):
    degree = 0
    current = n
    while len(current) > 1:
        fooSum = sum(map(int, current))
        current = str(fooSum)
        degree += 1
        if fooSum % 9 != 0:
            return f'{n} is not a multiple of 9.'
    if current == '9':
        return f'{n} is a multiple of 9 and has 9-degree {degree}.'
    else:
        return f'{n} is not a multiple of 9.'


while (1):
    n = input()
    if n == '0':
        break
    elif n == '9':
        print(f'9 is a multiple of 9 and has 9-degree 1.')
    else:
        print(solve(n))
