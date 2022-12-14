from employee import Employee

#TODO Erweiterung Array beschränken durch var max_emp
class GroupLeader(Employee):
    def __init__(self, reports, employee):
        self.reports = reports
        self.employee = employee
        super().__init__(employee.empnum, employee.person)

    def __str__(self):
        ret_str = "Has to check " + str(self.reports) + " Reports a Week\n"
        return ret_str + super().__str__() 
