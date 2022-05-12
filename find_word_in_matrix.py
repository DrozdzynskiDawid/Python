def read_matrix(h):
    matrix = []
    for i in range(h):
        matrix.append(input())
    return matrix

def rotate(matrix, r, c):
    res = []
    for i in range(c):
        col = ""
        for j in range(r):
            col += matrix[j][i]
        res.append(col)
    return res

n, m = [int(x) for x in input().split()]
word = input()
x = len(word)
matrix = read_matrix(n)
print(matrix)
matrix1 = rotate(matrix, n, m)
print(matrix1)
for row in matrix:
    if len(row) >= x:
        for i in range(m-x+1):
            if word == row[i:i+x] or word[::-1] == row[i:i+x]:
                print("YES")
                exit()
for col in matrix1:
    if len(col) >= x:
        for i in range(n-x+1):
            if word == col[i:i+x] or word[::-1] == col[i:i+x]:
                print("YES")
                exit()
print("NO")
