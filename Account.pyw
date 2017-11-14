"""
This program keeps track of the amount of money in a single bank account that is set aside for different purposes. The
user manually enters the amounts that were added or removed, and specifies a keyword for their purpose.
"""

import pickle
import tkinter
import BankAccount

main_window = tkinter.Tk()
main_window.configure(background='light green')
main_window.minsize(width=500, height=500)


def main():
    def existing_balance():
        def submit(): # set existing balance for any separate accounts
            account_purposes[purpose_box.get()] = BankAccount.BankAccount(float(amount_box.get()))
            save()
            existing_bal_window.destroy()
            top.destroy()
            bottom.destroy()

        existing_bal_window = tkinter.Toplevel()
        top_frame = tkinter.Frame(existing_bal_window)
        mid_frame = tkinter.Frame(existing_bal_window)
        bottom_frame = tkinter.Frame(existing_bal_window)

        purpose_label = tkinter.Label(top_frame, text="What is this money set aside for? ")
        purpose_box = tkinter.Entry(top_frame, width=35)
        amount_label = tkinter.Label(mid_frame, text="How much money in this account is set aside? $")
        amount_box = tkinter.Entry(mid_frame, width=10)
        okay_button = tkinter.Button(bottom_frame, text='OK', command=submit)
        cancel_button = tkinter.Button(bottom_frame, text='Cancel', command=existing_bal_window.destroy)

        purpose_label.pack(side='left')
        purpose_box.pack(side='left')
        amount_label.pack(side='left')
        amount_box.pack(side='left')
        okay_button.pack(side='left')
        cancel_button.pack(side='left')

        top_frame.pack()
        mid_frame.pack()
        bottom_frame.pack()

        existing_bal_window.mainloop()

    if account_purposes == {}:  # initial program run or no data has been entered

        top = tkinter.Frame(main_window)
        bottom = tkinter.Frame(main_window)

        greeting = tkinter.Label(top, text="Welcome! It doesn't look like you've been here before.\nIs there any money set aside in /"
                                 "this bank account already?")

        y = tkinter.Button(bottom, text='Yes', command=existing_balance)
        n = tkinter.Button(bottom, text='No', command=main_window.destroy)

        greeting.pack(side='left')
        y.pack(side='left')
        n.pack(side='left')
        top.pack()
        bottom.pack()

        main_window.mainloop()

    l1 = tkinter.Frame()
    l2 = tkinter.Frame()
    l2.configure(background='light green', pady=3)
    l3 = tkinter.Frame()
    l3.configure(background='light green', pady=3)
    l4 = tkinter.Frame()
    l4.configure(background='light green', pady=3)
    l5 = tkinter.Frame()
    l5.configure(background='light green', pady=3)

    choice = tkinter.Label(l1, text='Welcome! What would you like to do?')
    choice.configure(background='light green', padx=10, pady=10)
    add_button = tkinter.Button(l2, text='Add money', command=add_prompt)
    add_button.configure(width=12)
    remove_button = tkinter.Button(l3, text='Remove money', command=remove_prompt)
    remove_button.configure(width=12)
    show_button = tkinter.Button(l4, text='Show balances', command=show)
    show_button.configure(width=12)
    exit_button = tkinter.Button(l5, text='Exit', command=main_window.destroy)
    exit_button.configure(width=12)

    choice.pack()
    add_button.pack()
    remove_button.pack()
    show_button.pack()
    exit_button.pack()

    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()

    main_window.mainloop()


def add_prompt():
    def add():
        if account_box.get().lower() not in account_purposes.keys():  # create account if it doesn't exist
            account_purposes[account_box.get().lower()] = BankAccount.BankAccount(0.)

        account_purposes[account_box.get().lower()].add_money(float(amount_box.get()))
        save()
        add_window.destroy()

    add_window = tkinter.Toplevel()

    top_frame = tkinter.Frame(add_window)
    mid_frame = tkinter.Frame(add_window)
    bottom_frame = tkinter.Frame(add_window)

    account_label = tkinter.Label(top_frame, text='What is the purpose for this money? ')
    account_box = tkinter.Entry(top_frame, width=50)
    amount_label = tkinter.Label(mid_frame, text='What is the amount being added? ')
    amount_box = tkinter.Entry(mid_frame, width=30)
    okay_button = tkinter.Button(bottom_frame, text='OK', command=add)
    cancel_button = tkinter.Button(bottom_frame, text='Cancel', command=add_window.destroy)

    account_label.pack(side='left')
    account_box.pack(side='left')
    amount_label.pack(side='left')
    amount_box.pack(side='left')
    okay_button.pack(side='left')
    cancel_button.pack(side='left')
    top_frame.pack()
    mid_frame.pack()
    bottom_frame.pack()

    add_window.mainloop()


def remove_prompt():
    def check_if_exists():
        def remove():
            if account_box.get().lower() not in account_purposes.keys():
                account_purposes[account_box.get().lower()] = BankAccount.BankAccount(0.)
            account_purposes[account_box.get().lower()].remove_money(float(amount_box.get()))
            save()
            remove_window.destroy()

        if account_box.get().lower() not in account_purposes.keys() or account_purposes[account_box.get().lower()].get_balance() == 0:
            warning = tkinter.Label(warning_frame, text='Warning: There is no money in this account!')
            warning.pack()

        okay_button2 = tkinter.Button(bottom_frame2, text='OK', command=remove)
        cancel_button2 = tkinter.Button(bottom_frame2, text='Cancel', command=remove_window.destroy)
        bottom_frame1.destroy()
        okay_button2.pack(side='left')
        cancel_button2.pack(side='left')

        amount_label = tkinter.Label(mid_frame, text='How much are you removing from this account? $')
        amount_box = tkinter.Entry(mid_frame, width=50)

        amount_label.pack(side='left')
        amount_box.pack(side='left')
        mid_frame.pack()
        bottom_frame2.pack()

    remove_window = tkinter.Toplevel()
    top_frame = tkinter.Frame(remove_window)
    mid_frame = tkinter.Frame(remove_window)
    warning_frame = tkinter.Frame(remove_window)
    bottom_frame1 = tkinter.Frame(remove_window)
    bottom_frame2 = tkinter.Frame(remove_window)

    okay_button1 = tkinter.Button(bottom_frame1, text='OK', command=check_if_exists)
    cancel_button1 = tkinter.Button(bottom_frame1, text='Cancel', command=remove_window.destroy)
    account_label = tkinter.Label(top_frame, text='Which account are you removing money from? ')
    account_box = tkinter.Entry(top_frame, width=50)

    account_label.pack(side='left')
    account_box.pack(side='left')
    okay_button1.pack(side='left')
    cancel_button1.pack(side='left')
    top_frame.pack()
    warning_frame.pack()
    bottom_frame1.pack()

    remove_window.mainloop()


def show():
    show_window = tkinter.Toplevel()
    close_button = tkinter.Button(show_window, text="Close", command=show_window.destroy)

    if account_purposes == {}:
        no_balance = tkinter.Label(show_window, text="There are no balances to show.")
        no_balance.pack()

    else:
        balances = ""
        for i in account_purposes:
            balances += str(i.title()) + ' $' + str(format(account_purposes[i.lower()].get_balance(), ',.2f')) + '\n'

        bal_list = tkinter.Label(show_window, text=balances)
        bal_list.pack()

    close_button.pack()

    show_window.mainloop()


def save():  # save transactions
    with open("account.dat", "wb") as file:
        pickle.dump(account_purposes, file)


# PROGRAM START
try:
    with open("account.dat", "rb") as file:
        account_purposes = pickle.load(file)
except FileNotFoundError:
        account_purposes = {}  # create empty dictionary if the file does not exist

try:
    main()
except KeyboardInterrupt:
    pass



