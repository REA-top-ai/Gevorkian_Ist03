# print((6 * 6 - 1) == (8 + 1))
# print((13 - 7) != ((3 * 2) + 1))
# print((3 * (2 - 1)) == (4 - 1))
#
# print((6 * 6 - 1) >= (8 + 1))
# print((13 - 7) <= ((3 * 2) + 1))
# print((3 * (2 - 1)) > (4 - 1))

# bool_variable = 'true'
# print(bool_variable)
# print(type(bool_variable))
# bool_variable_2 = True
# print(bool_variable_2)
# print(type(bool_variable_2))


# user_name = input('Введите имя пользователя')
# dmitry_check = ('Дмитрий, твое рабочее место находится в другой комнате.'
#                 'Отойди от чужого компьютера и займись работой!')
# success = 'Добро пожаловать'
# if user_name == 'Дмитрий':
#     print(dmitry_check)
# else:
#     print(success)

# enter_number = 0
# password = input('Введите пароль ')
# if (3 - enter_number) >= 1:
#         enter_number += 1
#         print('Неверный пароль. У вас осталось '+str(3-enter_number)+' попыток')
# password = input('Введите пароль ')
# if (3 - enter_number) >= 1:
#         enter_number += 1
#         print('Неверный пароль. У вас осталось '+str(3-enter_number)+' попыток')
# password = input('Введите пароль ')
# if (3 - enter_number) >= 1:
#         enter_number += 1
#         print('Неверный пароль. У вас осталось '+str(3-enter_number)+' попыток. '
#                         'Вы превысили максимальное число попыток ввода пароля.')

# statement_one = print((2 + 2 + 2 >= 6) and (-1 * -1 < 0))
# statement_two = print((4 * 2 <= 8) and (7 - 1 == 6))

# employees = {
#     "Дмитрий": 1,
#     "Ангелина": 2,
#     "Василий": 3,
#     "Екатерина": 4
# }
# username = input("Введите имя пользователя: ")
# arm = int(input("Введите номер АРМ: "))
# if username in employees and employees[username] == arm:
#     print("Добро пожаловать!")
# elif username != "Дмитрий":
#     print("Логин или пароль не верный, попробуйте еще раз")
# else:
#     print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
#
# statement_one = print((2 - 1 > 3) and (-5 * 2 == -10))
# statement_two = print((9 + 5 <= 15) and (7 != 4 + 3))

# grade = float(input("Введите средний балл студента: "))
# if grade >= 4.0:
#     print("A")
# elif grade >= 3.0:
#     print("B")
# elif grade >= 2.0:
#     print("C")
# elif grade >= 1.0:
#     print("D")
# elif grade >= 0.0:
#     print("F")
# else:
#     print("Ошибка: средний балл не может быть отрицательным")