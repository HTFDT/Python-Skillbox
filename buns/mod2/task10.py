s = input().strip()
word = ""
for i in range(len(s)):
    if s[i] == " ":
        word += s[i - 1]
if len(s) > 0:
    word += s[-1]
print(word)
