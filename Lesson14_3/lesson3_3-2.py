def check(symbol):
    while symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/":
        symbol = input("Ошибка: такой операции не существует. Попробуйте ещё раз. \nВведите действие: ")
    else:
        return symbol


action = input("Введите действие: ")
sing = check(action)

result = 0
line = ""

numbers = int(input("Сколько операндов? "))

if sing == "+":
    for count_number in range(1, numbers + 1):
        number = int(input(f"Введите операнд {count_number}: "))
        if count_number < numbers:
            result += number    # Меняем значение 0 на number
            line += str(number) + sing
        else:
            line += str(number)

elif sing == "-":
    for count_number in range(1, numbers + 1):
        number = int(input(f"Введите операнд {count_number}: "))
        if count_number == 1:
            result = number   # Меняем значение 0 на number
            line += str(result) + sing
        elif count_number < numbers:
            result -= number
            line += str(number) + sing
        else:   # Часть кода предназначена для того, что б в переменную line не записывался знак sing. Если это последний операнд/(введенное число), то запись текста знака.
            result -= number
            line += str(number)

elif sing == "*":
    for count_number in range(1, numbers + 1):
        number = int(input(f"Введите операнд {count_number}: "))
        if count_number == 1:
            result = number   # Меняем значение 0 на number
            line += str(result) + sing
        elif count_number < numbers:
            result *= number
            line += str(number) + sing
        else:   # Часть кода предназначена для того, что б в переменную line не записывался знак sing. Если это последний операнд/(введенное число), то запись текста знака.
            result *= number
            line += str(number)

else:
    for count_number in range(1, numbers + 1):
        number = int(input(f"Введите операнд {count_number}: "))
        if count_number == 1:
            result = number   # Меняем значение 0 на number
            line += str(result) + sing
        elif count_number < numbers:
            result /= number
            line += str(number) + sing
        else:   # Часть кода предназначена для того, что б в переменную line не записывался знак sing. Если это последний операнд/(введенное число), то запись текста знака.
            result /= number
            line += str(number)

print(f"{line} = {result}")
