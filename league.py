teams = {}
n, m , t = [int(x) for x in input().split()]
for i in range(n):
    teams[input()] = 0
for i in range(m):
    match = input().split(sep=":")
    t1 = match[0]
    t2 = match[1]
    g1 = match[2]
    g2 = match[3]
    if int(g1) > int(g2):
        teams[t2] += 1
    else:
        teams[t1] += 1
res = []
for key, value in teams.items():
    if (n-1-value) >= t:
        res.append(key)
res.sort()
print(*res, sep="\n")