days = int(input('days please: '))
summa = 0
a = 0.5
itog = []
if days > 0:
    for i in range(1, days+1):
        a = a * 2
        summa += a
        itog.append(int(a))
elif days == 0:
    print('no days')
elif days < 0:
    print('error days must be > 0')
print(summa / 100)
print(itog)
