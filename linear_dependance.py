def is_linear(v1, v2):
    size = len(v1)
    if v1 == [0] * size or v2 == [0] * size:
        return False
    for i in range(size):
        if v2[i] != 0:
            r = v1[i]/v2[i]
    for i in range(size):
        if v2[i] * r != v1[i]:
            return False
    return True

n = int(input())
vectors = []
for i in range(n):
    row = [int(x) for x in input().split()]
    vectors.append(row)
for i in range(n):
    col = []
    for j in range(n):
        col.append(vectors[j][i])
    vectors.append(col)
counter = 0
for k in range(len(vectors)):
    for l in range(k+1, len(vectors)):
        if is_linear(vectors[k], vectors[l]):
            counter += 1
print(counter)