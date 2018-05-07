from account import Account


def printAccountDetails(id, balance, interestRate, withdrawAmt, depositAmt):
	myAccount = Account(id, balance, interestRate)
	myAccount.withdraw(withdrawAmt)
	myAccount.deposit(depositAmt)
	print("Account no.", myAccount.getId())
	print("Balance:", myAccount.getBalance())
	print("Monthly Interest Rate:", myAccount.getMonthlyInterestRate())
	print("Monthly Interest:", myAccount.getMonthlyInterest())

printAccountDetails(1122, 20000, 4.5, 2500, 3000)
