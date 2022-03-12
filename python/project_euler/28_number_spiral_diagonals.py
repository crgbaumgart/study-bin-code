# five_by_five = [i for i in range(1, 5*5 + 1)]

# print(five_by_five)

# def get_diagonals_sum(number):
#     diagonals = []
#     n = 0
#     step = 1
#     for i in [i for i in range(1, number*number + 1)]:
#
#         if len(diagonals) - 1 % 4 == 0:
#             step += 1
#
#     return diagonals
#
# get_diagonals_sum(5)


def get_diagonals_sum(number):
    x_by_x = [i for i in range(1, number * number + 1)]
    diagonals = []
    n = 0
    step = 1
    for i in range(0, len(x_by_x), step):
        if (len(diagonals) - 1) % 4 == 0:
            diagonals.append(x_by_x[i])
            step = n * 2
            n = 0

        n += 1

    print(diagonals)

get_diagonals_sum(5)