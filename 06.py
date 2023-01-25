from random import randint, randrange

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)  # оператор in возвращает буллево значение (Есть ли 'а' в х?)
# print('a' not in x)  # отрицание in

# lst = []
# # if len(lst) == 0:
# if not lst:  # то же самое, но более компактно
#     print('The list is empty')
# print(bool(lst))


# n1 = int(input('Введите длину 1-го списка: '))
# n2 = int(input('Введите длину 2-го списка: '))
#
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('Первый список:', a)
# print('Второй список:', b)
#
# c = []  # Можно было сделать проще, сложив оба списка и исключив повторения
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Третий список (оба списка без повторений):', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print('Четвертый список (повторения):', c)
#
# c = [min(a), min(b), max(a), max(b)]
# print('Пятный список (минимальные и максимальные значения:', c)


# Вывести определенноок количество уникальных чисел
# n = int(input('Введите длину списка: '))
# a = [randint(0, 10) for i in range(n)]
# c = []
# while len(c) < n:
#     num = randrange(n)
#     if num not in c:
#         c.append(num)
# print('Уникальные значения:', c)

m = [
    [1, 2, 3, 4],
    [4, 6, 7, 8],
    [9, 10, 11, 12]
]
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# for row in m:  # более компактная запись
#     # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 5, 3
# # matrix = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     matrix.append(new_row)
# matrix = [[0 for x in range(w)] for y in range(h)]  # более компактная запись
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# Распаковка массивов в переменные через for
# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)

# w, h = 3, 4
# comp = 1
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#         if x != 0:
#             comp *= x
#     print()
# print('Произведение:', comp)

# Поиск минимального значения по диагонали в матрице
# w = h = 6
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# s = []
# m = 101
# for i in range(w):
#     if m > matrix[i][i]:
#         m = matrix[i][i]
# print(m)
# #     s.append(matrix[i][i])  # более компактная запись
# #     m = matrix[i][i]
# # print(min(s))

# Модуль math
# import math
#
# num1 = math.sqrt(4)  # квадратный корень
# print(num1)
# num2 = math.ceil(3.2)  # округление в верхнюю сторону
# print(num2)
# num3 = math.floor(3.8)  # округление в нижнюю сторону
# print(num3)
# num4 = round(3.8436373, 2)  # round(число, количество чисел после запятой)
# print(num4)
