n = int(input())
l = list(input().split())
total = 0.0

for i in range(0, n):
    total = total + 1/float(l[i])

print(1/total)