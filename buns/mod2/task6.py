domen = input().strip()
p1, p2 = domen.find("."), domen.rfind(".")
print(domen[p2 + 1:], domen[p1 + 1:p2], domen[:p1], sep="\n")
