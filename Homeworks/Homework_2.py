money = int(input('Введите количество копеек (от 0 до 99): '))
money_units = money % 10
money_name = 'копеек'

if money < 0 or money > 99:
    print('Введено некорректное число')
else:
    if 11 <= money <= 14:
        money_name = 'копеек'
    else:
        if 2 <= money_units <= 4:
            money_name = 'копейки'
        elif money_units == 1:
            money_name = 'копейка'
    print(money, money_name)
