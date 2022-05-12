n = int(input())
for i in range(n):
    a, m = input().split()
    a = int(a)
    m = int(m)
    if m <= a:
        print(1)
        continue
    x = m // a + 1
    power = 1
    counter = 0
    while x >= power:
        power *= 2
        counter += 1
    print(counter)