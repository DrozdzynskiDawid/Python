def prime(a):
    if int(a) <= 2:
        return True
    for i in range(2,a//2+1):
        if a%i == 0:
            return False
    return True

n = int(input())
for j in range(2, n):
    if prime(j):
        print(j)
