class BankAccount:
    bank_name = "First National Bank"
    all_accounts = []
    def __init__(self, int_rate, checking_balance, savings_balance):
        self.int_rate = int_rate
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        BankAccount.all_accounts.append(self)

    def checking_deposit(self, amount):
        self.checking_balance += amount
        return self

    def checking_withdraw(self, amount):
        self.checking_balance -= amount
        return self

    def checking_display_account_info(self):
        print("Checking Account Balance:", str("$" + str(self.checking_balance)))

    def savings_deposit(self, amount):
        self.savings_balance += amount
        return self

    def savings_withdraw(self, amount):
        self.savings_balance -= amount
        return self

    def savings_display_account_info(self):
        print("Savings Account Balance:", str("$" + str(self.savings_balance)))

    def yield_interest(self):
        if self.savings_balance > 0:
            self.savings_balance += self.savings_balance * self.int_rate
        else:
            print("Your balance is zero!")
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print("Balance:", str("$" + str(account.balance)))

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .02, checking_balance = 1000, savings_balance = 2500)

    def make_checking_deposit(self, amount):
        self.account.checking_deposit(amount)
        return self

    def make_checking_withdrawal(self, amount):
        self.account.checking_withdraw(amount)
        return self

    def display_checking_balance(self):
        self.account.checking_display_account_info()
        return self

    def make_savings_deposit(self, amount):
        self.account.savings_deposit(amount)
        return self

    def make_savings_withdrawal(self, amount):
        self.account.savings_withdraw(amount)
        return self

    def display_savings_balance(self):
        self.account.savings_display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount

account_john = User("John Jones", "john@me.com")
print(account_john.name), account_john.make_checking_deposit(1500).make_savings_deposit(10000).display_checking_balance().display_savings_balance()