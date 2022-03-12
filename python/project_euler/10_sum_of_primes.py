import math


def sum_of_primes(n_th):
    primes = [2]
    iter = 0
    count = 3

    while True:
        is_prime = True

        for i in range(2, int(math.sqrt(count) +1)):
            if count % i == 0:
                is_prime = False
                break
        if is_prime:
            # print(count)
            primes.append(count)

        if n_th == 3 + iter:
            print(primes)
            return sum(primes)

        count += 1
        iter += 1


print(sum_of_primes(10))
print(sum_of_primes(2000000))
