import time
from functools import update_wrapper

from buns.mod7.task1 import validate_args
from buns.mod7.task2 import memoize


class Timer:
    def __init__(self, func):
        self.__func = func
        update_wrapper(self, func)
        self.__start_time = None

    def __call__(self, *args, **kwargs):
        if not self.__start_time:
            self.__start_time = time.time()
            res = self.__func(*args, **kwargs)
            elapsed = time.time() - self.__start_time
            print(f"'{self.__func.__name__}' function elapsed runtime is {elapsed}s")
            return res
        res = self.__func(*args, **kwargs)
        return res


@validate_args
@memoize
@Timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
