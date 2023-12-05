from bank_account import BankAccount


class Deposit(BankAccount):

    def __init__(self, amount):
        super().__init__()
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
