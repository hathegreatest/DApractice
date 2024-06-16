#Write a program in Python that defines an employee class 
#including name, income and gender. 
#Define a list of employees entered from the keyboard, 
#calculate the average income of male and female employees.

class Employee:
    def __init__(self, name, income,gender):
        self.name = name
        self.income = income
        self.gender = gender 
    def __str__(self):
        return f"{self.name}: {self.income}"
    
def main():
    n = int(input())
    employees = []
    for i in range(n):
        name, income,gender = input().split()
        income = int(income)
        employee = Employee(name, income,gender) 
        employees.append(employee) 
    income_for_female = [employee.income for employee in employees if employee.gender == "female"]
    income_for_male = [employee.income for employee in employees if employee.gender == "male"]
    print(average(income_for_female))
    print(average(income_for_male))

def average(l):
    sum = 0
    for i in l:
        sum += i
    return (sum/len(l))

if __name__ == "__main__":
    main()
