def C_K(temp):
    if temp + 273.15 >= 0:
        return temp + 273.15
    return "NO"

def C_F(temp):
    if (temp * 1.8) + 32 >= -459.67:
        return (temp * 1.8) + 32
    return "NO"

def K_C(temp):
    if temp - 273.15 >= -273.15:
        return temp - 273.15
    return "NO"

def K_F(temp):
    if (temp - 273.15)* 1.80 + 32.00 >= -459.67:
        return (temp - 273.15)* 1.80 + 32.00
    return "NO"

def F_K(temp):
    if (temp - 32) / 1.8 + 273.15 >= 0:
        return  (temp - 32) / 1.8 + 273.15
    return "NO"

def F_C(temp):
    if (temp - 32) /1.8 >= -273.15:
        return (temp - 32) /1.8 
    return "NO"


n = int(input())
results = []
for i in range(n):
    l = list(input().split())
    temperature = int(l[0])
    s1 = l[1]
    s2 = l[2]
    if s1 == "Kelvin" and s2 == "Celsius":
        results.append(K_C(temperature))
    if s1 == "Kelvin" and s2 == "Fahrenheit":
        results.append(K_F(temperature))
    if s1 == "Celsius" and s2 == "Kelvin":
        results.append(C_K(temperature))
    if s1 == "Celsius" and s2 == "Fahrenheit":
        results.append(C_F(temperature))
    if s1 == "Fahrenheit" and s2 == "Celsius":
        results.append(F_C(temperature))
    if s1 == "Fahrenheit" and s2 == "Kelvin":
        results.append(F_K(temperature))

for j in range(n):
    if type(results[j]) is float:
        print("%.2f" % results[j])
    else:
        print(results[j])
