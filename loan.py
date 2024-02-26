# get details of loan
money_owed = float(input("How much money do you owe (in dollars)? ")) #100,000 for example
apr = float(input("What's the APR on the money owed? ")) #3% for example
payment = float(input("What is your montly payment (in dollars)? ")) #1000
months = int(input("How many months do you want to see in the results? ")) #24 months or two years

monthly_rate = apr/100/12

for i in range(months):
        
    # calculate interest to pay
    interest_paid = money_owed*monthly_rate

    # add interest
    money_owed = money_owed + interest_paid

    if money_owed - payment < 0:
        print("The last payment is", money_owed)
        print('You paid off the loan in', i+1, 'months.')
        break

    # make payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest. ', end='')
    print('Now I owe', money_owed)