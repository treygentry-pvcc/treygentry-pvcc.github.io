#Name: Trey Gentry 
#Program Purpose: This program finds the cost of movie tickets 
#   Price for one ticket: $10.99
#   Sales tax rate : 5.5%
#   Price for one drink: $4.99
#   Sales tax rate: 5.5%

import datetime

# define global variables 
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET= 10.99
PR_POPCORN= 12.99

# Define global variables
num_tickets= 0
subtotal= 0 
sales_tax= 0
total= 0

# define program functions

def main():
    more_tickets=True

    while more_tickets:
            get_user_data()
            perform_calculations()
            display_results()

            askAgain=input("\nWould you like to order again (Y or N)?:")
            if askAgain.upper()=="N"or askAgain=="n":
                more_tickets= False
                print("Thank you for order.Enjoy your movie")

def get_user_data():
    global num_tickets
    num_tickets= int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    moneyf="8,.2f"
    print('------------------------------')
    print('****  CINEMA HOUSE MOVIES ****')
    print('------------------------------')
    print('Tickets       $'+ format(subtotal,moneyf ))
    print('Sales Tax     $'+ format(sales_tax, moneyf))
    print('Total         $'+ format(total, moneyf))
    print('------------------------------')
    print(str(datetime.datetime.now()))

    #call on main program to execute 
main()

    

