total = 0
expenses = []

# range is set to 7
# for i in range(7):
#     expenses.append(float(input("Enter your expense: ")))
# total = sum(expenses)
# print("Your total expense is: $", total, sep="")

# asking the user for number of expenses
num_expenses = int(input("Enter the number of expenses you want to report: "))

for i in range(num_expenses):
    expenses.append(float(input("Enter your expense: ")))
total = sum(expenses)
print("Your total expense is: $", total, sep="")