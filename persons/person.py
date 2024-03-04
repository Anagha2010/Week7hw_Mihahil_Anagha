class Person:

    def __init__(self, name, age, pronoun, profession=''):
        self.name = name
        self.age = age
        self.pronoun = pronoun
        self.profession = profession

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

    def get_personal_info(self):
        return f"\nName: {self.name}, Age:{self.age}, Profession: {self.profession}"
