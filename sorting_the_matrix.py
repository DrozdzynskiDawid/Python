n, m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    row = input().split()
    for j in range(m):
        matrix.append(int(row[j]))
matrix.sort()

for k in range(n):
    res_row = []
    l = 0 + k
    while l < len(matrix):
        res_row.append(matrix[l])
        l += n
    print(*res_row)
