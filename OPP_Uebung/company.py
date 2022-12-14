class Company:
    def __init__(self,name):
        self.name = name
        self.departments = []

    def add_department(self,department_name):
        self.departments.append(department_name)

    def how_much_groupleader(self):
        cnt = 0
        for d in self.departments:
            if d.groupleader != None:
                cnt+=1
        return cnt

    def how_much_employees(self):
        cnt = 0
        for d in self.departments:
            cnt += len(d.employees)
        return cnt

    def how_much_departments(self):
        return len(self.departments)

    def most_employees(self):
        cnt = []
        for d in self.departments:
            cnt.append(len(d.employees))
        return self.departments[cnt.index(max(cnt))]

    def percent_m_w(self):
        all_emp = []
        for d in self.departments:
            for e in d.employees:
                all_emp.append(e)
            for g in d.groupleader:
                all_emp.append(g)
        cnt_m = 0
        cnt_w = 0

        for e in all_emp:
            if e.gender == "w":
                cnt_w+=1
            else:
                cnt_m+=1

        percent_w = round((cnt_w / len(all_emp))*100,2)
        percent_m = round((cnt_m / len(all_emp))*100,2)

        return "Frauenanteil: " + str(percent_w) + "%\n" + "Männeranteil: " + str(percent_m) + "%"

    def print_department(self):
        for d in self.departments:
            print(d)

    def print_dep_groupleader(self):
        for d in self.departments:
            print(d.dept_print())

    def __str__(self):
        return self.name