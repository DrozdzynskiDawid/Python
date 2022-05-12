def distance(i1, j1, i2, j2):
    if i2 % i1 == 0 and j2 % j1 == 0:
        return abs(i1-i2) + abs(j1-j2)
    return 1000
n = int(input())
matrix = []
for a in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
positions = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            positions.append([i+1,j+1])
dist = []
for k in range(len(positions)):
    for l in range(k+1, len(positions)):
        dist.append(distance(positions[k][0],positions[k][1],positions[l][0],positions[l][1]))
dist.sort()
print(dist[0])
