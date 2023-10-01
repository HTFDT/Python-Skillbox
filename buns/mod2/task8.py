s, i = input().strip(), input().strip()
cnt = 0
for c in s:
    if c == i:
        cnt += 1
    else:
        break
print(cnt)
