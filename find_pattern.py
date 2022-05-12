def find_pattern(string, pattern):
    if len(pattern) > len(string):
        return "NO"
    result = string.find(pattern)
    if result == -1:
        return "NO"
    return "YES"
s = input()
p = input()
print(find_pattern(s,p))