s = input()
vowels = ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y")
for vowel in vowels:
    s = s.replace(vowel,"")

print(s)