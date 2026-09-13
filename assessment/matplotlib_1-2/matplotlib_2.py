from matplotlib import pyplot as plt



# -------
# .subplots_adjust() регулирует поля вокруг подграфиков и промежутки между ними:
#   left, right, bottom, top — поля рисунка (по умолчанию 0.125/0.9/0.1/0.9)
#   wspace — горизонтальный промежуток между соседними подграфиками (по умолч. 0.2)
#   hspace — вертикальный промежуток между подграфиками (по умолч. 0.2)
#


plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])
plt.xlabel('x-Label for Plot 1')
plt.ylabel('y-label for Plot 1')

plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])
plt.xlabel('x-Label for Plot 2')
plt.ylabel('y-label for Plot 2')

plt.subplots_adjust(wspace=0.35)
plt.suptitle("Теория: subplots_adjust(wspace=0.35)")
plt.show()


# ЗАДАНИЕ
# --------
# Фигура из двух рядов: 1 график сверху (во всю ширину),
# 2 графика снизу (слева и справа).
# Данные:
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

# 1-2. Верхний подграфик (сетка 2 строки x 1 столбец, позиция 1) — straight_line.
plt.subplot(2, 1, 1)
plt.plot(x, straight_line)
plt.title('Straight Line')

# 3. Нижний-левый подграфик (сетка 2x2, позиция 3) — parabola.
plt.subplot(2, 2, 3)
plt.plot(x, parabola)
plt.title('Parabola')

# 4. Нижний-правый подграфик (сетка 2x2, позиция 4) — cubic.
plt.subplot(2, 2, 4)
plt.plot(x, cubic)
plt.title('Cubic')

# 5. Увеличить промежуток между нижними графиками (wspace) до 0.35
#    и нижнее поле (bottom) до 0.2.
plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()


# plt.legend(['метка1', 'метка2']) подписывает линии в порядке их создания.
# Аргумент loc задаёт положение легенды (0=best, 1=upper right, 2=upper left,
# 3=lower left, 4=lower right, 5=right, 6=center left, 7=center right,
# 8=lower center, 9=upper center, 10=center).
# Также можно подписывать линии сразу через label=... в plt.plot(),
# но plt.legend() всё равно нужно вызвать, чтобы легенда отобразилась.

plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label="parabola")
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], label="cubic")
plt.legend()  # метки уже заданы через label=
plt.title("Теория: легенда через label=... в plt.plot()")
plt.show()


# ЗАДАНИЕ
# --------
# Температура в Хайруле, Какарико и Долине Герудо по месяцам.
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

# 1. Список меток легенды.
legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']

# 2. Легенда с этими метками.
plt.legend(legend_labels)

# 3. Легенда по центру графика (loc=10 -> 'center').
plt.legend(legend_labels, loc=10)

plt.title("Задание: температура в трёх регионах (легенда по центру)")
plt.show()


# Чтобы менять положения и подписи меток на осях, нужен объект осей (Axes):
#   ax = plt.subplot()               -- получить оси текущего графика
#   ax.set_xticks([...])             -- где именно ставить метки по X
#   ax.set_xticklabels([...])        -- какими строками их подписать
#   ax.set_yticks([...]) / ax.set_yticklabels([...]) -- то же для Y

ax_demo = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax_demo.set_yticks([0.1, 0.6, 0.8])
ax_demo.set_yticklabels(['10%', '60%', '80%'])
plt.title("Теория: кастомные подписи меток оси Y")
plt.show()


# ЗАДАНИЕ
# --------

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
               "Oct", "Nov", "Dec"]
months_d = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

# 1. Сохранить оси текущего графика в переменную ax.
ax = plt.subplot()
plt.plot(months_d, conversion)

# 2. Установить x-метки в позициях, соответствующих месяцам.
ax.set_xticks(months_d)

# 3. Подписать x-метки названиями месяцев.
ax.set_xticklabels(month_names)

# 4. Подписать ось Y процентами вместо долей.
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])

plt.title("Задание: конверсия подписки Dinnersaur")
plt.show()



# plt.close('all')            -- закрыть все текущие фигуры (чтобы старые линии
#                                 случайно не остались на новом графике)
# plt.figure(figsize=(w, h))  -- создать новую фигуру заданного размера (в дюймах)
# plt.savefig('имя.png')      -- сохранить текущий график в файл (png/svg/pdf...)

plt.close('all')
plt.figure(figsize=(4, 10))
plt.plot([0, 1, 2, 3, 3.5], [0, 1, 4, 9, 12])
plt.title("Теория: высокая узкая фигура (figsize=(4, 10))")
plt.show()

# 1. Закрываем все графики перед началом (на случай забытых линий).
plt.close('all')
word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

# 2. Длина слов-победителей Scripps National Spelling Bee по годам.
plt.figure()
plt.plot(years, word_length)
plt.title("Длина слова-победителя Spelling Bee по годам")
plt.xlabel("Год")
plt.ylabel("Длина слова")
plt.savefig('win_word_lengths.png')
plt.show()

# 3. Мощность атомных станций США по годам — фигура 7x3 дюйма.
plt.figure(figsize=(7, 3))
plt.plot(years, power_generated)
plt.title("Выработка атомной энергии в США по годам")
plt.xlabel("Год")
plt.ylabel("Мощность")
plt.savefig('power_generated.png')
plt.show()


# --------
# 1. Списки x, y1, y2 (для примера — что-то в духе "псевдо-корреляций":
#    количество выпитого кофе (y1) и количество решённых задач (y2)
#    по неделям (x)).
x = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [3, 5, 4, 6, 8, 7, 9, 10]      # чашек кофе в неделю
y2 = [12, 18, 15, 20, 25, 23, 28, 30]  # решённых задач в неделю

plt.close('all')

# 2. График y1 от x.
plt.plot(x, y1)

# 3. На том же графике — y2 от x.
plt.plot(x, y2)
plt.show()

# 4. Розовая линия для y1, серая для y2, у обеих — круглые маркеры.
plt.plot(x, y1, color='pink', marker='o', label='Coffee cups per week')
plt.plot(x, y2, color='gray', marker='o', label='Problems solved per week')

# 5. Заголовок и подписи осей.
plt.title('Две линии на одном графике')
plt.xlabel('Великолепная ось X')
plt.ylabel('Потрясающая ось Y')

# 6. Легенда в правом нижнем углу (loc=4 -> 'lower right').
plt.legend(loc=4)

plt.show()

# 7. Дополнительно: те же данные в виде двух подграфиков рядом,
#    чтобы попрактиковаться с несколькими осями на одной фигуре.
plt.close('all')

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='pink', marker='o')
plt.title('Coffee cups')
plt.xlabel('Week')
plt.ylabel('Cups')

plt.subplot(1, 2, 2)
plt.plot(x, y2, color='gray', marker='o')
plt.title('Problems solved')
plt.xlabel('Week')
plt.ylabel('Problems')

plt.subplots_adjust(wspace=0.4)
plt.suptitle('Итоговое задание: два подграфика')
plt.show()