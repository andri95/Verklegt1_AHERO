

class Employee:

    rais_amount = 1.04 
    num_of_employ = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'
        Employee.num_of_employ += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.rais_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.rais_amount = amount


        




emp_1 = Employee('Halldór', 'Holgersson', 420)
emp_2 = Employee('Hjördís', 'Steinarsdóttir', 30000)

Employee.set_raise_amt(1.05)  #  class methood skil ekki alveg .....

print(emp_1.email)
print(emp_2.email)

print('-'*10)

print(emp_1.fullName())

print('-'*10)

#print(Employee.__dict__)
emp_1.rais_amount = 1.05
print(emp_1.__dict__)

print(Employee.rais_amount)  #  prentar hvað raisamount er.
print(emp_1.rais_amount)
print(emp_2.rais_amount)


print('-'*10)

print(Employee.num_of_employ)  # number of employeeet


print('-'*10)








