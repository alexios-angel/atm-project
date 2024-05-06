#!/bin/env python3

class ATM:
    def __init__(self, checking_balance, savings_balance, annual_interest_rate):
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        self.annual_interest_rate = annual_interest_rate
        self.monthly_interest_rate = annual_interest_rate / 12

    def display_balance(self):
        print(f"Checking Balance: ${self.checking_balance:.2f}")
        print(f"Savings Balance: ${self.savings_balance:.2f}")

    def check_balance(self):
        while True:
            account_type = input("Enter account type (checking/savings): ")
            match account_type:
                case "checking" | 'c':
                    print(f"Checking Balance: ${self.checking_balance:.2f}")
                    return
                case "savings" | 's':
                    print(f"Savings Balance: ${self.savings_balance:.2f}")
                    while True:
                        answer = input("Get monthly interest? [Y]es/[N]o: ")
                        match answer:
                            case 'Y' | 'y' | "Yes" | "yes":
                                self.calculate_monthly_interest()
                                return
                            case 'N' | 'n' | "No" | "no":
                                return
                            case  _:
                                print("Invaild response")
                case _:
                    print("Invalid account type.")
        
        

    def deposit(self):
        account_type = input("Enter account type (checking/savings): ")
        amount = float(input("Enter the amount to deposit: "))

        match account_type:
            case "checking" | 'c':
                self.checking_balance += amount
                account_type = "checking"
            case "savings" | 's':
                self.savings_balance += amount
                account_type = "savings"
            case _:
                print("Invalid account type.")
                return

        print(f"Deposit of ${amount:.2f} into {account_type} account successful.")
        self.display_balance()

    def withdraw(self):
        account_type = input("Enter account type (checking/savings): ")
        amount = float(input("Enter the amount to withdraw: "))

        match account_type:
            case "checking" | 'c':
                if self.checking_balance >= amount:
                    self.checking_balance -= amount
                    print(f"Withdrawal of ${amount:.2f} from checking account successful.")
                else:
                    print("Insufficient funds in checking account.")
            case "savings" | 's':
                if self.savings_balance >= amount:
                    self.savings_balance -= amount
                    print(f"Withdrawal of ${amount:.2f} from savings account successful.")
                else:
                    print("Insufficient funds in savings account.")
            case _:
                print("Invalid account type.")
                return

        self.display_balance()

    def calculate_monthly_interest(self):
        monthly_interest = self.savings_balance * self.monthly_interest_rate
        print(f"Your monthly interest is ${monthly_interest:.2f}.")

def main():
    annual_interest_rate = 0.05  # 5% annual interest rate
    atm = ATM(1234, 56789, annual_interest_rate)

    while True:
        print("Options:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1" | "check" | "check balance":
                atm.check_balance()
            case "2" | "deposit":
                atm.deposit()
            case "3" | "widthdraw":
                atm.withdraw()
            case "4" | "exit" | 'e':
                print("Exiting the ATM :)")
                break
            case _:
                print("Invalid choice. Please try again.")

        #print newline to provide clear separation from the options
        print("")

if __name__ == "__main__":
    main()