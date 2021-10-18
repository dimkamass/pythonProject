class Person:
    def __init__(self, first_name, last_name, age):
        self.name = first_name
        self.surname = last_name
        self.age = age

    def full_name(self):
        return f'{self.surname} {self.name}'

    def is_adult(self):
        return self.age >= 18
