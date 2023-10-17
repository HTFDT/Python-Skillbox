def power(a, n):
    if n == 0:
        return 1
    if n == -1:
        return 1 / a
    if n == 1:
        return a
    even = power(a, n // 2)
    if n % 2 == 0:
        return even * even
    return even * power(a, n // 2 + 1)

