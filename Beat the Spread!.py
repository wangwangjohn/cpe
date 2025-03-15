n=int(input())
for k in range(1,n+1):
	a,b=map(int,input().split(" "))
	if(a<b or ((a+b)/2)%1!=0 or ((a-b)/2)%1!=0):
		print('impossible')
	else:
		 i=(a+b)//2
		 j=(a-b)//2
		 print(f'{i} {j}')