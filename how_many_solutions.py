n, x, y = input().split()
n = int(n)
x = int(x)
y = int(y)
counter = 0
for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                if (x*a*a) + (y*b*b) == (x*c*c) + (y*d*d):
                    counter += 1
print(counter)