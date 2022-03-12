# Input: name = "alex", typed = "aaleex"
# True

# Input: name = "saeed", typed = "ssaaedd"
# False

def is_input_long_press(name, typed):
    name_hash = {}

    if name == typed or len(name) == 1 and len(name) == len(typed):
        return False

    for i in name:
        if i in name_hash:
            name_hash[i] += 1
        else:
            name_hash[i] = 1

    type_hash = {}
    for i in typed:
        if i in type_hash:
            type_hash[i] += 1
        else:
            type_hash[i] = 1

    for i in name_hash:
        if len(name) == len(typed):
            if sorted(name_hash) == sorted(type_hash):
                return False
        elif i in type_hash:
            if name_hash[i] > type_hash[i]:
                return False
        else:
            return False

    print(name_hash)
    print(type_hash)
    return True

    # return name_hash


# print(is_input_long_press("alex", "aaleex"))
# print(is_input_long_press("saeed", "ssaaedd"))
# print(is_input_long_press("xnhtq", "xhhttqq"))
print(is_input_long_press("a", "b"))