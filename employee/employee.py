import datetime


class Employee:
    numofemps = 0
    raiseamount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.numofemps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raiseamount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raiseamount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raiseamount = 1.08

    def __init__(self, first, last, pay, programminglang):
        super().__init__(first, last, pay)
        self.programminglang = programminglang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_1 = Employee('Raquel', 'Stevens', 50000)
emp_2 = Employee('Juilia', 'Michaels', 50000)
emp_1.fullname()
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.__dict__)
print(Employee.numofemps)
Employee.set_raise_amt(1.05)
print(Employee.raiseamount)
emp_str_1 = 'anita-roy-90000'
new_emp = Employee.from_string(emp_str_1)
print(new_emp.email)
print(new_emp.pay)
print(Employee.is_workday(datetime.date(2020, 1, 18)))
dev1 = Developer('dixita', 'd', 70000, 'python')
dev2 = Developer('dixit', 'd', 70000, 'python')
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print(dev1.programminglang)
manager = Manager('Sam', 'Smith', 90000, [dev1])
print(manager.email)
manager.add_employee(dev2)
manager.print_employees()

