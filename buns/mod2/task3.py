s = input().strip()
a, b, c = int(s[0]), int(s[2]), int(s[4])
if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)
