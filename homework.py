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

# from random import randint
#
#
# def binary_search(s, item):
#     found = False
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midpoint = (first + last) // 2
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
# n = int(input("Введите число: "))
# if binary_search(a, n):
#     print(f"Число {n} в списке присутствует")
# else:
#     print(f"Число {n} в списке отсутствует")


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

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("Длина прямоугольника:", self.length)
        print("Ширина прямоугольника:", self.width)

    def s_rectangle(self):
        s = self.length * self.width
        print("Площадь прямоугольника:", s)

    def rectangle_perimeter(self):
        p = 2 * (self.length + self.width)
        print("Периметр прямоугольника:", p)

    def rectangle_hypotenuse(self):
        h = (self.length**2 + self.width**2)**0.5
        print("Гипотенуза прямоугольника:", round(h, 2))

    def print_rectangle(self):
        for x in range(self.length):
            for y in range(self.width):
                print("*", end='')
            print()


r = Rectangle(3, 9)
r.s_rectangle()
r.rectangle_perimeter()
r.rectangle_hypotenuse()
r.print_rectangle()
