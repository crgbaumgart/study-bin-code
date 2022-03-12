# Evaluate the sum of all the amicable numbers under 10,000: ?

def sum_of_proper_divisors(number):
    divisors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisors.append(i)

    return sum(divisors)


def sum_of_amicable_numbers(r):
    amicable = []
    for i in range(1, r):
        a = sum_of_proper_divisors(i)
        b = sum_of_proper_divisors(a)
        if i == sum_of_proper_divisors(a) and a != b:
            amicable.append(i)
    print(amicable)
    return sum(amicable)

print(sum_of_amicable_numbers(10000))