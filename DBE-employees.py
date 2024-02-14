class Employee:
    def __init__(self, first_name, surname, pay = 16000, job="Senior Admin Clerk"):
        self.first_name = first_name
        self.surname = surname
        self.pay = pay
        self.email = f'{surname.lower()}.{first_name[0].lower()}@dbe.gov.za'

    def display_employee(self):
        print(f'The new employee is: {self.first_name} {self.surname}')
        print(f'He/she gets paid {self.pay} and you can contact him at {self.email}')
        print(f'He/She is our new Senior Admin Clerk')


Jack = Employee('Jack', 'Smith', 16000)

Jack.display_employee()
print(Jack.__str__())

class Intern(Employee):
    def __init__(self, NQF_level):
        self.NQF_level = NQF_level
        if self.NQF_level == 4:
            super().pay = 3500
        elif self.NQF_level == 5 or self.NQF_level == 6:
            super().pay = 4200
        elif self.NQF_level == 7:
            super().pay = 6500
        elif self.NQF_level > 8:
            super().pay = 7500
        # elif if 4 < self.NQF_level > 0:
        #     throw(ValueError) 


class SETA_Intern(Intern):
        pass


Thabani = Employee("Thabani", "Manzini", 100000, "Intern")
#Thabani = SETA_Intern(5)

Thabani.display_employee()