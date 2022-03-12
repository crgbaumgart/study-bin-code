# a < b < c
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

SUM = 1000

for i in range(1, SUM):
    for j in range(i + 1, SUM):
        c = SUM - (i + j)
        if i**2 + j**2 == c**2 and i + j + c == SUM and i < j < c:
            print(i, j, c)
            print(i*j*c)



def check_pathagorean(a, b, c):
    return (a**2) + (b**2) == (c**2)

SUM = 1000

for i in range(1, SUM):
    for j in range(i+1, SUM):
        c = SUM - (i + j)
        if(check_pathagorean(i, j, c)):
            if i + j + c == SUM:
                print(i, j, c)
                print(i * j * c)
                break