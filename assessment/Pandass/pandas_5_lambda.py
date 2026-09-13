import pandas as pd
# Лямбда-функция — способ определить функцию в одну строку.
# Синтаксис: lambda аргумент(ы): выражение

mylambda_demo = lambda x: (x * 2) + 3
print("mylambda_demo(5) =", mylambda_demo(5), "\n")  # 13

# Лямбды работают с любыми типами данных, не только с числами:
stringlambda = lambda x: x.lower()
print('stringlambda("Oh Hi Mark!") =', stringlambda("Oh Hi Mark!"), "\n")


# -------------------------------------------------------------
# 2. Лямбда-функции с оператором if
# -------------------------------------------------------------
# Обычная функция с if/else:
def myfunction_regular(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x

# То же самое в виде лямбды:
# lambda x: [РЕЗУЛЬТАТ ЕСЛИ ИСТИНА] if [УСЛОВИЕ] else [РЕЗУЛЬТАТ ЕСЛИ ЛОЖЬ]
myfunction_lambda = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x

print("myfunction_lambda(35) =", myfunction_lambda(35))  # 35 (не больше 40)
print("myfunction_lambda(43) =", myfunction_lambda(43), "\n")  # 44.5


# -------------------------------------------------------------
# 3. Применение лямбда-функции к столбцу DataFrame (.apply)
# -------------------------------------------------------------
# .apply() применяет функцию к каждому значению столбца.

df_emails = pd.DataFrame({
    'Name': ['JOHN SMITH', 'Jane Doe', 'joe schmo'],
    'Email': ['john.smith@gmail.com', 'jdoe@yahoo.com', 'joeschmo@hotmail.com']
})

df_emails['Email Provider'] = df_emails.Email.apply(
    lambda x: x.split('@')[-1]
)
print("df_emails (с добавленным Email Provider):")
print(df_emails, "\n")


# -------------------------------------------------------------
# 4. Применение лямбды к строке целиком (axis=1)
# -------------------------------------------------------------
# Если не указывать конкретный столбец, а вызвать .apply() прямо на df
# с аргументом axis=1, в лямбду будет передаваться ЦЕЛАЯ строка.
# Доступ к значениям — через row['имя_столбца'] или row.имя_столбца.

df_shopping = pd.DataFrame({
    'Item': ['Apple', 'Milk', 'Paper Towels', 'Light Bulbs'],
    'Price': [1.00, 4.20, 5.00, 3.75],
    'Is taxed?': ['No', 'No', 'Yes', 'Yes']
})

df_shopping['Price with Tax'] = df_shopping.apply(
    lambda row: row['Price'] * 1.075
    if row['Is taxed?'] == 'Yes'
    else row['Price'],
    axis=1
)
print("df_shopping (с добавленной ценой с налогом):")
print(df_shopping, "\n")


# Лямбда, которая возвращает первую и последнюю буквы строки
# (строка должна быть длиной не менее 2 символов).
mylambda = lambda x: x[0] + x[-1]

print("mylambda('This is a string') =", mylambda('This is a string'), "\n")
# 'Tg'

# Лямбда, которая проверяет возраст пользователя.
mylambda_age = lambda age: (
    "Добро пожаловать в BattleCity!" if age >= 13
    else "Вам должно быть больше 13 лет"
)

print("mylambda_age(15) =", mylambda_age(15))
print("mylambda_age(10) =", mylambda_age(10), "\n")

# 1. Лямбда, которая из полного имени "Имя Фамилия" достаёт только фамилию.
get_last_name = lambda name: name.split(' ')[-1]

print("get_last_name('John Smith') =", get_last_name('John Smith'))

# 2. Демонстрационный DataFrame сотрудников (name, hourly_wage, hours_worked),
#    как описано в задании.
df_employees = pd.DataFrame({
    'name': ['Sarah Carney', 'Heather Carey', 'Gary Mercado', 'Cora Copaz'],
    'hourly_wage': [10, 12, 15, 9],
    'hours_worked': [43, 38, 40, 47]
})

# Применяем get_last_name к столбцу name, чтобы получить new-столбец last_name.
df_employees['last_name'] = df_employees.name.apply(get_last_name)

print("\ndf_employees (с добавленным last_name):")
print(df_employees, "\n")

# 1. Лямбда total_earned: считает заработок с учётом сверхурочных
#    (после 40 часов — оплата в 1.5 раза больше).
total_earned = lambda row: (
    row['hourly_wage'] * 40
    + row['hourly_wage'] * 1.5 * (row['hours_worked'] - 40)
    if row['hours_worked'] > 40
    else row['hourly_wage'] * row['hours_worked']
)

# Проверка на примере из задания: 43 часа по 10$ -> 445
example_row = pd.Series({'hourly_wage': 10, 'hours_worked': 43})
print("Проверка примера (43 часа, 10$/час) ->", total_earned(example_row))

# 2. Применяем total_earned к каждой строке df_employees (axis=1),
#    чтобы добавить столбец total_earned.
df_employees['total_earned'] = df_employees.apply(total_earned, axis=1)

print("\ndf_employees (с добавленным total_earned):")
print(df_employees)