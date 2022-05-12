h = int(input())
n = int(input())

for k in range(n):
    for i in range (h):
        for j in range (i+1):
            print("*", end=" ")
        print()
    h += 1