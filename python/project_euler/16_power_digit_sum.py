# what is the sum of the digits of number 2^1000

def get_sum_of_digits(num):
    l = []
    for i in str(num):
        l.append(int(i))

    return sum(l)

print(get_sum_of_digits(2**1000))