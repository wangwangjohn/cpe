# 氣泡排序法
def bubbleSort(a):
    L = len(a)
    sum = 0
    for i in range(L-1):
        for i in range(L-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                sum += 1
    return sum


n = int(input())
for i in range(n):
    l = int(input())
    a = list(map(int, input().split(" ")))
    sum = bubbleSort(a)
    print("Optimal train swapping takes {} swaps.".format(sum))
