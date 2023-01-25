# map() -> HW_5

# lst = [3, 6, 8, 9, 1, 2]
# print(list(map(lambda elem: elem * lst.index(elem) ** 3, lst)))


# ================================
# filter(function, iterable) - перебирает и возвращает значения при условии истинности
# ================================

# t = ('abcd', 'abc', 'abefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))  # возвращает (значения), длина которых = 3
# print(t2)
#
# b = [66, 90, 60, 64, 78, 45, 96, 83, 42, 88, 90]
# res = list(filter(lambda s: s > 75, b))  # вернет [то], что > 75
# print(res)


# Зд: Генерация 10 чисел, вывод тех, кто в [10:20]

# from random import randint
# lst = [randint(1, 50) for i in range(10)]
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)


#  Зд: Из списка выводятся только значения % 15 == 0

# lst = [45, 55, 60, 37, 100, 105, 220]
# lst2 = list(filter(lambda x: x % 15 == 0, lst))
# print(lst2)


# Зд: Квадраты нечетных чисел в [1:10)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# # range: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> filter: 1, 3, 5, 7, 9] -> map: [1, 9, 25, 49, 81]
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]  # то же самое, но по другому
# print(m1)


# ================================
# Декораторы
# ================================

# def hello():
#     return 'Hello, I am function "hello()"'
#
#
# test = hello  # сохраняем функцию (НО(!) не ВЫЗОВ функции) в переменную
# print(test())  # теперь вызываем test как функцию
#
# def hello():
#     return 'Hello, I am function "hello()"'
#
#
# def super_function(function):
#     print('Hello, I am function "super_function()"')
#     print(function())  # здесь добавлены (), что приводит к вызову функции
#
#
# super_function(hello)  # передаем в функцию другую функцию в кач-ве параметра


# Более сложный вид декоратора

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, I am function "func_test()"')
#
#
# test = my_decorator(func_test)
# test()


# Работа самого @декоратора

# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
#
#
# @my_decorator  # это сам декоратор (добавляем доп. функционал - как бы декор)
# def func_test():  # декорируемая функция
#     print('Hello, I am function "func_test()"')
#
#
# func_test()  # теперь простой вызов отработает с декоратором


#  Применение тегов html-разметки через декоратор

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @italic
# @bold
# def hello():  # на выходе будет <i><b>text</b></i> (важна ОЧЕРЕДНОСТЬ!)
#     return 'text'
#
#
# print(hello())


# Зд: Подсчет вызовов функции через декоратор

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()  # это -> вызов hello()
#         print('Вызов функции', count)
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# Декоратор с двумя аргументами

# def args_decorator(fn):  # fn - сюда приходит та функция, которую мы декорируем
#     def wrap(arg1, arg2):  # помещаем 2 аргумента сюда (можно было и first, last, т.к. области видимости закрыта)
#         print('Data:', arg1, arg2)
#         fn(arg1, arg2)  # и сюда, т.к. иначе не даст
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('My name is', first, last)
#
#
# print_full_name('Elisei', 'Kamenetsky')


# При разном количестве аргументов используем (*args, **kwargs)

# **kwargs для того, чтобы не ограничивать пользователя в том,
# как он передает данные в функцию (именованные и пр. пар.)

# def args_decorator(fn):  # fn - сюда приходит та функция, которую мы декорируем
#     def wrap(*args, **kwargs):  # помещаем 2 аргумента сюда (можно было и first, last, т.к. области видимости закрыта)
#         # print(*args)  # здесь произойдет распаковка кортежа -- Elisei Kamenetsky
#         print('Args:', args)  # args - выйдет просто кортеж
#         print('Kwargs:', kwargs)
#         fn(*args, **kwargs)  # и сюда, т.к. иначе не даст
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('My name is', first, last)
#
#
# @args_decorator
# def print_full_name1(first, second, last):
#     print('My name is', first, second, last)
#
# print_full_name('Elisei', 'Kamenetsky')
# print_full_name1('Elisei', 'Leonidovich', 'Kamenetsky')


#  Параметры декоратора

# def decor(args_1, args_2):  # чтобы передать параметр, создаем сверху еще функцию
#     def args_dec(fn):
#         def wrap(x, y):
#             # print(args[0], x, args[1], y, '=', end=' ')  # если вверху передать *args, то отработало бы так
#             print(args_1, x, args_2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')  # Сумма: -> args_1, + -> args_2
# def summa(a, b):
#     print(a + b)  # Здесь получили: Сумма: 2 и 3 = 5
#
#
# @decor('Разность:', '-')  # Разность: -> args_1, - -> args_2
# def sub(a, b):
#     print(a - b)  # Здесь получили: Разность: 2 и 3 = -1
#
#
# summa(2, 3)
# sub(2, 3)


# Зд: умножение чисел через декоратор

# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#     return decor
#
#
# @multiply(3)  # -> in num
# def return_num(mult):  # mult -> in mult
#     return mult
#
#
# print(return_num(5))


# Запрет через декоратор (напр. ТОЛЬКО для int и др.) + использование raise
# Вот тут прям пиздец какой-то, если честно

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Некорректный тип данных', f_args[i])  # даем объяснение, что некорректно отработало
#
#             for k in kwargs:  # делаем проверку для последнего вызова (с z)
#                 if type(f_kwargs[k]) != kwargs[k]:  # k - ключ, т.к. у словаря нет индексов
#                     raise TypeError('Некорректный тип данных', f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'Die'))  # вот тут будет ругаться из-за 'Die', т.к. заявлен int
# print(typed_fn2('3', '4', '5'))
# # print(typed_fn3('3', '4', z='5'))  # вот тут будет ругаться из-за '5', т.к. заявлен int


# Когда нужно использовать один и тот же декоратор в двух вариациях

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text='Hello, ')  # вывод: Hello, World!
# def hello_world(text):
#     print(text)
#
#
# @args_decorator  # если ничего не передаем, то попадаем сразу в my_decorator; если поставить () отработают значения
# def hello_world2(text):
#     print(text)
#
#
# hello_world('World!')
# hello_world2('Hi!')
