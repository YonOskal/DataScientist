# from random import randint

# Задача №1. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# inp = "a a a b c a a d c d d".split()
# print(inp)

# sl = {}  # Инициализация пустого словаря
# result = []  # Список для результата

# for char in inp:
#     if char in sl:  # Если символ уже в словаре
#         sl[char] += 1  # Увеличиваем количество встреч
#         result.append(f"{char}_{sl[char]}")  # Добавляем символ с постфиксом
#     else:
#         sl[char] = 0  # Добавляем новый символ в словарь с начальным значением 0
#         result.append(char)  # Первый раз добавляем символ без постфикса

# print(" ".join(result))


# Задача №2. Решение в группах
# Пользователь вводит текст(строка). Словом
# считается последовательность непробельных
# символов идущих подряд, слова разделены одним
# или большим числом пробелов. Определите, сколько
# различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
# 15 минут
# Семинар 4. Словари

# input = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# res = set(input.lower().replace("."," ").split())
# print(res)
# print(len(res))


# Задача Генерация необязательная

# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8

# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

# k = 4
# res = []


# for i in range(k + 1):
#     kof = randint(-10, 10)
#     if kof == 0:
#         continue
#     elif kof == 1:
#         res.append(f"x^{k - i}")
#         continue
#     if i == 0 and kof > 0:
#         res.append(f"{kof}*x^{k - i}")
#         continue
#     if i == k:
#         if kof > 0:
#             res.append(f"+ {kof}")
#         else:
#             res.append(f"{kof}")
#         continue
#     if i == k - 1:
#         if kof > 0:
#             res.append(f"+ {kof}")
#         else:
#             res.append(f"{kof}*x")
#         continue    
#     elif kof > 0:
#         res.append(f"+ {kof}*x^{k - i}")
#     else:
#         res.append(f"{kof}*x^{k - i}")
# print(*res, "= 0")

