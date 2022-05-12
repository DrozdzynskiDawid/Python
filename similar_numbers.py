def similar(a, b):
    return abs(a - b) == 1

n = int(input())
l = [int(a) for a in input().split()]
for i in range(n-1):
    for j in range(i, n):
        if similar(l[i], l[j]) == True:
            print("YES")
            exit()
print("NO")