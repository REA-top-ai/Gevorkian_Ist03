# def f_to_c(f_temp):
#     return round((f_temp - 32) * 5 / 9)
# f100_in_celsius = f_to_c(100)
# print("100°F =", f100_in_celsius, "°C")
# def c_to_f(c_temp):
#     return round(c_temp * (9 / 5) + 32)
# c0_in_fahrenheit = c_to_f(0)
# print("0°C =", c0_in_fahrenheit, "°F")
#
#
# def get_force(mass, acceleration):
#     return mass * acceleration
# train_mass = 22680
# train_acceleration = 10
# train_force = get_force(train_mass, train_acceleration)
# print("Сила поезда:", train_force, "Н")
# print(f"Поезд GE поставляет {train_force} ньютонов силы")
#
#
# def get_energy(mass, c=3 * 10 ** 8):
#     return mass * c ** 2
# bomb_energy = get_energy(1)
# print(f"1 кг бомбы составляет {bomb_energy} Джоулей")
#
#
# def get_work(mass, acceleration, distance):
#     force = get_force(mass, acceleration)
#     return force * distance
# train_distance = 100
# train_work = get_work(train_mass, train_acceleration, train_distance)
# print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров.")
#
#
# def show_wardrobe(clothes):
#     print("У меня большой гардероб")
#     for time in ["утром", "днем", "вечером", "ночью"]:
#         print(f"{time.capitalize()} лучше всего подходит {clothes}")
#
# def show_meal_preferences(meal):
#     print("Мои предпочтения в еде")
#     for time in ["завтрак", "обед", "ужин"]:
#         print(f"{time.capitalize()}: {meal}")
# clothes = "домашняя одежда"
# meal = "здоровый обед"
# show_wardrobe(clothes)
# print()
# show_meal_preferences(meal)
#
#
# def check_access(user_name, arm=None):
#     employees = {
#         "Дмитрий": 1,
#         "Ангелина": 2,
#         "Василий": 3,
#         "Екатерина": 4
#     }
#     if arm is None:
#         if user_name == "Дмитрий":
#             return "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
#         else:
#             return "Добро пожаловать"
#     else:
#         if user_name in employees:
#             if employees[user_name] == arm:
#                 return "Добро пожаловать!"
#             elif user_name == "Дмитрий":
#                 return "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
#             else:
#                 return "Логин или пароль не верный, попробуйте еще раз"
#         else:
#             return "Пользователь не найден"


def get_grade(grade):
    if grade >= 4.0:
        return "A"
    elif grade >= 3.0:
        return "B"
    elif grade >= 2.0:
        return "C"
    elif grade >= 1.0:
        return "D"
    elif grade >= 0.0:
        return "F"
    else:
        return "Ошибка: неверный балл"
grades_to_check = [4.5, 3.8, 2.5, 1.2, 0.7, -1.0]
for g in grades_to_check:
    print(f"Балл {g}: грейд {get_grade(g)}")