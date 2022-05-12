def grade(pts, pts_max):
    result = pts/pts_max
    if result < 0.5:
        return 2
    elif result < 0.7:
        return 3
    elif result < 0.9:
        return 4
    else:
        return 5

students = {}
grades = {}
final_grades = {}
n, s = [int(x) for x in input().split()]
for i in range(n):
    name, index = input().split()
    students[name] = index
    grades[name] = [0] * s
    final_grades[name] = 0

k = int(input())
for i in range(k):
    entry = input().split()
    if len(entry) == 2:
        id = entry[0]
        pts, pts_max = entry[1].split(sep="/")
    elif len(entry) == 3:
        id = entry[0]
        pts, pts_max = entry[2].split(sep="/")
    if id in students.keys():
        for j in range(s):
            if grades[id][j] == 0:
                grades[id][j] = grade(int(pts), int(pts_max))
                break
    else:
        if id[0] == "i":
            id = id[3:]
        for key in students.keys():
            if students[key] == id:
                for j in range(s):
                    if grades[key][j] == 0:
                        grades[key][j] = grade(int(pts), int(pts_max))
                        break

for student, values in grades.items():
    avg = sum(values)/s
    if avg < 3:
        grades[student] = 2
    elif avg < 3.5:
        grades[student] = 3
    elif avg < 4.5:
        grades[student] = 4
    else:
        grades[student] = 5
res = list(grades.items())
res.sort(key = lambda x: x[0])
for el in res:
    print(*el)
