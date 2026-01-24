# CLASS : Class is a blueprint or templete
# OBJECT : Object is instance of a class

class Employee:
    company = "HP"

    def get_salary(self):   # Self is a way to reference the object of the class which is being created
        return 34000
    
e1 = Employee()    # object
print(e1.get_salary())
print(e1.company)

e2 = Employee()
print(e2.get_salary())
print(e2.company)