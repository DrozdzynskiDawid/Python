def smallest_divisor(number):
    for i in range(2, number//2):
        if number % i == 0:
            return i
    return number

n = int(input())
print(smallest_divisor(n))