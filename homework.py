#  --------homework16-------------
# ---------1--------
# s = "I am learning Python. hello, WORLD!"
# ind1 = s.find('h')
# ind2 = s.rfind('h')
# res = s[0:ind1] + s[ind2 + 1:]
# print(res)

# ---------2--------
# s = "I am learning Python. hello, WORLD!"
# ind1 = s.find('h')
# ind2 = s.rfind('h')
# res = s[0:ind1 + 1] + s[ind1 + 1:ind2][::-1] + s[ind2:]
# print(res)

# ---------3--------
# s = "11 23 44 55 23 22"
# str1 = input("Введите заменяемую подстроку: ")
# str2 = input("Новая подстрока: ")
# print(s.replace(str1, str2))

# ---------4--------

# s = """
# Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели
# """
# col = 0
# for i in s.lower().split():
#     if i.startswith("е"):
#         col += 1
# print(f"Количество слов: {col}")

#  --------homework17-------------
# import re
# # ---------1--------
# # def validate_name(name):
# #     return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)
# #
# #
# # print(validate_name('my-p@ssw0rd'))
#
# # ---------2--------
# s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# reg = r"[0-3][0-9]/[0-1][0-9]/\d{4}"
# print(re.findall(reg, s))

#  --------homework18-------------
# import re
#  ---------1--------

# s = "+7 499 456-45-78, +7 4994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
# r = r"\+?(?:7|\d){1}\s?\(?\d{3}\)?\s?\d{3}\s?\-?\d{2}\s?\-?\d{2}"
# print(re.findall(r, s))


#  ---------2--------

# def sumNumbers(x):
#     if x == []:
#         return 0
#     else:
#         count = sumNumbers(x[1:])
#         if x[0] < 0:
#             count = count + 1
#         return count
#
#
# s = [-2, 3, 8, -11, -4, 6]
# n = sumNumbers(s)
# print("n = ", n)


#  --------homework19-------------

from random import randint


def binary_search(s, item):
    found = False
    first = 0
    last = len(s) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            found = True
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


a = [randint(1, 100) for i in range(10)]
print(a)
a.sort()
n = int(input("Введите число: "))
if binary_search(a, n):
    print(f"Число {n} в списке присутствует")
else:
    print(f"Число {n} в списке отсутствует")


#  --------homework20-------------
# from random import randint
#  ---------1--------


# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [randint(1, 100) for i in range(10)]
# print(lst)
# n = int(input("Введите число: "))
# if seq_search(lst, n):
#     print(f"Число {n} в списке присутствует")
# else:
#     print(f"Число {n} в списке отсутствует")


#  ---------2--------

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open("text2.txt", "r")
# read_f = f.readlines()
# print(read_f)
# pos = int(input("Введите индекс удаляемой строки: "))
# for i in range(len(read_f)):
#     print(read_f)
#     if i == pos:
#         read_f[i] = ""
# print(read_f)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_f)
# f.close()

#  ---------3--------

# a = [5, 9, 6, 7]
# b = [3, 11, 8]
# c = [2, 4]
# d = [10, 1, 12]
# lst = a + b + c + d
#
#
# def bubble(array, n):
#     if n == 1:
#         for i in range(len(array) - 1):
#             for j in range(len(array) - i - 1):
#                 if array[j] < array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#     elif n == 2:
#         for i in range(len(array) - 1):
#             for j in range(len(array) - i - 1):
#                 if array[j] > array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#
#
# print(lst)
# s = int(input("Выберите способ сортировки, где:\n 1 - сортировка по убыванию\n 2 - сортировка по возрастанию\n -> "))
# bubble(lst, s)
# print(lst)
#
#
# def seq_search(lst1, item):
#     y = 0
#     found = False
#     while y < len(lst1) and not found:
#         if lst1[y] == item:
#             found = True
#         else:
#             y += 1
#     return found
#
#
# pos = int(input("Введите значение для поиска: "))
# if seq_search(lst, pos):
#     print(f"Значение {pos} найдено")
# else:
#     print(f"Значение {pos} не найдено")

#  --------homework21-------------
#  -----1------

# with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
#     f1.write("Текст файла № 1")
#     f2.write("Текст файла № 2")
#
# with open("file3.txt", "a") as f3, open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
#     for line in f1:
#         f3.write(line)
#     f3.write("\n")
#     for line1 in f2:
#         f3.write(line1)

#  -----2------

# import os
#
#
# def file_found(ff):
#     cwd = os.getcwd()
#     x_file = os.path.join(cwd, ff)
#     if os.path.exists(x_file):
#         print(os.path.basename(x_file), os.path.dirname(x_file),
#         "- last access time", os.path.getatime(x_file), "sec")
#     else:
#         print("file not found")
#
#
# fl = input("Введите название файла: ")
# file_found(fl)


#  --------homework22-------------

# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         print("Длина прямоугольника:", self.length)
#         print("Ширина прямоугольника:", self.width)
#
#     def s_rectangle(self):
#         s = self.length * self.width
#         print("Площадь прямоугольника:", s)
#
#     def rectangle_perimeter(self):
#         p = 2 * (self.length + self.width)
#         print("Периметр прямоугольника:", p)
#
#     def rectangle_hypotenuse(self):
#         h = (self.length**2 + self.width**2)**0.5
#         print("Гипотенуза прямоугольника:", round(h, 2))
#
#     def print_rectangle(self):
#         for x in range(self.length):
#             for y in range(self.width):
#                 print("*", end='')
#             print()
#
#
# r = Rectangle(3, 9)
# r.s_rectangle()
# r.rectangle_perimeter()
# r.rectangle_hypotenuse()
# r.print_rectangle()

#  --------homework23-----------
# import math
#
#
# class Sphere:
#     r = 0.6
#     x = 0
#     y = 0
#     z = 0
#
#     def __init__(self, x1, y1, z1):
#         self.x1 = x1
#         self.y1 = y1
#         self.z1 = z1
#
#     def set_radius(self, r):
#         self.r = r
#
#     def get_radius(self):
#         return self.r
#
#     def get_volume(self):
#         return (4 / 3) * math.pi * self.r ** 3
#
#     def get_square(self):
#         return 4 * math.pi * self.r**2
#
#     def set_center(self, x1, y1, z1):
#         self.x1 = x1
#         self.y1 = y1
#         self.z1 = z1
#
#     def get_center(self):
#         return self.x1, self.y1, self.z1
#
#     def is_point_inside(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         return (self.x - self.x1)**2 + (self.y - self.y1)**2 + (self.z - self.z1)**2 < self.r**2
#
#
# s1 = Sphere(0, 0, 0)
# print("get_radius = ", s1.get_radius())
# print("get_volume = ", s1.get_volume())
# print("get_square = ", s1.get_square())
# print("get_center = ", s1.get_center())
# print("get_square = ", s1.get_square())
# s1.is_point_inside(0, -1.5, 0)
# print(f"is_point_inside{s1.x, s1.y, s1.z}:", s1.is_point_inside(0, -1.5, 0))
# s1.set_radius(1.6)
# print(f"set_radius({s1.r}) :", s1.get_radius())
# print(f"is_point_inside{s1.x, s1.y, s1.z}:", s1.is_point_inside(0, -1.5, 0))

#  --------homework23-----------
# ----------1-----------

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, n):
#         self.__num = n
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, s):
#         self.__surname = s
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, p):
#         self.__percent = p
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, v):
#         self.__value = v
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")
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
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print(f"Проценты были успешно начислены:")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account(num='12345', surname="Долгих", percent=0.03, value=1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.surname = "Дюма"
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

# -------2---------

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def set_num(self, n):
#         self.__num = n
#
#     def get_num(self):
#         return self.__num
#
#     def set_surname(self, s):
#         self.__surname = s
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_percent(self, p):
#         self.__percent = p
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_value(self, v):
#         self.__value = v
#
#     def get_value(self):
#         return self.__value
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")
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
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print(f"Проценты были успешно начислены:")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account(num='12345', surname="Долгих", percent=0.03, value=1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.set_surname("Дюма")
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

#  --------homework24-----------
# import math
#
#
# class Pair:
#     def __init__(self, a, b):
#         self._a = a
#         self._b = b
#
#     @property
#     def a(self):
#         return self._a
#
#     @a.setter
#     def a(self, num_a):
#         self._a = num_a
#
#     @property
#     def b(self):
#         return self._b
#
#     @b.setter
#     def b(self, num_b):
#         self._b = num_b
#
#     def prod_num(self):
#         print("Произведение:", self._a * self._b)
#
#     def sum_num(self):
#         print("Сумма:", self._a + self._b)
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b, c=0):
#         super().__init__(a, b)
#         self.c = c
#
#     def hypotenuse(self):
#         self.c = round(math.sqrt(self.a**2 + self.b**2), 2)
#         print("Гипотенуза ABC:", self.c)
#
#     def square(self):
#         print("Площадь ABC:", self.a * self.b / 2)
#
#     def info(self):
#         return self.a, self.b, self.c
#
#
# rec = RightTriangle(5, 8)
# rec.hypotenuse()
# print("Прямоугольный треуголник ABC ", rec.info())
# rec.square()
# print()
# rec.sum_num()
# rec.prod_num()
# print()
# rec.a = 7
# rec.b = 8
# rec.hypotenuse()
# rec.a = 17
# rec.b = 13
# rec.hypotenuse()
# rec.sum_num()
# rec.prod_num()
# rec.square()

#  --------homework25-----------

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

#  --------homework26-----------

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec % other.sec)
#
#
# c1 = Clock(600)
# c2 = Clock(200)
# c3 = c1 - c2
# print("c1:", c1.get_format_time())
# print("c1 - c2:", c3.get_format_time())
# c3 = c1 * c2
# print("c1 * c2:", c3.get_format_time())
# c3 = c1 // c2
# print("c1 // c2:", c3.get_format_time())
# c3 = c1 % c2
# print("c1 % c2:", c3.get_format_time())
# c1 -= c2
# print("c1 -= c2:", c1.get_format_time())
# c1 *= c2
# print("c1 *= c2:", c1.get_format_time())
# c1 //= c2
# print("c1 //= c2:", c1.get_format_time())
# c1 %= c2
# print("c1 %= c2:", c1.get_format_time())

#  --------homework27-----------

# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     def __add__(self, other):
#         return self.x + other.x, self.y + other.y, self.z + other.z
#
#     def __sub__(self, other):
#         return self.x - other.x, self.y - other.y, self.z - other.z
#
#     def __mul__(self, other):
#         return self.x * other.x, self.y * other.y, self.z * other.z
#
#     def __truediv__(self, other):
#         return self.x / other.x, self.y / other.y, self.z / other.z
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y and self.z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "x":
#             return self.x
#         elif item == "y":
#             return self.y
#         elif item == "z":
#             return self.z
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int or float):
#             raise ValueError("Значение должно быть числом")
#
#         if key == "x":
#             self.x = value
#
#         if key == "y":
#             self.y = value
#
#         if key == "z":
#             self.z = value
#
#
# p1 = Point3D(12, 15, 18)
# p2 = Point3D(6, 3, 9)
# print("Координаты 1-й точки:", p1)
# print("Координаты 2-й точки:", p2)
# p3 = p1 + p2
# print("Сложение координат:", p3)
# p3 = p1 - p2
# print("Вычитание координат:", p3)
# p3 = p1 * p2
# print("Умножение:", p3)
# p3 = p1 / p2
# print("Деление:", p3)
# if p1 == p2:
#     print("Равенство координат: True")
# else:
#     print("Равенство координат: False")
# print("x =", p1["x"], "x1 =", p2["x"])
# print("y =", p1["y"], "y1 =", p2["y"])
# print("z =", p1["z"], "z1 =", p2["z"])
# p1["x"] = 20
# print("Запись значения в координату x:", p1["x"])


# --------homework28-----------
# from abc import ABC, abstractmethod
# from math import sqrt
#
#
# class Shape(ABC):
#     def __init__(self, col):
#         self.col = col
#
#     @abstractmethod
#     def __call__(self):
#         ...
#
#     @abstractmethod
#     def area(self):
#         print("Площадь: ", end="")
#
#     @abstractmethod
#     def perimetr(self):
#         print("Периметр: ", end="")
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, s, col):
#         self.s = s
#         super().__init__(col)
#
#     def __call__(self):
#         print(f"===Квадрат===\nСторона: {self.s}\nЦвет: {self.col}")
#
#     def area(self):
#         super().area()
#         print(self.s ** 2)
#
#     def perimetr(self):
#         super().perimetr()
#         print(4 * self.s)
#
#     def draw(self):
#         for i in range(self.s):
#             print('*' * self.s)
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, col):
#         self.length = length
#         self.width = width
#         super().__init__(col)
#
#     def __call__(self):
#         print(f"===Прямоугольник===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.col}")
#
#     def area(self):
#         super().area()
#         print(self.length * self.width)
#
#     def perimetr(self):
#         super().perimetr()
#         print((self.length + self.width)*2)
#
#     def draw(self):
#         for i in range(self.length):
#             print('*' * self.width)
#
#
# class Triangle(Shape):
#     def __init__(self, s1, s2, s3, col):
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#         super().__init__(col)
#
#     def __call__(self):
#         print(f"===Треугольник==\nСторона 1: {self.s1}\nСторона 2: {self.s2}\nСторона 3: {self.s3}\nЦвет: {self.col}")
#
#     def area(self):
#         super().area()
#         print(round((self.s1 / 4) * (sqrt(4 * self.s2 ** 2 - self.s1 ** 2)), 2))
#
#     def perimetr(self):
#         super().perimetr()
#         print(self.s1 + self.s2 + self.s3)
#
#     def draw(self):
#         for i in range(self.s2):
#             print(' ' * (self.s2 - 1 - i) + '*' * (1 + i * 2))
#
#
# p1 = Square(3, "red")
# p2 = Rectangle(3, 7, "green")
# p3 = Triangle(11, 6, 6, "yellow")
# px = [p1, p2, p3]
#
# for x in px:
#     x()
#     x.area()
#     x.perimetr()
#     x.draw()
#     print()
#     print()
#
# # def draw(self):
# #     rows = []
# #     for n in range(self.side_y):
# #         rows.append(" " * n "*" * (self.side_x - 2 * n))
# #     print("\n".join(reversed(rows)))

# --------homework29-----------

# class Integer:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int) or value <= 0:
#             raise ValueError(f"Координата {value} должна быть целым, положительным числом")
#         instance.__dict__[self.name] = value
#
#
# class Triangle:
#     s1 = Integer()
#     s2 = Integer()
#     s3 = Integer()
#
#     def __init__(self, s1, s2, s3):
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#
#     def triangle_test(self):
#         if self.s1 + self.s2 > self.s3 and self.s1 + self.s3 > self.s2 and self.s2 + self.s3 > self.s1:
#             return f"Треугольник со сторонами {self.s1, self.s2, self.s3} существует."
#         else:
#             return f"Треугольник со сторонами {self.s1, self.s2, self.s3} не существует."
#
#
# p = Triangle(2, 5, 6)
# print(p.triangle_test())
# p = Triangle(5, 2, 8)
# print(p.triangle_test())
# p = Triangle(7, 3, 6)
# print(p.triangle_test())

# --------homework30-----------

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def gen_key():
#     key = ''
#     nums = ['1', '2', 'n', '4', 'a', 't', '6']
#
#     while len(key) != 8:
#         key += choice(nums)
#     return key
#
#
# def write_json(person_dict, key_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = dict()
#
#     data[key_dict] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person(), gen_key())


# --------homework31-----------

# import json
#
#
# class Place:
#     data = dict()
#
#     def __call__(self):
#         print('*' * 30, "\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                         "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы")
#
#     @staticmethod
#     def write_json(country_dict, city_dict):
#         data = json.load(open('country.json'))
#         data[country_dict] = city_dict
#         with open('country.json', 'w') as f:
#             json.dump(data, f, indent=2)
#         print("Файл сохранен")
#
#     @staticmethod
#     def delete_json(country_dict):
#         data = json.load(open('country.json'))
#         del data[country_dict]
#         with open('country.json', 'w') as f:
#             json.dump(data, f, indent=2)
#         print("Файл успешно отредактирован и сохранен")
#
#     @staticmethod
#     def search_json(country_dict):
#         data = json.load(open('country.json'))
#         if country_dict in data:
#             print(f"Страна: {country_dict}, со столицей: {data[country_dict]} хранится в нашей базе")
#         else:
#             print("Такая страна отсутствует в нашей базе")
#
#     @staticmethod
#     def redaction_json(country_dict, city_dict):
#         data = json.load(open('country.json'))
#         data[country_dict] = city_dict
#         with open('country.json', 'w') as f:
#             json.dump(data, f, indent=2)
#         print("Файл успешно отредактирован и сохранен")
#
#     @staticmethod
#     def info():
#         with open('country.json', 'r') as f:
#             data = json.load(f)
#             print(data)
#
#     def action(self, number):
#         while number != 6:
#             if number == 1:
#                 country1 = input("Введите название страны (с заглавной буквы): ")
#                 city1 = input("Введите название столицы (с заглавной буквы): ")
#                 self.write_json(country1, city1)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 2:
#                 country2 = input("Введите страну, которую хотите удалить (с заглавной буквы): ")
#                 self.delete_json(country2)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 3:
#                 country3 = input("Введите страну, которую хотите найти (с заглавной буквы): ")
#                 self.search_json(country3)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 4:
#                 country4 = input("Введите страну, которую хотите отредактировать (с заглавной буквы): ")
#                 city4 = input("Введите новое название столицы: ")
#                 self.redaction_json(country4, city4)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 5:
#                 self.info()
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             break
#
#
# s = Place()
# s()
# num = int(input("Ввод: "))
# s.action(num)
# print("Работа завершена")
# print(30 * '*')

# --------homework32-----------

# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# url = 'https://www.afisha.ru/tula/cinema/cinema_list/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# sp1 = []
# sp2 = []
# sp3 = []
# data = ["Кинотеатр", "Адрес", "Рейтинг"]
# cinema = soup.find_all('h2', class_="mQ7Bh")
# for plugin in cinema:
#     name = plugin.text
#     sp1.append(name)
#
# adress = soup.find_all('span', class_="MVlCc")
# for plugin in adress:
#     name = plugin.text
#     sp2.append(name)
#
# raiting = soup.find_all('span', class_="nk8aV naF5F j3T41 Gfeb7 eqBUk aOiwv KXiGd")
# for plugin in raiting:
#     name = plugin.text
#     sp3.append(name)
#
# with open('film.csv', 'a') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(data)
#     for i in range(len(sp1)):
#         if i < len(sp3):
#             writer.writerow([sp1[i], sp2[i], sp3[i]])
#         else:
#             writer.writerow([sp1[i], sp2[i], 'рейтинг отсутствует'])

# --------homework33-----------

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# class Parser:
#     html = ""
#     res = dict()
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     @staticmethod
#     def refined(price):
#         return re.sub(r"\D+", "", price)
#
#     def parsing(self):
#         block = self.html.find_all('article')
#         for item in block:
#             name = item.find('div', class_='product-title__head').text.strip()
#             try:
#                 author = item.find('div', class_="product-title__author").text.strip()
#             except AttributeError:
#                 author = ''
#             try:
#                 price = item.find('div', class_="product-price__value product-price__value--discount").text.strip()
#             except AttributeError:
#                 try:
#                     price = item.find('div', class_="product-price__value").text.strip()
#                 except AttributeError:
#                     price = ''
#             int_price = self.refined(price)
#
#             self.res = {
#                 'name': name,
#                 'author': author,
#                 'price': int_price
#             }
#             self.save(self.res)
#
#     @staticmethod
#     def save(lst):
#         with open('books.csv', 'a') as f:
#             writer = csv.writer(f, delimiter=';', lineterminator='\r')
#             writer.writerow((lst['name'], lst['author'], lst['price']))
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#
#
# def main():
#     for i in range(1, 7):
#         if i == 1:
#             pars = Parser('https://www.chitai-gorod.ru/collections/strana-koshmarov-detskie-uzhastiki-4878721')
#         else:
#             pars = Parser(f'https://www.chitai-gorod.ru/collections/strana-koshmarov-detskie-uzhastiki-4878721?page={i}')
#         pars.run()
#
#
# if __name__ == '__main__':
#     main()

# -------------homework61----------
# ------------1------------
# from jinja2 import Template
#
# lst = [
#     {'href': '/index', 'text': 'Главная'},
#     {'href': '/news', 'text': 'Новости'},
#     {'href': '/about', 'text': 'О компании'},
#     {'href': '/shop', 'text': 'Магазин'},
#     {'href': '/contacts', 'text': 'Контакты'},
# ]
#
# link = """<ul>
# {% for l in lst -%}
# {% if l.text == 'Главная' -%}
#     <li><a href="{{ l['href'] }}" class="active">{{ l['text'] }}</a></li>
# {% else -%}
#     <li><a href="{{ l['href'] }}">{{ l['text'] }}</a></li>
# {% endif -%}
# {% endfor -%}
# </ul>
# """
#
# tm = Template(link)
# msg = tm.render(lst=lst)
#
# print(msg)

# ------------2------------

# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from faker import Faker
# from sqlalchemy import and_, or_, not_, desc, func, distinct, text
# import os
# #
# engine = create_engine(f"sqlite:///hospital.db")
# Session = sessionmaker(bind=engine)
# Base = declarative_base()
# session = Session()
#
# # Создаем таблицу в базе данных
#
#
# class Hospital(Base):
#     __tablename__ = 'hospital'
#
#     id = Column(Integer, primary_key=True)
#     country = Column(String(250), nullable=False)
#     town = Column(String(250), nullable=False)
#     name = Column(String(250), nullable=False)
#     number = Column(String(250), nullable=False)
#     number_hospital = Column(Integer)
#
#     def __init__(self, country, town, name, number, number_hospital):
#         self.country = country
#         self.town = town
#         self.name = name
#         self.number = number
#         self.number_hospital = number_hospital
#
#     def __repr__(self):
#         return f"Больница (Страна: {self.country}, Город: {self.town}, Название: {self.name}, " \
#                f"Номер телефона: {self.number}, Номер больницы: {self.number_hospital})"
#
#
# Base.metadata.create_all(engine)
# faker = Faker('ru_RU')
# session.commit()
#
# # Заполняем таблицу
#
# group_list = ['Областная больница', 'Больница имени Лазарева', 'Больница имени Бушева', 'Детская больница']
#
# for _ in range(10):
#     country = faker.country()
#     town = faker.city()
#     name = faker.random.choice(group_list)
#     number = faker.phone_number()
#     number_hospital = faker.random.randint(1, 25)
#     hospital = Hospital(country, town, name, number, number_hospital)
#     session.add(hospital)
#
# session.commit()
# session.close()

# # 1.Ввывести всю таблицу в консоль
#
# for it in session.query(Hospital):
#     print(it)
# print('*' * 50)
#
# # 2.Ввывести все страны, где находятся таблицы
#
# for it in session.query(Hospital):
#     print(it.country)
# print('*' * 50)
#
# # 3.Ввывести всю информацию о больницах, где номер больницы больше 10
#
# for it in session.query(Hospital).filter(Hospital.number_hospital > 10):
#     print(it)
# print('*' * 50)
#
# # 4.Ввывести всю информацию о больницах, которые находятся в России
#
# for it in session.query(Hospital).filter(Hospital.country == "Россия"):
#     print(it)
# print('*' * 50)
#
# # 5.Ввывести всю информацию о больницах, имена стран которых начинаются на С
#
# for it in session.query(Hospital).filter(Hospital.country.like('С%')):
#     print(it)
# print('*' * 50)
#
# # 6.Ввывести всю информацию о детских больницах, которые находятся в России или Греции
#
# for it in session.query(Hospital).filter(and_(Hospital.country.in_(['Россия', 'Греция']),
#                                               Hospital.name == "Детская больница")):
#     print(it)
# print('*' * 50)
#
# # 7.Ввывести всю информацию о больницах, где номер больницы от 5 до 7 включительно
#
# for it in session.query(Hospital).filter(Hospital.number_hospital.between(5,7)):
#     print(it)
# print('*' * 50)
#
# # 8.Ввывести все страны и города, где находятся больницы с сортировкой по стране
#
# for it in session.query(Hospital.country, Hospital.town).order_by(Hospital.country):
#     print(it)
# print('*' * 50)
#
# # 9.Ввывести все телефоны тех больниц, которые начинаются с 8
#
# for it in session.query(Hospital.name, Hospital.number).filter(Hospital.number.like("8%")):
#     print(it)
# print('*' * 50)
#
# # 10.Ввывести сколько всего областных больниц
#
# print(session.query(Hospital).filter(Hospital.name == "Областная больница").count())
# print('*' * 50)


