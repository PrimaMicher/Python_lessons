# Lesson_2
# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# max_xp = 100
# health = int(input("Put your health point: "))
# if max_xp - health > 0:
#     print('Live')
# else:
#     print('Dead')

# or
# def check_health(point):
#     while point > 0:
#         print('Alive')
#     else:
#         print('Dead')

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

# num = int(input('Input yor number: '))
# if num%2==0:
#     print('Even')
# else:
#     print('Odd')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

# year = int(input("Введіть рік, який вас цікавить "))
# if year%4==0 and year%100 ==0:
#     print("Цей рік високосний, певно був/буде тяжким")
# elif year%400==0:
#     print("Цей рік високосний, певно був/буде тяжким")
# else:
#     print("Все в нормі, рік не високосний")

# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# text = input("Input text: ")
# row = int(input("How many times it shoud repeat: "))
# print((text + '\n') * row)








































# Lesson_3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[2])