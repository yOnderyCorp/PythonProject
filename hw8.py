a = float(input("Число a: "))
b = float(input("Число b: "))
op = input("Дія (+, -, *, /): ")
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Ділення на нуль")