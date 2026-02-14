correct_answers = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)
user_input = input("Введите 20 ответов через пробел: ")
user_answers = list(map(int, user_input.split()))
if tuple(user_answers) == correct_answers:
    print("Экзамен сдан")
else:
    print("Экзамен провален")