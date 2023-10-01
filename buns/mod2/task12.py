s = input().strip()
res = ""
for c in s:
    if c != " " and c != "-" and c != "(" and c != ")":
        res += c
print(res)
