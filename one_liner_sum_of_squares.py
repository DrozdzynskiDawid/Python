s = input()
print(sum(list(map(lambda x: int(x)*int(x),list(range(int(s.split()[0]),int(s.split()[1])+1))))))