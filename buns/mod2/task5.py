i, n = input().strip(), int(input().strip())
print(chr(97 + (ord(i) + n - 97) % 26))
