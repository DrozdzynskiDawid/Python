s1 = input()
s2 = input()
d1 = {}
d2 = {}
counter = 0
for i in range(len(s1)):
    if s1[i] in d1:
        d1[s1[i]] += 1
    else:
        d1[s1[i]] = 1
for j in range(len(s2)):
    if s2[j] in d2:
        d2[s2[j]] += 1
    else:
        d2[s2[j]] = 1

print(d1,d2)