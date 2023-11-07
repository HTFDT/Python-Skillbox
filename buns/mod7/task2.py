from functools import wraps


def memoize(func):
    cache = dict()

    @wraps(func)
    def wrapper(*args):
        n = args[0]
        if n in cache:
            return cache[n]
        res = func(n)
        cache[n] = res
        return res
    return wrapper




