# def sum_of_mutltiples_of_naturual_numbers(x, y, numerator):
#     x_max = 0
#     x_sum = []
#     y_max = 0
#     y_sum = []
#
#     n = 0
#     while (x_max + x) * x < numerator:
#         if x * n < numerator:
#             n += 1
#             x_sum.append(x * n)
#             x_max = x * n
#
#     n = 0
#     while (y_max + y) * y < numerator:
#         if y * n < numerator:
#             n += 1
#             y_sum.append(y * n)
#             y_max = y * n
#
#     print(x_sum)
#     print(x_max)
#     print(y_sum)
#     print(y_max)
#
#     print(sum(x_sum) + sum(y_sum))
#
# sum_of_mutltiples_of_naturual_numbers(3, 5, 1000)
#

def answer():
    total_sum = 0
    for i in range(1000):
        if (i % 3 == 0 or i % 5 == 0):
            total_sum = total_sum + i
            print(i)
    print(total_sum)

answer()
