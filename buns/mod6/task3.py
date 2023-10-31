def generator():
    i = 10
    while True:
        s = str(i)
        l = len(s)
        sm = 0
        for ch in s:
            sm += int(ch) ** l
        if i == sm:
            yield i
        i += 1


def wrapper(g):
    def return_value():
        return next(g)
    return return_value


get_armstrong_numbers = wrapper(generator())
