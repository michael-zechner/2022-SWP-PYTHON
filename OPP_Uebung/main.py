from person import Person
from employee import Employee
from groupleader import GroupLeader
from department import Department
from company import Company
from gender import Gender

if __name__ == "__main__":
    p = Person("Michael","Zechner","11-06-2004",Gender.m)
    e = Employee("E123456",p)
    g = GroupLeader(5,e)

    p2 = Person("Lea","Mustermann","11-06-1981",Gender.w)
    e2 = Employee("E654321",p2)
    g2 = GroupLeader(5,e2)

    p3 = Person("Max", "Mustermann","12-01-1980", Gender.m)
    e3 = Employee("E98765",p3)

    p4= Person("Franz","Mustermann","18-03", Gender.m)
    e4=Employee("E726932",p4)

    c = Company("HTL")

    d1 = Department("IT-Development")
    d2 = Department("SAP")

    d1.add_groupleader(g)
    d2.add_groupleader(g2)

    d1.add_employee(e3)
    d2.add_employee(e4)

    c.add_department(d1)
    c.add_department(d2)

    c.print_dep_groupleader()
    print("##########")
    print(c.percent_m_w())