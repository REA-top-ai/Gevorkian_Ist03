tort = ["торт", 1]
print(tort)

household_chemicals = [
    ["стиральный порошок", 1],
    ["средство для мытья посуды", 1]
]
print(household_chemicals)

shopping_list = ['хлеб', 'яйца', 'молоко', 'кофе']
quantity = [1, 10, 1, 1]
names_and_dogs_names = zip(shopping_list, quantity)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

orders = ['маргаритки', 'васильки']
print(orders)

orders.append('тюльпаны')
orders.append('розы')
print(orders)

orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print(new_orders)

broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

list1 = list(range(9))
print(list1)

list2 = list(range(7))
print(list2)

list1 = list(range(5, 15, 3))
print(list1)

list2 = list(range(0, 40, 5))
print(list2)

first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = list(zip(first_names, all_ages))
ids = list(range(4))
