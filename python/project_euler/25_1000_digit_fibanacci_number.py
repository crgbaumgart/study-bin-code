# What is the index of the first term in the Fibonocci sequence to contain 1000 digits?

def fibonacci_sequence_with_three_digits():
    n = 0
    sequence = [1, 1]
    while sequence[-1] < 10 ** (1000 - 1):
        # f = sequence[n] + sequence[n + 1]
        sequence.append(sequence[n] + sequence[n + 1])
        print(sequence[-1])
        print()
        n += 1
    # print(sequence)

    return n + 2

print(fibonacci_sequence_with_three_digits()) # 4782