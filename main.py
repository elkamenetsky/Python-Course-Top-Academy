# ЗАНЯТИЕ 1

name = 'Elisei'
print('Hello,', name)

# Список ключевых слов
# Переменные так называть нельзя
# Запуск через консоль
# import keyword
# keyword.kwlist

age = 26
print(age)

# Эксперимент: ячейка не зависит от переменной, но зависит от содержимого?

# a = 4
# b = 3
# print(id(a))
# print(id(b))
# b = a
# print(id(a))
# print(id(b))
# c = 3
# print(id(c))

# Множественное присваивание
# a = b = c = 10
# print(a, b, c)

# a, b, c = 10, 20, 30
# print(a, b, c)

# Питон не поддерживает константы. Есть соглашение
# между программистами: если имя переменной записано
# в верхнем регистре, то ее значение нельзя изменять
# (типа, предполагаемая константа)
# PI = 3.14
# print(PI)

# Взаимозамена переменных
# a, b = b, a
# Универсальный способ
# a = a + b
# b = a - b
# a = a - b


# ЗАНЯТИЕ 2

print('Сумма:', 5 + 7 + 3)
print('Произведение:', 5 * 7 * 3)
print('Среднее арифметическое:', (5 + 7 + 3) / 3)

num = 1234
a = num % 10
b = (num // 10) % 10
c = (num // 100) % 10
d = (num // 1000) % 10
print(int(str(a) + str(b) + str(c) + str(d)))

# num_1 = '2.5'
# num_2 = 3
# print(int(num_1) + num_2)  # так будет ошибка. Он не сможет перевести '2.5' в int

print(round(3.8))  # математическое округление
print(round(3.845, 2))  # математическое округление до 2 цифр после запятой

# Именованные параметры
print(a, b, c, d, sep='--')  # sep - разделитель
print('Hello, my name is', name + '. I am', age, 'years old.', end=' ')  # end - конец строки
print('I am learning Python')

# user_name = input('Enter your name: ')
# print(user_name)

# number, degree = int(input('Введите число: ')), int(input('Введите степень: '))
# print('Число', number, 'в степени', degree, 'равно', number ** degree)

#  Функции явного преобразования
# str()
# int()
# float()
# bool()

# Логические операторы
# or - ИЛИ
# and - И
# not - НЕ

# Если ...
# number = 15
# if number < 10:
#     number += 1
#     print(number)
# else:
#     print(number)

# Задача про треугольники
# a, b, c = int(input('Введите первую сторону: ')), \
#     int(input('Введите вторую сторону: ')), \
#     int(input('Введите третью сторону: '))
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# Задача про месяцы
# month = int(input('Введите номер месяца: '))
# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май',
#           'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
#           'Ноябрь', 'Декабрь']
# if month <= 0 or month > 12:
#     print('Введен некорректный номер')
# else:
#     print(months[month - 1])

# Конструкция match - case
password = 'moderator'
match password:
    case 'admin':
        print('Welcome, admin')
    case 'user':
        print('Welcome, user')
    case 'moderator':
        print('Welcome, moderator')
    case _:
        print('Incorrect password')

# Перечисление значений и условий в case
# day = 'Friday'
# time = 10
# match day:
#     case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' if 9 <= time >= 17:
#         print('The day for working')
#     case 'Suturday' | 'Sunday':
#         print('Weekend')
#     case _:
#         print('Incorrect day or not-working time')

# Тернарное выражение
a, b = 30, 20
minimum = a if a < b else b
print(minimum)
# Вложенное тернарное выражение
print('a = b' if a == b else 'a > b' if a > b else 'b > a')

# a, b = 2, 0
# print(a / b if b != 0 else 'На ноль делить нельзя!')

# Обработка исключений 'try-except'
# try:
#     n = int(input('Enter a number: '))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')

# try: # попытаться сделать что-то
#     n = int(input('Enter a divisible: '))
#     m = int(input('Enter a divider: '))
#     print(n / m)
# except ValueError: # исключение 1
#     print('Некорректные значения')
# except ZeroDivisionError: # исключение 1
#     print('Нельзя делить на ноль')
# else: # когда в блоке try не возникло исключение
#     print('Все нормально. Вы ввели числа', n, 'и', m)
# finally: # фрагмент, который выполняется в любом случае
#     print('The end of program')

# Циклы

# while
# i = 1
# while i <= 20:
#     if i % 2 != 0:
#         i += 1
#     else:
#         print('i =', i, end='; ')
#         i += 1

# Сумма всех целых нечетных чисел в диапазоне от a до b
# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# i = a
# court = 0
# while i <= b:
#     if i % 2 != 1:
#         i += 1
#     court += i
#     i += 1
# print(court)

# Цикл while с исключением
# n = input('Введите целое число: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# Использование break и continue
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# Установление условия для выхода из бесконечного цикла
# while True:
#     n = int(input('Введите положительное целое число: '))
#     if n < 0:
#         break

