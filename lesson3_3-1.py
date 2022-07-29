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
        line += str(number) + sing
        result += number    #Меняем значение 0 на number
    
elif sing == "-": 
    for count_number in range(1, numbers + 1):
        number = int(input(f"Введите операнд {count_number}: "))
        if count_number == 1:
            result = number #Меняем значение 0 на number
            line += str(result) + sing
        else:   #  count_number > 1
            result -= number
            line += str(number) + sing
        
elif sing == "*":
    for count_number in range(1, numbers + 1):
        number = int(input(f"Введите операнд {count_number}: "))
        if count_number == 1:
            result = number #Меняем значение 0 на number
            line += str(result) + sing
        else:   #  count_number > 1
            result *= number
            line += str(number) + sing

else:
    for count_number in range(1, numbers + 1):
        number = int(input(f"Введите операнд {count_number}: "))
        if count_number == 1:
            result = number #Меняем значение 0 на number
            line += str(result) + sing
        else:   #  count_number > 1
            result /= number
            line += str(number) + sing
            
print(f"{line[:-1]} = {result}") # [:-1] удаляет последний лишний символ sing из else: line += str(number) + sing