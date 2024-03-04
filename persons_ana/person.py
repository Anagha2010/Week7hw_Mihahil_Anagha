# defining Person class which is base class for Customer and Employee
class Person:
    # CONSTRUCTOR
    def __init__(self, name, age, pronoun, profession=''):
        self.name = name
        self.age = age
        self.pronoun = pronoun
        self.profession = profession
    # getters and setters

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_profession(self):
        return self.profession

    def set_profession(self, prof):
        self.profession = prof

    # method
    def get_personal_info(self):
        return f"\nName: {self.name}, Age:{self.age}, Profession: {self.profession}"

    def __str__(self):
        return (
            f"\n{'*' * 30}\nName: {self.name}\nProfession: {self.profession}\n"
            f"Age:{self.age}\nPreferred pronoun:{self.pronoun}\n{'*' * 30}")

