def all_numbers(numbers):
    numbers1 = numbers.copy()
    numbers1.sort()
    for i in range(1,9):
        if i != numbers1[i-1]:
            return False
    return True

sudoku = []
for i in range(9):
    row = input().split()
    row = [int(x) for x in row]
    sudoku.append(row)
    if all_numbers(row) == False:
        print("False")
        quit()

for j in range(9):
    col = []
    for k in range(9):
        col.append(sudoku[k][j])
    if all_numbers(col) == False:
        print("False")
        quit()

diagonal1 = []
diagonal2 = []
for l in range(9):
    diagonal1.append(sudoku[l][l])
for m in range(9):
    diagonal2.append(sudoku[m][8-m])

if all_numbers(diagonal1) == True and all_numbers(diagonal2) == True:
    print("X")
else:
    print("True")