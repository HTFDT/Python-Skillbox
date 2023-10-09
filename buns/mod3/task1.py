a, b, c = [int(x) for x in input().split()]
print(a + b + c - max(a, b, c) - min(a, b, c))
