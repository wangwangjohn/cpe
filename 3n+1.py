def cal(x):
    length = 0
    while x != 1:
        if x % 2 != 0:
            x = 3*x+1
        else:
            x = x//2
        length += 1
    return length+1


maxlength = 0
i, j = map(int, input().split(" "))
start_i, start_j = i, j
if i > j:
    i, j = j, i
for i in range(i, j+1):
    n = cal(i)
    if n > maxlength:
        maxlength = n
print(start_i, start_j, maxlength)
