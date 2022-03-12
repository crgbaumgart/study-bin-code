def factorial_digit(n):
    factorial = n
    while n > 1:
        factorial = (factorial * (n - 1))
        n -= 1

    return factorial

def digit_sum(digit):
    s = 0
    for i in str(digit):
        s += int(i)
    return s

print(digit_sum(factorial_digit(100)))