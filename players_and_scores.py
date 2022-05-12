matches = int(input())
players = {}
for i in range(matches):
    l = input().split()
    for j in range(2):
        if l[j].split(sep=":")[0] not in players:
            players[l[j].split(sep=":")[0]] = []
            players[l[j].split(sep=":")[0]].append(int(l[j].split(sep=":")[1]))
            players[l[j].split(sep=":")[0]].append(0)
        else:
            players[l[j].split(sep=":")[0]][0] += int(l[j].split(sep=":")[1])
    if int(l[0].split(sep=":")[1]) > int(l[1].split(sep=":")[1]):
        players[l[0].split(sep=":")[0]][1] += 1
    elif int(l[0].split(sep=":")[1]) < int(l[1].split(sep=":")[1]):
        players[l[1].split(sep=":")[0]][1] += 1

res = list(players.items())
res.sort(key = lambda x: x[0])
res.sort(key = lambda x: -x[1][0])
res.sort(key = lambda x: -x[1][1])
for el in res:
   print(el[0])
