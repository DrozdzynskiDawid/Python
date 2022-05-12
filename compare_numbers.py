t = int(input())

for i in range(t):
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n > m:
        print(n," is greater than ",m)
    elif n < m:
        print(n," is smaller than ",m)
    else:
        print("n is equal m: ",n)
    
