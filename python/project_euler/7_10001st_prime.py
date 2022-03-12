# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?
import math


def main(value):
    count = 3
    n = 1
    while n < value:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            print(count)
            n += 1
        count += 1

# main(6)
main(10001)