import math
def solve(n,m):
	n=int(n,2)
	m=int(m,2)
	if math.gcd(n,m)>1:return f'All you need is love!'
	return f'Love is not all you need!'
T=int(input())
for i in range(T):
	n=input()
	m=input()
	print(f'Pair #{i+1}: {solve(n,m)}')