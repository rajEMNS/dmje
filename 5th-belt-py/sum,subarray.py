def find_subarray_with_sum(nums, target_sum):
    current_sum = 0
    start_index = 0
    sum_map = {}
    
    for end_index, num in enumerate(nums):
        current_sum += num
        
        if current_sum == target_sum:
            print(start_index, end_index)
            return
        
        if current_sum - target_sum in sum_map:
            print(sum_map[current_sum - target_sum] + 1, end_index)
            return
        
        sum_map[current_sum] = end_index

    print("No subarray found")

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
find_subarray_with_sum(nums, k)