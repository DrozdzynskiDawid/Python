def check_slice(l):
    l.sort()
    if len(l) <= 2:
        return True
    diff = l[1] - l[0]
    for i in range(1, len(l)-1):
        if diff != l[i+1] - l[i]:
            return False
    return True

a = [int(x) for x in input().split()]
print(check_slice(a))