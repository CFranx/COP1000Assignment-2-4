# input statements
def salaryDependents():
  salary = float(input("Enter Salary: "))
  numDependents = float(input("Enter Dependents: "))
  
# calculate taxes here
  stateTax = salary * 0.065
  federalTax = salary * 0.28
  dependentDeduction = salary * (numDependents * 0.025)
  totalWithholding = stateTax + federalTax +       dependentDeduction
  takeHomePay = salary - totalWithholding
  
# output statements
  print("State Tax: $" + str(stateTax)) 
  print("Federal Tax: $" + str(federalTax))
  print("Dependents: $" + str(round(dependentDeduction,1)))
  print("Salary: $" + str(salary))
  print("Take Home Pay: $" + str(takeHomePay))
  
  return "State Tax: $" + str(stateTax), \
         "Federal Tax: $" + str(federalTax), \
         "Dependents: $" + str(round(dependentDeduction,1)), \
         "Salary: $" + str(salary), \
         "Take Home Pay: $" + str(takeHomePay)

if __name__ == "__main__":
  salaryDependents()