n = int(input())
i, j = [int(x) for x in input().split()]
matrix_rows = []
for k in range(n):
    row = [int(x) for x in input().split()]
    matrix_rows.append(row)
matrix_cols = []
for k in range(n):
    col = []
    for l in range(n):
        col.append(matrix_rows[l][k])
    matrix_cols.append(col)
while matrix_rows[i][j] != min(matrix_rows[i]) or matrix_cols[j][i] != min(matrix_cols[j]):
    if matrix_rows[i][j] != min(matrix_rows[i]):
        j = matrix_rows[i].index(min(matrix_rows[i]))
        continue
    if matrix_cols[j][i] != min(matrix_cols[j]):
        i = matrix_cols[j].index(min(matrix_cols[j]))
print(i, j)