from random import randint

print('\nЗадание 1')

# Задание 1
numbers_1 = [randint(0, 100) for i in range(10)]
print('Сгенерированный массив:', numbers_1)
print('Максимальное значение массива:', max(numbers_1))
numbers_1.insert(0, numbers_1.pop(numbers_1.index(max(numbers_1))))
print('Измененный массив:', numbers_1)


print('\nЗадание 2')

# Задание 2
numbers_2 = [randint(-20, 20) for j in range(10)]
print('Сгенерированный массив:', numbers_2)
numbers_2.sort(reverse=True)
print('Измененный массив:', numbers_2)


print('\nЗадание 3')

# Задание 3
numbers_3 = [randint(0, 100) for k in range(10)]
print('Сгенерированный массив:', numbers_3)
print('Минимальное значение:', min(numbers_3))
index_of_minimum = numbers_3.index(min(numbers_3))
print('Индекс минимального значения:', index_of_minimum)
del numbers_3[:numbers_3.index(min(numbers_3))]
print('Измененный массив:', numbers_3)