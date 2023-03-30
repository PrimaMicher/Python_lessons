# -------Lists
# Create a list: option 1
import setuptools.command.register

# my_list = [1, "hello", 2.0, True, None]

# sentance = 'Python is awesome!'
# print(sentance.split(' ', maxsplit=1))
#
# print(my_list[1])
# print(my_list[-2])
# print('Before', my_list)
# print(id(my_list))
# my_list[0] = 25
# print('After', my_list)
# print(id(my_list))

# Методи для роботи зі списками
# .append() метод для добавлення елемента в список
# .extand() добавляє список2 в кінець списку1
# .insert() для добавллення елемента в конкретне місце в списку
# .index() для получення індекса елемента
# .clear() для очистки списка
# del list[] можна видаляти елемент з вказаним індексом
# .remove() для видалення елемента списку
# .reverse() щоб розвернути список в зворотню сторону
# .count() порахувати кількість елементів в списку
# sum() для складання елементів списку
# min() показує елемент з найнижчим значенням списку
# max()        з найвищим

# my_list = [1, "hello", 2.0, True, None, 1, 1]
# sentance = 'Python is awesome!'
# # my_list.append(sentance)
# # my_list.insert(3, sentance)
# print(my_list.count(1))
# print(len(my_list))
# # print(my_list.index('hello'))

# my_list1 = [1, 2, 5, 6, 4, [1, 2, 3, 4, 5]]
# print(sum(my_list1))
# print(min(my_list1))
# print(max(my_list1))
# print(my_list1[-1])
# print((my_list1[-1][-1]))

# my_list1 = [1, 2, 5, 6, 4, [1, 2, 3, 4, 5, [1, 2]]]
# # print((my_list1[-1][-1][1]))
# # my_list1.reverse()
# print(my_list1)

# ----For loop with list

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num**2)
# # List comprehension (генерація списків)
# new_l = [i*i for i in numbers if i%2 == 0]
# print(new_l)

# -----TUPLES кортежи (вони є незмінним типом даних)
# Create a tuple: option 1

# my_tupel = 1, 2, 3
# print(my_tupel)
# print(type(my_tupel))

# Create a tuple: option 2
# my_tupel = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tupel)

# якщо після значення стоїть кома, тоді утвориться tupel name = 'Mark', або name = ('Mark',)
# без коми - це строкове значення
# name = 'Mark',
# print(name)

# -----decomposition
# my_tuple = ('apple', 'banana', 'cat')
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# my_tuple[0] = 'pineapple'
# print(my_tuple) that will be Error

# letters = list(my_tuple)
# letters[0] = 'pineapple'
# print(letters)

# Getting index of item
# my_tupel = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tupel.index('name'))
# print(my_tupel.count('name'))

# Filtering
# my_tupel = (1, True, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tupel if isinstance(item, int)])
# print(result)

# при наступному виді фільтрації вийде list
# my_tupel = (1, True, 'name', None, 'name', 'name', 25)
# result = ([item for item in my_tupel if isinstance(item, int)])
# print(result)

# ---Tuple method
# my_tupel = (1, True, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tupel if isinstance(item, int)])
# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Length of my_tuple is: {len(my_tupel)}')
# print(f'Length of result is: {len(result)}')

# Iterate tuple with for loop
# for (index, item) in enumerate(my_tupel):
#     print(index, item)
#
# # Iterate tuple with while loop
# i = 0
# while i < len(my_tupel):
#     print((i, my_tupel[i]))
#     i += 1

# Nested list in tuple якщо в кортежі є вложений лист, то можна вміст цього листа міняти
# fruits = ('apple', ['pineapple', 'mango'], 'melon')
# fruits[1][0] = 'cherry'
# print(fruits)

#  swaping variables
# a = 5
# # b = 10
# # a, b = b, a
# # print(a)
# # print(b)

# Passing tuple as an argument in function
# def sum_it(*args):
#     total = 0
#     print(args)
#     for num in args:
#         total += num
#     return total
# print(sum_it(4, 5, 10, 6, 20))

# def func(*args):
#     l = []
#     print(len(args))
#     for item in args:
#         l.append(item*item)
#     return l
# print(func(2, 5, 6, 8, 10))

# Dictionary

# my_dict = {
#     'name': 'Marianna',
#     'last_name': 'Pristash',
#     'age': 35,
#     'department': 'IT'
#
# }
# # print(type(my_dict))
# # print(my_dict)
# # print(id(my_dict))
# # print(my_dict['name'])
#
# my_dict['last_name'] = 'Prokurat'
# # print(my_dict)
# # print(id(my_dict))
# # print(len(my_dict))
#
# my_dict['salary'] = 7000
# print(my_dict)

# Методи роботи зі Словниками
# .keys() - викор. для виводу ключів
# .values - вивід значень без ключів
# .item() - викор. для створення кортежів з ключами і значеннями
# .get() - метод для отримання значення ключа
# .clear() - очистити словник
# .copy() - скопіювати весь словник
# .pop() - видаляє значення зі словника
# zip() - об'єднати ключ-значення
# len() - довжина словника
# type() - тип
# min() - ключ з мін
# max() - ключ з мах

# print((my_dict.keys()))
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('salary', "Not found"))

# Another way to create the dictionary
# keys = ['name', 'salary', 'department']
# values = ['Alex', '5000', 'HR']
# employee = dict(zip(keys, values))
# print(employee)

# One more way

# employee1 = dict(name='John', position='developer', salary=5000, department='IT', city='NY')
# print(employee1)

#  SETS (Множинність)
# SETS схоже на словник, в якому значення відкинуть, а залишаються лише
# як і в словнику, ключі мають бути унікальні
# SETS зручно використовувати для видалення повторювальних елементів в листі

# my_list = [1, 8, 2, 1, 1, 5, 5, 8, 9, 9]
# print((set(my_list)))

# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}

# Method
# .issubset визначити чи явсяється set1 підсетом іншого set2, повне співпадіння
# .issuperset set2 включає в себе set1, повне співпадіння
# .intersection() провіряються співпадіння
# .difference() чим відміняються два сети, але лише що відмінного в першому від другого
# .symmetric_difference() усі відмінності що є як в першому так і в другому сетах
# .remove() видалення одного ключа
# add() добавлення
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))
# print(set1)
# print(id(set1))
# print(set1.remove(1))
# print(set1)
# print(id(set1))
# print(set1.add(8))
# print(set1)
# print(id(set1))

# frozenset щоб множинність не змінювалась

# fs = frozenset({1, 2, 3})
# # fs.remove(1)
# # print(fs)
#
# fs.add(5)
# print(fs)

# lst = [1, 2, 3]
# print(lst)
# print(type(lst))

# the second option to create list
# lst = []
# print(lst)

#  the 3d option to create list
# lst = []
# lst1 =list(range(3))
# print(lst1)
# print(type(lst1))

# lst = [1, 2, 'red', False, [1, 2, 5]]
# lst1 = [6, 7]
# print(lst+lst1)
# print(2 in lst)
# if 10 in lst:
#     print('Yes')
# else:
#     print('No')

# print(lst[3])

# lst = [1, 4, 3, 5, 19, 10]
# lst1 = ['Anna', 'Dima']

# print(sum(lst))
# print(min(lst))
# print(max(lst))
# lst.append(45)
# lst.extend(lst1)
# print(lst)

# lst = [1, 4, 3, 5, 19, 10]
# lst1 = ['Anna', 'Dima']

# del lst[0]
# lst.remove(19)
# lst.clear()
# print(lst)

# lst = [1, 4, 3, 5, 19, 10]
# lst1 = ['Anna', 'Dima']
# a = lst.pop(3)
# print(a)
# print(lst)

# lst.reverse()
# print(lst)

# lst2 = lst.copy()
# print(lst)
# print(id(lst))
# print(lst2)
# print(id(lst2))

# lst = [1, 2, 3]
# lst1 = lst
# print(id(lst))
# print(id(lst1))
# lst += [100]
# print(lst)
# print(lst1)

#  (*list) розпаковує список
# lst = [1, 2, 3, 4]
# print(*lst)

# lst = [1, 2, 3, 4]
# for i in lst:
#     print(i, end=' ')
# print('---'*5)
# print(*lst)

# Генерація листа [вираз for i in range()]
# number = [i for i in range(5)]
# print(number)

# number = [i for i in range(10) if i % 2 != 0]
# print(number)

# ==============TUPLE===================

# number1 = [1, 2, 3, 4]
# number2 = (1, 2, 3, 4)
# number1[1] = 10
# # number2[1] = 10
# print(number1)
# print(number2)

# number = (1, 2, 3, 4)
# num = (1,)
# print(type(number))
# print(type(num))

# lst = [1, 2, 3, 4, 5, 6]
# tpl = (1, 2, 3, 4, 5, 6)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3)
# b = list(a)
# b[1] = 15
# c = tuple(b)
# print(a)
# print(b)
# print(c)
# print(id(a))
# print(id(b))
# print(id(c))
# print(type(a))
# print(type(b))
# print(type(c))

# number = (2, 6, 9, 1, 8 )
# number1 = sorted(number)
# number2 = tuple(number1)
# print(number)
# print(number1)
# print(number2)

# =============SETS===============
# так як множинність - це не впорядкований список, визначити індекс ми не можем
# sum дає суму всіх неповторювальних чисел
# number = {1, 1, 3, 4, 5, 5}

# number1 = set()
# print(number1)
# print(type(number1))
# print(number)
# print(type(number))
# print(sum(number))
# print(len(number))
# print(min(number))
# print(max(number))
# for i in number:
#     print(i)

# number = {1, 1, 3, 4, 5, 5}
# number1 = {1, 3, 4, 5}
# number2 = {1, 2, 3, 4, 5}
# print(number == number1)
# print(number == number2)
# sorted_number = sorted(number)
# print(sorted_number)

# підмножинність

# number = {1, 1, 3, 4, 5, 5}
# number1 = {1, 3, 4}
# number2 = {1, 2, 3, 4, 5}
# print(number1 in number)

# number1 = {1, 2, 3}
# number2 = number1.copy()
# print(number1)
# print(number2)

# якщо елементе не буде в сеті, то дасть помилку
# number1 = {1, 2, 3}
# number1.remove(6)
# print(number1)

# discard не дасть помилки про видалення, якщо немає елемента, а поверне сет
#  METHOD add added 1 element
# number1 = {1, 2, 3}
# number = {6, 7, 8}
# lst = ['hello', True, 5]
# number1.discard(6)
# number1.add(19)
# number1.update(number, lst)
# print(number1)

# my_set1 = {1, 2, 3, 4}
# my_set2 = {3, 4, 10, 18}
# a = my_set1.union(my_set2)
# b = my_set1.intersection(my_set2)
# c = my_set1.difference(my_set2)
# d = my_set1.symmetric_difference(my_set2)
# print(a)
# print(b)
# print(c)
# print(d)

# my_set1 = {1, 2, 3, 4, 5}
# my_set2 = {10, 30, 40}
# # print(my_set1.issubset(my_set2))
# # print(my_set2.issubset(my_set1))
# # print(my_set2.issuperset(my_set1))
# # print(my_set1.issuperset(my_set2))
# print(my_set1.isdisjoint(my_set2))
# print(my_set2.isdisjoint(my_set1))

# num = {int(i) for i in input()}
# print(num)

# num = {int(i) for i in range(10)}
# print(num)
# number = int(input("Введіть з якої кількості має складатись множинність: "))
# num = {i for i in range(number)}
# print(num)

# ========Dictionary==========

# dct = {
#     ('USA',): '+1',
#     'Ukraine': '+38',
#     'Turkey': '+90'
# }
#
# print(dct)
# print(type(dct))

# dct = {}
# print(dct)
# print(type(dct))

# dct = dict(kyiv=324, lviv=322, stryi=769)
# dct = dict([['kyiv', 324], ['lviv', 322],['srtyi', 769]])
# print(dct)
# print(type(dct))

# dct = {
#     ('USA',): '+1',
#     'Ukraine': '+38',
#     'Turkey': '+90'
# }
# dct1 = {
#     'name': 'Mariana',
#     'age': 18
#
# }
# dct3 = dct | dct1
# print(dct3)
# if 'France' in dct:
#     print("YES")
# else:
#     print("NO")
# print(len(dct))


# dct = {
#     'USA': '+1',
#     'Ukraine': '+38',
#     'Turkey': '+90'
# }
# # розпаковує словник та перетворює в строкове значення
# print(*dct, sep='\n')


# Способи виведення словників
# for key in dct.keys():
#     print(key)

# for key in dct:
#     print(key)

# виводить значення
# for key in dct:
#     print(dct[key])

# for value in dct.values():
#     print(value)

# print(dct.get('USA'))
# print(dct.get('France', 'поки немає такого значення в словнику'))

# for key, value in dct.items():
#     print(key, value)

# добавлення нових значень в словник
# print(dct.setdefault('France', '+75'))
# print(dct.setdefault('USA', '+75'))
# print(dct)

# print(dct.pop('Turkey'))
# print(dct.popitem())
# print(dct)


# dct = {
#     'USA': '+1',
#     'Ukraine': '+38',
#     'Turkey': '+90'
# }
# keys = list(dct.keys())
# print(keys)

# keys = list(dct.values())
# print(keys)

# keys = list(dct.items())
# print(keys)
#
# keys = tuple(dct.keys())
# print(keys)
#
# keys = set(dct.keys())
# print(keys)