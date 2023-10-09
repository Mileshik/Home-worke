# 1задача
# num1 = int(input("Введіть число перше - "))
# num2 = int(input("Введіть число друге - "))
# num3 = int(input("Введіть число третє - "))
# print("Виберіть математичну дію ")
# print("1. сума")
# print("2. множення")
# num4 = int(input("Введіть дію: "))
# if num4 == 1:
# print(num1 + num2 + num3)
# elif num4 == 2:
# print(num1 * num2 * num3)

# 2 задача
# num1 = int(input("Введіть число перше - "))
# num2 = int(input("Введіть число друге - "))
# num3 = int(input("Введіть число третє - "))
# print("Виберіть математичну дію ")
# print("1. максимум")
# print("2. мінімум")
# print("3. середнє арифм")
# num4 = int(input("Введіть дію: "))
# if num4 == 1:
#   if num1 > num2:
#      print(num1)
# elif num2 > num3:
#    print(num2)
# elif num1 < num3:
#   print(num3)
# elif num4 == 2:
#   if num1 < num2:
#      print(num1)
# elif num2 < num3:
#    print(num2)
# elif num3 < num1:
#   print(num3)
# elif num4 == 3:
#   print((num1 + num2 + num3)/3)

# 3 задача

'''num1 = int(input("Number of meters -"))
print("Введите единицы перевода")
print("1. Мили")
print("2. Дюйм")
print("3. Ярд")
num2 = int(input("Введите номер выбора: "))
if num2 == 1:
    print(num1 * 0.000621371)
elif num2 == 2:
    print(num2 * 39.3701)
elif num1 == 3:
    print(num2 * 1.09361)'''

# 4 задача
'''day = int(input("Введите  номер дня недели -"))
if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")'''

# 5 задача
'''m = int(input("Введите  номер месяца -"))
if m == 1:
    print("Январь")
elif m == 2:
    print("Февраль")
elif m == 3:
    print("Март")
elif m == 4:
    print("Апрель")
elif m == 5:
    print("Май")
elif m == 6:
    print("Июнь")
elif m == 7:
    print("Июль")
elif m == 8:
    print("Август")
elif m == 9:
    print("Сентябрь")
elif m == 10:
    print("Октябрь")
elif m == 11:
    print("Ноябрь")
elif m == 12:
    print("Декабрь")'''

# 6 задача

'''num = int(input("Enter number -"))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negativ")
elif num == 0:
    print("Number is equal to zero")'''

# 7 задача
'''num1 = int(input("Enter number1 -"))
num2 = int(input("Enter number2 -"))
if num1 == num2:
    print("Numbers equals")
elif num1 != num2:
    if num1 < num2:
        print(int(num1, num2))
    else:
        print(num2, num1)'''

# 9 задача

'''kof1, kof2, kof3 = 0.3, 0.3, 0.3

p1 = int(input("Уровень продаж менеджера 1 -"))
if 500 <= p1 <= 1000:
    kof1 = 0.5
elif p1 > 1000:
    kof1 = 0.8
p2 = int(input("Уровень продаж менеджера 2 -"))
if 500 <= p2 <= 1000:
    kof2 = 0.5
elif p2 > 1000:
    kof2 = 0.8
p3 = int(input("Уровень продаж менеджера 3 -"))
if 500 <= p3 <= 1000:
    kof3 = 0.5
elif p3 > 1000:
    kof3 = 0.8
salary1, salary2, salary3 = 200, 200, 200
m1 = salary1 + p1 * kof1
m2 = salary2 + p2 * kof2
m3 = salary3 + p3 * kof3
print(m1)
print(m2)
print(m3)
if m1>m2 and m1>m3:
    print("1 менеджер лучший ")
elif m2>m3 and m2>m1:
    print("2 менеджер лучший ")
elif m3>m2 and m3>m1:
    print("3 менеджер лучший ")'''

# 8 задача

cc = float(input("Введите время разговора: "))
print("1. Vodafon")
print("2.Kievstar")
print("3.Life")
of = int(input("Введите оператор, с которого звоните: "))
ot = int(input("Введите оператор, на который звоните: "))
if of == 1 and ot == 2:
    print(cc * 0.5)
elif of == 1 and ot == 3:
    print(cc * 0.2)
elif of == 2 and ot == 1:
    print(cc * 0.3)
