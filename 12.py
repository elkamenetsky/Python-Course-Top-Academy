# Задача с подсчетом посещений городов (с nonlocal)

# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
#
# res1 = func('Москва')  # переменная будет хранить в себе состояния
# res1()  # поэтому при повторном вызове счетчик работает дальше
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()


# Перевод оценок-баллов в буквы и ранжирование через замыкание

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69,
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v <= upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(60, 80)
# C = classifier(40, 60)
# D = classifier(0, 40)
#
# print('A-score: ', A(students))
# print('B-score: ', B(students))
# print('C-score: ', C(students))
# print('D-score: ', D(students))


# Штука из ООП - обращение к функции через .

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():  # функция для связки остальных
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#
#     return replace
#
#
# obj1 = func(5, 2)  # obj1 == replace
# print(obj1.add())  # obj1.add == replace.add
# print(obj1.sub())  # obj1.sub == replace.add
# print(obj1.mul())  # obj1.add == replace.add


# ============================================
# Lambda-выражения - анонимные функции
# Имени у нее нет (поэтому анонимная), но это та же функция
# ============================================

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y  # ее можно сохранить и в переменную, но будет _ ( + смысла нет)
# print(func(1, 2))
# print(func('a', 'b'))
#
# (lambda: print('Hello'))()  # можно и такую форму
#
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))  # lambda для суммы квадратов
#
# summ = lambda a, b, c: a + b + c
# print(summ(10, 20, 30))
#
# func = lambda *args: args  # передача значений в кортеж
# print(func(1, 2, 3, 4, 5, 6, 7))
# print(func(1, 2, 3))


# Проход в цикле по lambda-выражению

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for t in c:
#     print(t('abc_'))


# Lambda и замыкание

# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))
#
# # более компактный вариант записи
# inc1 = (lambda n: lambda x: n + x)
# f1 = inc1(42)
# print(f1(3))
#
# # еще боле компактный вариант записи
# print((lambda n: lambda x: n + x)(42)(3))


# Умножение 3-х чисел через lambda-выражение

# print((lambda i: lambda j: lambda k: i * j * k)(2)(4)(6))


# Сортировка с помощью lambda

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Васильев', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семёнов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])  # сортировка по фамилии
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)  # сортировка по рейтингу (по убыванию)
# print(res)


# Зд: сортировка по значениям (словарь -> список кортежей -> словарь)

# d = {'b': 15, 'a': 3, 'c': 7}
# lst = list(d.items())
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))


# Список из lambda-выражений

# a = [(lambda x, y: x + y),
#      (lambda x, y: x - y),
#      (lambda x, y: x * y),
#      (lambda x, y: x / y)]
# print(a[0](12, 3))


# Lambda-выражение в виде значений ключей словаря

# a = {'one': lambda x: x - 1,
#      'two': lambda x: x - 3,
#      'three': lambda x: x}
#
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#          print(a['one'](i))
#     else:
#          print(a['three'](i))


# d = {
#      1: lambda: print('Понедельник'),
#      2: lambda: print('Вторник'),
#      3: lambda: print('Среда'),
#      4: lambda: print('Четверг'),
#      5: lambda: print('Пятница'),
#      6: lambda: print('Суббота'),
#      7: lambda: print('Воскресенье')
# }
#
# d[3]()  # вызов среды


# Lambda и тернарное выражение

# n = lambda a, b: a if a > b else b
# print(n(10, 20))


# map(function, iterable) - проход по каждому элементу и выполнение функции

# def nul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# lst2 = tuple(map(nul, lst))
# print(lst2)
#
# lst3 = tuple(map(lambda t: t ** 2, lst))  # тоже самое, но через lambda (сокращает код)
# print(lst3)


# Приведение к типу через map

# t = (2.88, -1.79, 100.03)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
#
# t2 = tuple(map(int, t))  # НО(!) можно и без lambda, т.к. int() - это готовая функция
# print(t2)


# Округление round через map

# area = [3.4363463, 5.34763573, 2.56835433, 2.125412, 9.421574561, 0.2352677437]
# res = list(map(round, area, range(1, 7)))  # будет увеличиваться дробная часть с каждым разом
# print(res)
# res = list(map(round, area, range(1, 3)))  # выведет только 2 элемента с тем же увеличением
# print(res)
# res = list(map(round, area, [2, 2, 2, 2, 2, 2]))  # по количеству элементов (6) - 2 цифры после точки
# print(res)


# Получение списка кортежей через map

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)


# Зд: найти поэлементно сумму чисел 2-х списков

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# 
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)
