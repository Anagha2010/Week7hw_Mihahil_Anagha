from persons.person import Person
from persons.invalidSalaryException import InvalidSalaryException

class Employee(Person):

    def __init__(self, name, surname, age, company_name, emp_id, role, salary, pronoun='they'):
        super().__init__(name, age, pronoun, profession=role)
        self.surname = surname
        self.company_name = company_name
        self.emp_id = emp_id
        self.salary = salary
        self.role = role

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def increment_salary(self, add_salary):
        if add_salary > 0:
            self.salary += add_salary
        else:
            raise InvalidSalaryException()

    def calculate_bonus(self):
        bonus = 0.10 * self.salary
        return bonus

    def change_role(self, new_role, new_salary, new_company, new_emp_id):
        self.role = new_role
        self.salary = new_salary
        self.company_name = new_company
        self.emp_id = new_emp_id
        return f"{self.name} {self.surname} has changed role!"

    def __str__(self):
        return (
            f"\n{'*' * 30}\nEmployee ID: {self.emp_id}\nName: {self.name} {self.surname}\nRole: {self.role}\nSalary:"
            f" Galleon {self.salary}\n{'*' * 30}")
