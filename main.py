# name_new = "Nadezhda"
# age = 20
# print("Hello,", name_new)
# print(type(age))

# a = b = c = 1
# print(a, b, c)
#
# a, b, c = "Hello", 5, False
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "Hello"
# print(a)
# print(type(a))
# a = 5
# print(type(a))

# name = "Ольга"
# age = 21
# print("Меня зовут " + name + ". Мне " + str(age))

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
# print("a:", a)
# print("b:", b)
# # a, b = b, a
# c = a
# a = b
# b = c
# print("a:", a)
# print("b:", b)

# print("строка \
# cимволов")
# print('строка cимволов')

# print("Документ \"file.py\" находится по заданному пути \nD:\\Python\\file.py")

# s1 = "Hello"
# s2 ="Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3)
# print(s3 * 5)

# print(454657567865875745)
# print(4.4564586787687686)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 5) # 1.2
# print(6 // 5) # 1
# print(6 ** 2)
# print(7 % 2) # 1

# a, b, c = 5, 7, 3
# print("Сумма: ", a + b + c)
# print("Произведение: ", a * b * c)
# print("Среднее арифметическое: ", (a + b + c)/3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
#
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5 # num = num + 5
# print(num)  # 15
#
# num -= 3 # num = num - 3
# print(num) # 12
#
# num *= 4 # num = num * 4
# print(num) # 48

# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# print(num)
# c = num % 10
# print(c)
# num = num // 10
# print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res = num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# a = 1
# b = 2
# c = a + b
# a = c - a
# b = c - b
# print("a:", a)
# print("b:", b)

# Функции явного преобразования типов
# int()
# str()
# float()
# bool()

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
#
# print(int(3.8))
# a = 3.8
# print(type(round(a)))
#
# print(round(3.891, 2))

# print(5 / 2)
#
# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="\n\n")
# print("Я учу Python.")

# name = input("Введите имя: ")
# print("Hello", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# num3 = int(input("Введите число: "))
# num4 = int(input("Введите число: "))
#
# s1 = num1 + num2
# s2 = num3 + num4
# x = s1 / s2
# print("Результат: ", round(x, 2))
# sum =  s1 + s2

# b1 = True #1
# b2 = False #0
# print(b1 + 5) # 1 + 5 = 6
# print(b2 + 5) # 0 + 5 = 5

# print(bool("python"))
# print(bool("")) # False
# print(bool(" "))
# print(bool(5))
# print(bool(0))  # False
# print(bool(False)) # False
# print(bool(None)) # False
#
# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print("привет" == "Привет")
#
# print(2 < 4 < 9) #  True && True => True
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2) # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4) # True (True and True)
# print(5 - 3 == 2 and 1 + 3 < 4) # False (True and False)

# print(5 - 3 == 2 or 1 + 3 == 4) # True (True and True)
# print(5 - 3 == 2 or 1 + 3 < 4) # True (True and False)

# print(not 9 - 5)
# print(not 7 - 7)
#
# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a == b")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
# if a == b == с:
#     print("Треугольник равносторонний")
# elif a == b or b == c or c == a:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  #(day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")

# m = int (input("Введите месяц (цифрой): "))
# if 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Зима")
#     if m > 12 or m < 1:
#         print("Такого месяца нет")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end="")
#     if n == 1:
#         print("ворона")
#     if 2 <= n <= 4:
#         print("вороны")
#     if 5 <= n <= 9 or n == 0:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# money = int(input("Введите число от 1 до 99: "))
# x = money % 10
# if 1 <= money <= 99:
#     if (11 <= money <= 14) or (x == 0) or (5 <= x <= 9):
#         print(money, "копеек")
#     elif x == 1:
#         print(money, "копейка")
#     elif 2 <= x <= 4:
#         print(money, "копейки")
# else:
#     print("Ошибка ввода данных")

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minim)


# a = int(input("Введите делимое: "))
# b = int(input("Введите делитель: "))
# res = a/b if b != 0 else "На ноль делить нельзя"
# print(res)

# Исключения

# try:
#     n = int(input("Введите делимое число: "))
#     m = int(input("Введите делитель число: "))
#     print(n / m)
# except ValueError:
#     print("Что-то пошло не так")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое число: "))
#     m = int(input("Введите делитель число: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или делить на ноль")
# else:
#     print("Все нормально. Вы ввели", n, "и", m) # когда в блоке try не возникло исключение
# finally:
#     print("Конец программы") # выполняется в любом случае

# n = input("Введите первое число ")
# m = input("Введите второе число ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#       print(n + m)

# цикл while

# while условие:
#     тело цикла

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# start = int(input('Start: '))
# end = int(input('End: '))
# i = start
# sum_ = 0
# while i <= end:
#     if i % 2:
#         sum_ += i
#     i += 1
# print('Summa:', sum_)

# n = input("Введите целое число")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")

# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=" ")
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#      n = int(input("Введите положительное число: "))
#      if n < 0:
#          break
#  print("Цикл завершен")


# mult = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     mult *= n
#
# print("Произведение:", mult)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i=", i)

# kol = int(input("Введите количество чисел последовательности: "))
# i = 1
# ch = float(input("Введите число: "))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     i += 1
#
# print("Количество чисел: ", kol)
# print("Минимальное число: ", min_ch)
# print("Максимальное число: ", max_ch)
# print("Среднее арифметическое: ", sum_ch / kol)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1
#
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#   тело цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green', 1, 20, 0.3:
#     print("color:", color)

# range(start, stop, step)

# print(range(1, 3))

# for i in range(100, 0, -10):
#     print(i, end=" ")

# print()
# # i = 11
# # while i > 2:
# #     print(i, end=" ")
# #     i -= 2

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# for i in range(10, 100): # 11 => 1 == 1
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(1, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     if i == 1:
#         break
#     print(i)
# else:
#     print('done')

# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)


# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# letter = [i for i in "Hello"]
# print(letter)
#
#
# for i in 'Hello':
#     print(i)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(id(nums[1]))
# print(type(nums))
# print(nums[0])
# print(nums[2])
# print(nums[-4])
# nums[1] = 256
# print(nums)
# print(id(nums[1]))
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print("Длина списка: ", len(nums))

# s = []
# print(s)
#
# s1 = list()
# print(s1)
#
# s2 = list("Hello")
# print(s2)

# s = [1, 3, 5]
# print(s)
# n = s * 6
# print(n)

# n = list(range(2, 10, 3))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = a * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("Введите число: ")
# print(a)

# a = [int(input("Введите число: ")) for i in range(int(input("n = ")))]
# print(a)

# a = [8, 4, 2, 9, 1]
#
# for i in range(len(a)):  # 0 1 2 3 4
#     print(a[i], end=" ")
# print()
# for elem in a:  # 8, 4, 2, 9, 1
#     print(elem, end=" ")


# a = [int(input("Введите число: ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов: ", s)

# k = 0
# s = 0
# n = list(range(21, 41))
# print(n)
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Количество четных элементов списка: ", k)
# print("Сумма нечетных элементов: ", s)

# sp = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = 0
# j = 0
# for i in sp:
#     if i > 0:
#         s += i
#         j += 1
# print("Среднее арифметическое:", s/j)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print[a]

# список[start:stop:step]

# a = [7, 8, 2, 1, 17, 9]
# print(a[1:4])
# print(a[::2])
# print(a[-2:-4:-1])
# print(a[1:4:-1])
# print(a[10:20])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4::])
# print(s[-3:])
# print(s[-3:1:-1])
# print(s[2:5])
# print(s[:])
#
# a = [7, 8, 2, 1, 17, 9]
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# методы списков
# print(dir(list))

# s = [7, 8, 2, 1, 17, 9]
# print(s)
# s.append(99) # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3]) # добавляет список элемнтов в конец первоначального списка
# # print(s)
# s.extend('add')
# print(s)
# s.insert(2, 100) # добавляет элемент в список. Первый параметр - это индекс, второй параметр - добавляемое значение
# print(s)


# a = []
# n = int(input("n = "))
# for i in range(n):
# x = input("-> ")
# a.append(x)

#     a.append(int(input("-> ")))
# print(a)

# [a.append(int(input("-> "))) for i in range(int(input("n = ")))]
# print(a)

# a = []
# n = int(input("Кол-во элементов списка: "))
# for i in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         a.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(a)
#
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
#
#
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# __________________
# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# print("a = ", a)
# print("b = ", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)): # range(3, 5)
#         c.append(b[i])
#     print(c)
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)): # range(3, 5)
#         c.append(a[i])
#     print(c)

# a = [1, 2, 3, 4, 2, 55, 99]
# print(a)
# a.remove(2)  # удаляет из списка указанный по значению. Если несколько, то удалится только первый
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удалямое значение
# print(last)
# print(a)
# last = a.pop(1)  # удаляет элемент по индексу
# print(last)
# print(a)
# a.clear() # удаляет из списка все элементы
# print(a)

# a = []
# print("Введите элементы списка:")
# [a.append(int(input("-> "))) for i in range(int(input("n = ")))]
# k = int(input("Введите индекс: "))
# a.pop(k)
# print(a)

# a = [5, 9, 7, 6, 9, 4, 9, 0, 9]
# print(a)
# num = a.count(9) # количество заданных значений в списке
# print(num)
# ind = a.index(7) # возращает индекс первого вхождения заданного значения, если значение не найдено то выводится ошибка ValuError
# print(ind)
# ind = a.index(9, 2) # выводит индекс элемента указанного в скобках вторым элемента
# print(ind)
# ind = a.index(9, 3, -1)  # выводит индекс начиная с 7 до -1
# print(ind)
#
# ch = 7
# if ch in a:
#     ind = a.index(ch)
#     print(ind)

# a = [5, 9, 7]
# b = a
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)
# print(id(a))
# print(id(b))

# a = [5, 9, 7]
# b = a.copy()  # создает копию списка
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)
# print(id(a))
# print(id(b))

# a = [5, 9, 7, 6, 9, 4, 9, 0, 9]
# print(a)
# a.reverse()  #переместили элементы списка в обратном порядке
# print(a)
# a.sort()  # сортирует элементы списка по возрастанию
# print(a)
# a.sort(reverse=True) # сортирует элементы списка по убыванию
# print(a)

# b = sorted(a, reverse=True)
# print("b = ", b)
# print("a = ", a)
# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s)
# s.sort(key=len, reverse=True)
# print(s)

# Генерация случайных чисел

# import random
#
# print(random.random())
# print(random.randint(1, 9)) # от 1 по 9 (9 - включительно)
# print(random.randrange(9)) #от 0 до 9 (9 - не включительно)
# print(random.randrange(0, 10, 2))

# from random import randint, randrange
# from random import *
# print(randint(1, 9))
# print(randrange(9))

# import random as r
#
# print(r.randint(1, 9))
# print(r.randrange(9))
# print(r.uniform(10.5, 25.5))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
# print(r.choice(city, k=3))
# r.shuffle(city)
# print(city)

# city = [7, 8, 5, 34, 7, 54, 3, 5]
# print(r.choice(city))
# print(r.choice(city, k=3))
# r.shuffle(city)
# print(city)


# mas = [r.randint(1, 20) for i in range(5)]
# print(mas)
#
# lst = [4, 6, 8, 9, 1]
# print(min(lst))
# print(max(lst))
# print(sum(lst))
# import random as r

# mas = [r.randint(1, 20) for i in range(10)]
# print(mas)
# b = max(mas)
# mas.remove(b)
# mas.insert(0, b)
# print(mas)

# mas = [r.randint(-20, 20) for i in range(20)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# mas = [r.randint(-20, 20) for i in range(20)]
# print(mas)
# b = min(mas)
# lst = mas.index(b)
# print(lst)
# del mas[0:lst]
# print(mas)

# x = list['1a2b3c4d']
# print(x)
# print('a' not in x)
# print('b' not in x)

# lst = [1]
# if len(lst) == 0:
#     print("Список пустой")
# if not lst:
#     print("Список пустой")

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [r.randint(0, 100) for i in range(n1)]
# b = [r.randint(0, 100) for i in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
#
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
#
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списков", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# for row in range(len(m)):
#     print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col],end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# print()
#
# for row in m:
#     for x in row:
#         print(x**2, end="\t\t")
#     print()

# w, h = 10, 10
# matrix = [[x*y for x in range(1, w)] for y in range(1, h)]
# # matrix = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     matrix.append(new_row)
# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# _________________________________________

# import math
#
# num1 = math.ceil(3.2)
# num2 = math.floor(3.8)
# num3 = math.sqrt(2)
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# from math import *
#
# num1 = ceil(3.2)
# print(num)
#
# x = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2*pi*x, 2))

# import time

# second = time.time()
# print(second)
# a = 171522089
# local_time = time.ctime(a)
# print(local_time)
# res = time.localtime()
# print(res)
# print(res.tm_mon, res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(a)))

# pause = 0.5
# print("Запуск программы")
# time.sleep(pause)
# print(pause, "сек.")

# text = input("Название напоминания: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, "")
# print(time.strftime("Сегодня %B %d, %Y"))

# Функции

# def hello(name, age):
#     print("Hello,", name, ". I am ", age, sep="")
#
#
# hello("Irina", 20)
# hello("Ivan", 26)

# def get_sum(a, b):
#     print(a + b)
#
#
#  x = 2
#  y = 5
# get_sum(x, y)
# get_sum('abc', 'hello')
# get_sum(2.5, 4.3)

# def symbol(count, a, b):
#     for i in range(count):
#         print(a, end="")
#         a, b = b, a
#     print()
#
# # def symbol(n, a, b):
# #     [print(b, end='') if i % 2 else print(a, end='') for i in range(n)]
# #     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False
#
# x = 15
# y = 70
# if get_sum(x, y):
#     print(x, "больше", y)
# else:
#     print(y, "больше", x)

# def razn(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# a, b = int(input("a = ")), int(input("b = "))
# print(razn(a, b))

# def cube(a):
#     return a * a * a
#
#
# for i  in range(1, 11):
#     print(i, "в кубе = ", cube(i))

# def change(lst):
#     # lst[-1], lst[0] = lst[0], lst[-1]
#     n = lst.pop()
#     m = lst.pop(0)
#     lst.insert(0, n)
#     lst.append(m)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if "9" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль.")
# else:
#     print("Это ненадежный пароль")


# print( 6 / -3)
# print( 6 // -3)
# print()
# print( 5 / 3)
# print( 5 // 3)
# _______________________________________


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
#
# set_param(10, s="+")
# set_param(5, "*")
# set_param(7)


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         num = n % 10
#         if even and num % 2 == 0:
#             s += num
#         if not even and num % 2 != 0:
#             s += num
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38373))
# print(digits_sum(123465567576))
#
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38373, even=False))
# print(digits_sum(123465567576, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
#
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
#
# print(a == b)
# print(a is b)
#
# s = "Hello"
# print(s, id(s))
# s = s + "World"
# print(s, id(s))
#
# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# s = "Hello"
# print(s, id(s))
# s = s[1:-1]
# print(s, id(s))

# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n += 1
#     print("Измененное значение:", n, id(n))
#     return n
#
# x = 1
# print("До функции:", x, id(x))
# m = add_number(x)
# print("После функции:", m, id(m))


# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n += [4]
#     print("Измененное значение:", n, id(n))
#
#
# x = [1, 2, 3]
# print("До функции:", x, id(x))
# add_number(x)
# print("После функции:", x, id(x))


# Кортеж (turple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst)
# print(tpl)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(a, type(a))
# c = 1, 2, 3, 4, 5
# print(type(c))
# b = tuple(c)
# print(b, type(b))
#
# t = (2,)
# print(type(t))

# a = (1, 2, 3, 4, 5)
# print(a)
# print(a[3])
# print(a[1:3])
# a[3] = 55
# print(a)

# s = turple(int(input("-> ")) for i in range(3))
# print(s)

# from random import randint

# s = tuple(randint(1, 20) for i in range(6))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4))
#
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
#
#
# for i in range(len(t3)):
#     # t3(i) = t3(i) * 2
#     print(t3[i] * 2, end=" ")
# print("\n", t3)

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el)+1)+1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
# def tuple_func(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
# tuple_1 = tuple_func(0, 5)
# tuple_2 = tuple_func(-5, 0)
# tuple_3 = tuple_1 + tuple_2
# count_0 = tuple_3.count(0)
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print('Count 0:', count_0)

# t = (10, "Hello", [1, 2, 3], (4, 5, 6), ["Hello", "world"])
# print(t, id(t))
# t[-1][0] = 'new'
# print(t, id(t))
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# name1, age1, is_married1 = user
# print(user[0])
# print(user[1])
# print(user[2])
# print(name1, age1, is_married1)
#
#
# name2, age2, is_married2 = get_user()
# print(name2, age2, is_married2)

#  ______________________________________

# t = (1, 2, 3)
# # del t
# # print(t)
# print(t)
# t = list(t)
# print(list(t))
# print(t)
# t.append(4)
# t = tuple(t)
# print(t)


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "Население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)


# Множество (set) уникальный тип данныз

# s = {"banana", "apple", "orange", "apple"}
# print(type(s))
# print(len(s))
# print(s)
# b = 'Hello', 'Hi'
# a = set(b)
# print(type(a))
# print(a)

# s = {x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# # num = {i for i in numbers if i % 2 == 0}
# num = list(set(numbers))
# print(num)

# def to_set(s):
#     st = set(s)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# # print('green' not in t)
#
# pr = {2, 5, 3, 7, 11}
# for i in t:
#     print(i, end="")

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s}
# # a = {i for i in s if 'a' not in i}
# print(a)


# a = {0, 1, 2, 3}
# a.add(4)  # добавление элемента
# print(a)
# if 1 in a:
#     a.remove(1)  # удаление элемента
# print(a)
# a.discard(5)  # удаление элемента, без генерации исключения
# print(a)
# a.pop()  # удаление первого элемента, генерация исключения будет при попытке удаления из пустого множества
# print(a)
# a.clear()
# print(a)  # очистка множества

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a.union(b)
# c = a | b
# a |= b
# c = a & b
# a &= b
# c = a - b
# c = a ^ b
# a ^= b
# a -= b
# c = b <= a
# print(a)
# print(c)
#
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7) | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print("Max =", max(s))
# print("Min =", min(s))

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")

# str1 = "Python"
# str2 = "Programming language"
# s = set(str1) - set(str2)
# print(s)
# for i in s:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Женя", "Илья"}
#
# only_one_hobby = drawing ^ music
# print("Только одно хобби:", only_one_hobby)
#
# both_hobbies = drawing & music
# print("Два хобби:", both_hobbies)
#
# drawing = drawing - both_hobbies
# print(drawing)

# frozenset
#
# s = frozenset([1, 2, 3, 4, 5])
# print(s.)
# print(type(s))

# Словарь (dict)

# s = [1, 2]
# d = {'one': 1, 'two': 2, 'ten': 10}
#
# print(d)

# d = {"one": "один", "two": "два"}
# print(d)
# # print(type(d))
# # d["one"] = "один"
# # d["two"] = "два"
# # print(d)
#
# d1 = dict(one="один", two="два")
# print(d1)

# d = {0: "text1", "one": 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# d["one"] = 100
# d[42][1] += 100
# print(d)

# d = {a: a ** 2 for a in range(2, 7)}
# print(d)

# d = [1, 2, 3]
# print(d)
# print(dict(d))


# users = [
#     ['igor@gmail.com', 'Igor'],
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna'],
# ]

# print(users)
# d_users = dict(users)
# print(d_users)
# print()

# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna'),
# )
#
# print(user)
# d_user = dict(user)
# print(d_user)
#
# # print('irina@gmail.com' in d_user)
#
# for key in d_user:
#     print(key, "->", d_user[key])

# ------------------------------------

# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'two1'
#
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print(d)


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# mult = 1
# for key in d:
#     mult *= d[key]
#
# print(mult)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Исключить: "))
# del d[dislike]
# print(d)


# d = {'one': 1, 'two': 2, 'three': 3}
# print(len(d))

# goods = {
#     "1": ["Core-i-4330", 9, 4500],
#     "2": ["Core i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium 63220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         m = int(input("Количество: "))
#         goods[n][1] = m
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")

# Методы словарей
#
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d["two"])
# value = d.get("two1", "Ключа нет")
# print(value)
# print(d.keys()) # список ключей из словаря
# print(d.items()) # список ключей и значений словаря в виде кортежа
# print(d.values()) # список значений словаря

# for key, value in d.items():
#     print(key, "=>", value)

# d.clear()  # очистить словарь
# d = {'one': 1, 'two': 2, 'three': 3}
# d2 = d.copy()  # копия словаря
# print("D =", d)
# print("D2 =", d2)
#
# d["four"] = 4
# d2["five"] = 5
# print("D =", d)
# print("D2 =", d2)


# d = {'one': 1, 'two': 2, 'three': 3}

# item = d.pop('two')  # удаляет элемент по ключу, возвращает удаляемое значение (не ключ)
# item = d.pop('two', "Ключа нет")
# item = d.setdefault("four", 4) # добавляет ключ и значение в словарь по умолчанию, если ключа нет
# item = d.popitem()  # удаляет последнюю (произвольную) пару ключ и значение, возвращает удаляемое значение
# в виде кортежа
# print(item)
# print(d)

# d.update({'four': 4, 'five': 5})
# d.update([('four', 4), ('five', 5)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# # z = x | y  # объединение словарей с сохранением в новый словарь
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# # print(d)
# # print(new_d)
#
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     },
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")


# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anna": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3654, "E": 8821, "W": 2451},
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_d = {v: k for k, v in d.items()}
# print(new_d)

# d = {'three': 3, 'one': 1, 'two': 2, 'four': 4}
# new_d = {k: v for k, v in d.items() if v == 1 or v == 2}
# print(new_d)


# s = "Hello"
# d = {i: i * 3 for i in s}
# print(d)

# lt = [1, 2, 3, 4]
# value = input("-> ")
# d = {i: value for i in lt}
# print(d)

# d = {'three': 3, 'one': 1, 'two': 2, 'four': 4}
# value = list(d)
# value = list(d.items())
# value = list(d.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i # s = 'one'
#     else:
#         d[s].append(i)  # d['one'}.append(10)
# print(d)

# zip()

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# d = list(zip('one', 'two'))
# print(d)

# a = [1, 2, 3]
# print(list(zip(a)))

# print(list(zip(range(5), range(95, 100))))
#
# a = [1, 2, 3]
# b = {'one', 'two', 'three'}
# c = (4.0, 5.4, 6.7)
# print(tuple(zip(a, b, c)))

# ___________________________

# stud = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i+1) + "- й студент: ")
#     point = int(input("Балл: "))
#     stud[sname] = point
#     s += point
#
# avrg = s / n
# print(stud)
# print(avrg, 2)
#
# for i in stud:
#     if stud[i] > avrg:
#         print(i)

# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, v1)
#     print(k2, v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # print(dict(pairs))
# a, b = zip(*pairs)
# print(a)
# print(b)

# letters = ['b', 'a', 'd', 'c']
# numbers = [3, 1, 2, 4]
# data = list(zip(letters, numbers))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(numbers, letters))
# data1.sort()
# print(data1)
# data2 = dict(data1)
# print(data2)
# data3 = sorted(data2.items())
# print(data3)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
#
# print({**two, **one})  # распаковка словаря
#
# for k, v in {**two, **one}.items():
#     print(k, "->", v)

# data = [2, 5, 3, 4, 1, 5]
# for i in data:
#     print(i, end=" ")
# print()
# for i in range(6):
#     print(i, end=" ")
#
# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ")", color, sep="")
#     i += 1

# colors = ['red', 'green', 'blue']
# for num, val in enumerate(colors, 1):
#     print(num, ") ", val, sep="")


# n = {i: i + 1 for i in range(10, 18)}
# print(n)
#
# for i, (j, v) in enumerate(n.items(), 100):
#     print(i, ": ", j, " ->", v, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(2, 3, 4, 5, 1))
# print(func(2, 4, 7))
# print(func())


# def to_dict(*lst):
#     return {i: i for i in lst}
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def ch(*args):
#     res = []
#     sr = sum(args) / len(args)
#     print(sr)
#
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# def print_scores(student, *scores):
#     print("Student Name:", student)
#     for score in scores:
#         print(score)
#
#
# print_scores("Джонатан", 100, 95, 88, 92, 99)
# print_scores("Роман", 96, 20, 33)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d="python"))


# def db(**data):
#     my_dict.update(data)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='gray')
# print(my_dict)


# def func(aa, *args, d=0, **kwargs):
#     return aa, args, d, kwargs
#
#
# print(func('one', 5, 9, 7, 8, 1, a=1, b=2, c=3, d=6))


# Области видимости

# name = "Tom"  # глобальная переменная
# surname = None
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # локальная переменная
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name, surname)
#
#
# print(name)
# hi()
# bye()
# print(name)

# i = 5
# arg = 5
#
#
# def func(arg):
#     print(arg)
#
#
# i = 6
# arg = 6
# func(arg)  # 6

# x = 7
#
# def add_five(a):
#     x = 2
#
#     def add_two():
#         return a + x
#
#     return add_two()
#
#
# print(add_five(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# min = [5, 6, 8, 9, 7]
# print(max(min))
# a = [5, 6, 7, 8, 8]
# print(min(a))


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
# outer_func('World!')


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("a + b =", a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal: ", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# z = x + t  # 25 + 30 = 60
# print(z)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()

# _______________________


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add1(10))
#
# print(outer(7)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2()
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def func1():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return func1()
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
#
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
#
#
# # Lambda (анонимная функция)
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))
#
#
# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
# print(summa('a', 'b'))

# print((lambda x, y: x**2 + y**2)(2, 5))

# s = lambda a=1, b=2, c=3: a + b + c
#
# print(s())
# print(s(10, 20, 30))
#
# s = lambda *args: args
#
# print(s(1, 2, 3, 4))
# print(s(10, 20, 30))
#
# f = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for i in f:
#     print(i('abc_'))

# def inc1(n):
#     def add_two(x):
#         return x + n
#
#     return add_two
#
#
# def inc(n):
#     return lambda x: x + n


# f = inc(42)
# print(f(1))
# print(f(3))
#


# inc = (lambda n: (lambda x: x + n))
#
#
# print(inc(42)(1))
# print(inc(42)(3))
# f = inc(42)
# print(f(1))
# print(f(3))
#
# sum3 = (lambda x: lambda y: lambda z: x + y + z)
# print(sum3(2)(4)(6))

# d = {'b': 15, 'a': 10, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)

# def func(i):
#     return i[1]
#
# d = {'b': 15, 'a': 10, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](15, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: x + 3, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda : print('Понедельник'),
#     2: lambda : print('Вторник'),
#     3: lambda : print('Среда'),
#     4: lambda : print('Четверг'),
#     5: lambda : print('Пятница'),
#     6: lambda : print('Суббота'),
#     7: lambda : print('Воскресенье'),
# }
#
# d[4]()

# print((lambda a, b: a if a > b else b)(15, 13))
#
# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(9))
# print((lambda a, b, c))

# def mult(t):
#     return t * 2
#
#
# lst = [1, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst))
#
# print(lst2)
#
# print(list(map(lambda t: t * 2, lst)))

# t = (2.88, -1.75, 100.55)
#
# print(turple(map(lambda x: int(x), t)))
# print(turple(map(int, t)))

# areas = [3.456789, 5.578945, 7.45689, 45.45678, 78.985423, 1.245678]
#
# print(list(map(round, areas, range(1, 3))))
# print(list(map(int, areas, range(2, 8))))
#
# # print(round(3.456789, 2))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))
# print(dict(map(lambda x, y: (x, y), st, num)))
#
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))
#
# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(turple(filter(lambda s: len(s) == 3, t)))
#
# b = [66, 90, 68, 59, 76, 60, 80, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# lst = [random.randint(1, 30) for _ in range(10)]
# lst_new = list(filter(lambda x: 9 < x < 21, lst))
# print(lst)
# print('[10; 20] =', lst_new)
#
# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
# m1 = [x ** 2 for]

#  ____________________

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('**************')
#         func()
#         print('==============')
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def bye():
#     print("Hello, I am func 'bye'")
#
#
# func_test()
# bye()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         # print("1)", args[0])
#         # print("kw", kwargs['study'])
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(n1):
#     def mult(fn):
#         def wrap(n2):
#             return n1 * fn(n2)
#
#         return wrap
#     return mult
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k] != kwargs[k])
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Dog"))
# print(typed_fn2("Hello", "World", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello", "World", z='5'))

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world('Hi!')
# hello_world2('world!')


# print(int("18"))
# print(int(18.5))
# print(int("18.5"))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  #0b10010
# print(oct(18))  #0o22
# print(hex(18))  #0x12

# print(0b10010)
# print(0o22)
# print(0xFF)

#  #FF0000
#  rgb(255, 0, 0)

# ---------------
# def decor(func):
#     def wrap(*args):
#         print("Среднее арифметическое чисел", str(args)[1:-1], "=", func(*args) / len(args))
#     return wrap
#
#
# @decor
# def summ(*args):
#     print("Сумма чисел", str(args)[1:-1], "=", sum(args))
#     return sum(args)
#
#
# summ(2, 3, 3, 4)


#  ______________

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print(e in "I am learn Python1")
#
# print(e[5::-1])
# print(e[3])
# e = e[:3] + "t" + e[4:]
# print(e)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# print(str1)
# print(str2)

# print("Привет")
# print(u"Привет")

# print('C:\\program\\file\\')
# print(r'C:\program\file' + "\\")
# print(r'C:\program\file\\'[:-1])

# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age), 'лет.')
# print(f"Меня зовут {name}. Мне {age} лет.")

# from math import pi
#
# print(f"Значение числа pi: {round(pi, 2)}")
# print(f"Значение числа pi: {pi:.2f}")

# x = 10
# y = 5
# print(f"{x=}\n{y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# a = 74
# print(f"{{{{{a}}}}}")

# dir_name = "my_doc"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print(f"home\\{dir_name}\\{file_name}")
# print(r"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# s = """
# <div>
#     <a href="a">content</a>
# </div>
# """
# s1 = '''
# <div>
#     <a href="#">content</a>
# </div>
# '''
# print(s)
# print(s1)

# def square(n):
#     """Принимает число n возвращает квадрат числа n"""
#     return n ** 2
# print(square(5))
# print(square.__doc__)

# import math as m
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('к'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for mes"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# mean = round(sum(arr) / len(arr))
# arr.insert(0, mean)
# arr = [int(sum(arr)/len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr +=[x for x in [ord(x) for x in (input("-> " + " ")[:6])]if x not in arr]
# # arr += [ord(x) for x in (input("->" + " ")[:6])if x not in arr]
# print(arr)
# arr.sort(reverse = True)
# print(arr)

# print(chr(101))
# print(chr(94))
# print(chr(1085))

# a = 122
# b = 97
#
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))
#
# q = [chr(x) for x in range(min(a, b), max(a, b) +1)]
# print(*q)
#  ________________

# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))  # 97
# print(ord('A'))  # 68

# def decor(func):
#     def wrap(*args):
#         print("Среднее арифметическое чисел", str(args)[1:-1], "=", func(*args) / len(args))
#     return wrap
#
#
# @decor
# def summ(*args):
#     print("Сумма чисел", str(args)[1:-1], "=", sum(args))
#     return sum(args)
#
#
# summ(2, 3, 3, 4)


#  ______________

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print(e in "I am learn Python1")
#
# print(e[5::-1])
# print(e[3])
# e = e[:3] + "t" + e[4:]
# print(e)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# print(str1)
# print(str2)

# print("Привет")
# print(u"Привет")

# print('C:\\program\\file\\')
# print(r'C:\program\file' + "\\")
# print(r'C:\program\file\\'[:-1])

# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age), 'лет.')
# print(f"Меня зовут {name}. Мне {age} лет.")

# from math import pi
#
# print(f"Значение числа pi: {round(pi, 2)}")
# print(f"Значение числа pi: {pi:.2f}")

# x = 10
# y = 5
# print(f"{x=}\n{y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# a = 74
# print(f"{{{{{a}}}}}")

# dir_name = "my_doc"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print(f"home\\{dir_name}\\{file_name}")
# print(r"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# s = """
# <div>
#     <a href="a">content</a>
# </div>
# """
# s1 = '''
# <div>
#     <a href="#">content</a>
# </div>
# '''
# print(s)
# print(s1)

# def square(n):
#     """Принимает число n возвращает квадрат числа n"""
#     return n ** 2
# print(square(5))
# print(square.__doc__)

# import math as m
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('к'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for mes"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# mean = round(sum(arr) / len(arr))
# arr.insert(0, mean)
# arr = [int(sum(arr)/len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr +=[x for x in [ord(x) for x in (input("-> " + " ")[:6])]if x not in arr]
# # arr += [ord(x) for x in (input("->" + " ")[:6])if x not in arr]
# print(arr)
# arr.sort(reverse = True)
# print(arr)

# print(chr(101))
# print(chr(94))
# print(chr(1085))

# a = 122
# b = 97
#
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))
#
# q = [chr(x) for x in range(min(a, b), max(a, b) +1)]
# print(*q)
#  ________________

# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))  # 97
# print(ord('A'))  # 68

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#     print("Ваш случайный пароль:", random_password())

# print(dir(str))

# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize())  # приводит первую букву в верхний регистр, остальные в нижний
# print(s.lower())  # преобразует все символы в нижний регистр
# print(s.upper())  # преобразует все символы в верхний регистр
# print(s.swapcase())  # меняет регистр на противоположный
#
# print(s.count('o'))  #  подсчитывает количество вхождений подстроки в строки (количество заданных символов)
# print(s.lower().count('o', 0, -5))
#
# print(s.find("Python")) # возвращает первый индекс, который соответствует заданной подстроке. Если совпадений нет.
#
# print(s.index("Python", -3))
#
# print(s.index("Python1"))  # возвращает первый индекс, который соответствует заданной подстроке. Если совпадений нет.
# # то возвращается ошибка ValueError

# s = 'один два'
# ind = s.find(' ')
# print(ind)
# s = s[ind + 1:] + ' ' + s[:ind]
# print(s)

# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)

# s = "hello, WORLD! I am learning Python."
#
#
# print(s.rfind("l"))
# print(s.rindex("l"))
# print(s.find("l", 4))

# a = "Nearly all web services collect this basic information from users in their server logs. " \
#     "However, Python Tutor does not collect any personally identifiable information from its users."
#
# n = 'f'
#
# if a.count(n) == 1:
#     print(a.find(n))
# elif a.count(n) > 2:
#     print(a.find(n), a.rfind(n))

# s = "I am learning Python, hello, WORLD"
# ind1 = s.find('h')
# print(ind1)
# ind2 = s.rfind('h')
# print(ind2)
# res = s[:ind1] + s[ind2 + 1:]
# print(res)

# s = "hello, WORLD! I am learning Python."
#
#
# print(s.startswith("he"))  # с чего начинается строка
# print(s.endswith("Python."))  # чем заканчивается строка
# # возвращает True или False

# print('abc123'.isalnum())  # строка состоит избукв и цифр
# print('abc?123'.isalnum())
# print(''.isalnum())
#
# print('abcABC'.isalpha()) # строка состоит только из букв (любой регистр)
# print('abc123'.isalpha())
#
# print('aa$123'.isdigit())
# print('123'.isdigit())  # строка состоит только из цифр

# print('py'.center(10, "-"))
# print('py'.center(7, "-"))
#
# print("   py".lstrip())  # удаление пробельных символов слева
# print("py  ".rstrip())  # удаление пробельных символов справа
# print("     py  ".strip())  # удаление пробельных символов справа и слева одновременно
#
# print('https://www.python.prg'.lstrip('/;pths'))
# print('py.$$$;'.rstrip(';$.'))
#
# print('https://www.python.orgw'.strip('/:pths.org'))
# print('https://www.python.orgw'.lstrip('/:pths').rstrip('.orgs'))
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python", 2))  #  заменяет вхождение подстроки в строку


# s = "-"
# seq = ['a', 'b', 'c']
# print(s.join(seq))
#
# print("..".join(['1', '99']))
# print("..".join(['1', '2']))
#
# print(":".join("Hello"))  #  объединяет итерируемую последовательность в строку через символ разделитель


# print("Строка разделения пробелами".split())
# print('www.python.org.ru'.split(".", 2))
# print('1,2,3'.split(","))
# print('www.python.org.ru'.rsplit(".", 2))

# a = input("-> ").split()
# print(a)
# a = list(map(int, a))
# print(a)

# s = "В строке заменить пробелы звездочками"
# s = s.split()
# s= "*".join(s)
# print(s)

# s = input('FIO: ').split()
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')

#  Регулярные выражение

# import re
#
# # print(dir(re))
#
# import re
#
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812"
# reg = r'2[0-9][0-9][0-9][0-9]'
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения сзаданным шаблоном
#
# print(re.search(reg, s))  # возвращает данные по соответствию первого совпадения с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
#
# print(re.match(reg, s))  #  поиск по заданному шаблону в начале строки

# print(re.split(reg, s, 1))  # разбивает строку на список подстрок
#
# print(re.sub(reg, "!", s, 1))  # поиск и замена
# print(re.findall(reg, s))

#  _____________________

# print("Hello")
# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812. [Hello]"
# reg = r'[^0-9]'
# print(re.findall(reg, s))
# print(ord("Я"))
# print(ord("а"))

# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапозоне от 00 до 59. 2021-06-15T01:09"
# r1 = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(r1, s1))

# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12. [Hello]"
# reg = r'20*'
# # print(re.findall(reg, s))
# #
# # d = "Цифры: 7, +17, -42, 0013, 0.3"
# # print(re.findall(r'[+-]?[\d.]+', d))
#
#
# d = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub('#.*', '', d))
# print("Дата рождения:", re.sub('-', '.', re.sub('#.*', '', d)))

# d = "author=Пушкин А.С.; title = Евгений Онегин; price -200; year= 1831"
# # r1 = r'\w+\s*=\s*\w+\s*[\w.]*'
# r1 = r'\w+\s*=[^;]+'
# print(re.findall(r1, d))

# s1 = "12 сентября 2023 года"
# r1 = r"\d{2,4}"
# print(re.findall(r1, s1))

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# r = r"\+?7\d{10}"
# print(re.findall(r, s))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12."
# reg = r'\w+\.$'
# print(re.findall(reg, s))
# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = "hello world"
# print(re.findall(r'\w\+', text, re.DEBUG))
# reg = "я"
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one$", text))
# # print(re.findall(r"one$", text, re.MULTILINE))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall("""
# [\w-]+  # part
# @       # @
# [\w-]+  # part2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))


# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name)[0]
#
#
# print(validate_name('Python_master'))
# print(validate_name('Pyt'))

# s1 = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# # reg = r'[\w.-]+@\w*\.?\w*\.?\w*'
# reg = r'[\w.-]+@[\w.-]+[\w]{2,3}'
# print(re.findall(reg, s1))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
#
# # *?, +?, ?? - "ленивое соответствие" - захватывает минимально возможное число символов
# # {m,n}?, {,n}?, {m,}?
#
# s1 = "12 сентября 2023 года 568561"
# r1 = r"\d{3,}?"
# print(re.findall(r1, s1))

# t = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*>'
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# print(re.findall(reg, t))


# t = "Петр, Ольга и Виталий отилично учатся"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, t))

# t = "int = 4, float = 4.0, double = 8.0f"
# reg = r"(int|double)\s*=\s*\d+[\w.]*"
# print(re.findall(reg, t))


# (?: ) - скобки не сохраняющие (группирующие)

# def validate_name(name):
#     return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)
#
#
# print(validate_name('my-p@ssw0rd'))

# s1 = '127.0.0.1'  # 192.168.255.255
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s1))


# s1 = "Word2016, PS6, AI5"
# reg = r'(([a-z]+)(\d+))'
# print(re.findall(reg, s1, re.IGNORECASE)[0][0])

# s1 = "5 + 7*2 -4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s1))


# a = '31-08-2021'
# reg = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])$'
# print(re.findall(reg, a))
# print(re.search(reg, a))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s)[0])
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.findall(r'\s*(\w+)\s*', text))
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))

# s = "<p>Изображения <img src=\'bg.jpg\'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=(['\"])(.+)\1>"
# print(re.findall(reg, s)[0][1])

# s = "<p>Изображения <img src=\'bg.jpg\'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=(?P<q>['\"])(.+)(?P=q)>"
# print(re.findall(reg, s)[0][1])
#
# # (?P<name>) (?P=name)

# s = "Самолет прилетает 10/23/2023. Будем вас рады видеть после 10/21/2023"  # 24.10.2023
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)  # 5
#     print(n, end=" ")
#
# n1 = int(input("На каком вы этаже: "))  # 5
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += 1
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  # 7
#     convert = "0123456789ABCDEF"
#     if n < 0:
#         covert = convert[0] + convert[:0:-1]
#         if n * (-1) < base:
#             return "-" + convert[n]
#         else:
#             return to_str((n // base) + 1, base) + convert[(n % base)]
#     else:
#         if n < base:
#             return convert[n]
#         else:
#             return to_str(n // base, base) + convert[n % base]  # '9' '6'
#
#
# print(to_str(254, 16))
#
# # print(hex(-255))
# # print(int('FF', 16))
#
# #  _________________


# def negative(a):
#     if not a:
#         return 0
#     else:
#         count = negative(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(lst)
# n = negative(lst)
# print(n)

# def validate_phone(number):
#     reg = r"^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$"
#     return re.search(reg, number).group()
#
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+7 4994564578'))
# print(validate_phone('7 (499) 456 45 78'))
# print(validate_phone('7 (499) 456-45-78'))


# names = ["Adam", ["Bob", ["Chat", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# # print(names[0])
# # print(names[1])
# # print(isinstance(names[0], str))
# # print(isinstance(names[1], list))
# # print(names[1][1][0])
# # print(isinstance((names[1][1][0], list)))
# # print(len(names))
# print(names)
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# names = ["Adam", ["Bob", ["Chat", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for name in item_list:
#         if isinstance(name, str):
#             count += 1
#         elif isinstance(name, list):
#             for n in name:
#                 if isinstance(n, str):
#                     count += 1
#                 elif isinstance(n, list):
#                     count += len(n)
#     print(count)
#
#
# count_items(names)

# names = ["Adam", ["Bob", ["Chat", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
#
#
# def count_items(item_list):
#     count = 0
#     stack - []
#     current_list = item_list
#     i = 0
#     while True:
#         if i == len(current_list):
#             if current_list == item_list:
#                 return count
#             else:
#                 current_list, i = stack.pop()
#                 i += 1
#         if isinstance(current_list[i], list):
#             stack.append([current_list, i])
#             current_list = current_list[i]
#             i = 0
#         count += 1
#         i += 1
#
#
# print(count_items(names))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
#
#
# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[0:1] + union(s[1:])  # ["Adam", "Bob", "Chet", "Cat"]
#
#
# print(union(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " " or text[0] == "$":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" $Hello\tWorld!$ "))


# Линейный (последовательный) поиск

# def seq_search(s, item):
#     pos = 0  # 2
#     found = False  # True
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 28, 65]
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 3))  # False

# def seq_search(s, item):
#     pos = 0  # 2
#     found = False  # True
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 28, 65]
# lst.sort()
# print(lst)
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 28))  # False

# Бинарный поиск

# def binary_search(s, item):
#     first = 0  # 0
#     last = len(s) - 1  # 9
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2  # 4
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
# print(binary_search(lst, 26))
# print(binary_search(lst, 28))

# Алгоритмы сортировки
# "пузырьковая сортировка"

# from random import randint
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [randint(1, 100) for i in range(10)]
#
# print(a)
# bubble(a)
# print(a)


# def binary_search(s, item):
#     found = False
#     first = 0
#     last = len(s) - 1  # 9
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2  # 4
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# a = [randint(1, 100) for i in range(10)]
# print(a)
# a.sort()
# print(a)
# n = int(input("Введите число: "))
# if binary_search(a, n):
#     print(f"Число {n} в списке присутствует")
# else:
#     print(f"Число {n} в списке отсутствует")


# from random import randint
# import time
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [randint(1, 100) for i in range(10000)]
#
# # print(a)
# start = time.monotonic()
# bubble(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# n = int(input("Введите число: "))
# if binary_search(a, n):
#     print(f"Число {n} в списке присутствует")
# else:
#

# from random import randint
# import time
#
#
# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n // 2])
#     right = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# array = [randint(1, 100) for i in range(10000)]
# # print(array)
# start = time.monotonic()
# array = merge_sort(array)
# # print(array)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# Сортировка Шелла

# from random import randint
# import time
#
#
# def shell_sort(s):
#     qap = len(s)
#
#     while qap > 0:
#         for val in range(qap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= qap and s[pos - qap] > cur_val:
#                 s[pos] = s[pos - qap]
#                 pos -= qap
#                 s[pos] = cur_val
#
#         qap //= 2
#     return s
#
#
# a = [randint(1, 100) for i in range(10000)]
# # print(a)
# start = time.monotonic()
# shell_sort(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")


# Быстрая сортировка

# from random import randint
# import time
#
#
# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         hi = [i for i in a if i > x]
#         a = quick_sort(low) + eq + quick_sort(hi)
#     return a
#
#
# lst = [randint(1, 100) for i in range(10000)]
# start = time.monotonic()
# # print(lst)
# # lst = quick_sort(lst)
# # print(lst)
# lst.sort()
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# работа с файлами

# f = open(r'C:\Users\Admin\Desktop\python\text1.txt')
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)
#
#
# f = open('text1.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# count = 0
# f = open('test.txt')
# for line in f:
#     count += 1
# print(count)
#
# f.close()
#
# fail = open('test.txt')
# count_lines = len(fail.readlines())
# print(count_lines)


# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld')
# f.close()

# f = open('xyz.txt', 'a')
# # f.write('Hello\nWorld')
# # lines = ['This is line 1', 'This is line 2']
# lines = [str(i ** 5) for i in range(1, 20)]
# print(lines)
# # f.writelines(lines)
# for index in lines:
#     f.write(index + "\t")
# f.close()


# f = open(("text2.txt", "w"))
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open("text2.txt", "r")
# read_f = f.readline()
# print(read_f)
# for i in range(len(read_f)):
#     if read_f[i] == "Изменить строку в списке;\n":
#         read_f[i] = "Hello World!"
# print(read_f)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_f)
# f.close()
#
# f.close()

#  ____________________

# f = open("text1.txt", "r")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text1.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# with open('text3.txt', 'w+') as f:
#     print(f.write('0123456789\n123456789'))
#
#
# with open('text3.txt', 'r') as f:
#     for line in f:
#         print(line[:6])


# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 1.0, 0.3, 4.33, 7.777]
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return '\t'.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")

# file_name = 'res_1.txt'
#
# numbers = [4.5, 2.8, 1.0, 0.3, 4.33, 7.777]
#
# def get_string(l: list) -> str:
#     return '\t'.join(map(str, l))
#
#
# with open(file_name, 'r+', encoding='utf-8') as file:
#     nums = file.read()
#     print(nums)
#     nums_list = list(map(float, nums.split('\t')))
#     print(nums_list)

# def longest_world(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = 'res_1.txt'
# print(longest_world(file_name))

#
# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)


# read_file = 'one_txt'
# write_file = 'two_txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)


# Модуль OS (OS.PATH)

# import os
# import os.path
# import time
#
# print(os.path.split(r'C:\Users\Admin\Desktop\python'))

# print(os.getcwd())  # возращает текущую директорию
# print(os.listdir())  # возвращает список папок и файлов, находящихся в текущей директории
# print(os.listdir("../.."))  #

# os.mkdir("folder")  # создает директорию по указанному пути
# os.makedirs("nested1/nested2/nested3")  # создает не только конечную директорию, но и промежуточные папки

# os.remove("xyz.txt")  # удаление файла

# os.rename("nested1", "test")  # переименование папок и файлов

# os.rename("text.txt", "test/text1.txt")  # перемещение файла, все промежуточные директории должны существовать обязательно
# os.renames("text1.txt", "text/text.txt")  # создаются промежуточные директории

# os.rmdir("folder")  # удаление пустой директории

# for root, dirs, files in os.walk("test", topdown=True):  #  topdown=True - сверху сниз, topdown=False - снизу вверх
#     print("Root:", root)
#     print("Sub_dirs:", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
#
# remove_empty_dirs("test")

# os.path

# print(os.path.split(r'C:\Users\Admin\Desktop\python\.txt')[1])  # разбивает путь на кортеж
# print(os.path.dirname(r'C:\Users\Admin\Desktop\python\.txt'))  # имя директории
# print(os.path.basename(r'C:\Users\Admin\Desktop\python\.txt'))  # имя файла

# print(os.path.join(r'D:\Python212', '212', 'test', 'xyz.txt'))  # соединяет один или несколько компонентов пути с
# # учетом особенностей OS
#
# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()
#
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirss, fl in os.walk(root, topdown):
#         print(root)
#         print(dirss)
#         print(fl)
#     print('-' * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', True)


# print(os.path.exists(r'D:\Python212\212\test\nested2\nested3\xyz1.txt'))  # возвращает True, если путь указывает на
# # существующий путь в файловой системе

# path = r'D:\Python212\212\venv\Script\python.exe'
# k_size = os.path.getsize(path)  # размер файла
# print(k_size // 1024)
# print(os.path.getmtime(path))  # время последнего изменения файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
# t = os.path.getctime(path)  # время создания файла
# print(time.strftime(("%d.%m.%Y, %H:%M:%S", time.localtime(t))))

# ________________

# file_path = r'test\nested2\test.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getmtime(file_path)
#     print(f"{name} ({dirs})) - last access time {time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(atime))}")
# else:
#     print(f"File {file_path} does not exist!")

# print(os.path.isfile(file_path))  # возвращает True, если указанный путь является файлом
# print(os.path.isdir(file_path))  # возвращает True, если указанный путь является директорией


# dir_name = r"test\nested2"
#
# obj = os.listdir(dir_name)
# print(obj)
#
# for i in obj:
#     p = os.path.join(dir_name, i)
#     # print(p)
#     if os.path.isfile(p):
#         print(f'{i} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{i} - dir')

# ООП (объектно-ориентированное программирование)


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# print(dir(Point))
# print(Point.__doc__)
# class Point3D:
#     pass
#
#
# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 410
# p1.y = 200
# Point.y = 100
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(Point.__dict__)
# print(type(p1))
# print(isinstance(p1, Point))

# p2 = Point()
# print(p2.x, p2.y)
#
# print(id(Point))
# print(id(p1))
# print(id(p2))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         # print(self.__dict__)
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
#
# p1.set_coord(5, 10)
# Point.set_coord(p1, 8, 12)
# # print(p1.__dict__)
#
#
# p2 = Point()
# # p2.x = 20
# # p2.y = 30
# p2.set_coord(20, 30)
# print(p2.__dict__)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.city = city
#         self.country = country
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Анна")
# print(h1.get_name())


# class Car:
#     model = None
#     year = None
#     name_pr = None
#     power = None
#     color = None
#     price = None
#
#     def input_data(self, m, y, name, p, c, pr):
#         self.model = m
#         self.year = y
#         self.name_pr = name
#         self.power = p
#         self.color = c
#         self.price = pr
#
#     def output_data(self):
#         print("Название модели:", self.model)
#         print("Год выпуска:", self.year)
#         print("Производитель:", self.name_pr)
#         print("Мощность двигателя:", self.power, 'Л.,С.')
#         print("Цвет машины:", self.color)
#         print("Цена:", self.price)
#
#     def get_model(self):
#         return self.model
#
#     def set_model(self, value):
#         self.model = value
#
#
# BMW = Car()
# BMW.input_data('X7 N501', 2021, 'BMW', 530, "white", 10790000)
# BMW.output_data()


# class Person:
#     skill = 10
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Инициализатор {self.name} {self.surname}")
#
#     def __del__(self):
#         print("Удаление экземпляра\n\n")
#
#     def print_info(self):
#         print("Данные о сотруднике:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника:, {self.name}", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
# del p1
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# print("count =", Point.count)
# p2 = Point(15, 20)
# print(p2.count)
# p3 = Point(23, 39)
# print(p3.count)
# print("count =", Point.count)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация {self.name}")
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "Был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print()
# del droid1
# del droid2
# print("Численность роботов:", Robot.k)
# _______________________________

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата {self.__x} должна быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата {self.__y} должна быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(1.5, 7)
# p1.x = 100
# print(p1.get_coord())
# p1.x = 100
# p1.y ='abc'
# print(p1.x, p1.y)
# p1.set_x('8')
# p1.set_y(16)
# print(p1.get_x())
# print(p1.get_y())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)

# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата {self.__x} должна быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата {self.__y} должна быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# # print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         print("вызов __get")
#         return self.__x
#
#     def __set_x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print("Вызов __get")
#         return self.__x
#
#     @x.getter
#     def x(self):
#         print("Вызов __get")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class KgToPounds:
#     def __init(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "Фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "Фунтов")
# weight.kg = 'abc'
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "Фунтов")

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.old = 31
# print(p1.old)
# # del p1.name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(p1.__dict__)
# print(Point.get_count())
# print(p2.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Count:
#
#     @staticmethod
#     def maxin(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def print(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def avg(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def fact(a):
#         factorial = 1
#         for i in range(1, a + 1):
#             factorial += 1
#         return factorial
#
# print(Count.maxin(3, 5, 7, 9))
# print(Count.minin(3, 5, 7, 9))

# import math
#
#
# class Area:
#     count = 0
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         p = (a + b + c) / 2
#         Area.count += 1
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print(f"Площадь треугольника по формуле Герона:", Area.triangle_area(3, 4, 5))
# print(f"Площадь треугольника через основание и высоту:", Area.triangle_area2(6, 7))
# print(f"Площадь квадрата:", Area.square_area(7))
# print(f"Площадь прямоугольника:", Area.rect_area(2, 6))
# print(f"Количество подсчетов площади: {Area.get_count()}")

# __________

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '89.12.2021',
#     '12.31.2022'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Неправильная дата или формат строки с датой")
#
#
# # string_date = "23.10.2021"
# # day, month, year = map(int, string_date.split("."))
# # date = Date(day, month, year)
# date = Date.from_string("23.10.2021")
# print(date.string_to_db())
#
# # string_date2 = "15.11.2021"
# # day, month, year = map(int, string_date2.split("."))
# date2 = Date.from_string("15.11.2021")
# print(date2.string_to_db())

#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print(f"Проценты были успешно начислены:")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account(num='12345', surname="Долгих", percent=0.03, value=1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# _______________
# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.__password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#
#         letters = "".join(re.findall(r'[а-яё-]', fio, re.IGNORECASE))
#         for s in f:
#             print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 18 or old > 90:
#             raise TypeError("Возраст должен быть числом в диапозоне от 18 до 90 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественный числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, '1234 567890', 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# p1.old = 35
# p1.password = '4567 123456'
# p1.weight = 70.0
# print(p1.__dict__)


# Наследование
#
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         print("Переопределенный инициализатор Line")
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# # class Rect(Prop):
# #     def draw_rect(self) -> None:
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# # print(line.__dict__)
# # line._width = 5
# line.draw_line()
#
# # rect = Rect(Point(1, 2), Point(10, 20))
# # rect.draw_rect()
# # print(dir(Rect))
#
# # DRY (Don't Repeat Yourself) - не повторяйся!

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         print("Площадь: ", end="")
#         return self.__width * self.__height
#
#     def print_info(self):
#         print(f"Прямоугольник\nШирина: {self.__width}\nВысота: {self.__height}\nЦвет: {self.color}")
#
#
# rect = Rectangle(10, 20, "зеленый")
# rect.color = "синий"
# rect.print_info()
# print(rect.area())


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         print("Prop")
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         print("Line")
#         super().set_coord(sp, ep)
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(10, 20), Point(100, 200))
# line.draw_line()
# print()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
# rect.set_coord(Point(20.3, 30), Point(50, 70))
# rect.draw_rect()

# ________________
# class Rect:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.__width}\nВысота: {self.__height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return "\t".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# Перегрузка методов

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координаты должны быть числами")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(10, 20), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе долже быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()


# Абстрактный метод

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")
#
# for elem in e:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")


# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Обычный метод")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод внутреннего класса", MyOuter.age) # self.name
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# print(g.name)
# print(outer.name)

# class Intern:
#     def __init__(self):
#         self.name = "Intern"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Head"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
#
# d1.display()
# d2.display()

# _______________________
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end=" ")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i7'
#             self.ram = 16
#
#         def show(self):
#             print(f" => {self.brand}, {self.cpu}, {self.ram}")
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.show()
# s2.show()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner")
#
#         class InnerClass:
#
#             def show(self):
#                 print("InnerClass")
#
#
# out = Outer()
# out.show()
#
# inner1 = out.inner
# inner1.show()
#
# inner2 = inner1.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
#
# b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + "is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + "is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()


# class A:
#     def __init__(self):
#         print("A")
#
#     def hi(self):
#         print("A_hi")
#
#
# class AA:
#     def __init__(self):
#         print("AA")
#
#     def hi(self):
#         print("AA_hi")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#
#     def hi(self):
#         print("B_hi")
#
#
# class C(AA):
#     def __init__(self):
#         print("C")
#
#     def hi(self):
#         print("C_hi")
#
#
# class D(B, C):
#     def __init__(self):
#         print("D")
#         B.__init__(self)
#         C.__init__(self)
#
#     def hi(self):
#         C.hi(self)
#
#
# d = D()
# d.hi()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color, width):
#         print("Инициализатор Pos")
#         self.sp = sp
#         self.ep = ep
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     # def __init__(self, sp: Point, ep: Point, color="red", width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Styles.__init__(self, color, width)
#
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
# print(Line.mro())


# Миксины (Примеси)
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)  # "Это строка будет отображаться и записываться в файл
#
#
# class LoggedMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):  # "Это строка будет отображаться и записываться в файл
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggedMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# sub = MySubClass()
# sub.display("Это строка будет отображаться и записываться в файл")
#
#
# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_log()

# Перегрузка операторов

# Число секунд в одном дне: 24*60*60 = 86400

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)


c1 = Clock(100)
c2 = Clock(200)
c4 = Clock(300)
# c3 = c1 + c2 + c4  # c3 = Clock(300)
# c2 += c1
c3 = c1 + c2
print(c1.get_format_time())
print(c2.get_format_time())
# print(c4.get_format_time())
print(c3.get_format_time())

#  _________________________
