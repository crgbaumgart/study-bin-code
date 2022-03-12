def search(nums, target):
    if target in nums:
        return nums.index(target)
    return -1

def binary_search_template_1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1


print(binary_search_template_1(sorted([4, 2, 10, 5, 99, 8, 11]), 99))