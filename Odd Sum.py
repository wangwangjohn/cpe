n=int(input())
for i in range(1,n+1):
	sum=0
	a=int(input())
	b=int(input())
	if(a>b):
		c=a
		a=b
		b=a
	for j in range(a,b+1):
		if j%2!=0:
			sum+=j
	print(f'Case {i}: {sum}')