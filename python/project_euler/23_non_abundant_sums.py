# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers: ?
import time

t0 = time.time()
def is_abundant_number(number):
    factors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            factors.append(i)
    # print(factors)
    return sum(factors) > number


def get_abundant_numbers_in_range(min, max):
    abundants = []
    for i in range(min, max):
        if is_abundant_number(i):
            abundants.append(i)
    return abundants


abs = get_abundant_numbers_in_range(1, 28123)

print(abs)
print(len(abs))

#28092, 28098, 28100, 28104, 28110, 28112, 28116, 28120, 28122
# print(is_abundant_number(28122))

def values_of_all_abundant_number_pairs(abundants):
    values = {}
    for i in abundants:
        for j in abundants:
            values[i + j] = None

    print(len(values))
    return values

# 28122 max abundant
# 56244 max abundant sum
# 53871 count

abs_pairs = values_of_all_abundant_number_pairs(abs)
print(abs_pairs.keys())
print(len(abs_pairs))

non_abundant_summable = []

for i in range(1, 28124):
    if i not in abs_pairs.keys():
        non_abundant_summable.append(i)

t1 = time.time()
print(non_abundant_summable)
print(len(non_abundant_summable))
print('SUM', sum(non_abundant_summable))
print('TIME :', t1-t0)

# CORRECT count: 1456
# CORRECT sum  : 4179871