x = input()
n = len(x)
for i in range(1, n):
    d = {}
    j = 0
    while j <= n - i:
        if int(x[j:j+i]) in d:
            d[int(x[j:j+i])] += 1
        else:
            d[int(x[j:j+i])] = 1
        j += 1
    l = list(d.items())
    l.sort(key = lambda x: x[0])
    l.sort(key = lambda x: -x[1])
    print(l[0][0])
print(int(x))