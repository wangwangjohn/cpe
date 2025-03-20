def solve(n, nums):
    count = 0
    while (n > 1):
        n -= 1
        for i in range(n):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                count += 1
    return f'Optimal train swapping takes {count} swaps.'


T = int(input())
for i in range(T):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    print(solve(n, nums))
