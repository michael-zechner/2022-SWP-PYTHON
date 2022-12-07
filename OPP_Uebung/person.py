from gender import Gender

class Person:
    def __init__(self, first_name, last_name, birthdate, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = Gender.m if Gender.m == gender else Gender.w

    def __str__(self):
        return "Name: " + self.first_name + " " + self.last_name + "\nBirthdate: " + self.birthdate + "\nGender: " + self.gender.name + "\n"