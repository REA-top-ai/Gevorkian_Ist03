k1 = input('Введите количество монет 5 копеек: ')
k2 = input('Введите количество монет 10 копеек: ')
k3 = input('Введите количество монет 50 копеек: ')
summa = (int(k1)*5 + int(k2)*10 + int(k3)*50) / 100
if summa == 1:
    print('good')
elif summa < 1:
    print('small')
elif summa > 1:
    print('big')

