# Задание 1
symbol = input('Введите символ: ')
number_of_symbols = int(input('Введите количество символов: '))
orientation = int(input('Выберите ориентацию линии:'
                    '\n0 - горизонтальная'
                    '\n1 - вертикальная'
                    '\nВведите необходимый номер: '))
if orientation == 1:
    print((symbol + '\n') * number_of_symbols)
elif orientation == 0:
    print((symbol + ' ') * number_of_symbols)
else:
    print('Введены некорректные значения')

# Задание 2
width = int(input('Укажите ширину прямоугольника (числом): '))
height = int(input('Укажите высоту прямоугольника (числом): '))
i = 1
while i <= height:
    print('+' * width)
    if i == height:
        break
    j = 0
    while j < 1:
        print('-'* width)
        j += 1
    i += 2

# Задание 3
a, b, c = int(input('Введите значение 1: ')), int(input('Введите значение 2: ')), int(input('Введите значение 3: '))
print('Максимальное значение:', a if a > b and a > c else b if b > a and b > c else c)

# Задание 4
operation = int(input('Список возможных операций:'
                  '\n1 - "r" - применяет унарный минус к операнду'
                  '\n2 - "+" - сложение'
                  '\n3 - "-" - вычитание'
                  '\n4 - "/" - деление'
                  '\n5 - "*" - умножение'
                  '\n6 - "%" - остаток от деления'
                  '\n7 - "<" - минимальное из двух чисел'
                  '\n8 - ">" - максимальное из двух чисел'
                  '\nВведите номер необходимой операции: '))
if operation == 1:
    number = int(input('Введите число, которое необходимо преобразовать: '))
    print('Результат операции:', number * (-1))
elif 1 < operation < 9:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    if operation == 2:
        print('Результат сложения:', first_number + second_number)
    elif operation == 3:
        print('Результат вычитания:', first_number - second_number)
    elif operation == 4:
        print('Результат деления:', first_number / second_number)
    elif operation == 5:
        print('Результат умножения:', first_number * second_number)
    elif operation == 6:
        print('Результат деления по модулю:', first_number % second_number)
    elif operation == 7:
        print('Минимальное значение:', min(first_number, second_number))
    else:
        print('Максимальное значение:', max(first_number, second_number))
else:
    print('Введен некорректный номер операции')
