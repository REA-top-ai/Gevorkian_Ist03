#1
class Facade:
    pass
facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

#2
class Grade:
    minimum_passing = 65
a = Grade()
print(a.minimum_passing)

#3
class Rules:
    def washing_brushes(self):
        return 'Point bristles towards the basin while washing your brushes.'
a = Rules()
print(a.washing_brushes())

#4
class Circle:
    pi = 3.1415
    def area(self, radius):
        area = self.pi * radius ** 2
        return area
a = Circle()
print(a.area(2))

#5
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print(f'New circle with diameter: {diameter}')
teaching_table = Circle(36)

#6
class Circle:
    pi = 3.1415
    def __init__(self, diameter):
        self.radius = diameter / 2

    def circumference(self):
        circumference = 2 * self.pi * self.radius
        return circumference
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11_460)
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#7
print(dir(5))
def this_function_is_an_object():
    pass
print(dir(this_function_is_an_object()))

#8
class Circle:
    pi = 3.1415
    def __init__(self, diameter):
        self.radius = diameter / 2
    def __repr__(self):
        return f'Circle with radius {self.radius}'
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11_460)
print(medium_pizza)
print(teaching_table)
print(round_room)