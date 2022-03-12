n_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

nn_dict = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def if_single_digit(n):
    if n in n_dict:
        return n_dict[n]
    return ""


def if_double_digit(n):
    if 10 <= n <= 19:
        return nn_dict[n]
    elif 20 <= n <= 99:
        if n in nn_dict:
            return nn_dict[n]
        else:
            _n = str(n)
            return "%s-%s" % (nn_dict[int(_n[0]) * 10], n_dict[int(_n[1])])
    return ""


def if_triple_digit(n):
    if 100 <= n <= 999:
        return n_dict[int(str(n)[0])] + " " + "hundred"
    return ""


def int_to_word(n):
    # print(n)
    word = ""
    _n = str(n)
    if len(_n) == 3:
        if _n[1:] == "00":
            word += if_triple_digit(n)
        elif _n[1] == "0":
            word += if_triple_digit(n) + " and " + if_single_digit(int(str(n)[2:]))
        else:
            word += if_triple_digit(n) + " and " + if_double_digit(int(str(n)[1:]))
    elif len(_n) == 2:
        word += if_double_digit(n)
    elif len(_n) == 1:
        word += if_single_digit(int(str(n)))

    return word

def total_characters_counted(min, max):
    chars = 0
    for i in range(min, max):
        chars += len(int_to_word(i).replace(" ", "").replace("-", ""))
    return chars + len("onethousand")



print(int_to_word())
print(total_characters_counted(1, 1001))