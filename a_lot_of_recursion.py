import sys
sys.setrecursionlimit(10000)
def a(n, d):
    if n in d:
        return d[n]
    
    d[n] = a(n-a(a(n-1, d), d), d) + 1
    return d[n]

x = int(input())
print(a(x, {1: 1}))