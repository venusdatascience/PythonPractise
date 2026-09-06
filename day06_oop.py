#bank management system

# Customer Class

class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def info(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Phone:", self.phone)


# Account Class

class Account:
    def __init__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.__balance = balance

    def account_info(self):
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount")

    def check_balance(self):
        print("Balance:", self.__balance)


# Create Customers

customer1 = Customer(123, "Ram", "1234567897")
customer2 = Customer(345, "Sita", "2345678765")


# Display Customer Information

customer1.info()
print()

customer2.info()
print()


# Create Accounts

account1 = Account(1001, "Savings", 5000)
account2 = Account(1002, "Current", 10000)


# Display Account Information

account1.account_info()
print()


# Deposit

account1.deposit(2000)

# Withdraw

account1.withdraw(1000)

# Check Balance

account1.check_balance()