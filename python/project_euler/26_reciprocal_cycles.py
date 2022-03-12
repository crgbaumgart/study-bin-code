# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part: ?

def is_number_reciprocal(input):
    input = str(input)
    n = 2
    max = []
    for i in range(len(input)//2 + 1):
        if input.count(input[0:n - 1]) > 1 and input.count(input[0]) != len(input) and len(input[0:n - 1]) <= len(input) / 2:
            if input.count(input[0:n - 1]) * input[0:n - 1] == len(input):
                continue
            else:
                max.append(input[0:n - 1])
        n += 1

    return max

# print(is_number_reciprocal('9999'))
# print(is_number_reciprocal('123456123456123456123456123'))
# print(is_number_reciprocal('000900090009000900'))
# print(is_number_reciprocal('9999'))
# print(is_number_reciprocal('009009009009009009'))

from time import time

start = time()


def divide(n, d, p):
    i = 0  # Counts the cycles
    remainders = set()  # Empty set of remainders

    while i < p:
        if n < d:
            n = n * 10  # If the numerator < denominator, multiply by 10

        # r = r + str(n // d) #Floor division would give whole number part of the division
        n = n % d  # sets the remainder as the new numerator
        if n in remainders:  # If this is repeated remainder, we have reached the end of a repeating cycle
            return (d, i)  # Returns the denominator and the length of the repeating decimal
        else:
            remainders.add(n)  # Adds the new remainder to set of remainders

        i = i + 1  # Increments the counter (number of digits found)

print(divide(1, 983, 983))

longest = [0, 0]
largest_denominator = 1000
for x in range(2, largest_denominator + 1):
    y = divide(1, x, x)  # p = x due to upper bound on length of repeating decimal (see above)
    if y[1] > longest[1]:
        longest = y
e = 1000 * (time() - start)
print('1 / %s has longest recurring decimal (length = %s) for denominators less than %s' % (
longest[0], longest[1], largest_denominator))
print('Solution in %s ms' % (round(e, 2)))