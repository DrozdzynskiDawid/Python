n, m = input().split()
s = input()
maxs = s
for i in range(int(m)):
    a, b, x = input().split(sep=";")
    a = int(a)
    b = int(b)
    if a < b:
        s = s[0:a] + x + s[b+1:len(s)]
    else:
        s = s[0:b] + x + s[a+1:len(s)]
    if len(s) > len(maxs):
        maxs = s

print(s,maxs,sep='\n')