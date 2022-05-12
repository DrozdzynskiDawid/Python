def palindrome_without2letters(t):
    if t.lower() == t[::-1].lower():
        return True
    for i in range(len(t)):
        t1 = t[0:i] + t[i+1:len(t)]
        if t1.lower() == t1[::-1].lower():
            return True
        else:
            for j in range(len(t1)):
                t2 = t1[0:j] + t1[j+1:len(t1)]
                if t2.lower() == t2[::-1].lower():
                    return True            
    return False

s = input()

if palindrome_without2letters(s) == True:
    print("YES")
else:
    print("NO")