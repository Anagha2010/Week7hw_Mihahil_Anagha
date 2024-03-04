from persons.person import Person
from persons.customer import Customer
from persons.employee import Employee
from persons.invalidSalaryException import InvalidSalaryException

draco = Customer('Malfoy', 127, 'Borgin & Burkes')
order = draco.place_order('Cupboard', 100)
print(order)

colin = Customer('Colin Creevy', 324, "Weasley's Wizard, Wheezes")
order1 = colin.place_order('Misc Practical Joke Objects', 50)
print(order1)

draco.set_profession("Businessman")
info = draco.get_personal_info()
print(info)

hermione = Employee('Hermione', 'Granger', 36, 'Ministry of Magic', '001',
                    'Minister of Magic', 60000, 'she')
print(hermione)
print(f"\nHermione's role at work: {hermione.get_role()}")

harry = Employee('Harry', 'Potter', 35, 'Ministry of Magic', '007',
                 'Auror', 50000, 'he')
print(f"Harry's profession:\t{harry.get_profession()}")

ginny = Employee('Ginny', 'Weasley', 35, 'World Quiditch Association',
                 '002', 'VP', 50000, 'she')
print(f"Ginny's bonus:\tGalleon {ginny.calculate_bonus()}")

ron = Employee('Ronald', 'Weasley', 36, 'Weasley & Weasley', '003',
               'partner', 40000, 'he')
try:
    ex_occurred = False
    # ron.increment_salary(-5000)
    ron.increment_salary(5000)
    print(f"\n{ron.name+' '+ron.surname}, your salary has been revised to: {ron.get_salary()}")
except InvalidSalaryException as ex:
    print(ex.get_message())
    ex_occurred = True
finally:
    if ex_occurred: # noqa
        print("Error: Increment salary value has to be positive!")
    else:
        print("Congrats on your increment!")

neville = Person('Neville',  35,  'he', 'Professor')
print(f"\n{neville.get_personal_info()}")

new_role = ron.change_role('Auror', 50000, 'Ministry of Magic', '008')
print(new_role)
print(ron)




