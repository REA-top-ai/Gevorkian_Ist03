from matplotlib import pyplot as plt

x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
plt.plot(x_values, y_values)
plt.show()


# 1. Базовый линейный график
# -------------------------------------------------------------
# plt.plot(x_values, y_values) создаёт линейный график.
# plt.show() отображает его на экране.


# -------------------------------------------------------------
# 2. Несколько линий на одном графике
# -------------------------------------------------------------
# Если вызвать plt.plot() несколько раз до plt.show(),
# все линии окажутся на одних и тех же осях.
# По умолчанию первая линия синяя, вторая — оранжевая, и т.д.

days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]

plt.plot(days, money_spent)         # ваши расходы
plt.plot(days, money_spent_2)       # расходы друга
plt.title("Теория 2: две линии на одном графике")
plt.show()


# -------------------------------------------------------------
# 3. Linestyles: цвет, стиль линии, маркеры
# -------------------------------------------------------------
# color     — цвет (имя HTML-цвета или HEX-код, например '#AAAAAA')
# linestyle — '--' пунктир, ':' точки, '' без линии
# marker    — 'o' круг, 's' квадрат, '*' звезда

plt.plot(days, money_spent, color='green', linestyle='--')
plt.plot(days, money_spent_2, color='#AAAAAA', marker='o')
plt.title("Теория 3: цвет, стиль линии и маркеры")
plt.show()


# -------------------------------------------------------------
# 4. Оси и метки — plt.axis()
# -------------------------------------------------------------
# plt.axis([xmin, xmax, ymin, ymax]) задаёт видимый диапазон осей.

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.axis([0, 3, 2, 5])
plt.show()


# -------------------------------------------------------------
# 5. Подписи осей и заголовок
# -------------------------------------------------------------
# plt.xlabel(), plt.ylabel(), plt.title() — все принимают строку.

hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
happiness = [9.8, 9.9, 9.2, 8.6, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]
plt.plot(hours, happiness)
plt.xlabel('Time of day')
plt.ylabel('Happiness Rating (out of 10)')
plt.title('My Self-Reported Happiness While Awake')
plt.show()


# -------------------------------------------------------------
# 6. Subplots — несколько графиков на одном рисунке
# -------------------------------------------------------------
# plt.subplot(кол-во строк, кол-во столбцов, индекс подграфика)
# Индекс отсчитывается с 1, слева направо, сверху вниз.
# Любой plt.plot() после plt.subplot() рисуется именно в этом подграфике.

x_sub = [1, 2, 3, 4]
y_sub = [1, 2, 3, 4]

plt.subplot(1, 2, 1)
plt.plot(x_sub, y_sub, color='green')
plt.title('First Subplot')

plt.subplot(1, 2, 2)
plt.plot(x_sub, y_sub, color='steelblue')
plt.title('Second Subplot')

plt.show()



# 1. Списки days и money_spent.
days_task = [0, 1, 2, 3, 4, 5, 6]
money_spent_task = [10, 12, 12, 10, 14, 22, 24]

# 2-3. Построить и показать график.
plt.plot(days_task, money_spent_task)
plt.show()

time = list(range(8))                       # 0..7 (например, месяцы)
income = [1000, 1100, 1200, 1150, 1300, 1400, 1450, 1500]
costs = [800, 850, 900, 950, 1000, 1000, 1050, 1100]

# 1. График дохода от времени.
plt.plot(time, income)
# 2. График затрат от времени на том же поле.
plt.plot(time, costs)
# 3. Показать график.
plt.title("Задание 2: доход и затраты во времени")
plt.show()


# 1. Доход — фиолетовая ('purple') пунктирная ('--') линия.
plt.plot(time, income, color='purple', linestyle='--')
# 2. Затраты — линия цвета #82edc9 с квадратными маркерами ('s').
plt.plot(time, costs, color='#82edc9', marker='s')
plt.title("Задание 3: стилизованные линии дохода и затрат")
plt.show()


# 1.  исходный график.
x_coffee = list(range(12))
y_coffee = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x_coffee, y_coffee)
plt.title("Задание 4а: расходы на кофе (исходный масштаб)")
plt.show()

# 2. Увеличить масштаб: x от 0 до 12, y от 2900 до 3100.
plt.plot(x_coffee, y_coffee)
plt.axis([0, 12, 2900, 3100])
plt.title("Задание 4б: расходы на кофе (увеличенный масштаб)")
plt.show()

plt.plot(x_coffee, y_coffee)
plt.xlabel('Время')
plt.ylabel('Доллары, потраченные на кофе')
plt.title('Мои последние двенадцать лет употребления кофе')
plt.show()

months = list(range(12))
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

# 1. Слева: температура от месяцев (фигура из 1 строки и 2 столбцов).
plt.subplot(1, 2, 1)
plt.plot(months, temperature)
plt.title('Temperature by month')
plt.xlabel('Month')
plt.ylabel('Temperature')

# 2. Справа: рейсы на Гавайи от температуры — точечная диаграмма ('o').
plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii, 'o')
plt.title('Flights to Hawaii vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Flights to Hawaii')

# 3. Показать оба подграфика.
plt.show()