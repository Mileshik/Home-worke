# 1 задача
'''start = int(input("enter start -"))
end = int(input("enter end -"))
while start <= end:
    if start % 7 == 0:
        print(start, end=' ')
    start += 1'''

# 2 задача
'''start = int(input("enter start -"))
end = int(input("enter end -"))
i = 0
while start <= end:
     print(start, end=' ')
     print(end, end=' ')
     end -= 1
     if start % 7 == 0:
         print(start, end=' ')
     elif start % 5 == 0:
         i += 1
         print(i, start, end=' ')
     start += 1'''

# 3 задача
'''start = int(input("enter start -"))
end = int(input("enter end -"))
sum_ev = 0
sum_od = 0
sum_9 = 0
i = 0
k = 0
j = 0
while start <= end:
    if start % 2 == 0:
        sum_ev += start
        i += 1
    elif start % 2 != 0:
        sum_od += start
        k += 1
    if start % 9 == 0:
        sum_9 += start
        j += 1
    start += 1
print("sумма четних -", sum_ev)
print("середнєарифм четних -", sum_ev / i)
print("sумма нечетних -", sum_od)
print("середнєарифм нечетних -", sum_od / k)
print("sумма крат 9  -", sum_9)
print("середнєарифм крат 9 - ", sum_9 / j)'''

# 4 задача
'''length = int(input("Enter line length -"))
symbol = input("Enter a character to fill the line:")
num = 0
while num < length:
    print(symbol, end='')
    print()
    num += 1'''

# 5 задача
'''num = int(input("enter number -"))
while True:
    if num < 0:
        print("Number is negative -", num)
    elif num > 0:
        print("Number is positive -", num)
    elif num == 0:
        print("Number is equal to zero")
    if num == 7:
        print("Good bye!")
        break'''

# 6 задача

'''sum = 0
maxi = 0
mini = 0
while True:
    number = int(input("Введите число: "))
    if number != 7:
        sum += number
        if number > maxi:
            maxi = number
        if mini == 0:
            mini = number
        elif mini > number:
            mini = number
    else:

        print("Good bye!")
        break
print('Сумма введённых чисел:', sum)
print('Максимальное число:', maxi)
print('Минимальное число:', mini)'''


j = 0
i = 0
summ = 0
l = 0
number = int(input("Введите число: "))
while number:
    i += 1
    l = number % 10
    summ += l
    if l == 0:
        j += 1
    number = int(number / 10)
print(i)
print(summ)
print(summ/i)
print(j)