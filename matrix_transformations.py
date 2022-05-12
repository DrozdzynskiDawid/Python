def read_matrix(h):
    res = []
    for i in range(h):
        row = input().split()
        res.append(row)
    return res

def Transpose(matrix, h, w):
    res = []
    for i in range(w):
        row = []
        for j in range(h):
            row.append(matrix[j][i])
        res.append(row)
    return res

def ReverseRow(a, matrix):
    matrix[a].reverse()
    return matrix

def ReverseColumn(a, matrix, h):
    for i in range(h//2):
        matrix[i][a], matrix[h-i-1][a] = matrix[h-i-1][a], matrix[i][a]
    return matrix

rows, columns = [int(x) for x in input().split()]
matrix = read_matrix(rows)
k = int(input())
for op in range(k):
    operation = input().split()
    if operation[0] == "T":
        matrix = Transpose(matrix, rows, columns)
        rows, columns = columns, rows
    elif operation[0] == "RR":
        matrix = ReverseRow(int(operation[1]),matrix)
    elif operation[0] == "RC":
        matrix = ReverseColumn(int(operation[1]),matrix, rows)
for el in matrix:
    print(*el)
