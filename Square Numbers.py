import math
while(True):
	n,m=map(int,input().split(" "))
	if(n==0 or m==0):
		break
	count=0
	for i in range(n,m+1):
		if math.isqrt(i)**2==i:
			count+=1
	print(count)