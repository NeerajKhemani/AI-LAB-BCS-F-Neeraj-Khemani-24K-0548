#Task 2: Employee Payroll System
#Design an Employee Payroll System using inheritance.
#Requirements:
#1. Base class Employee (name, emp_id)
#2. Child classes:
#- FullTimeEmployee (monthly_salary)
#- PartTimeEmployee (hours_worked, hourly_rate)
#3. Override calculate_salary() method
#4. Create objects and display salary


# Neeraj Khemani 24K-0548
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        pass  

    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        salary = self.monthly_salary
        print("Salary:", salary)

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        salary = self.hours_worked * self.hourly_rate
        print("Salary:", salary)


emp1 = FullTimeEmployee("Kamran Akmal", 100, 80000)
emp2 = PartTimeEmployee("Umar Akmal", 101, 100, 500)

emp1.display()
emp1.calculate_salary()
print("\n")

emp2.display()
emp2.calculate_salary()
