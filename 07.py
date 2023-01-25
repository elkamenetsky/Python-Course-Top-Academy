# import time
# import locale

# s = time.time()  # отсчет секунд с 1970 года
# print(s)
# local_time = time.ctime()  # дата / время в стандартном формате (аргумент: кол-во секунд)
# print(local_time)  # данные передаются строкой
#
# res = time.localtime()  # точные данные
# print(res)
# print(res.tm_year)  # используя ключ, можно вывести нужное значение
#
# print(time.strftime('Today is %d %B, %Y'))  # через % указываются форматы
# print(time.strftime('Today is %d/%m/%Y, %H:%M:%S'))  # текущие дата и время
# print(time.strftime('Today is %d/%m/%Y, %H:%M:%S', time.localtime(85435624)))  # через какое-то кол-во секунд от 1970
#
# print(time.strftime('Сегодня %d %B, %Y'))  # нужно перевести название месяца
# locale.setlocale(locale.LC_ALL, 'ru')  # setlocal(категория (что переводить?), язык)
# print(time.strftime('Сегодня %d %B, %Y'))

# Функция sleep

# pause = 5
# print('Program started ...')
# time.sleep(pause)  # задержка pause секунд (имитация задержки)
# print(pause, 'seconds')

# Напоминалка с вводом времени

# text = input('Название напоминания: ')
# local_time = float(input('Через сколько минут напомнить? '))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# Замер времени выполнения программы

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, 'sec.')  # вывод с погрешностью

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res, 'sec.')  # не дает погрешность

# ФУНКЦИИ
# print(1)
#
#
# def hello(name, word):  # 2 пустые строки сверху и снизу (синтаксическое визуальное требование)
#     print('Hey', name, 'say', word)
#
#
# hello('Elisei', 'hello')  # если параметр не передать, будет ошибка

# def get_sum(a, b):
#     print(a + b)
#
#
# c = 2  # желательно, чтобы переменные не пересекались (вне и внутри области видимости функции)
# d = 5
# get_sum(c, d)


# def symbol(count, a, b):
#     print((a + b) * (count // 2) + a * (count % 2))
#
#
# symbol(9, '+', '-')


# def get_sum(a, b):
#     return a + b  # теперь значение будет возвращаться
#     # return  # без значений сработает как прерывание функции
#
# c = 2
# d = 5
# w = get_sum(c, d)  # через return мы можем сохранить ее в w
# print(w)


# Функция - нахождение максимума с использованием буллевых значений

# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(1, 3):
#     print('Первое число больше')
# else:
#     print('Второе число больше')


# Функция - проверка надежности пароля

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:  # проверка наличия разных символов
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:  # проверка длины пароля
#         return True
#     return False  # здесь else можно не писать
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Этот пароль надежный')
# else:
#     print('Этот пароль ненадежный')


# Функция возведения чисел в куб через for

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cube(i))


# Функция перестановки первого и последнего значений в списке

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]  # другой вариант (без методов списка)
#     # return lst
#
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.insert(0, end)
#     lst.append(start)
#     return lst

# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def get_sum(a, b, c, d=1):  # именованный аргумент d = 1, теперь заработает с 3 аргументами
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5))
# print(get_sum(1, 2, d=5, c=0))  # можно напрямую передать и отсюда


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digits = n % 10
#         if even and cur_digits % 2 == 0:
#             s += cur_digits
#         if not even and cur_digits % 2 != 0:
#             s += cur_digits
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр:', digits_sum(9874823))
# print('Сумма нечетных цифр:', digits_sum(9874823, even=False))


def display_info(name, age):
    print('Name:', name, '\nAge:', age)


display_info('Elisei', 26)
display_info(26, 'Elisei')  # отработает формально верно, т.к. язык не явно типизированный
display_info(age=26, name='Elisei')  # так можно позиционные аргументы сделать именованными


