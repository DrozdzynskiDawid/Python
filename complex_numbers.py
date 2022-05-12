import cmath
number_real, number_imag = input().split(sep=" + ")
number_imag = number_imag[0:-1]
number = complex(int(number_real),int(number_imag))
result = cmath.polar(number)
print (result[0], result[1], sep="\n")