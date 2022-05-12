s = input().lower()
max_counter = 0
letter = "z"
for i in range(len(s)):
    counter = 0
    if 97 <= ord(s[i]) <= 122:
        counter = s.count(s[i])
        if counter > max_counter and ord(letter) > ord(s[i]):
            letter = s[i]
            max_counter = counter
print(letter)