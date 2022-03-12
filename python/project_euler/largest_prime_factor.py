# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(value):
    next_factor = 0
    primes = []
    for i in range(2, int(value/2)):
        while value % i == 0:
            value = value / i
            primes.append(i)

    print(primes)


def multiplication(list_1):
    mul_num = 1
    for i in list_1:
        mul_num *= i
    return mul_num


import math


def _largest_prime_factor(value):
    max_prime = 0
    while value % 2 == 0:
        max_prime = 2
        value = value / 2

    for i in range(3, int(math.sqrt(value)) + 1, 2):
        while value % i == 0:
            max_prime = i
            value = value / i

    if value > 2:
        max_prime = value
    print(max_prime)

_largest_prime_factor(6044085)
_largest_prime_factor(600851475143)