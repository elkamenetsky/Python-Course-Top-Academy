# КОРТЕЖ
# lst = [10, 20, 30]  # список (изменяемый)
# crt = (10, 20, 30)  # кортеж (неизменяемый)

# __sizeof__() - показывает занимаемый в памяти размер

# print(lst.__sizeof__())
# print(crt.__sizeof__())

# a = 1, 2, 3, 4, 5  # создание кортежа
# a = tuple([1, 2, 3, 4, 5])  # тоже самое но из списка
# a = tuple(1, 2, 3, 4, 5)  # ТАК РАБОТАТЬ НЕ БУДЕТ! Должно быть одно значение
# a = 2,  # ГЛАВНОЕ - ЗАПЯТАЯ!
# print(a)

# t = tuple(['Hello'])
# print(t)
# t = tuple('Hello')
# print(t)

# s = input('-> ')
# print(tuple(s))
# print(int(tuple(s)[1]))

# s = tuple([input('-> ') for i in range(3)])
# print(s)

# s = []
# for i in range(1, 13):
#     s.append(2 ** i)
# print(tuple(s))

# s = tuple(2 ** i for i in range(1, 13))  # Та же самая задача, что и выше
# print(s)

# from random import randint
#
# s = tuple(randint(1, 30) for i in range(3))  # генерация случайных чисел в кортеж
# print(s)

# t1 = tuple('Hello')
# t2 = tuple('world')
# t3 = t1 + t2  # объединяет два кортежа в новый кортеж
# print(t3)
# print(len(t3))
#
# print(t3.count('l'))  # подсчет элементов
# print(t3.index('l'))  # индекс первого совпадения (value, start, stop). Выдаст ошибку, если нет элемента
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print('There is not this symbol')
#
# for i in t3:  # по кортежу можно пройтись циклом
#     print(i, end=' ')

# def slicer(tpl, num):
#     if num not in tpl:
#         return tuple()
#     first = tpl.index(num)
#     if num not in tpl[first + 1:]:
#         return tpl[first:]
#     last = tpl.index(num, first + 1)
#     return tuple(tpl[first:last + 1])
#
# print(slicer((1, 2, 3, 4, 5), 8))
# print(slicer((1, 8, 4, 3, 1, 8, 6, 6), 8))
# print(slicer((1, 8, 4, 3, 1, 3, 2), 8))


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3, 4, 5), 8))
# print(slicer((1, 8, 4, 3, 1, 8, 6, 6), 8))
# print(slicer((1, 8, 4, 3, 1, 3, 2), 8))

from random import randint

# a = tuple(randint(0, 5) for i in range(10))
# b = tuple(randint(-5, 0) for j in range(10))
# c = a + b
# count = c.count(0)
# print(a)
# print(b)
# print(c, count)


# def comp(a, b):  # то же самое, но через функцию
#     return tuple(randint(a, b) for _ in range(10))  # если i нигде не участвует, то можно использовать _
#
#
# t1 = comp(0, 5)
# t2 = comp(-5, 0)
# print(t1 + t2, (t1 + t2).count(0))


# Кортеж и match
# point = (10, 20)
# # point = 10
# match point:
#     case (0, 0):
#         print('Точка находится в коррдинатах 0:0')
#     case (x, 0):  # x взял значение из point, т.к. значение не передано
#         print('Точка находится в коррдинате', x, 'по оси Х и координате 0 по оси Y')
#     case (0, y):
#         print('Точка находится в коррдинате 0 по оси Х и координате', y, 'по оси Y')
#     case (x, y):
#         print('Точка находится в коррдинате', x, 'по оси Х и координате', y, 'по оси Y')
#     case _:
#         print('Это не координаты точки')

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'  # изменили список внутри кортежа (так можно)
# t[4].append('hi')
# print(t, id(t))


# Распаковка кортежей

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # более компактная запись
# # x, y, z, q = t  # будет ошибка, т.к. количество должно совпадать (!)
# print(x, y, z)

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married  # в python можно вернуть несколько значений (в виде кортежа!)
#
#
# user = get_user()
# # print(user[0])
# # print(user[1])
# # print(user[2])
# name1, age1, is_married1 = user
# print(name1, age1, is_married1)
#
# name2, age2, is_married2 = get_user()  # такой вариант используется чаще!
# print(name2, age2, is_married2)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# crt = tuple(lst)
# print(crt)
# lst = list(crt)
# print(lst)
# # Так можно преобразовывать элементы: кортеж в список, меняем, назад в кортеж

# Распаковка кортежа через вложенные for
# countries = (
#     ('Russia', 144, (('Moscow', 15), ('Omsk', 2))),
#     ('France', 80, (('Paris', 10), ('Leon', 3)))
# )
# print(countries)
# print()
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nCountry:', country_name + ', population =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tCity: ', city_name + ', population = ', city_population)

