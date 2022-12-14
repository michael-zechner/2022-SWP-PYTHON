from person import Person
from employee import Employee
from groupleader import GroupLeader
from department import Department
from company import Company
from gender import Gender
from matplotlib import pyplot as plt  
import numpy as np


def init():
    p = Person("Michael","Zechner","11-06-2004","m")
    e = Employee("E123456",p)
    g = GroupLeader(5,e)

    p2 = Person("Lea","Mustermann","11-06-1981","w")
    e2 = Employee("E654321",p2)
    g2 = GroupLeader(5,e2)

    p3 = Person("Max", "Mustermann","12-01-1980", "m")
    e3 = Employee("E98765",p3)

    p4= Person("Franz","Mustermann","18-03-1999", "m")
    e4=Employee("E726932",p4)

    p5 = Person("Herbert", "Mustermann", "12-04-2000","m")
    e5 = Employee("E28348", p5)
    
    c = Company("HTL")

    d1 = Department("SWP")
    d2 = Department("INFI")
    
    d1.add_groupleader(g)
    d2.add_groupleader(g2)

    d1.add_employee(e3)
    d1.add_employee(e4)
    d2.add_employee(e5)

    c.add_department(d1)
    c.add_department(d2)
    return c

def choice(c):
    menu = input("Was wollen sie sehen?\n- Wie vie Mitarbeiter gibt es (1)\n"+
    "- Wie viel Gruppenleiter gibt es (2)\n" +
    "- Wie viel Abteilungen gibt es (3)\n" +
    "- Welche Abteilungen hat die Meisten Mitarbeiter (4)\n" +
    "- Prozentualer Männer- und Frauenanteil (5)\n" +
    "- Grafik zu Männer- und Frauenanteil (6)\n"
    "- Abteilungen ausgeben (7)\n" +
    "- Gruppenleiter ausgeben und deren Mitarbeiter (8)\n\n")
    
    print("\n")
    if menu == "1":
        print("Anzahl Mitarbeiter: " + str(c.how_much_employees()))
    elif menu == "2":
        print("Anzahl Gruppenleiter: " + str(c.how_much_groupleader()))
    elif menu == "3":
        print("Anzahl der Abteilungen: " + str(c.how_much_departments()))
    elif menu == "4":
        print("Abteilung mit den meisten Mitarbeiter: " + str(c.most_employees()))
    elif menu == "5":
        print(c.percent_m_w())
    elif menu == "6":
        chart(c)
    elif menu == "7":
        c.print_department()
    elif menu == "8":
        c.print_dep_groupleader()

    back = str(input("Nochmal (Y/N)\n"))
    if back == "Y":
       choice(c) 
    elif back == "N":
        print("Servus!")

def chart(c):
    m,w = c.percent_m_w()
    percent = [m,w]
    names = ["Männer", "Frauen"]
    plt.pie(percent,labels=names,autopct='%1.2f%%')
    plt.show()

if __name__ == "__main__":
    c = init()
    choice(c)