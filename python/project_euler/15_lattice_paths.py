import math


def n_choose_k(n,k):
    return (math.factorial(n))/(math.factorial(n - k) * math.factorial(k))

print(n_choose_k(40, 20))
