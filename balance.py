n = int(input())
weights = input().split()
weights = [int(x) for x in weights]
s2 = sum(weights)
s1 = 0
minimum = s2
for t in range(n-1):
    s2 -= weights[t]
    s1 += weights[t]
    if abs(s1-s2) < minimum:
        minimum = abs(s1-s2)
'''
for t in range(n-1):
    s1 = sum(weights[0:t+1])
    s2 = sum(weights[t+1:n])
    if abs(s1-s2) < minimum:
        minimum = abs(s1-s2)
'''
print(minimum)