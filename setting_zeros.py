n, m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

matrix0_row = []
for row in matrix:
    if 0 in row:
        new_row = [0]*m
    else:
        new_row = row
    matrix0_row.append(new_row)
matrix1 = list(zip(*matrix))
matrix0_col = []
for col in matrix1:
    if 0 in col:
        new_col = [0]*m
    else:
        new_col = list(col)
    matrix0_col.append(new_col)
matrix0_col = list(zip(*matrix0_col))

for i in range(n):
    for j in range(m):
        if matrix0_row[i][j] != matrix0_col[i][j]:
            matrix0_row[i][j] = 0
for el in matrix0_row:
    print(*el) 