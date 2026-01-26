class Employee:
    company = "Asus"
    
    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
        
    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name} And salary is {self.salary}. The bond is for {self.bond} years.")
    
e1 = Employee("34000", "Amit", 5, "Tesla")
print(e1.company)  # Will always print instance attribute
print(Employee.company)

# Object introspection
print(dir(e1))
