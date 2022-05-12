def all_the_same(l):
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            return False
    return True

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(all_the_same(l))