import math
print(math.factorial(5))


def my_function_summ_factorial(n):
    factorial_n = 1
    summ = 0

    for numbers in range(1, n + 1):
        factorial_n *= numbers
        summ += factorial_n
    return summ


number = int(input("Введи число: "))
print(my_function_summ_factorial(number))
