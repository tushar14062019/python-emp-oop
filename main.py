# Main file

from abc import ABC, abstractmethod

class Emp(ABC):
    def __init__(self, Emp_id, name, Dept):
        self.Emp_id = Emp_id
        self.name = name
        self.Dept = Dept

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print(f"Emp ID: {self.Emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.Dept}")
        print(f"Total Salary: ${self.calculate_salary():,.2f}")
        print('---------------------------------------------------------')
        
class Permanent_Emp(Emp):
    def __init__(self, Emp_id, name, Dept, basic_salary, bonus):
        super().__init__(Emp_id, name, Dept)
        self.basic_salary = basic_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus

class Contract_Emp(Emp):
    def __init__(self, Emp_id, name, Dept, hourly_rate, hours_worked):
        super().__init__(Emp_id, name, Dept)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Intern(Emp):
    def __init__(self, Emp_id, name, Dept, stipend):
        super().__init__(Emp_id, name, Dept)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


A = Permanent_Emp("143", "Harshal Chavan", "IT-PROG", 80000, 7500)
A.display_details()

B = Contract_Emp("756", "Anuj Kadam", "Software Developer", 70, 160)
B.display_details()

C = Intern("1406", "Pooja Chavan", "BPO", 7500)
C.display_details()
