class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def add_money(self):
        value = float(input("Add to account: $"))
        self.__balance += value

    def remove_money(self):
        value = float(input("Remove from account: $"))
        self.__balance -= value


