from collections import defaultdict


def get_stats(filename):
    d = defaultdict(int)
    with open(filename, "r") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c.isalpha():
                d[c] += 1
    with open("output.txt", "w") as f:
        for k in sorted(d, key=lambda x: d[x]):
            f.write(f"{k} {d[k]}\n")


get_stats("input.txt")
