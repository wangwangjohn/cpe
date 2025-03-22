def solve(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def solve2(n):
    if solve(n) and solve(int(str(n)[::-1])) and n != int(str(n)[::-1]):
        return f'{n} is emirp.'
    elif solve(n):
        return f'{n} is prime.'
    else:
        return f'{n} is not prime.'


while (1):
    try:
        n = int(input())
    except EOFError:
        break
    print(solve2(n))
