n = int(input())
h = input().split()
h = [int(x) for x in h]
counter = 0
maxcounter = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        counter += 1
    else:
        counter = 0
    if counter > maxcounter:
        maxcounter = counter
print(maxcounter)
