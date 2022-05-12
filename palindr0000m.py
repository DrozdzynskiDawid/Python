def palindr0000m(a):
    if a[0] == "0":
        return False
    if len(a) == 1:
        return True
    x = len(a) - 1
    while a[x] == "0":
        x -= 1
    a = a[0:x+1]
    return a == a[::-1]

number = input()
n = len(number)
counter = 0
if palindr0000m(number) == True:
    counter += 1
for i in range(1, n):
    j = 0
    while j <= n-i:
        if palindr0000m(number[j:j+i]) == True:
            counter += 1
        j += 1
print(counter)