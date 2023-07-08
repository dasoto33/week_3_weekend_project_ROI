# roi = net income / cost of investment x100
# use a while loop
# try block to test/handle errors 
# use ValueErrors as well to return 'invalid' statement if incorrect input is made
# must get inputs for price, income, expenses, taxes, etc...
# use .2f in roi print statement to make sure number is displayed with 2 digits after decimal
# was not being very friendly, use float for the inputs see if that helps
# try to integrate zillow api

# import requests

def roi_calculator():
    while True:
        try:
            purchase_price = float(input('What was the total purchase price of the home? $ '))
            rental_income = float(input('What is your estimated yearly rental income? $ '))
            maintenance_expense = float(input('What are your estimated yearly maintenance expenses? $ '))
            prop_tax = float(input('What are your estimated yearly property taxes? $ '))
            hold_period = int(input('How many years do you intend to keep the property? '))

            if purchase_price <= 0 or rental_income <= 0 or maintenance_expense <= 0 or prop_tax <= 0 or hold_period <= 0:
                print('Invalid input. Please enter positive values and try again.')
                continue

            net_cash_flow = rental_income - maintenance_expense - prop_tax
            total_cash_flow = net_cash_flow * hold_period
            roi = (total_cash_flow / purchase_price) * 100

            print(f'\nReturn on Investment (ROI) for this property is: {roi:.2f}%')
            break

        except ValueError:
            print('Invalid input. Enter numerical values.')
            continue

roi_calculator()



