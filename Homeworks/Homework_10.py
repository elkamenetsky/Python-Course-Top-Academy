# Задание 1
a = ['red', 'green', 'blue']
b = ['#FF0000', '008000', '#0000FF']
c = dict(zip(a, b))
print(c)


# Задание 2
number_dict = {}
for i in range(1, 11):
    number_dict.update({i: i ** 3})
print(number_dict)


# Задание 3
c = ['color', 'fruit', 'pet']
d = ['blue', 'apple', 'dog']
new_dict = {c: d for c, d in zip(c, d)}
print(new_dict)


# Задание 4
def function_minimum(n):
    return min(n)


print(function_minimum([10, 9]))
print(function_minimum([2, 3, 4]))
print(function_minimum([3, 5, 10, 6]))


# Задание 5
def function_amount(m):
    new_list = m
    for i in range(len(new_list)):
        if i != 0:
            new_list[i] = new_list[i] + new_list[i - 1]
        else:
            continue

    print(' '.join(map(str, new_list)))


function_amount([3, 9, 1])
function_amount([2, 5, 4, 2])
function_amount([3, 5, 10, 6, 3])
