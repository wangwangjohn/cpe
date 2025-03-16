while(True):
	n=int(input())
	total=n
	empty=n
	while empty>=3:
		new=empty//3
		total+=new
		empty=empty%3+new
	if(empty==2):
		total+=1
	print(total)
