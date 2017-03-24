class Employee():
    raise_rate = 1.04
    emp_num = 0
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@company.com'
        self.emp_num += 1

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def raise_salary(self):
        self.salary = int(self.pay * self.raise_rate)

    def set_raise_rate(cls, amount):
        cls.raise_rate = amount

    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split('-')
        return cls(first_name, last_name, salary)
        
class Engineer(Employee):
    eng_num = 0
    
    def __init__(self, first_name, last_name, salary, field):
        Employee.__init__(self, first_name, last_name, salary)
        self.field = field
        self.eng_num += 1

    def show(self):
        print('Name: ' +str( self.full_name()))
        print('Field: ' + str(self.field))
        print('Salary: ' + str(self.salary))
        print('Engineers: ' + str(self.eng_num))

Bob = Engineer('Bobby', 'Bob', 500, 'dirt')

Bob.show()

