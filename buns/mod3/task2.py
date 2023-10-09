s = input().strip()
print("Неверный ввод" if s.startswith('-') or not s.isdigit() else " ".join(
    [bin(int(s))[2:], oct(int(s))[2:], hex(int(s))[2:]]))
