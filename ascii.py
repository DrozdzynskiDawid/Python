l = input().split()
for i in range(len(l)):
    l[i] = chr(int(l[i],2))
for el in l:
    print(el, end="")