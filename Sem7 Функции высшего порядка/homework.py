from functools import reduce
from collections import Counter
# Задание 1. Новые списки
# Даны три списка:
# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.

# floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers = [2, 3, 10, 4, 1, 2, 1]

# # print(map(round(floats, 3)lamda x: x ** 3, floats))
# print(list(map(lambda x: round(x ** 3,2), floats)))
# print(list(filter(lambda x: len(x) >= 5, names)))
# print(reduce(lambda x, y: x * y, numbers))

# Задача 2. Zip
# Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N
# элементов. Создайте кортежи из пар элементов списков и запишите их в список
# results. Не используйте функцию zip. Решите задачу в одну строку (не считая
# print(results)).
# Примеры списков:
# letters: List[str] = ['a', 'b', 'c', 'd', 'e']
# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
# Результат работы программы:
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# letters = ['a', 'b', 'c', 'd', 'e']
# numbers = [13, 26, 3, 412, 52, 77, 78, 38]
# # results = [(letters[i], numbers[i]) for i in range(min(len(letters), len(numbers)))]
# results = [(l, numbers[i]) for i, l in enumerate(letters)]

# print(results)
"""
Функция enumerate() принимает два параметра: iterable и start.

iterable — это итерируемый объект (список, кортеж и т.д.), который будет возвращен в виде пронумерованного объекта (объекта enumerate)
start — это начальный индекс для возвращаемого объекта enumerate. 
Значение по умолчанию равно 0, поэтому, если вы опустите этот параметр, в качестве первого индекса будет использоваться 0.
Конструкция [(l, numbers[i]) for i, l in enumerate(letters)] — это списковое включение (list comprehension), 
которое используется для создания нового списка на основе существующих списков.

Вот детальное объяснение каждого элемента:

enumerate(letters):

Функция enumerate позволяет проходить по списку letters, возвращая индекс и элемент одновременно.
Например, если letters = ['a', 'b', 'c'], то enumerate(letters) создаст пары: (0, 'a'), (1, 'b'), (2, 'c').
i — это индекс (позиция элемента в списке letters).
l — это сам элемент списка letters.
Цикл for: for i, l in enumerate(letters):

Мы итерируем по списку letters, получая одновременно индекс i и сам элемент l.
Например, для первой итерации i = 0, l = 'a', для второй — i = 1, l = 'b' и т.д.
Тело списка: (l, numbers[i]):

На каждой итерации создается кортеж (l, numbers[i]).
l — это элемент из списка letters, а numbers[i] — это соответствующий элемент из списка numbers на той же позиции.
Например, на первой итерации будет кортеж ('a', 1), на второй — ('b', 2).
Результат:

По окончании всех итераций создается список кортежей. Каждый кортеж состоит из элемента из списка letters и соответствующего по индексу элемента из списка numbers.
Например, если letters = ['a', 'b', 'c'] и numbers = [1, 2, 3], то результатом будет: [('a', 1), ('b', 2), ('c', 3)].
Это решение автоматически завершает процесс, как только индекс достигает конца списка letters.
"""

# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False


# def can_be_poly(str):
#     count_nechet = 0 
#     count_str = Counter(str)
#     for keys, value in count_str.items():
#         if value % 2 == 1:
#             count_nechet += 1
#     if count_nechet == 1:
#         print("Можно сделать палиндромом")
#     else:
#         print("Нельзя сделать палиндромом")   
#     # # Проверяем количество символов с нечетным количеством вхождений
#     # odd_count = len(list(filter(lambda x: x % 2,
#     # char_counts.values())))
#     # # Условие для проверки возможности формирования палиндрома
#     # return odd_count < 2
        
# can_be_poly("abcbda")

"""
Модуль Collections
Collections — это встроенный модуль Python, реализующий специализированный контейнер типов данных. 
Является альтернативой встроенным контейнерам общего назначения Python, таким как dict, list, set и tuple.

Рассмотрим несколько структур данных, представленных в этом модуле:

1. namedtuple()
Доступ к данным, хранящимся в обычном кортеже, можно получить с помощью индексов. Пример:

plain_tuple = (10,11,12,13)
plain_tuple[0]
10
plain_tuple[3]
13
Не обязательно давать названия отдельным элементам, хранящимся в кортеже. 
В этом есть необходимость лишь в том случае, если кортеж обладает множеством полей.

Именно здесь функциональность namedtuple проявляет свои силы. 
Это функция для кортежей с именованными полями (Named Fields), которую можно рассматривать как расширение встроенного типа данных tuple. 
Именованные кортежи задают значение для каждой позиции в кортеже, делая код более читаемым и самодокументируемым. 
Доступ к объектам, хранящимся в кортеже, можно получить с помощью уникального (удобного для чтения) идентификатора. 
Это избавляет от необходимости запоминать целочисленные индексы. Рассмотрим его реализацию.

from collections import namedtuple
fruit = namedtuple('fruit','number variety color')
guava = fruit(number=2,variety='HoneyCrisp',color='green')
apple = fruit(number=5,variety='Granny Smith',color='red')
Построение namedtuple начинается с передачи названия объекта type (fruit). 
Затем передается строка с пробелами между названиям каждого поля. Теперь можно обращаться к различным параметрам:

guava.color
'green'
apple.variety
'Granny Smith'
Namedtuples — эффективная для памяти опция при определении неизменяемых полей в Python.

2. Counter
Counter — это подкласс dict, который используется для подсчета объектов hashable. 
Элементы хранятся в качестве ключей словаря, а количество объектов сохранено в качестве значения. Рассмотрим несколько примеров с Counter.

#Importing Counter from collections
from collections import Counter
Со строками
c = Counter('abcacdabcacd')
print(c)
Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})
Со списками
lst = [5,6,7,1,3,9,9,1,2,5,5,7,7]
c = Counter(lst)
print(c)
Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})
С предложением
s = 'the lazy dog jumped over another lazy dog'
words = s.split()
Counter(words)
Counter({'another': 1, 'dog': 2, 'jumped': 1, 'lazy': 2, 'over': 1, 'the': 1})
Помимо доступных для всех словарей методов, объекты Counter поддерживают еще три дополнительных:

elements()
Возвращает количество каждого элемента. В случае, если количество элемента меньше одного, метод не выполняется.

c = Counter(a=3, b=2, c=1, d=-2)
sorted(c.elements())
['a', 'a', 'a', 'b', 'b', 'c']
most_common([n])
Возвращает список наиболее повторяемых элементов и количество каждого из них. Количество элементов указывается в значении n. 
Если ни одно из значений не указано, возвращается количество всех элементов.

s = 'the lazy dog jumped over another lazy dog'
words = s.split()
Counter(words).most_common(3)
[('lazy', 2), ('dog', 2), ('the', 1)]
Распространенные шаблоны использования объекта Counter()
sum(c.values())                 # total of all counts 
c.clear()                       # reset all counts 
list(c)                         # list unique elements 
set(c)                          # convert to a set 
dict(c)                         # convert to a regular dictionary c.items()                       # convert to a list like (elem, cnt) 
Counter(dict(list_of_pairs))    # convert from a list of(elem, cnt) 
c.most_common()[:-n-1:-1]       # n least common elements 
c += Counter()                  # remove zero and negative counts
"""


# Задача 4. Уникальный шифр
# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5.

# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# str = message.lower()
# res = Counter(str)

# print(res)

# unique_count = list(filter(lambda key: res[key] < 2, res))
# print(unique_count,"количество уникальных символов в строке —", len(unique_count))