n = int(input())
l = [int(x) for x in input().split()]
l.sort()
for el in l:
    print(el, end=" ")
