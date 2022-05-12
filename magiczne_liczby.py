def magic_number(n):
    i = len(n) - 1
    for j in range(len(n)-1):
        if (int(n[j])>int(n[j+1])):
            i = j
            break
    for k in range(len(n)-1-i):
        if (int(n[k+i])<int(n[k+i+1])):
            return False
    return True

x = input()
l = []
l.append(x[0])
for i in range (len(x)+1):
    for j in range (len(x)+1):
        l.append(x[i:j])
        for k in range (len(l)-1):
            if (x[i:j]==l[k] or x[i:j]==""):
                l.pop(-1)
                break
result = []
for i in range (len(l)):
    if (magic_number(l[i])==True):
        result.append(int(l[i]))
result = list(set(result))
result.sort()
for i in range (len(result)):
    print(result[i])