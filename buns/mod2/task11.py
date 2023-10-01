string = input().strip()


def check_for_reps(s):
    for i in range(0, len(s), 2):
        for j in range(0, len(s), 2):
            if i == j:
                continue
            if s[i] == s[j]:
                return True
    return False


print(check_for_reps(string))

