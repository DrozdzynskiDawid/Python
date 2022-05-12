n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

res = []
for i in range(n):
    res_row = []
    for j in range(n):
        around = []
        avg = 0
        if matrix[i][j] >= 3:
            res_row.append(1)
        else:
            if i>0:
                around.append(matrix[i-1][j])
            if i<n-1:
                around.append(matrix[i+1][j])
            if j>0:
                around.append(matrix[i][j-1])
            if j<n-1:
                around.append(matrix[i][j+1])
            if j>0 and i>0:
                around.append(matrix[i-1][j-1])
            if j<n-1 and i<n-1:
                around.append(matrix[i+1][j+1])
            if j>0 and i<n-1:
                around.append(matrix[i+1][j-1])
            if j<n-1 and i>0:
                around.append(matrix[i-1][j+1])
            avg = sum(around)/len(around)
            if avg >= 3:
                res_row.append(1)
            else:
                res_row.append(0)
    res.append(res_row)
for el in res:
    print(*el)