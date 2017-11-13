"""
This program keeps track of the amount of money in a single bank account that is set aside for different purposes. The
user manually enters the amounts that were added or removed, and specifies a keyword for their purpose.
"""

import pickle
import tkinter
import tkinter.messagebox
import BankAccount

def validate_input(inp_list,qst):
    selection = input('')
    while selection.upper() not in inp_list:
        selection = input("Please enter a valid selection. " + qst)

    return selection



def main():
    if account_purposes == {}:  # initial program run or no data has been entered
        print("Welcome. It doesn't look like you've been here before.")

        print("Is there any money set aside in this bank account already (Y/N)?", end=' ')
        existing_balance = validate_input(['Y', 'N'], 'Is there any money set aside in this bank account already (Y/N)? ')

        if existing_balance.upper() == "Y":
            account_purposes[input('What is this money set aside for? ')] = BankAccount.BankAccount(float(input("How much money in this account is set aside? $")))

    cont = True
    while cont:
        print("What would you like to do? \n"
                "1: Add money\n"
                "2: Remove money\n"
                "3: Show balances\n"
                "4: Cancel/Exit\n")

        transaction = validate_input(['1', '2', '3', '4'], "What would you like to do? \n1: Add money\n2: Remove money\n"
                                                           "3: Show balances\n4: Cancel/Exit\n")

        if transaction == '1':
            account = input('Which account are you adding money to? ')
            if account.lower() not in account_purposes.keys(): # create account if it doesn't exist
                account_purposes[account.lower()] = BankAccount.BankAccount(0.)

            account_purposes[account.lower()].add_money()

        elif transaction == '2':
            account = input('Which account are you removing money from? ')
            if account.lower() not in account_purposes.keys():
                account_purposes[account.lower()] = BankAccount.BankAccount(0.)
            if account_purposes[account.lower()].get_balance() == 0:
                    print("Warning: There is no money in this account!")
            account_purposes[account.lower()].remove_money()
        elif transaction == '3':
            if account_purposes == {}:
                print("There are no balances to show.")
            else:
                for i in account_purposes:
                    print(str(i.title()) + ' $' + str(account_purposes[i.lower()].get_balance()))

        print("Are there any more transactions to enter (Y/N)? ")
        next = validate_input(['Y', 'N'], 'Are there any more transactions to enter (Y/N)? ')

        if next.upper() == "N":
            cont = False


try:
    with open("account.dat", "rb") as file:
        account_purposes = pickle.load(file)
except FileNotFoundError:
        account_purposes = {}

try:
    main()
except KeyboardInterrupt:
    print("Your transactions have not been saved.")

with open("account.dat", "wb") as file:
    pickle.dump(account_purposes, file)
    print("All transactions have been saved.")

