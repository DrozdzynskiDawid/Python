def cipher(k, t):
    result = ""
    for i in range(len(t)):
        if t[i].isupper():
            if ord(t[i]) - k < 65:
                result += chr(ord(t[i]) - k + 26)
            else:
                result  += chr(ord(t[i]) - k)
        else:
            if ord(t[i]) - k < 97:
                result += chr(ord(t[i]) - k + 26)
            else:
                result  += chr(ord(t[i]) - k)        
    return result

key = int(input()) % 26
plain = input()
print(cipher(key,plain))
