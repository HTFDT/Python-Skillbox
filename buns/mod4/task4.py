from collections import defaultdict


def palindromize(word):
    d = defaultdict(int)
    for c in word:
        d[c] += 1

    res = [""] * len(word)
    l, r = 0, len(word) - 1
    cur = next(iter(d))
    while l <= r:
        if d[cur] == 0:
            d.pop(cur)
            if len(d) == 0:
                break
            cur = next(iter(d))
            if d[cur] % 2 == 1:
                if len(word) % 2 == 0 or res[len(word) // 2] != "":
                    return False
                res[len(word) // 2] = cur
                d[cur] -= 1
                continue

        if d[cur] % 2 == 0:
            res[l] = cur
            l += 1
        else:
            res[r] = cur
            r -= 1
        d[cur] -= 1

    return "".join(res)
