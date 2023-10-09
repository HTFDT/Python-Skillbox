with open("input9.txt", "r") as f:
    n = int(f.readline().strip())

pos = [0, 0]
steps = 1
dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
i = 0
while n > 0:
    if steps > n:
        steps = n
    n -= steps
    pos = [y[0] + y[1] for y in zip(pos, [x * steps for x in dirs[i]])]
    i += 1
    if i == 2 or i == 4:
        steps += 1
    i %= len(dirs)

with open("output9.txt", "w") as f:
    f.write(" ".join([str(x) for x in pos]))
