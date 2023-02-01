# Задание 1
def function(n):
    res = []
    empty = []
    for i in n:
        if i > 0 and i % 13 == 0:
            res.append(i)
    if res == empty:
        res = 'Нет подходящих значений'
    else:
        res = max(res)
    return res


print(function([2, 7, 0, 3, 1, 5, -13]))
print(function([2, 7, 0, 3, 1, 5, -13, 13]))
print(function([26]))
print(function([99, 99, 100, 34, -39]))
print(function([99, 39, 99, 100, 34]))


# Задание 2
crt = ('ab', 'abcd', 'cde', 'abc', 'def')
s = 'ab'

if s in crt:
    print('Yes')
else:
    print('No')


# Задание 3
num = 253523651
crt = tuple(str(num))

for i in set(crt):
    print(f'Количество {i} = {crt.count(i)}')
