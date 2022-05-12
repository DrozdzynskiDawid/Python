n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
startrow = 0
startcol = 0
while n>0:
    for i in range(n):
        print(matrix[0+startrow][i+startcol], end=" ")
    for i in range(1,n):
        print(matrix[i+startrow][n-1+startcol], end=" ")
    for i in range(n-2,-1,-1):
        print(matrix[n-1+startrow][i+startcol], end=" ")
    for i in range(n-2,0,-1):
        print(matrix[i+startrow][0+startcol], end=" ")
    startrow += 1
    startcol += 1
    n -= 2
