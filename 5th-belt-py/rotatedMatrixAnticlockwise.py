rows = int(input())
matrix = []
for i in range (rows):
    r = list(map(int,input().split()))
    matrix.append(r)
    
transpose = [[matrix[i][j] for i in range(rows)]for j in range(rows)]
rotated = transpose[::-1]
for i in rotated:
    print(" ".join(map(str,i)))