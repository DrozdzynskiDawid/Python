def is_prime(number):
    if number[0] == "0":
        return False
    number = int(number)
    if number < 2:
        return False
    i = 2
    while i <= number/2:
        if number%i == 0:
            return False
        i += 1
    return True

primes = []
n = input()
if is_prime(n):
    primes.append(int(n))
for i in range(1, len(n)):
    j = 0
    while j <= len(n)-i:
        if is_prime(n[j:j+i]):
            primes.append(int(n[j:j+i]))
        j += 1

primes = list(set(primes))
primes = [str(x) for x in primes]
primes.sort(reverse=True)
for el in primes:
    print(el)