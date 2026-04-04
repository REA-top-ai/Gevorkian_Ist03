#1
class Employee:
    new_id = 1
    def __init__(self):
        self.self_id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print(f'My id is {self.self_id}')


e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()

#2
class Admin(Employee):
    pass

e3 = Admin()
e3.say_id()

#3
class Admin(Employee):
    def say_id(self):
        print('I am an Admin')


e3 = Admin()
e3.say_id()

#4
class Admin(Employee):
    def say_id(self):
        print('I am an Admin')
        super().say_id()

e3 = Admin()
e3.say_id()

#5
class Manager(Admin):
    def say_id(self):
        print('I am responsible')
        super().say_id()


e4 = Manager()
e4.say_id()

#6
class Employee:
    new_id = 1
    def __init__(self):
        self.self_id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print(f'My id is {self.self_id}')


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"Username: {self.username}, Role: {self.role}")


class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.self_id, 'Admin')

    def say_id(self):
        print('I am an Admin')
        super().say_id()


e3 = Admin()
e3.say_id()
e3.say_user_info()

#7
class Employee:
    new_id = 1
    def __init__(self):
        self.self_id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print(f'My id is {self.self_id}')


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"Username: {self.username}, Role: {self.role}")


class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.self_id, 'Admin')

    def say_id(self):
        print('I am an Admin')
        super().say_id()


class Manager(Admin):
    def say_id(self):
        print('I am responsible')
        super().say_id()


e = Employee()
a = Admin()
m = Manager()

meeting = [e, a, m]
for o in meeting:
    o.say_id()
    print()

#8
class Employee:
    new_id = 1
    def __init__(self):
        self.self_id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print(f'My id is {self.self_id}')


class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, new_chel):
        self.attendees.append(new_chel)

    def __len__(self):
        return len(self.attendees)

m1 = Meeting()
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

#9
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.self_id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


class Employee(AbstractEmployee):
    def say_id(self):
        print(f"My id is {self.self_id}")


e1 = Employee()
e1.say_id()

#10
class Employee:
    new_id = 1
    def __init__(self):
        self.self_id = Employee.new_id
        Employee.new_id += 1
        Employee.__id1 = 6
    _id = 5
    def say_id(self):
        print(f'My id is {self.self_id}')

e1 = Employee()
print(dir(e1))

#11
class Employee:
    new_id = 1
    def __init__(self):
        self.self_id = Employee.new_id
        Employee.new_id += 1
        self._name = None

    def say_id(self):
        print(f'My id is {self.self_id}')

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise TypeError

    def del_name(self):
        print("_name Deleted")
        del self._name

a = Employee()
print(a.get_name())

a.set_name('arsen')
print(a.get_name())

a.del_name()
print(a.get_name())