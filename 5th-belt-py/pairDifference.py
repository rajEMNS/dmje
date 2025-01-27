def find_pair_with_difference(n, arr, k):
    i, j = 0, 1 
    while i < n and j < n:
        if i != j and arr[j] - arr[i] == k:
            return 1 
        elif arr[j] - arr[i] < k:
            j += 1 
        else:
            i += 1  
    return 0  

n = int(input())  
arr = list(map(int, input().split()))  
k = int(input()) 

print(find_pair_with_difference(n, arr, k))