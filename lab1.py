employee_salaries = {}

while True:
    employee_name = input("Enter employee name: ")
    if employee_name.lower() == 'no':
        break
    employee_salary = float(input("Enter employee salary: "))
    employee_salaries[employee_name] = employee_salary

print(employee_salaries)

