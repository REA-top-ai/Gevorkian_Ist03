
import pandas as pd


# =============================================================
# 1. ВЫБОР НЕСКОЛЬКИХ СТРОК (.iloc со срезами)
# =============================================================
# orders.iloc[3:7]  -- строки с 3-й по 6-ю включительно (7-я не входит)
# orders.iloc[:4]   -- строки с 0-й по 3-ю включительно (4-я не входит)
# orders.iloc[-3:]  -- последние 3 строки

# Данные о посещениях четырёх клиник (те же, что и в предыдущих файлах)
df = pd.DataFrame([
    ['January', 100, 100, 23, 100],
    ['February', 51, 45, 145, 45],
    ['March', 81, 96, 65, 96],
    ['April', 80, 80, 54, 180],
    ['May', 51, 54, 54, 154],
    ['June', 112, 109, 79, 129]],
    columns=['month', 'clinic_east',
             'clinic_north', 'clinic_south',
             'clinic_west']
)

# --- данные за апрель, май, июнь (строки с 3 по 6) ---
april_may_june = df.iloc[3:6]
print("ЗАДАНИЕ (выбор нескольких строк): april_may_june =")
print(april_may_june, "\n")


# =============================================================
# 2. ВЫБОР СТРОКИ С ПОМОЩЬЮ ЛОГИКИ
# =============================================================
# df[df.MyColumnName == desired_value]
#
# Операторы сравнения:
#   ==   -- равно
#   >    -- больше
#   <    -- меньше
#   !=   -- не равно
#
# Примеры (df.age == 30, df.age > 30, df.age < 30,
#          df.name != 'Clara Oswald')

# --- Задание: строка, где месяц равен "January" ---
january = df[df.month == 'January']
print("ЗАДАНИЕ (логика ==): january =")
print(january, "\n")


# =============================================================
# 3. КОМБИНИРОВАНИЕ НЕСКОЛЬКИХ ЛОГИЧЕСКИХ ОПЕРАТОРОВ (| и &)
# =============================================================
# | означает "или", & означает "и". Каждое условие — в круглых скобках:
# df[(df.age < 30) | (df.name == 'Martha Jones')]

# --- Задание: данные за март ИЛИ апрель ---
march_april = df[(df.month == 'March') | (df.month == 'April')]
print("ЗАДАНИЕ (логика |): march_april =")
print(march_april, "\n")


# =============================================================
# 4. ОТБОР ПО СПИСКУ ЗНАЧЕНИЙ — .isin()
# =============================================================
# df[df.name.isin(['Martha Jones', 'Rose Tyler', 'Amy Pond'])]
# Проверяет, что значение столбца входит в переданный список.

# --- Задание: данные за январь, февраль ИЛИ март (через isin) ---
january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print("ЗАДАНИЕ (isin): january_february_march =")
print(january_february_march, "\n")


# =============================================================
# 5. ОБНОВЛЕНИЕ ИНДЕКСОВ — .reset_index()
# =============================================================
# После выбора подмножества строк индексы становятся "рваными"
# (непоследовательными), что неудобно для .iloc().
# .reset_index()              -> новый DataFrame, старый индекс становится
#                                 обычным столбцом "index"
# .reset_index(drop=True)     -> старый индекс просто отбрасывается
# .reset_index(inplace=True)  -> изменяет df2 "на месте", возвращает None

# df2 — подмножество строк df (индексы 1, 3, 5 -> будут "рваными")
df2 = df.loc[[1, 3, 5]]
print("ЗАДАНИЕ 1 (reset_index): df2 (с рваными индексами) =")
print(df2, "\n")

# Задание 2: создать df3, сбросив индексы df2 (без inplace и drop)
df3 = df2.reset_index()
print("ЗАДАНИЕ 2: df3 = df2.reset_index() =")
print(df3)
print("df2 после этой команды (не изменился, т.к. inplace не использовался):")
print(df2, "\n")

# Задание 3: сбросить индексы df2 с inplace=True и drop=True
df2.reset_index(inplace=True, drop=True)
print("ЗАДАНИЕ 3: df2 после reset_index(inplace=True, drop=True) =")
print(df2)
print("Пояснение: теперь df2 изменился 'на месте' (новые индексы 0,1,2,")
print("без лишнего столбца 'index'). В отличие от df3, у df2 нет столбца")
print("'index' со старыми значениями — drop=True его отбросил.\n")


# =============================================================
# 6. ЗАКЛЮЧЕНИЕ — итоговое задание: аналитик ShoeFly.com
# =============================================================


orders = pd.DataFrame({
    'id': [54791, 53450, 91987, 14437, 79357, 52386, 20487, 76971, 21586, 62083],
    'first_name': ['Rebecca', 'Emily', 'Joyce', 'Justin', 'Andrew',
                    'Julie', 'Thomas', 'Janice', 'Gabriel', 'Frances'],
    'last_name': ['Lindsay', 'Joyce', 'Waller', 'Erickson', 'Banks',
                   'Marsh', 'Jensen', 'Hicks', 'Porter', 'Palmer'],
    'email': ['RebeccaLindsay57@hotmail.com', 'EmilyJoyce25@gmail.com',
              'Joyce.Waller@gmail.com', 'Justin.Erickson@outlook.com',
              'AB4318@gmail.com', 'JulieMarsh59@gmail.com',
              'TJ5470@gmail.com', 'Janice.Hicks@gmail.com',
              'GabrielPorter24@gmail.com', 'FrancesPalmer50@gmail.com'],
    'shoe_type': ['clogs', 'ballet flats', 'sandals', 'clogs', 'boots',
                   'sandals', 'clogs', 'clogs', 'clogs', 'wedges'],
    'shoe_material': ['faux-leather', 'faux-leather', 'fabric', 'faux-leather',
                        'leather', 'fabric', 'fabric', 'faux-leather',
                        'leather', 'leather'],
    'shoe_color': ['black', 'navy', 'black', 'red', 'brown',
                    'black', 'navy', 'navy', 'brown', 'black']
})


print("orders.head() =")
print(orders.head(), "\n")

emails = orders['email']
print("emails =")
print(emails, "\n")
frances_palmer = orders[(orders.first_name == 'Frances') &
                          (orders.last_name == 'Palmer')]
print("frances_palmer =")
print(frances_palmer, "\n")
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
print("comfy_shoes =")
print(comfy_shoes)