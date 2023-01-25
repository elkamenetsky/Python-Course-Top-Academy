# Множество - set()

# s = {'banana', 'apple', 'orange'}
# print(s)
# print(type(s))  # class 'set'
#
# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)  # последние 2 дубля не отобразятся
# print(len(s))  # длина множества так и осталась - 3
#
# # Множество хранит только УНИКАЛЬНЫЕ значения
# # Это неупорядоченный тип данных (выведет так, как хочет) - НЕТ ИНДЕКСОВ
#
# a = {}
# print(type(a))  # class 'dict' (ЭТО ДРУГОЙ ТИП ДАННЫХ)
#
# b = set()  # set создается ТОЛЬКО ТАК
# c = set('hello')  # выйдет набор 4 букв, а не 5 (l встречается дважды)
# print(c)
#
# c = ['green', 'black', 'blue']
# a = set(c)  # преобразование из списка
# print(a)
#
# s = {i for i in range(10)}
# print(s)
#
# numbers = [1, 2, 3, 4, 4, 5, 5, 6, 8, 9, 6, 7, 5]
# s = {i for i in numbers}  # перебор готового списка
# print(s)
#
# s = list({i for i in numbers if i % 2 == 0})  # вывод только четных чисел и конвертирование их в список
# print(s)


# Задача по преобразованию данных в множество через функцию

# def to_set(par):
#     return set(par), len(set(par))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# s = {'banana', 'apple', 'orange'}
# print('apple' in s)  # выдаст True
#
# for i in s:  # вывод через цикл
#     print(i)
#
# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}  # будет проверять каждый элемент
# print(a)
# b = {'A' + i[1:] if i[0] == 'a'
#      else 'B' + i[1:] for i in r}  # замена первой буквы на ВЕРХНИЙ РЕГИСТР через тернарный оператор
# print(b)
# c = {'A' + i[1:] if i[0] == 'a'
#      else 'B' + i[1:] for i in r if i[1] == 'c'}  # доп. условие к предыдущему
# print(c)


# s = {'banana', 'apple', 'orange'}
# # множество - изменяемый тип данных, но конкретный элемент поменять нельзя (т.к. неупорядоченные данные)
#
# s.add('potato')  # добавление
# s.add(10)
# s.remove('apple')  # удаление
# print(s)
# if 10 in s:  # удаление с проверкой наличия элемента
#     s.remove(10)
# print(s)
# s.discard(4)  # удаление, но без вывода ошибки если элемента нет
# print(s)
# s.pop()  # удаление и возвращение (удаляет "типа" первый элемент - он постоянно будет меняться)
# print(s)
# s.clear()  # полная очистка множества - вернет просто set()
# print(s)


# ! Есть целый раздел работы с множествами с кучей математических действий
# Операции над множествами (используются спец. символы - не арифметические)
# Есть табличка с операциями в материалах к курсу

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a | b  # | - оператор объединения
# print(c)
# c = a.union(b)  # тоже самое, но через метод
# print(c)

# Задача на разные операции с множествами

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7  # объединение всех в один
# print(s)
# print(len(s))  # количество элементов множества
# print(max(s))  # максимальное значение
# print(min(s))  # минимальное значение


# Общие буквы в разных строках

# a = set(input('Введите первую строку: '))
# b = set(input('Введите вторую строку: '))
# print('Общими буквами являются: ', a & b)
# print('Отсутствующие буквы: ', a - b)


# =====================================

# list() - список
# tuple() - кортеж
# set() - множество
# frozenset() - замороженное множество
# frozenset нужен для того, чтобы предохранить множество от изменений

# =====================================

# Словарь - dict / ассоциативный массив (т.к. ассоциируется с каким-то ключом)

# a = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}  # словарь требует [уникальный] 'КЛЮЧ': значение
# print(a[0])  # обращаемся по индексу
# print(d['one'])  # обращаемся по ключу (по индексу нельзя, хоть и порядок формально есть)
#
# d = {}  # создается пустой словарь (НЕ МНОЖЕСТВО!)
# print(d)
# d = dict(one=1, two=2, three=3)  # второй способ создания (через функцию)
# # d = dict(1=1, 2=2, 3=3)  # в такой форме нельзя ключ обозначить числом (ограничение такой формы записи)
# print(d)

# a = [1, 2, 3]
# # b = dict(a)  # так не выйдет, т.к. не хватает ключей
# b = (
#     ('igor@gmail.com', 'Igor'),
#     ('viktor@gmail.com', 'Viktor'),
#     ('irina@gmail.com', 'Irina'),
# )
# c = dict(b)  # теперь все отработает: e-mail как ключ, имя как значение (можно и списком, но будет ворчать)
# print(c)

# d = {i: i for i in range(7)}  # генерация через for (ключ = значение)
# print(d)
# d = {i: i ** 2 for i in range(7)}  # генерация через for (ключ = квадрат значение)
# print(d)
# d[3] = 15  # словарь - измененяемый тип данных
# print(d)

# d = {0: 'text', 'one': 1}  # значением может быть любой тип; ключом - только неизменяемый тип (!)
# print(d)
# print(d[0][1])  # [0] - ключ, [1] - индекс. Выведется 'e'
# print('one' in d)  # проверка по ключам
# del d['one']  # удаление по ключу (ошибка, если ключа нет)
# print(d)
# # Удаление через try - except. Можно и через if
# try:
#     del d['one']
# except KeyError:
#     print('Элемента с таким ключом нет в словаре')

# d = {0: 'text', 'one': 1, (1, 2.3): 'Кортеж', 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
#
# for key in d:
#     print(key)  # сюда попадут ключи
#     print(d[key])  # так выведутся значения по ключу

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# c = 1
# for i in d:
#     c *= d[i]
# print(c)

# Задача с вводом значений в словарь и действия со словарем

# # d = dict()  # большой вариант
# # d[1] = input('-> ')
# # d[2] = input('-> ')
# # d[3] = input('-> ')
# # d[4] = input('-> ')
# d = {i: input('-> ') for i in range(1, 5)}  # компактный вариант
# print(d)
# dislike = int(input('Что исключить? '))
# del d[dislike]
# print(d)


# Задача с товарами

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], ' рублей', sep='')
#
# while True:
#     n = input('Введите номер товара: ')
#     if n != '0':
#         qty = int(input('Введите количество товара: '))
#         goods[n][1] = qty
#         for i in goods:
#             print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], ' рублей', sep='')
#     else:
#         break

