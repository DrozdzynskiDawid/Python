def seats_in_row(row_number):
    l = []
    for i in range(5):
        l.append(5*(row_number-1) + i + 2)
    if row_number % 2 == 0:
        l.reverse()
    return l


t = int(input())
for i in range(t):
    seat = int(input())
    if seat == 1:
        print("poor conductor")
    else:
        row = ((seat - 2) // 5) + 1
        seats_list = seats_in_row(row)
        if seat == seats_list[0] or seat == seats_list[1]:
            direction = "L"
            if seat == seats_list[0]:
                position = "W"
            else:
                position = "A"
        else:
            direction = "R"
            if seat == seats_list[2]:
                position = "A"
            elif seat == seats_list[3]:
                position = "M"
            else:
                position = "W"
        print(row, position, direction)
