# What is the value of the first triangle number to have over five hundred divisors?

def triangle_numbers(seq):
    return sum(list(range(1, seq + 1)))


def factors(SUM):
    divisors = []
    for i in range(1, int(SUM + 1)):
        if SUM % i == 0:
            divisors.append(i)

    return divisors


def find_n_divisors(num):
    n = 1
    while True:
        number = triangle_numbers(n)
        print("Tri #   :", number)
        f = factors(number)
        print("Divisors:", len(f))
        if len(f) < num:
            n += 1
        else:
            # print(f)
            return n


# print(find_num_divisors(generate_triangle_sequence_sum(5550000)))
# print(len(find_num_divisors(generate_triangle_sequence_sum(1000))))

print(find_n_divisors(500))