def read_matrix(h):
    matrix = []
    for i in range(h):
        matrix.append(input().split())
        matrix[i] = [int(x) for x in matrix[i]]
    return matrix

def create_result(w, h):
    matrix = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(0)
        matrix.append(row)
    return matrix

w1, h1 = input().split()
matrix1 = read_matrix(int(h1))
w2, h2 = input().split()
matrix2 = read_matrix(int(h2))
result = create_result(int(w2), int(h1))
for i in range(int(h1)):
    for j in range(int(w2)):
        for k in range(int(h2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for el in result:
    for item in el:
        print(item, end=" ")
    print()