class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Person Name: {self.name}, Age: {self.age}")


class Employee(Person):
    # Method Overloading (Multiple ways to initialize)
    def __init__(self, name, age, employee_id=None, salary=0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id     # Encapsulated attribute
        self.__salary = salary               # Encapsulated attribute

    # Getter and Setter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id

    # Getter and Setter for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # Method Overriding: display()
    def display(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, "
              f"ID: {self.__employee_id}, Salary: ${self.__salary}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        print(f"Manager Name: {self.name}, Age: {self.age}, "
              f"ID: {self.get_employee_id()}, Salary: ${self.get_salary()}, "
              f"Department: {self.department}")
        
class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        print(f"Developer Name: {self.name}, Age: {self.age}, "
              f"ID: {self.get_employee_id()}, Salary: ${self.get_salary()}, "
              f"Language: {self.programming_language}")
        
def main():
    persons = []
    employees = []
    managers = []
    developers = []

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            person = Person(name, age)
            persons.append(person)
            print(f"Person created with name: {name} and age: {age}.")

        elif choice == '2':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            emp = Employee(name, age, emp_id, salary)
            employees.append(emp)
            print(f"Employee created with name: {name}, age: {age}, "
                  f"ID: {emp_id}, and salary: ${salary}.")

        elif choice == '3':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            manager = Manager(name, age, emp_id, salary, dept)
            managers.append(manager)
            print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, "
                  f"salary: ${salary}, and department: {dept}.")

        elif choice == '4':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            dev = Developer(name, age, emp_id, salary, lang)
            developers.append(dev)
            print(f"Developer created with name: {name}, age: {age}, ID: {emp_id}, "
                  f"salary: ${salary}, and language: {lang}.")

        elif choice == '5':
            print("\nChoose details to show:")
            print("1. Persons")
            print("2. Employees")
            print("3. Managers")
            print("4. Developers")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                if persons:
                    for p in persons:
                        p.display()
                else:
                    print("No Person records found.")
            elif sub_choice == '2':
                if employees:
                    for e in employees:
                        e.display()
                else:
                    print("No Employee records found.")
            elif sub_choice == '3':
                if managers:
                    for m in managers:
                        m.display()
                else:
                    print("No Manager records found.")
            elif sub_choice == '4':
                if developers:
                    for d in developers:
                        d.display()
                else:
                    print("No Developer records found.")
            else:
                print("Invalid option!")

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    # Check inheritance
    print("Is Manager a subclass of Employee?", issubclass(Manager, Employee))
    print("Is Developer a subclass of Employee?", issubclass(Developer, Employee))
    main()