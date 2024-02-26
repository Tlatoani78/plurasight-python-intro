expenses = [10.5, 8, 16, 23, 85, 78, 13]

# sum = 0

# one way of doing loops
# for x in expenses:
#     sum = sum + x
# print("You spent $", sum, sep="")

# another one is using the sum() function for lists
total = sum(expenses)
print("You spent $", total, sep="")