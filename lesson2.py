import sys
# compare = 3 == 3
# print(compare)

# x = 7
# print(x > 3 and x < 6)
# print(x > 2 or x < 6)
# print (x > 2 and not x < 6)

# умовні оператори
# if x != 5:
#     print('Five')
# else:
#     print('Other result')

# if x == 5:
#     print('Five')
# elif x > 5:
#     print('More than 5')
# else:
#     print('Less than five')

# age = int(input('Please, enter your age: '))
# if age >= 18:
#     print('Welcome!')
# else:
#     print('Go home, baby!')



# try:
#     num1 = int(input('Number 1: '))
#     num2 = int(input('Number 2: '))
#
# except ValueError:
#     print("Це не число")
#     sys.exit()
# 5operator = input('Operator: ')
#
# if num2 == 0 and operator == "/":
#     try:
#      result = num1 / num2
#      print(f'Result = {result}')
#     except ZeroDivisionError:
#         print("На нуль ділити не можна")
# else:
#     result = num1 * num2
#     print(f'Result = {result}')

# ________ Cycle While
# num = 0
# while num < 5:
#     print(num)
#     num += 1

# message = "Hello"
# i = 0
# while i < 6:
#     print(i, message)
#     i += 1

#  -----------------break------------
# message = "Hello"
# i = 0
# while i < 6:
#     if i == 3:
#         break
#     print(i, message)
#     i += 1

# message = "Hello"
# i = 0
# while i < 6:
#     print(i, message)
#     if i == 3:
#         break
#     i += 1

# ----------continue-----------
# безкінечний цикл
# message = "Hello"
# i = 0
# while i < 6:
#     print(i, message)
#     if i == 3:
#         continue
#     i += 1


# message = "Hello"
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)

#  ------------Cycle FOR ------

# for i in range(6):
#     print(i)

#  (start, stop)#
# for i in range(1, 8):
#     print(i)

# (start, stop, step)
# for i in range(1, 8, 2):
#     print(i)

# for i in "Hello":
#     print(i)

# message = "Hello"
# print(message[2])
# print(message[0: 5: 2])

# -------Function

# def num():
#     return 2 * 2
#
# start = num()
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)

# i = 0
# x = 0
# while i < 4:
#     x += i
#     i += 1
#     print(x)
#     print(f"x = {x}, i = {i}")

# message = ''
# if message:
#     print(message)
# else:
#     print('The sting is empty')

# num = 5
# if num%2 != 0 :
#     print('Odd numbers')
# else:
#     print('Even numbers')

# num = 4
# if not num%2:
#     print('Even numbers')
# else:
#     print('Odd numbers')

# def num(num1, num2):
#     return num1 - num2

# print(num(10, 5))
# print(num(9, 2))

# start = num(8, 3)
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)

# ------Method of String
# --------replace

# s = 'hello world'
# print(s.replace('e', 'a'))
# print(s.replace('l', '?', 2))
# print(s.replace(' ', ''))

# ---------count
# s = 'hello world'
# print(s.count('o'))

# ----------split
# w = "denisov denis denisovich"
# w1 = '1, 2, 3, 4, 5'
# print(w.split())
# print(w.split('e'))
# print(w1.split(',', maxsplit=2))

# ---------join
# w = "denisov denis denisovich"
# w1 = '1, 2, 3, 4, 5'
# w2 = w1.split(',')
# print(''.join(w1))
# print(type(''.join(w1)))
# print('?'.join(w1))

# ---------strip
# w3 = '      hello       '
# print(w3)
# print(w3.strip())

# w3 = '    123hello123    '
# print(w3)
# print(w3.strip())
# print(w3.strip().strip('123'))

# ---------------find

# w4 = 'hello world'
# print(w4.find('e'))
# print(w4.find('o', 2, 5))

# -------------index
# w4 = 'hello world'
# print(w4.index('l', 2, 5))
# якщо не буде такого значення, то видасть помилку

# -------upper --------lower
# w5 ='hElLo worLd'
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print(w5.swapcase())

# ---------islower

# w6 = 'qwerty'
# w7 = 'Qwerty'
# w8 = '123456'
# w9 = '123456a'
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())
# print(w9.islower())

# ----------isupper
# w6 = 'QWERTy'
# w7 = 'QWERTY'
# w8 = '123456'
# w9 = '12345A'
# print(w6.isupper())
# print(w7.isupper())
# print(w8.isupper())
# print(w9.isupper())

# ----------isdigit

# w6 = '0123'
# w7 = ''
# w8 = '0,13'
# w9 = '12345A'
# print(w6.isdigit())
# print(w7.isdigit())
# print(w8.isdigit())
# print(w9.isdigit())

# -----isalpha

# w6 = '0123'
# w7 = 'qwERty'
# w8 = '0,13a'
# w9 = '12345A'
# print(w6.isalpha())
# print(w7.isalpha())
# print(w8.isalpha())
# print(w9.isalpha())


# ---------IF ElSE

# a = int(input("Input number: "))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f"{a} is devision on 2 and 10")
#     else:
#         print(f'{a} is devision on 2 but not to 10')
# else:
#     print(f"{a} is  not devision on 2 and 10")

# q = int(input("Введіть вашу оцінку: "))
# if q >= 90:
#     print(5)
# elif q >= 80:
#     print(4)
# elif q >= 70:
#     print(3)
# else:
#     print(2)

# number = int(input('Input your number: '))
# if number < 10:
#     print('Однозначне число')
# elif 10 <= number <= 99:
#     print("Двозначне число ")
# elif 100 <= number <= 999:
#     print("Тризначне число ")
# else:
#     print('Я до стількох не рахую)) ')

# ----------Тернарний оператор

# x, y = 45, 50
# s = x if x > y else y
# print(s)

# value = 3
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print("Other number")

# c = 0
# while c < 5:
#     if c % 2 == 0:
#         print('Parne')
#     else:
#         print('Neparne')
#     c += 1

# text = int(input('Input number: '))
# count = 0
# while text != 'stop':
#     num = int(text)
#     count += num
#     text = input("Для продовження введіть число, якщо хочете закінчити, то введіть stop: ")
# print(f'Sum of numbers equel {count}')


# ----------FOR
# num = 10
# for i in range(1, num+1, 2):
#     print(i)

# string_1 = "hello"
# for i in range(len(string_1)):
#     # print(i)
#     print(string_1[i])

# string_1 = "hello"
# for i in string_1:
#     print(i)

# string_1 = "HellO123"
# for i in range(len(string_1)):
#     if string_1[i].islower():
#         print(i, string_1[i])
#     if string_1[i].isdigit():
#         print(i, string_1[i])