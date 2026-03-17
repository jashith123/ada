class Account:
    # -------- Class Variables (Static Members) --------
    bank_name = "National Python Bank"
    total_accounts = 0

    # -------- Constructor --------
    def __init__(self, account_number=0, holder_name="Unknown", balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = balance  # Private variable

        Account.total_accounts += 1

    # -------- Encapsulation: Getter --------
    def get_balance(self):
        return self.__balance

    # -------- Deposit --------
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"{self.holder_name}: Deposited ₹{amount}")

    # -------- Withdraw --------
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"{self.holder_name}: Withdrew ₹{amount}")

    # -------- Balance Inquiry --------
    def show_balance(self):
        print(f"{self.holder_name}: Current Balance = ₹{self.__balance}")

    # -------- Interest (Polymorphic Method) --------
    def calculate_interest(self):
        # Default implementation (may be overridden)
        print("Interest calculation not defined for this account type.")
        return 0

    # -------- Display Account Info --------
    def display_info(self):
        print(f"Account No: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ₹{self.__balance}")
        print("-" * 40)


# =====================================================
# Savings Account (Inheritance + Method Overriding)
# =====================================================

class SavingsAccount(Account):

    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate  # percentage

    # Override Interest Calculation
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print(f"{self.holder_name}: Interest = ₹{interest}")
        return interest


# =====================================================
# Current Account (Inheritance + Overdraft Facility)
# =====================================================

class CurrentAccount(Account):

    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    # Override Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        available = self.get_balance() + self.overdraft_limit

        if amount > available:
            print("Overdraft limit exceeded.")
        else:
            # Accessing private balance safely through deposit/withdraw logic
            new_balance = self.get_balance() - amount
            # Directly modifying via name mangling (controlled internal use)
            self._Account__balance = new_balance
            print(f"{self.holder_name}: Withdrew ₹{amount} (Overdraft allowed)")


# =====================================================
# Driver Program (Demonstrates Polymorphism)
# =====================================================

def main():

    print(f"Welcome to {Account.bank_name}")
    print("=" * 50)

    # Creating accounts
    acc1 = SavingsAccount(101, "Jashith", 50000, 5)
    acc2 = CurrentAccount(102, "Aman", 20000, 10000)
    acc3 = SavingsAccount(103, "Riya", 75000, 4)

    # Runtime Polymorphism
    accounts = [acc1, acc2, acc3]

    for acc in accounts:
        acc.display_info()
        acc.deposit(5000)
        acc.withdraw(30000)
        acc.show_balance()
        acc.calculate_interest()   # Polymorphic call
        print("\n")

    print("=" * 50)
    print(f"Total Accounts Created: {Account.total_accounts}")


if __name__ == "__main__":
    main()