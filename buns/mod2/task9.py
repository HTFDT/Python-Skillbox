s = input().strip()
vow, cons = "аеёиоуыэюя", "бвгджзйклмнпрстфхцчшщ"
print(len([x for x in s if x in vow]), len([x for x in s if x in cons]))

