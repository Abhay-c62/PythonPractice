class Bank:
    # Constructor: Automatically called when an object of the class is created
    def __init__(self):
        #private instance variable
        #initializing balance to 5000
        #double underscore is used to make the variable private
        self .__balance = 5000

    # Method to deposit money
    def deposit(self, amount):
        #add the amount to the balance
        self .__balance += amount

    def withdraw(self, amount):
        #check if the balance is sufficient for withdrawal
        if amount <= self .__balance:
            #subtract the amount from the balance
            self .__balance -= amount
        else:
            print("Insufficient balance")
    #Display balance
    def show_balance(self):
        print("Balance:", self .__balance)

# Create a object(instance) of the Bank class
b=Bank()
b.deposit(10000)
b.withdraw(2000)
b.show_balance()
