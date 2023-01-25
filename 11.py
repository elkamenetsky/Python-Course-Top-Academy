# Создание функции передачи значений в словарь (ключ = значение)

# def to_dict(*lst):
#     print(lst)  # выходит кортеж
#     print(*lst)  # происходит распаковка кортежа
#     return {i : i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# Функция из чисел выдает среднее арифметическое и выводит те, которые меньше

# def fun(*a):
#     return [i for i in a if i < sum(a) / len(a)]
#
#
# print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))


# Когда в функцию приходят и именованные, и позиционные аргументы

# def func(a, *args):
#     return a, args
#
#
# print(func(1, 2, 3, 'abc'))  # должно быть хотя бы одно значение - он уйдет в позиционный а, остальные в args
#
#
# def print_scores(student, *scores):  # имя должно быть 1, а оценок - много
#     print('Student Name: ', student, end=', Scores: ')
#     a, b = None, ''
#     for score in scores:
#         a = str(score) + ', '
#         b += a
#     print(b[:-2])
#
#
# print(print_scores('Elisei', 5, 4, 3, 5))


# Функция, разворачивающая числа из списка (по запросу - нечетные)

# def reverse_num(n):  # 12 -> 21
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd = False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):
#             res.append(reverse_num(i))  # внутри одной функции вызов другой
#     return res
#
#
# print(12, 5432, 6544, 7865, 26, 437, 18, 19)
# print(func(12, 5432, 6544, 7865, 26, 437, 18, 19))
#
# print(func(12, 5432, 6544, 7865, 26, 437, 18, 19, only_odd = True))


# Keword arguments -> создание словаря

# def func(**kwargs):  # keyword arguments (ключ (не число!) = значение -> ключ: значение)
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(a='python', b='java'))


# def function(**data):
#     for key, value in data.items():
#         print(key, 'is', value)
#     print()
#
#
# function(name='Irina', surname='Sharma', age=22, phone=89115554621)
# function(name='Igor', surname='Wood', email='igor@mail.ru', country='Russia', age=36, phone=89216782320)


# Задача на аккумуляцию новых элементов в словарь

# my_dict = {'one': 'first'}
#
#
# def func(**data):
#     for key, value in data.items():
#         my_dict[key] = value
#     print(my_dict)
#
#
# func(k1=22, k2=31, k3=11, k4=91)
# func(name='Bob', age=31, weight=61, eyes_color='grey')


# Передача разных видов в функцию и их порядок

# def func(a, *args, **data):  # позиционный a - должен стоять первым (возьмет первый э! (args) {data}
#     print(a, args, data)
#     print(args[1], data['k1'])
#
#
# func(4, 5, 6, 7, k1=22, k2=31, k3=11, k4=91)


# ==================================================
# Области видимости (scope)
# ==================================================

# name = 'Tom'  # глобальная переменная
#
#
# def hi():
#     global name  # сделали переменную глобальной (можно перечислить несколько)
#     name = 'Sam'  # локальная переменная (только внутри функции)
#     surname = 'Wood'  # локальная переменная (только внутри функции)
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Bye', name)  # здесь вновь обращение к глобальной переменной (-> global)
#
#
# print(name)  # тут выйдет Tom
# hi()
# print(name)  # а здесь уже Sam
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # выведется 5, т.к. в функции идет присваивание (!), оно записывается ранее

# def add_two(a):
#     x = 2  # объемлющая область видимости
#
#     def add_some():  # вложенная функция
#         x = 3  # теперь это локальная переменная (имеет приоритет в данном случае)
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))
# # print(x)  # х за пределами функции не существует - будет ошибка!
# # add_some()  # будет ошибка, т.к. вложенной функции за пределами функции не существует


# ==================================================
# LEGB - правило работы областей видимости
# Local -> Enclosed -> Global -> Built-in (встроенная область не видна! - она на уровне самого языка)
# ==================================================


# Вывод элементов (разные типы) встроенного уровня
# import builtins
# name = dir(builtins)
# for i in name:
#     print(i)


# Проблема перезаписи элемента built-in
# она отрабатывает самой последней и ее легко перезаписать. Так не делать!

# max = [8, 1, 2, 3, 4, 5, 9]  # перезаписали элемент встроенного уровня - ниже будет ошибка!
# print(min(max))
#
# a = [7, 8, 5, 6, 9]
# print(max(a))


# ==================================================
# Вложенные функции
# ==================================================

# Работать будет только в таком виде:
# внутри функции вызываем вложенную, затем вызываем саму функцию

# def outer_func(what):
#     def inner_func():
#         print('Hello,', what)
#     inner_func()
#
#
# outer_func('world')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print('a =', a)
#     fun2(4)
#
#
# fun1()


# Ограничения PyCharm

# Здесь PyCharm будет подчеркивать, но Python все нормально отработает
# x = 25
# t = 0
#
#
# def fun():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a  # перезапишет a = 30
#         a = 35
#
#     inner()
#     t = a
#
#
# fun()
# z = x + t  # 25 + 30 = 55 -> nonlocal a -> 25 + 35 = 60
# t = ''
# print(z)
# print(t)  # тут PyCharm покажет тип int, хотя это не так

# Работа 3-х вложенных функций

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             x = 55
#
#         fn3()  # здесь x = 55 перестала существовать, как только мы вышли за пределы функции
#         print('fn2, x =', x)
#
#     fn2()  # здесь x = 33 перестала существовать, как только мы вышли за пределы функции
#     print('fn1, x =', x)  # здесь х снова = 25
#
#
# fn1()

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33  # если эту строку убрать, то перезапись пойдет на x = 25
#
#         def fn3():
#             nonlocal x  # x = 33 теперь не существует (перезапись на 55)
#             x = 55
#
#         fn3()
#         print('fn2, x =', x)
#
#     fn2()
#     print('fn1, x =', x)
#
#
# fn1()


# Работа с локальной областью видимости

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         # nonlocal a, b  # чтобы заработало, нужен nonlocal
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)  # здесь будут корректные значения
#
#     inner()
#     return [a, b]  # которые сюда не попадут, т.к. область другая
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# Замыкание - это когда наружная функция возвращает внутреннюю (но не ее вызов)

# def outer(n):
#     def inner(x):  # сюда мы теперь обращаемся через add
#         return n + x
#
#     return inner  # если теперь сюда передать число, будет ошибка
#
#
# add = outer(5)
# print(add(10))  # 10 отсюда передается в х !
# # Если не передать, то выведется <function outer.<locals>.inner at 0x0000014C095F7F60>
#
# add1 = outer(1)  # можем снова обращаться с другими значениями
# print(add1(10))
# print(add1(25))
#
# print(outer(5)(15))  # можно вызвать так, но обычно так не используют (так - в основном для lambda-выражений)


def func1():
    a = 1
    b = 'Line'
    c = [1, 2, 3]

    def func2():
        nonlocal a
        c.append(4)
        a = a + 1  # нужен nonlocal, т.к. объект неизменяемый (!)
        return a, b, c

    return func2


func = func1()
print(func())
