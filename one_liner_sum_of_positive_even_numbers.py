s = input()
print(sum(list(map(lambda x: int(x) if int(x) % 2 == 0 and int(x) > 0 else 0, list(s.split())))))