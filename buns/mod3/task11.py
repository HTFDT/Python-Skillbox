with open("input11.txt", "r") as f:
    field = [list(x.strip()) for x in f.readlines()]


def get_winner(data):
    main_diag = True
    side_diag = True
    n = len(data)
    for i in range(n):
        row, col = True, True
        for j in range(n):
            if i == j == 0:
                continue
            if data[i][j] != data[i][j - 1]:
                row = False
            if data[j][i] != data[j - 1][i]:
                col = False
            if i == j:
                if data[i][j] != data[i - 1][j - 1]:
                    main_diag = False
                if data[-i - 1][j] != data[-i][j - 1]:
                    side_diag = False

        if row and data[i][0] != "_":
            return data[i][0]
        if col and data[0][i] != "_":
            return data[0][i]
    if main_diag and data[-1][-1] != "_":
        return data[-1][-1]
    if side_diag and data[0][-1] != "_":
        return data[0][-1]
    return "Ничья"


print(get_winner(field))
