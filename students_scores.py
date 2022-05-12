# wczytanie danych
students = {}
tests = {}
n = int(input())
for i in range(n):
    data = input().split()
    student_name = data[0]
    students[student_name] = []
    for j in range(1, len(data)):
        students[student_name].append(float(data[j].split(sep = ":")[1]))
        test_id = data[j].split(sep = ":")[0]
        if test_id in tests:
            tests[test_id].append(float(data[j].split(sep = ":")[1]))
        else:
            tests[test_id] = []
            tests[test_id].append(float(data[j].split(sep = ":")[1]))
# liczenie średnich i wypisanie
s_res = {}
for k, v in students.items():
    x = float(sum(v)/len(v))
    s_res[k] = x
s_list = list(s_res.items())
s_list.sort(key = lambda x: x[0])
for i in range(len(s_list)):
    print(s_list[i][0], s_list[i][1])

t_res = {}
for k, v in tests.items():
    x = float(sum(v)/len(v))
    t_res[k] = x
t_list = list(t_res.items())
t_list.sort(key = lambda x: x[0])
for i in range(len(t_list)):
    print(t_list[i][0], t_list[i][1])
