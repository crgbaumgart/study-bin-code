a = [1, 1, 2, 1, 4, 3]
d = [1, 1, 4, 2, 1, 3]

b = [5,  1, 2, 3, 4, 5]

c = [1, 2, 3, 4, 5]


def height_checker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    _sorted = sorted(heights)
    if heights == _sorted:
        return 0, []

    else:
        unordered = 0
        unordered_set = []
        for i in range(0, len(heights)):
            if heights[i] == _sorted[i]:
                continue
            else:
                unordered += 1
                unordered_set.append(heights[i])

        return unordered, unordered_set


print(height_checker(a))
print(height_checker(d))
print(height_checker(b))
print(height_checker(c))
