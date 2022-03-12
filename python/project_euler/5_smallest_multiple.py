# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?


def smallest_range_divided(max):
    import math
    def lcm(list):
        lcm = list[0]
        for i in range(1, len(list)):
            lcm = lcm * list[i] // math.gcd(lcm, list[i])
        return lcm

    l = list(range(2, 21))
    print(lcm(l))
    # smallest = max
    # n = 1
    # while n <= max:
    #
    #     for i in range(1, max + 1):
    #         if smallest % i != 0:
    #             smallest = smallest // i * i + i
    #             # print(i, smallest)
    #             n = 0
    #         else:
    #             n += 1
    #
    # print(smallest)


smallest_range_divided(10)
smallest_range_divided(20)