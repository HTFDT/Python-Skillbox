def euclid(a, b):
    mx = max(a, b)
    mn = min(a, b)
    if mx % mn == 0:
        return mn
    return euclid(mn, mx % mn)

