n = int(input("Факторіал числа: "))
f = 1
for i in range(1, n + 1):
    f *= i
print(f"Результат: {f}")