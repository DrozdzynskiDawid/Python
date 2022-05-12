l = [int(x) for x in input().split()]
n = len(l)
maxsum = 0
for i in range(n):
    sum_in_list = 0
    for j in range(i,n):
        sum_in_list += l[j]
        if sum_in_list > maxsum:
            maxsum = sum_in_list
print(maxsum)