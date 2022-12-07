class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.groupleader = []
    
    def add_employee(self,e):
        self.employees.append(e)

    def add_groupleader(self,g):
        self.groupleader.append(g)    

    def dept_print(self):
        ret_str_e = ""
        for e in self.employees:
            ret_str_e += str(e) + "\n"
        ret_str_g = ""
        for g in self.groupleader:
            ret_str_g += str(g) + "\n"
        return self.name + "\n" + "Groupleader: " + ret_str_g + "\n" + "Employees:"  + "\n" + ret_str_e

    def __str__(self):
        return self.name