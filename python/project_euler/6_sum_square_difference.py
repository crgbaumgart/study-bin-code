# 2:25
# Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum.

def diff_of_squares_and_sum_squared(value):
    sum_of_squares = None
    square_of_sum = None

    value_list = list(range(1, value + 1))

    def squared(i):
        return i ** 2

    sum_of_squares = sum(map(squared, value_list))
    square_of_sum = sum(value_list) ** 2

    # print(sum_of_squares)
    # print(square_of_sum)

    return square_of_sum - sum_of_squares


print(diff_of_squares_and_sum_squared(10))
print(diff_of_squares_and_sum_squared(100))