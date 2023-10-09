#Задание 1
'''try:
    num1 = int(input("Введите число 1: "))
    num2 = int(input("Введите число 2: "))
    rezult = num1**num2
    print("Результат возведения num1 в степень num2 -", rezult)
except ValueError:
    print("Преобразование прошло неудачно")
except BaseException:
    print("Общее исключение")
print("Завершение программы")

#Задание 2
try:
    num = input("Введите целое число: ")
    result = ""
    for char in num:
        if char != '3' and char != '6':
            result += char
    result_integer = int(result)
    print("Число без 3 и 6:", result_integer)
except ValueError:
    print("Преобразование прошло неудачно")
except BaseException:
    print("Общее исключение")
print("Завершение программы")'''

#Задание 3
try:
    num1 = int(input("Введите число 1: "))
    num2 = int(input("Введите число 2: "))
    print("Виберіть математичну дію ")
    print("1. сума")
    print("2. множення")
    print("3. віднімання")
    print("4. ділення")
    num4 = int(input("Введіть дію: "))
    if num4 == 2:
        print(num1*num2)
    elif num4 == 1:
        print(num1+num2)
    elif num4 == 3:
        if num1>num2:
            print(num1 - num2)
        elif num2>num1:
            print(num2-num1)
    elif num4 == 4:
        print(num1/num2)
except ZeroDivisionError:
    print("Деление на 0 невозможно")
except ValueError:
    print("Преобразование прошло неудачно")
print("Завершение программы")