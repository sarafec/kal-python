class Account:
	def __init__(self, id=0, balance=0, annualInterestRate=0):
		self.__id = id
		self.__balance = balance
		self.__annualInterestRate = annualInterestRate
		
		# accessor methods
		def getId(self):
			return self.__id

		def getBalance(self):
			return self.__balance

		def getAnnualInterestRate(self):
			return self.__annualInterestRate

		# mutator methods
		def setId(self, num):
			self.__id = num

		def setBalance(self, amt):
			self.__balance += amt

		def setAnnualInterestRate(self, rate):
			self.__annualInterestRate = rate

		# methods
		def getMonthlyInterestRate(self):
			return self.getAnnualInterestRate() / 12

		def getMonthlyInterest(self):
			return (self.__balance * self.getMonthlyInterestRate())/100

		def withdraw(self, amt):
			self.setBalance(-amt)
			print("You've withdrawn ", amt, " from your account. You have a balance of ", self.getBalance())

		def deposit(self, amt):
			self.setBalance(amt)
			print("You've deposited ", amt, " You have a balance of ", self.getBalance())
