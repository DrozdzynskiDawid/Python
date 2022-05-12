n = int(input())
maxheight = 0
l = []
for k in range(n):
    a = int(input())
    if a > maxheight:
        maxheight = a
    l.append(a)
biggest = 0
height = 1
currl = 0
while height <= maxheight:
    maxl = 0
    for i in range(n):
        currl = 0
        for j in range(i,n):
            if l[j] >= height:
                currl += 1
                if currl > maxl:
                    maxl = currl
            else:
                if currl > maxl:
                    maxl = currl
                break
    area = maxl * height
    if area > biggest:
        biggest = area
    height += 1

print(biggest)
