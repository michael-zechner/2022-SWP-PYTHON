from employee import Employee

#TODO Erweiterung Array beschränken durch var max_emp
class GroupLeader(Employee):
    def __init__(self, max_emp, employee):
        self.max_emp = max_emp
        self.employee = employee
        super().__init__(employee.empnum, employee.person)

    def __str__(self):
        ret_str = "Maximum amount on Employees he can lead: " + str(self.max_emp) + "\n"
        return ret_str +super().__str__() 
