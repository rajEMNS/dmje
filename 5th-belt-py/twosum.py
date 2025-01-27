def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            print(num_indices[complement], i)
            return
        num_indices[num] = i
    print(-1)

n = int(input())
if n == 0:
    print(-1)
else:
    nums = list(map(int, input().split()))
    target = int(input())
    two_sum(nums, target)