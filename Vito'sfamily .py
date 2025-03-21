def solve(n, nums):
    nums.sort()
    mid = nums[n//2]
    ans = 0
    for i in nums:
        ans += abs(i-mid)
    return ans


T = int(input())
for i in range(T):
    nums = list(map(int, input().split(" ")))
    print(solve(nums[0], nums[1:]))
