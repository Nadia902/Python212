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

s = """
Ежевику для ежат 
Принесли два ежа. 
Ежевику еле-еле 
Ежата возле ели съели
"""
col = 0
for i in s.lower().split():
    if i.startswith("е"):
        col += 1
print(f"Количество слов: {col}")
