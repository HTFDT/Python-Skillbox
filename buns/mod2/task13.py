s = input().strip()
odd = 0
even = 0
for d in s[::2]:
    odd += int(d)
for d in s[1::2]:
    even += int(d)
print("yes" if (odd + even * 3) % 10 == 0 else "no")
