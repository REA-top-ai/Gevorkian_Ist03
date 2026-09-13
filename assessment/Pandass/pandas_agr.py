
import numpy as np
import pandas as pd


# 1. Расчёт статистики столбца (агрегатные функции)
# -------------------------------------------------------------
# Агрегатные функции сводят множество значений столбца к одному числу.
# Общий синтаксис:  df.column_name.command()
#
# Основные команды:
#   mean     — среднее значение
#   std      — стандартное отклонение
#   median   — медиана
#   max      — максимум
#   min      — минимум
#   count    — количество значений
#   nunique  — количество УНИКАЛЬНЫХ значений
#   unique   — список уникальных значений

customers = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'age': [23, 25, 31, 35, 35, 46, 62]
})
print("customers.age =", list(customers.age))
print("customers.age.median() =", customers.age.median(), "\n")

shipments = pd.DataFrame({
    'state': ['CA', 'CA', 'CA', 'CA', 'NY', 'NY', 'NJ', 'NJ',
              'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
})
print("shipments.state.nunique() =", shipments.state.nunique(), "\n")

inventory = pd.DataFrame({
    'color': ['blue', 'blue', 'blue', 'blue', 'blue',
              'green', 'green', 'orange', 'orange', 'orange']
})
print("inventory.color.unique() =", inventory.color.unique(), "\n")


# -------------------------------------------------------------
# 2. Вычисление агрегатных функций I — groupby
# -------------------------------------------------------------
# df.groupby('column1').column2.measurement()
#   column1     — столбец, по которому группируем
#   column2     — столбец, к которому применяем измерение
#   measurement — сама агрегатная функция (mean, max, count и т.д.)
#
# Результат groupby без .reset_index() — это Series (не DataFrame).

grades_df = pd.DataFrame({
    'student': ['Amy', 'Amy', 'Bob', 'Bob'],
    'assignment_name': ['Assignment 1', 'Assignment 2',
                         'Assignment 1', 'Assignment 2'],
    'grade': [75, 35, 99, 35]
})
grades = grades_df.groupby('student').grade.mean()
print("Пример groupby (средняя оценка по студентам):")
print(grades, "\n")


# -------------------------------------------------------------
# 3. Вычисление агрегатных функций II — reset_index() и rename()
# -------------------------------------------------------------
# groupby создаёт Series, где "индексами" стали значения column1.
# .reset_index() превращает эту Series в DataFrame, а индекс -
# в обычный столбец.
#
# Пример (чай):

teas = pd.DataFrame({
    'id': [0, 1, 2, 3, 4, 5],
    'tea': ['earl grey', 'english breakfast', 'irish breakfast',
            'jasmine', 'matcha', 'camomile'],
    'category': ['black', 'black', 'black', 'green', 'green', 'herbal'],
    'caffeine': [38, 41, 37, 23, 48, 0],
    'price': [3, 3, 2.5, 4.5, 5, 3]
})

teas_counts = teas.groupby('category').id.count().reset_index()
print("teas_counts (до переименования столбца):")
print(teas_counts)

# После groupby столбец называется id (по имени столбца, который считали),
# но по смыслу это "количество". Переименуем его:
teas_counts = teas_counts.rename(columns={"id": "counts"})
print("teas_counts (после rename):")
print(teas_counts, "\n")


# -------------------------------------------------------------
# 4. Вычисление агрегатных функций III — apply() + лямбда, percentile
# -------------------------------------------------------------
# Для более сложных вычислений (например, процентилей) используем
# .apply() с лямбда-функцией. Входные данные лямбды — список значений
# группы.

employees = pd.DataFrame({
    'id': [10131, 14189, 15004, 11204],
    'name': ['Sarah Carney', 'Heather Carey', 'Gary Mercado', 'Cora Copaz'],
    'wage': [39, 17, 33, 27],
    'category': ['product', 'design', 'marketing', 'design']
})

high_earners = (
    employees.groupby('category').wage
    .apply(lambda x: np.percentile(x, 75))
    .reset_index()
)
print("high_earners (75-й процентиль зарплаты по категориям):")
print(high_earners, "\n")


# -------------------------------------------------------------
# 5. Вычисление агрегатных функций IV — группировка по нескольким столбцам
# -------------------------------------------------------------
# Передаём список имён столбцов в groupby(), чтобы сгруппировать сразу
# по нескольким признакам.

sales = pd.DataFrame({
    'Location': ['West Village', 'West Village', 'Chelsea', 'Chelsea'],
    'Date': ['February 1', 'February 2', 'February 1', 'February 2'],
    'Day of Week': ['W', 'Th', 'W', 'Th'],
    'Total Sales': [400, 450, 375, 390]
})

sales_by_loc_day = (
    sales.groupby(['Location', 'Day of Week'])['Total Sales']
    .mean()
    .reset_index()
)
print("sales_by_loc_day (средние продажи по месту и дню недели):")
print(sales_by_loc_day, "\n")


# =============================================================
# ЧАСТЬ 2. РЕШЕНИЯ ЗАДАНИЙ (данные ShoeFly.com)
# =============================================================

# Настоящего файла orders.csv нет, поэтому создаём демонстрационный
# DataFrame с такой же структурой, чтобы весь код ниже можно было
# запустить и увидеть реальный результат.


orders = pd.DataFrame({
    'id': [54791, 53450, 91987, 14437, 79357, 52386,
           20487, 76971, 21586, 62083, 45832, 33221],
    'shoe_type': ['clogs', 'ballet flats', 'sandals', 'clogs', 'boots',
                   'sandals', 'clogs', 'clogs', 'clogs', 'wedges',
                   'ballet flats', 'boots'],
    'shoe_color': ['black', 'navy', 'black', 'red', 'brown', 'black',
                    'navy', 'navy', 'brown', 'red', 'white', 'brown'],
    'price': [55, 42, 38, 60, 89, 40, 58, 62, 65, 75, 45, 95]
})

# 1. Изучить первые 10 строк.
print(orders.head(10), "\n")

# 2. Цена самой дорогой пары обуви.
most_exurance = orders.price.max()
print("most_exurance (самая дорогая пара) =", most_exurance)

# 3. Сколько разных цветов обуви продаём.
num_colors = orders.shoe_color.nunique()
print("num_colors (кол-во разных цветов) =", num_colors, "\n")


# Самая дорогая обувь для каждого типа обуви (shoe_type).
# Сразу с reset_index(), чтобы результат был DataFrame (а не Series).
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print("pricey_shoes =")
print(pricey_shoes)
print("type(pricey_shoes) ->", type(pricey_shoes))
print("Пояснение: без reset_index() результат groupby — это Series,")
print("где индексом являются значения shoe_type. После reset_index()")
print("это уже полноценный DataFrame с shoe_type как обычным столбцом.\n")


# 25-й процентиль цены для каждого цвета обуви (shoe_color).
cheap_shoes = (
    orders.groupby('shoe_color').price
    .apply(lambda x: np.percentile(x, 25))
    .reset_index()
)
print("cheap_shoes =")
print(cheap_shoes, "\n")

# Количество заказов для каждой комбинации shoe_type + shoe_color.
# Столбец, по которому считаем (count), не важен — берём id.
shoe_counts = (
    orders.groupby(['shoe_type', 'shoe_color']).id
    .count()
    .reset_index()
)
# По желанию можно сразу переименовать итоговый столбец в "count":
shoe_counts = shoe_counts.rename(columns={'id': 'count'})
print("shoe_counts =")
print(shoe_counts)




#============================================================
# inventory = pd.DataFrame({
#     'color': ['blue', 'blue', 'blue', 'blue', 'blue',
#               'green', 'green', 'orange', 'orange', 'orange']
# })

# print(inventory.color.unique())
# # ['blue' 'green' 'orange']   <- сам список уникальных цветов (3 штуки)

# print(inventory.color.nunique())
# # 3   <- просто количество уникальных цветов
#============================================================