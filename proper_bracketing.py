def proper_bracketing(s):
    if s[0] == ")" or s[0] == "}" or s[0] == "]":
        return False
    if s.count("{") != s.count("}") or s.count("(") != s.count(")") or s.count("[") != s.count("]"):
        return False
    for i in range(len(s)-1):
        if s[i] == "(":
            if s[i+1] == "}" or s[i+1] == "]":
                return False
        if s[i] == "[":
            if s[i+1] == "}" or s[i+1] == ")":
                return False
        if s[i] == "{":
            if s[i+1] == ")" or s[i+1] == "]":
                return False
    return True
    
s = input()
print(proper_bracketing(s))