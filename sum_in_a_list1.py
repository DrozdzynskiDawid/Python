l = list(input().split())
interval = tuple(input().split())
i = int(interval[0])
j = int(interval[1])
result = 0

while i<=j:
    result = result + int(l[i])
    i += 1

print(result)