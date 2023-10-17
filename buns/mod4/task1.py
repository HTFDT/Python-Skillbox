def inspect_list(lst):
    if len(lst) == 0:
        raise ValueError("Пустой список")
    s = set(lst)
    if len(s) == len(lst):
        return "Все числа разные"
    if len(s) == 1:
        return "Все числа равны"
    return "Есть равные и неравные числа"
