# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_num_palindrome(number):
    str_n = str(number)

    if len(str_n) % 2 == 0:
        # print('even', number)
        a = str_n[0:int(len(str_n) / 2)]
        b = str_n[int(len(str_n) / 2):][::-1]
        # print(a, b)
        return a == b
    else:
        # print('not even', number)
        a = str_n[0:len(str_n) // 2]
        b = str_n[int(len(str_n) // 2 + 1):][::-1]
        # print(a, b)
        return a == b


def max_pal_n_by_n(n):
    biggest = 0

    for i in range(0, 10 ** n):
        for j in range(0, 10 ** n):
            # print(i, j)
            if is_num_palindrome(i * j):
                # print(i, j)
                if i * j >= biggest:
                    biggest = i * j
                    biggest_pair = [i, j]

    print(biggest_pair)
    print(biggest)


max_pal_n_by_n(2)
# print()
max_pal_n_by_n(3)


print(is_num_palindrome(91 * 99))
# print(is_num_palindrome(99994999))
