"""
We want to model the banking world, by creating the classes Account, Holder, and Bank.

The Account class has attributes for:
    - the bank (an object of class Bank)
    - the account number (an int)
    - the holder (an object of class Holder)
    - the current balance (float). The only private attribute.
        - if an opening balance is not provided, it is initially set to 0.0 

The Account class has the following methods:
    - get_balance, that returns the current balance
    - deposit, that adds an amount to the current balance. If the amount is negative or zero, it does not deposit anything. In all cases, it returns the deposited amount.
    - withdraw, that subtracts an amount from the balance. If the amount is negative or zero, it does not withdraw anything. If the balance is insufficient, prints `Insufficient
      funds` and withdraws all the balance. In any case, it returns the actual amount withdrawn.

The Holder class has attributes for:
    - a string which is a unique identifier for the holder (suppose it is unique without checking)
    - the name of the holder (a string)
    - the surname of the holder (a string)
    - a dictionary of the accounts the holder holds (i.e., the values are Account objects - more on the key later). The attribute must be "private"

The first three are taken as parameters by the __init__, the last one is initialized as an empty dictionary.

The Holder class has the following methods:
    - add_account, that adds an Account object to the dictionary of holder's accounts, after checking that it is not already in the list of accounts. Do not return anything. 
        - The key is a tuple of two elements. The first element is a reference to the  Bank object of that  Account object, the second element is the number of that  Account 
        - The value is a (reference to the) Account object passed as parameter
    - total_balance, that returns the sum of the balances of all the accounts held by the holder. Challenge: do it in one line ;)

The Bank class has attributes for:
    - the name of the bank (a string) - the only one passed as parameter to the  __init__
    - a "private" counter (int) holding the number of the last created account, so it is possible 
      to assign a new number when a new account will be created. Initially 0
    - a "private" dictionary of holders (objects of class Holder), containing all the holders of 
      accounts in that bank. Initially empty. The keys will be the holder unique identifier, the values a reference to the object of class Holder
    - a "private" dictionary of accounts (objects of class Account), containing all the accounts of 
      the bank. Initially empty. The keys will be the account number, the values a reference to the object of class Account

The Bank class has the following methods:
    - print_holders, that prints
        - a first line with the string `Holders of bank` followed by a space and then by the name of the bank.
        - a line for each holder present in the bank, printing - separated by one space: identifier, name, surname. For testing purposes: iterate over sorted(self.__holders.values()) 
    - print_accounts, that prints
        - a first line with the string Accounts of bank followed by a space and then by the name of the bank.
        - a line for each account present in the bank, printing - separated by one space: account number, identifier of the holder, balance of the account. For testing purposes: iterate over sorted(self.__accounts.values()) 
    - new_account, that 
        - checks that the holder is an instance of class Holder, and that the initial balance is not negative
        - if so, creates a new account with a new number
        - inserts the new account into the dictionary of accounts of the bank
        - inserts the new account into the dictionary of accounts of the holder
        - if not yet present, inserts the holder into the dictionary of holders of the bank
        - returns the newly created Account
    - __get_account that takes an account number (int) and returns the object of class Account that corresponds to that number. If not found, returns None.
    - same_bank_transfer, that transfers two funds between two accounts of the same bank (the number of the accounts are passed as integers)
        - if the Debit account does not exist, print `Debit account not available` and return None 
        - if the Credit account does not exist, print `Credit account not available` and return None
        - if the balance of the Debit account is lower than the amount to be transferred, print `Insufficient funds` and return None
        - otherwise, do  the transfer and return None
    - another_bank_transfer, that transfers two funds between an account from the current bank to an account of another bank (an object of class Bank is passed, the number of the accounts are passed as integers)
        - if the Debit account does not exist, print `Debit account not available` and return None 
        - if the balance of the Debit account is lower than the amount to be transferred, print `Insufficient funds` and return  None
        - if the object for the other bank passed as a parameter is not an instance of class Bank, print `Credit bank not available` and return None 
        - otherwise, do  the transfer and return None
    - deposit, that deposits on the account with the number passed as parameter a certain amount
        - if the account is not present, print `Account not available` and return None
        - otherwise, deposit the amount 
        - let's call c the deposited amount, print the following: print("Deposited", c, "on account", account_number)
          and return None
    - withdraw, that withdraws from the account with the number passed as parameter a certain amount
        - if the account is not present, print `Account not available` and return None
        - otherwise, withdraw the amount
        - let's call p the withdrawn amount, print the following: print("Withdrawn", p, "from account", account_number)
          and return None
"""

class Account():
    def __init__(self, bank, number, holder, opening_balance=0):
        self.bank = bank
        self.number = number
        self.holder = holder
        self.__current_balance = float(opening_balance)

    def get_balance(self):
        return self.__current_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__current_balance += amount

        return self.__current_balance
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__current_balance > amount:
                self.__current_balance -= amount
            else:
                self.__current_balance = 0
                print("Insufficient funds")

        return self.__current_balance
    
    def __lt__(self, other):
        #for sorting purposes. DO NOT EDIT.
        return self.number < other.number

class Holder():
    def __init__(self, ident, name, surname):
        self.ident = ident
        self.name = name
        self.surname = surname
        self.accounts = {}

    def add_account(self, account):
        account_key = (account.bank, account.number)

        if account_key not in self.accounts.keys():
            self.accounts[account_key] = account

    def total_balance(self):
        return sum(value._Account__current_balance for value in self.accounts.values())

    def __lt__(self, other):
        #for sorting purposes. DO NOT EDIT
        return self.surname < other.surname

class Bank():
    def __init__(self, name):
        self.name = name
        self.__counter = 0
        self.__holders = {}
        self.__accounts = {}

    def print_holders(self):
        print("Holders of bank", self.name)

        for value in sorted(self.__holders.values()):
            print(value.ident, value.name, value.surname)

    def print_accounts(self):
        print("Accounts of bank", self.name)

        for value in sorted(self.__accounts.values()):
            print(value.number, value.holder.ident, value._Account__current_balance)

    def new_account(self, holder, initial_balance = 0):
        if isinstance(holder, Holder):
            self.__counter += 1

            new_account = Account(self.name, self.__counter, holder, initial_balance)

            self.__accounts[new_account.number] = new_account
            holder.add_account(new_account)

            idents = [ident for ident in self.__holders.keys()]    
            if holder.ident not in idents:
                self.__holders[holder.ident] = holder

            return new_account
        
    def __get_account(self, number):
        if number in self.__accounts.keys():
            return self.__accounts[number]
        
        return None
    
    def same_bank_transfer(self, debit_number, credit_number, amount):
        if debit_number not in self.__accounts.keys():
            print("Debit account not available")
            
            return None
        
        if credit_number not in self.__accounts.keys():
            print("Credit account not available")
            
            return None
        
        debit_account = self.__accounts[debit_number]
        credit_account = self.__accounts[credit_number]

        if debit_account._Account__current_balance < amount:
            print("Insufficient funds")

            return None
        
        debit_account.withdraw(amount)
        credit_account.deposit(amount)

        return None

    def another_bank_transfer(self, debit_number, credit_bank, credit_number, amount):
        if debit_number not in self.__accounts.keys():
            print("Debit account not available")
            
            return None
        
        if not isinstance(credit_bank, Bank):
            print("Credit bank not available")

            return None
        
        debit_account = self.__accounts[debit_number]
        credit_account = credit_bank._Bank__accounts[credit_number]
        
        if debit_account._Account__current_balance < amount:
            print("Insufficient funds")

            return None
        
        debit_account.withdraw(amount)
        credit_account.deposit(amount)

        return None
    
    def deposit(self, account_number, amount):
        if account_number not in self.__accounts.keys():
            print("Account not available")

            return
        
        account = self.__accounts[account_number]
        account.deposit(amount)

        print("Deposited", amount, "on account", account_number)

        return None
    
    def withdraw(self, account_number, amount):
        if account_number not in self.__accounts.keys():
            print("Account not available")

        account = self.__accounts[account_number]
        balance = account._Account__current_balance

        account.withdraw(amount)

        if balance > amount:
            print("Withdrawn", amount, "from account", account_number)
        else:
            print("Withdrawn", balance, "from account", account_number)

        return None

michael = Holder('ldomhl', 'M', 'L')
chiara = Holder('brbchr', 'C', 'B')

b1 = Bank("Banca1")
b2 = Bank("Banca2")
b1.new_account(michael, 1000)
b2.new_account(chiara, 50)
b1.new_account(chiara)
b1.print_holders()
b1.print_accounts()
b2.print_holders()
b2.print_accounts()

print(chiara.total_balance())

b1.same_bank_transfer(1, 2, 300)
b1.print_accounts()
b1.withdraw(1, 50)
b1.withdraw(1, 1000)

print(michael.total_balance())
print(chiara.total_balance())