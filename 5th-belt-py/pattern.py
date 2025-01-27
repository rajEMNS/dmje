n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    subarray = []
    for j in range(i,n):
        subarray.append(a[j])
        print(" ".join(map(str,subarray)))
    
    
    