def can_place_flowebed(flowerbed,n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == flowerbed[i] -1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return n < 0
        
size = int(input())
n = int(input())
flowerbed = list(map(int,input().split()))
if can_place_flowebed(flowerbed,n):
    print("True")
else:
    print("False")