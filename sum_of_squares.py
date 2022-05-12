interval = tuple(input().split())
i = int(interval[0])
sum = 0
while i <= int(interval[1]):
    sum = sum + (i*i)
    i += 1
print(sum)