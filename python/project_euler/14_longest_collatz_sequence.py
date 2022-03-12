import time


def collatz_sequence(input):
    seq = []
    while input > 1:
        if input % 2 == 0:
            input = int(input/2)
        else:
            input = int(input * 3 + 1)

        seq.append(input)

    return seq


def longest_collatz_sequence(n, iter_start):
    max = []
    max_iter = 1
    for i in range(iter_start, n):
        seq = collatz_sequence(i)
        if len(seq) > len(max):
            # print("seq :", len(max))
            # print("iter:", i)
            max, max_iter = seq, i

    return len(max), max_iter, max

start = time.time()
print(longest_collatz_sequence(1000000, 500000))
finish = time.time()
print(finish - start)
print()

# print(longest_collatz_sequence(1000000, 500000))