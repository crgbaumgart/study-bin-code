def mySqrt(x):
    n = 0
    left = 0
    right = 0
    while True:
        if n * n < x:
            left = n
            n += 1
        else:
            right = n
            break

    print(left, right)
    return left

def faster_sqrt(x):
    if x == 0 or x == 1:
        return x

    left = 0
    right = x
    ans = None
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

def guess(n, m):
    if n < m:
        return 1
    elif n > m:
        return -1
    elif n == m:
        return 0

def guessNumber(n):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if guess(mid, 6) == 0:
            return mid
        elif guess(mid, 6) == -1:
            left = mid - 1
        else:
            right = mid - 1

    return mid

print(guessNumber(10))

