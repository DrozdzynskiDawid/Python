nm = tuple(input().split())
letters = list(input().split())

for i in range(int(nm[1])):
    swap = list(input().split())
    letters[int(swap[0])], letters[int(swap[1])] = letters[int(swap[1])], letters[int(swap[0])]

for j in range(len(letters)):
    print(int(letters[j]), end=" ")