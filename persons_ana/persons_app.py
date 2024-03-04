# importing classes Person, Customer, Employee and InvalidSalaryException
from persons_ana.person import Person
from persons_ana.customer import Customer
from persons_ana.employee import Employee
from persons_ana.invalidSalaryException import InvalidSalaryException

# Instantiating Customer class
draco = Customer('Malfoy', 127, 'Borgin & Burkes')
order = draco.place_order('Cupboard', 100)
print(order)

# Instantiating Customer class
colin = Customer('Colin Creevy', 324, "Weasley's Wizard, Wheezes")
order1 = colin.place_order('Misc Practical Joke Objects', 50)
print(order1)

# calling Customer class method on its instance
draco.set_profession("Businessman")
info = draco.get_personal_info()
print(info)

# Instantiating Employee class
hermione = Employee('Hermione', 'Granger', 36, 'Ministry of Magic', '001',
                    'Minister of Magic', 60000, 'hg@mom.com', 'she')

# overriding method of Object class to print readable version of class
print(hermione)
# Calling getter
print(f"\nHermione's role at work: {hermione.get_role()}")

# creating another instance of Employee class
harry = Employee('Harry', 'Potter', 35, 'Ministry of Magic', '007',
                 'Auror', 50000, 'hp@mom.com', 'he')

# calling base class method on derived class instance
print(f"Harry's profession:\t{harry.get_profession()}")

# creating another instance of Employee class
ginny = Employee('Ginny', 'Weasley', 35, 'World Quiditch Association',
                 '002', 'VP', 50000, 'gw@wqa.com''she')

# calling calculate_bonus method of Employee class
print(f"Ginny's bonus:\tGalleon {ginny.calculate_bonus()}")

# creating another instance of Employee class
ron = Employee('Ronald', 'Weasley', 36, 'Weasley & Weasley', '003',
               'partner', 40000, 'ron@wandw.com', 'he')
try:
    ex_occurred = False
    # calling increment_salary method might throw exception if increment is negative
    # ron.increment_salary(-5000)
    ron.increment_salary(5000)
    print(f"\n{ron.name + ' ' + ron.surname}, your salary has been revised to: {ron.get_salary()}")
except InvalidSalaryException as ex:
    print(ex.get_message())
    ex_occurred = True
finally:  # this block is always executed
    if ex_occurred:  # noqa
        print("Error: Increment salary value has to be positive!")
    else:
        print("Congrats on your increment!")

# calling another method of Employee class on instance ron
new_role = ron.change_role('Auror', 50000, 'Ministry of Magic', '008')
print(new_role)
print(ron)

# Instantiating base class object
neville = Person('Neville', 35, 'he', 'Professor')
# base class method
print(f"\n{neville.get_personal_info()}")

# Instantiating Employee class
neville_emp = Employee('Neville', 'Longbottom', 35, 'Hogwarts', '700',
                       'Professor of Herbology', 50000, 'nlb@thehogwarts.com', 'he/his')
# overriding __str__ method of Object class to print Employee class instance
print(neville_emp)

# assigning Person class instance to Employee class and reprint same Employee class instance
neville_emp = neville
print(neville_emp)


