from random import randint
# Задание 1
number = randint(1, 100)
choise = int(input('Введите число от 1 до 100: '))
count = 1
while choise != number:
    if choise < number and choise != 0:
        choise = int(input('Попробуйте еще раз. Загаданное число больше: '))
        count += 1
    elif choise > number:
        choise = int(input('Попробуйте еще раз. Загаданное число меньше: '))
        count += 1
    elif choise == 0:
        print('Игра закончена. К сожалению, вы не угадали число')
        break
else:
    print('Поздравляем! Вы угадали число с', count, 'попытки')

# Задание 2
m = [int(input('Введите значение: ')) for i in range(int(input('Введите количество элементов списка: ')))]
print(m[::2])

# Задание 3
m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
n = []
for i in m:
    if m.count(i) == 1:
        n.append(i)
print(' '.join(map(str, n)))

# Задание 4
base = int(input('Введите высоту треугольника: '))
while base != 0:
    print('*' * base)
    base -= 1
