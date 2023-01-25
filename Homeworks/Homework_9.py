# Задание 1
dictionary = {'emp1': {'name': 'John', 'salary': 7500},
              'emp2': {'name': 'Emma', 'salary': 8000},
              'emp3': {'name': 'Brad', 'salary': 6500}}

dictionary['emp3']['salary'] = 8500

for i in dictionary:  # вывод через for, чтобы было в 3 строки, а не в 1
    print(dictionary[i])

# Задание 2
medium = 0
dictionary = {}

quantity = int(input('Введите количество студентов: '))

for i in range(quantity):
    surname = input(f'Введите фамилию {i + 1}-го студента: ')
    name = input(f'Введите имя {i + 1}-го студента: ')
    mark = int(input(f'Введите балл {i + 1}-го студента: '))
    dictionary[i + 1] = surname, name, mark

for j in dictionary:
    medium += dictionary[j][2]
medium /= len(dictionary)

print('\nСредний балл:', medium)
print('Студенты с баллом выше среднего:')

for k in dictionary:
    if dictionary[k][2] > medium:
        good_student = dictionary[k][0] + ' ' + dictionary[k][1]
        print(good_student)