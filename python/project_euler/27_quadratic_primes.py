import math

def is_prime(value):
    if value == 2 or value == 3: return True
    if value % 2 == 0 or value < 2: return False

    for i in range(3, int(math.sqrt(value)), 2):
        if value % i == 0:
            return False

    return True

def quadratic_primes(r):
    n = 0
    max_a = 0
    max_b = 0
    max_n = 0
    for a in range(-1 * r, r):
        for b in range(-1 * r, r + 1):
            n = 0
            while True:
                if is_prime(n * (n + a) + b) and a != max_a and b != max_b:
                    n += 1
                    # print('ITER :', n, a, b)
                    # print('MAX  :', max_n, max_a, max_b)
                else:
                    # print(n, a, b)
                    if n > max_n:
                        max_n = n
                        max_a = a
                        max_b = b
                        # print(max_n, max_a, max_b)
                    break

    return max_a, max_b, max_a * max_b, max_n

print(quadratic_primes(1000))