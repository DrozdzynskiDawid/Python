def read_matrix(h):
    matrix = []
    for i in range(h):
        matrix.append(input().split())
        matrix[i] = [int(x) for x in matrix[i]]
    return matrix

n = int(input())
matrix = read_matrix(n)
maxsum = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        for k in range(i, len(matrix)):
            for l in range(j, len(matrix[0])):
                currsum = 0
                for row in range(i, k+1):
                    for col in range(j, l+1):
                        currsum += matrix[row][col]
                maxsum = max(currsum, maxsum)
print(maxsum)