def f(l, i, res):
    res += int(l[i])
    if i < len(l)-1:
        return f(l, i+1, res)
    return res

x = input().split()
print(f(x, 0, 0))