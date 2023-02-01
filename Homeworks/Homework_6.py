import math
# Задача 1
print('Выбор фигуры:'
      '\n1 - треугольник'
      '\n2 - прямоугольник'
      '\n3 - круг')
figure = int(input('Введите номер фигуры: '))
if figure == 1:
    a = int(input('Введите сторону a: '))
    b = int(input('Введите сторону b: '))
    c = int(input('Введите сторону c: '))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь треугольника равна', round(s, 2))
elif figure == 2:
    a = int(input('Введите сторону a: '))
    b = int(input('Введите сторону b: '))
    s = a * b
    print('Площадь прямоугольника равна', s)
elif figure == 3:
    r = int(input('Введите радиус: '))
    s = math.pi * r ** 2
    print('Площадь круга равна', round(s, 2))
else:
    print('Введено некорректное значение!')

# Задание 2
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
for row in matrix:
    for x in row:
        print(x, end='\t')
    print()
print()
a = len(matrix)
b = len(matrix[0])
new_matix = [[0] * a for i in range(b)]
for i in range(a):
    for j in range(b):
        new_matix[j][i] = matrix[i][j]
for row in new_matix:
    for x in row:
        print(x, end='\t')
    print()




