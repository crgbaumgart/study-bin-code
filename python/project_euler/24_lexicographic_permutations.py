# What is the millionth leixcographic permutation of the digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9: ?

perm = {}

objects = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n = 0

def get_permutations(string, i = 0, perms = {}):
    # perms = {}

    if i == len(string):
        # print("".join(string))
        perms["".join(string)] = None

    for j in range(i, len(string)):
        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]

        if len(perms.keys()) < 999999: # 2785960341 # 2785963410 # 2783915460
            get_permutations(words, i + 1, perms)
        else:
            return perms.keys()

    return perms

# print(sorted(get_permutations("012")))

print(sorted(get_permutations("0123456789")))


