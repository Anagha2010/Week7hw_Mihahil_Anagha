# importing base class and the used exception class
from persons_ana.person import Person
from persons_ana.invalidSalaryException import InvalidSalaryException

# class definition
class Employee(Person):
    # class constructor
    def __init__(self, name, surname, age, company_name, emp_id, role, salary, email, pronoun='they'):
        # calling base class constructor
        super().__init__(name, age, pronoun, profession=role)
        # attributes
        self.surname = surname
        self.company_name = company_name
        self.emp_id = emp_id
        self.salary = salary
        self.role = role
        self.email = email

    # getters and setters
    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    # methods

    # Adds increment amount to the salary if positive otherwise raises exception
    def increment_salary(self, add_salary):
        if add_salary > 0:
            self.salary += add_salary
        else:
            raise InvalidSalaryException()

    # calculates bonus as 10% of yearly income
    def calculate_bonus(self):
        bonus = 0.10 * self.salary
        return bonus

    # method to update employee role and related info
    def change_role(self, new_role, new_salary, new_company, new_emp_id, new_email=''):
        self.role = new_role
        self.salary = new_salary
        self.company_name = new_company
        self.emp_id = new_emp_id
        self.email = new_email
        return f"{self.name} {self.surname} has changed role!"

    # overriding method from object class
    def __str__(self):
        return (
            f"\n{'*' * 30}\nEmployee ID: {self.emp_id}\nName: {self.name} {self.surname}\nRole: {self.role}\nSalary:"
            f" Galleon {self.salary}\n{'*' * 30}")
