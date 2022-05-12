def read_matrix(h):
    matrix = []
    for i in range(h):
        matrix.append(input().split())
        matrix[i] = [int(x) for x in matrix[i]]
    return matrix

n, m = [int(x) for x in input().split()]
matrix = read_matrix(m)
sorted_matrix = []
for i in range(n):
    col = []
    for j in range(m):
        col.append(matrix[j][i])
    col.sort()
    sorted_matrix.append(col)

for i in range(m):
    for j in range(n):
        print(sorted_matrix[j][i], end=" ")
    print()