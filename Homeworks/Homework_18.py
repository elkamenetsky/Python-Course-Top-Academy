# Задание 1: кол-во отрицательных чисел через рекурсию

a = [-2, 3, 8, -11, -4, 6]


def func(lst):
    if not lst:
        return 0
    else:
        count = func(lst[1:])
        if lst[0] < 0:
            count += 1
        return count


print('Количество отрицательных чисел:', func(a))

