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
