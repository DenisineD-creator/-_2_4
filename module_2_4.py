"""numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = [2,3,5,7,11,13]
not_primes = [4,6,8,9,10,12,14,15]
print(primes)
print(not_primes)
primes = []
not_primes = []
for i in numbers:
    print(i)
numbers_1 = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
for i in numbers_1:
    print(i)
    is_prime = True
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue

    is_prime = True
    for d in range(2, number):
        if number % d == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)


print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')


















