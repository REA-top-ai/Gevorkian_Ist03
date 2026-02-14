import datetime
from matplotlib import pyplot as plt
import random
current_time = datetime.datetime.now()
print(current_time)


random_list = [random.randint(1, 100) for i in range(101)]
random_number = random.choice(random_list)

number_a = range(1, 13)
number_b = random.sample(range(1000), 12)
plt.plot(number_a, number_b)
plt.show()

employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]

def calculate_programmer_bonus(emp):
    if "программист" in emp[1].lower():
        return emp[3] * 0.03
    return 0

def calculate_indexation(emp):
    hire_date = datetime.datetime.strptime(emp[2], "%d.%m.%Y")
    years_worked = (datetime.datetime.now() - hire_date).days / 365.25
    if years_worked > 10:
        return emp[3] * 0.07
    else:
        return emp[3] * 0.05

def more_than_6_months(emp):
    hire_date = datetime.datetime.strptime(emp[2], "%d.%m.%Y")
    months_worked = (datetime.datetime.now() - hire_date).days / 30.44
    return months_worked > 6

vacation_candidates = [emp[0] for emp in employees if more_than_6_months(emp)]

def lottery():
    admin_number = random.randint(1, 9)
    print(f"Загаданное число администрации: {admin_number}")
    user_numbers = []
    count = 0
    for num in range(1000):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum % admin_number == 0:
            print(num)
            count += 1
            if count == 5:
                break

def coin_flip():
    attempts = int(input("Введите количество попыток: "))
    for i in range(attempts):
        result = random.choice(["Орел", "Решка"])
        print(result)

def dice_roll():
    attempts = int(input("Введите количество попыток: "))
    for i in range(attempts):
        result = random.randint(1, 6)
        print(result)

def password_generator():
    length = int(input("Введите длину пароля: "))
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        password = "".join(random.choice(symbols))
    print(password)