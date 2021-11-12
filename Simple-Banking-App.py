import unittest
from abc import ABC, abstractmethod

# Creation of bank_account class
class bank_account(ABC):
    def __init__(self, acc_no, acc_holder, balance):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = balance

# method to get the account no
    def get_acc_no(self):
        return self.acc_no
    
# method to get the account holder name
    def get_acc_holder(self):
        return self.acc_holder

# method to get the current balance 
    def get_cur_balance(self):
        return self.balance

# method to add new account holder 
    def addNewAccHolder(self, name): 
         self.acc_holder = name

# method to make a deposit
    def deposit(self,amount):
        self.balance = amount + self.balance
        print('You have deposited $',amount,' into your account and your new balance is $',self.balance)

# method for withdrawal 
    @abstractmethod
    def withdraw(self, withdraw_money):
        pass

# method for calcuating interest
    @abstractmethod
    def calculate(self):
       pass

# Creation of Checking class
class Checking(bank_account):

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

# withdrawal method for checking account 
    def withdraw(self, withdraw_money):
        if(self.balance > withdraw_money):
            self.balance = self.balance - withdraw_money
            print('You have withdrawn $',withdraw_money,' from your account and your new balance is $',self.balance)
        else:
            raise Exception("The balance is insufficient to perform the withdrawal")

# Performs interest for the checking account
    def calculate(self):
        interest = (self.balance * 0.01 * 1)/100
        self.balance = self.balance + interest
        print('Your balance after calculating interest is: $',self.balance)

# Creation of Saving class
class Savings(bank_account):

    def __init__(self, acc_no, balance):
        if(balance < 100):
            raise Exception("Minimum balance of $100 is required to create an account")
        self.acc_no = acc_no
        self.balance = balance

# withdrawal method for savings account 
    def withdraw(self, withdraw_money):
        if(self.balance - withdraw_money >= 100):
            self.balance = self.balance - withdraw_money
            print('You have withdrawn $',withdraw_money,' from your account and your new balance is $',self.balance)
        else:
            raise Exception("The balance is insufficient to perform the withdrawal")
    
# Performs interest for the savings account
    def calculate(self):
        if(self.balance < 2000):
            interest = (self.balance * 0.01 * 1)/100
            self.balance = self.balance + interest
            print('Your balance after calculating interest is: $',self.balance)
        elif(self.balance >= 2000 and self.balance < 12000):
            interest = (self.balance * 0.05 * 1)/100
            self.balance = self.balance + interest
            print('Your balance after calculating interest is: $',self.balance)
        else:
            interest = (self.balance * 0.1 * 1)/100
            self.balance = self.balance + interest
            print('Your balance after calculating interest is: $',self.balance)

# Creation of Test Checking class
class Test_Checking(unittest.TestCase):

    # Checks Checking acc accepts zero inital deposit
    def test_no_balance(self):
        checking_acc_test_obj_1 = Checking(977836766123, 0)
        self.assertEqual(checking_acc_test_obj_1.get_cur_balance(), 0)

    # Checks Checking acc accepts deposit deposit
    def test_with_balance(self):
        checking_acc_test_obj_2 = Checking(977836766124, 1000)
        self.assertEqual(checking_acc_test_obj_2.get_cur_balance(), 1000)

    # Checks adding a new account holder to checking account without inital deposit
    def test_adding_accountholder(self):
        checking_acc_test_obj_3 = Checking(977836766125, 0)
        checking_acc_test_obj_3.addNewAccHolder('Pluto')
        self.assertEqual(checking_acc_test_obj_3.get_acc_holder(), 'Pluto')

    #Checking deposit to a account
    def test_deposit(self):
        checking_acc_test_obj_4 = Checking(977836766126, 3000)
        checking_acc_test_obj_4.addNewAccHolder('Tom')
        checking_acc_test_obj_4.deposit(3000)
        self.assertEqual(checking_acc_test_obj_4.get_cur_balance(), 6000)

    #Checks withdrawal from a account (valid withdrawal which is less than current balance)
    def test_withdrawal(self):
        checking_acc_test_obj_5 = Checking(977836766127, 3000)
        checking_acc_test_obj_5.addNewAccHolder('Jerry')
        self.assertGreaterEqual(checking_acc_test_obj_5.get_cur_balance(), 3000)
        checking_acc_test_obj_5.withdraw(2000)
        self.assertEqual(checking_acc_test_obj_5.get_cur_balance(), 1000)

    #Checks Invalid withdrawal from a account shows the exception or not (Invalid withdrawal which is more than current balance)
    def test_withdrawal_with_low_balance(self):
        checking_acc_test_obj_6 = Checking(977836766128, 2000)
        checking_acc_test_obj_6.addNewAccHolder('Spike')
        self.assertGreaterEqual(checking_acc_test_obj_6.get_cur_balance(), 2000)
        with self.assertRaises(Exception):
            checking_acc_test_obj_6.withdraw(3000)
    
    # Checks that the balance after interest of a current balance
    def test_interest(self):
        checking_acc_test_obj_7 = Checking(977836766129, 2000)
        checking_acc_test_obj_7.addNewAccHolder('Quacker')
        checking_acc_test_obj_7.calculate()
        self.assertEqual(checking_acc_test_obj_7.get_cur_balance(), 2000.2)

# Creation of Test Savings class
class Test_Savings(unittest.TestCase):

    #Checks whether the savings account throws exception if the account is created with Zero inital deposit
    def test_no_balance(self):
        with self.assertRaises(Exception):
            savings_acc_test_obj_1 = Savings(987836766123, 0)
        
    #checks whether the account accepts less than $100 as inital deposit
    def test_low_balance(self):
        with self.assertRaises(Exception):
            savings_acc_test_obj_2 = Savings(987836766124, 50)

    # checks whether the account accpets the inital deposit as $100
    def test_edge_balance(self):
        savings_acc_test_obj_3 = Savings(987836766125, 100)
        self.assertEqual(savings_acc_test_obj_3.get_cur_balance(),100)

    # checks whether the account accpets the inital deposit greater than 100
    def test_greater_balance(self):
        savings_acc_test_obj_4 = Savings(987836766126, 1000)
        self.assertGreaterEqual(savings_acc_test_obj_4.get_cur_balance(),100)

    # checks new account holder is added 
    def test_adding_accountholder(self):
        savings_acc_test_obj_5 = Savings(97836766127, 2000)
        savings_acc_test_obj_5.addNewAccHolder('Pluto')
        self.assertEqual(savings_acc_test_obj_5.get_acc_holder(), 'Pluto')

    # checks the savings account holder can add deposit in account
    def test_deposit(self):
        savings_acc_test_obj_6 = Savings(977836766128, 3000)
        savings_acc_test_obj_6.addNewAccHolder('Tom')
        savings_acc_test_obj_6.deposit(3000)
        self.assertEqual(savings_acc_test_obj_6.get_cur_balance(), 6000)
    
    #Checks withdrawal from a account (valid withdrawal which is less than current balance) 
    def test_withdrawal(self):
        savings_acc_test_obj_7 = Savings(977836766129, 3000)
        savings_acc_test_obj_7.addNewAccHolder('Jerry')
        self.assertGreaterEqual(savings_acc_test_obj_7.get_cur_balance(), 3000)
        savings_acc_test_obj_7.withdraw(2000)
        self.assertEqual(savings_acc_test_obj_7.get_cur_balance(), 1000)

    #Checks Invalid withdrawal from a account is throwing an exception or not (Invalid withdrawal which is more than current balance)
    def test_withdrawal_with_low_balance(self):
        savings_acc_test_obj_8 = Savings(977836766130, 2000)
        savings_acc_test_obj_8.addNewAccHolder('Spike')
        self.assertEqual(savings_acc_test_obj_8.get_cur_balance(), 2000)
        with self.assertRaises(Exception):
            savings_acc_test_obj_8.withdraw(3000)
     
    # Checks exception is performed when total withdrawal can be performed 
    def test_withdrawal_with_zero_balance(self):
        savings_acc_test_obj_9 = Savings(977836766131, 2000)
        savings_acc_test_obj_9.addNewAccHolder('Quacker')
        self.assertEqual(savings_acc_test_obj_9.get_cur_balance(), 2000)
        with self.assertRaises(Exception):
            savings_acc_test_obj_9.withdraw(2000)

    # checks whether the edge balance withdrawal can be performed i.e correct maintainance of $100 after withdrawal
    def test_withdrawal_with_edge_balance(self):
        savings_acc_test_obj_10 = Savings(977836766132, 2000)
        savings_acc_test_obj_10.addNewAccHolder('Tyke')
        self.assertEqual(savings_acc_test_obj_10.get_cur_balance(), 2000)
        savings_acc_test_obj_10.withdraw(1900)
        self.assertGreaterEqual(savings_acc_test_obj_10.get_cur_balance(), 100)
    
    # checks the interest of >= $2,000 & < $12,000 balance: 0.05%
    def test_interest_cond1(self):
        savings_acc_test_obj_11 = Savings(977836766133, 2000)
        savings_acc_test_obj_11.addNewAccHolder('Cuckoo')
        savings_acc_test_obj_11.calculate()
        self.assertEqual(savings_acc_test_obj_11.get_cur_balance(), 2001)

    # Checks the interest of < $2,000 balance: 0.01% 
    def test_interest_cond2(self):
        savings_acc_test_obj_11 = Savings(977836766134, 1000)
        savings_acc_test_obj_11.addNewAccHolder('Tuffy')
        savings_acc_test_obj_11.calculate()
        self.assertEqual(savings_acc_test_obj_11.get_cur_balance(), 1000.1)
    
    #Checks the interest of >= $2,000 & < $12,000 balance: 0.05%
    def test_interest_cond3(self):
        savings_acc_test_obj_11 = Savings(977836766135, 15000)
        savings_acc_test_obj_11.addNewAccHolder('Topsy')
        savings_acc_test_obj_11.calculate()
        self.assertEqual(savings_acc_test_obj_11.get_cur_balance(), 15015)

#Driver/main function 
if __name__== "__main__" :

    # Executing tests
    unittest.main(exit=False)

    #Creation of checking account with zero inital deposit
    checking_acc_obj = Checking(97783676667688, 0)

    #Adding a new account holder name
    checking_acc_obj.addNewAccHolder('Alejandro Lopez-Perez')

    #display the account number for the user’s benefit. 
    print('Hi',checking_acc_obj.get_acc_holder(), 'your account number is',checking_acc_obj.get_acc_no())

    # Deposit $1500 into the Alejandro account. 
    checking_acc_obj.deposit(1500)

    # Withdraw $150 from the Alejandro account. 
    checking_acc_obj.withdraw(150)

    # Perform interest accumulation for Alejandro account.
    checking_acc_obj.calculate()

    # Perform Withdraw $750 from the Alejandro account
    checking_acc_obj.withdraw(750)

    # Perform interest accumulation after the withdrawal
    checking_acc_obj.calculate()

    # Create a Savings account for Sasha Ivanov with an initial deposit of $600.
    savings_acc_obj = Savings(88235783767575, 600)

    # Creating new holder as Sasha Ivanov
    savings_acc_obj.addNewAccHolder('Sasha Ivanov')

    #displaying the account number for the user’s benefit. 
    print('Hi',savings_acc_obj.get_acc_holder(), 'your account number is',savings_acc_obj.get_acc_no())

    #Perform interest accumulation of Sasha account
    savings_acc_obj.calculate()

    # Perform Deposit $150 into the Sasha account
    savings_acc_obj.deposit(150)

    #Perform interest accumulation into Sasha account
    savings_acc_obj.calculate()

    #Perform Withdraw $600 from the Sasha account
    savings_acc_obj.withdraw(600)