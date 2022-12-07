from person import Person

class Employee(Person):
    def __init__(self, empnum, person):
        self.empnum = empnum
        self.person = person
        super().__init__(person.first_name,person.last_name,person.birthdate,person.gender)
    
    def __str__(self):
        ret_str = "Empployee Number: " + self.empnum + "\n"
        return super().__str__() + ret_str