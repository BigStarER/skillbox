def check(symbol):
    while symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/":
        symbol = input("Ошибка: такой операции не существует. Попробуйте ещё раз. \nВведите действие: ")
    else:
        return symbol


action = input("Введите действие: ")
sing = check(action)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = 0

if sing == "+":
    c = a + b
    print(f"{a} + {b} = {c}")
elif sing == "-":
    c = a - b
    print(f"{a} - {b} = {c}")
elif sing == "*":
    c = a * b
    print(f"{a} * {b} = {c}")
else:
    c = a / b
    print(f"{a} / {b} = {c}")
