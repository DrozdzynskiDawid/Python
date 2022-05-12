n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
counter = 0
for i in range(n):
    for j in range(i,n):
        if l[i] > l[j]:
            counter += 1
print(counter)